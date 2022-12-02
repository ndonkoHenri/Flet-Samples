import time
import flet as ft
import pyshorteners  # pip install pyshorteners

shortener = pyshorteners.Shortener()


class ShortLinkRow(ft.Row):
    # a row containing the shortened url, and two buttons ('copy' button, and 'open in browser')

    def __init__(self, short_link, source):
        super().__init__()

        self.controls = [
            ft.Text(value=short_link, size=16, selectable=True, italic=True),
            ft.IconButton(ft.icons.COPY, on_click=lambda e: self.copy(short_link), bgcolor=ft.colors.BLUE_700,
                          tooltip="copy"),
            ft.IconButton(ft.icons.OPEN_IN_BROWSER_OUTLINED, tooltip="open in browser",
                          on_click=lambda e: e.page.launch_url(short_link))
        ]
        self.alignment = "center"
        self.tooltip = source

    def copy(self, value):
        """
        It copies the value to the clipboard.

        :param value: The value to be copied to the clipboard
        """
        self.page.set_clipboard(value)
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Link copied to clipboard!"),
                open=True
            )
        )


def main(page: ft.Page):
    page.title = "URL Shortener"
    page.theme_mode = "light"  # by default, page.theme_mode=None
    # page.window_always_on_top = True
    page.splash = ft.ProgressBar(visible=False)
    page.vertical_alignment = "start"
    page.horizontal_alignment = "center"
    # set the width and height of the window.
    page.window_width = 522
    page.window_height = 620
    page.scroll = "hidden"

    page.fonts = {"sf-simple": "/fonts/San-Francisco/SFUIDisplay-Light.ttf",
                  "sf-bold": "/fonts/San-Francisco/SFUIDisplay-Bold.ttf"}

    page.theme_mode = "light"
    page.theme = ft.Theme(font_family="sf-simple")

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

    def shorten(e: ft.ControlEvent):
        """
        It takes a URL, and returns a shortened version of it

        :param e: ft.ControlEvent
        :type e: ft.ControlEvent
        """
        if url_field.value:
            try:
                page.add(ft.Text(f"Long URL: {url_field.value}", italic=False, weight='bold'))
                page.add(ShortLinkRow(shortener.tinyurl.short(url_field.value), "Source: tinyurl.com"))
                page.add(ShortLinkRow(shortener.chilpit.short(url_field.value), "Source: chilp.it"))
                page.add(ShortLinkRow(shortener.clckru.short(url_field.value), "Source: clck.ru"))
                page.add(ShortLinkRow(shortener.dagd.short(url_field.value), "Source: da.dg"))
                page.add(ShortLinkRow(shortener.isgd.short(url_field.value), "Source: is.gd"))
                page.add(ShortLinkRow(shortener.osdb.short(url_field.value), "Source: os.db"))

                # page.add(ShortLinkRow(shortener.gitio.short(url_field.value), "Source: git.io"),
                # page.add(ShortLinkRow(shortener.owly.short(url_field.value), "Source: ow.ly"),
                # page.add(ShortLinkRow(shortener.qpsru.short(url_field.value), "Source: qps.ru"),

            except Exception as exception:
                print(exception)
                e.page.set_clipboard(exception)
                e.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text(f"An error occurred. Please retry, or refresh the page."),
                        open=True
                    )
                )

        else:
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Verify your URL please! A valid one must be entered."),
                    open=True
                )
            )

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(color={"": ft.colors.BLACK, "selected": ft.colors.WHITE}, ),
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            "URL Shortener",
            color="white"
        ),
        center_title=True,
        bgcolor="blue",
        actions=[theme_icon_button],
    )

    page.add(
        url_field := ft.TextField(
            label="Long URL",
            hint_text="type long url here",
            max_length=200,
            width=800,
            keyboard_type="url",
            on_submit=shorten,
            suffix=ft.FilledButton("Shorten!", on_click=shorten),
            value='https://github.com/ndonkoHenri/Flet-Samples/tree/master/URL%20shortener'
        ),
        ft.Text("Generated URLs:", weight="bold", size=23, font_family="sf-bold")
    )


ft.app(target=main, assets_dir="assets")
