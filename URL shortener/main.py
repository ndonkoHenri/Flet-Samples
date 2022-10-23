import time
import flet
from flet import colors, icons, IconButton, Text, Row, Page, ProgressBar, Theme, SnackBar, ButtonStyle, AppBar, \
    TextField, Ref, FilledButton
import pyshorteners     # pip install pyshorteners
from flet.control_event import ControlEvent

shortener = pyshorteners.Shortener()


class ShortLinkRow(Row):
    # ta row containing the shortened url, and two buttons ('copy' button, and 'open in browser')

    def __init__(self, short_link, source):
        super().__init__()

        self.controls = [
            Text(value=short_link, size=16, selectable=True, italic=True),
            IconButton(icons.COPY, on_click=lambda e: self.copy(short_link), bgcolor=colors.BLUE_700,
                       tooltip="copy"),
            IconButton(icons.OPEN_IN_BROWSER_OUTLINED, tooltip="open in browser",
                       on_click=lambda e: e.page.launch_url(short_link))
        ]
        self.alignment = "center"
        self.tooltip = source

    def copy(self, value):
        self.page.set_clipboard(value)
        self.page.show_snack_bar(
            SnackBar(
                Text("Link copied to clipboard!"),
                open=True
            )
        )


def main(page: Page):
    page.title = "URL Shortener"
    page.theme_mode = "light"  # by default, page.theme_mode=None
    # page.window_always_on_top = True
    page.splash = ProgressBar(visible=False)
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    # set the width and height of the window.
    page.window_width = 522
    page.window_height = 620
    page.scroll = "hidden"

    page.fonts = {"sf-simple": "/fonts/San-Francisco/SFUIDisplay-Light.ttf",
                  "sf-bold": "/fonts/San-Francisco/SFUIDisplay-Bold.ttf"}

    page.theme_mode = "light"
    page.theme = Theme(
        font_family="sf-simple",
        # use_material3=True,
        # visual_density="compact",
    )

    # page.horizontal_alignment = "center"
    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark. A splash(progress bar) is also shown.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        page.splash.visible = False
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        time.sleep(0.3)  # shows the progress bar for a second indicating that work is being done..
        page.update()

    def shorten(e: ControlEvent):
        if url_field.current.value:
            try:
                page.add(Text(f"Long URL: {url_field.current.value}", italic=False, weight='bold'))
                page.add(ShortLinkRow(shortener.tinyurl.short(url_field.current.value), "Source: tinyurl.com"))
                page.add(ShortLinkRow(shortener.chilpit.short(url_field.current.value), "Source: chilp.it"))
                page.add(ShortLinkRow(shortener.clckru.short(url_field.current.value), "Source: clck.ru"))
                page.add(ShortLinkRow(shortener.dagd.short(url_field.current.value), "Source: da.dg"))
                page.add(ShortLinkRow(shortener.isgd.short(url_field.current.value), "Source: is.gd"))
                page.add(ShortLinkRow(shortener.osdb.short(url_field.current.value), "Source: os.db"))

                # page.add(ShortLinkRow(shortener.gitio.short(url_field.current.value), "Source: git.io"),
                # page.add(ShortLinkRow(shortener.owly.short(url_field.current.value), "Source: ow.ly"),
                # page.add(ShortLinkRow(shortener.qpsru.short(url_field.current.value), "Source: qps.ru"),

            except Exception as exception:
                print(exception)
                e.page.set_clipboard(exception)
                e.page.show_snack_bar(
                    SnackBar(
                        Text(f"An error occurred. Try refreshing the page. If it persists, raise an issue. Link in the "
                             f"'credits' section."),
                        open=True
                    )
                )

        else:
            e.page.show_snack_bar(
                SnackBar(
                    Text("Verify your URL please! A valid one must be entered."),
                    open=True
                )
            )

    theme_icon_button = IconButton(
        icons.DARK_MODE,
        selected=False,
        selected_icon=icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ButtonStyle(color={"": colors.BLACK, "selected": colors.WHITE}, ),
    )

    page.appbar = AppBar(
        title=Text(
            "URL Shortener",
            color="white"
        ),
        center_title=True,
        bgcolor="blue",
        actions=[theme_icon_button],
    )

    url_field = Ref[TextField]()

    page.add(
        TextField(
            url_field,
            label="Long URL",
            hint_text="type long url here",
            max_length=200,
            width=800,
            keyboard_type="url",
            on_submit=shorten,
            suffix=FilledButton("Shorten!", on_click=shorten),
            value='https://github.com/ndonkoHenri/Flet-Samples/tree/master/URL%20shortener'
        ),
        Text("Generated URLs:", weight="bold", size=23, font_family="sf-bold")
    )


flet.app(target=main, assets_dir="assets")
