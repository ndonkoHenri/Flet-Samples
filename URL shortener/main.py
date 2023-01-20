import flet as ft
import pyshorteners  # pip install pyshorteners

shortener = pyshorteners.Shortener()


class ShortLinkRow(ft.Row):
    # a row containing the shortened url, and two buttons ('copy', and 'open in browser')

    def __init__(self, shortened_link, link_source):
        """
        We create a new class called `ShortenedLinkRow` that inherits from `ft.Row`.
        The constructor takes two arguments/parameters: `shortened_link` and `source`.

        :param shortened_link: the shortened link
        :param link_source: the service hosting the shortened_link
        """
        super().__init__()  # required when overwriting the constructor

        self.tooltip = link_source  # set the tooltip of the row itself to the link provider/source
        self.alignment = "center"   # center the contents of this row

        # the controls/content of our Row
        self.controls = [
            ft.Text(value=shortened_link, size=16, selectable=True, italic=True),
            ft.IconButton(
                icon=ft.icons.COPY, # the icon to be showed
                on_click=lambda e: self.copy(shortened_link),   # when this button is clicked, call the `copy` method, passing the shortened link as parameter
                bgcolor=ft.colors.BLUE_700,
                tooltip="copy"  # to be showed when hovering on this button
            ),
            ft.IconButton(
                icon=ft.icons.OPEN_IN_BROWSER_OUTLINED, # the icon to be showed
                tooltip="open in browser",  # to be showed when hovering on this button
                on_click=lambda e: e.page.launch_url(shortened_link)    # when this button is clicked, open a browser tab with that shortened link
            )
        ]

    def copy(self, value):
        """
        It copies the given value to the clipboard, and opens a Snackbar to inform the user.
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
    page.title = "URL Shortener"    # title of application/page
    page.theme_mode = "light"  # by default, page.theme_mode=None
    page.splash = ft.ProgressBar(visible=False)
    page.horizontal_alignment = "center"  # center our page's content (remove or change at wish)
    # set the width and height of the window on desktop
    page.window_width = 522
    page.window_height = 620
    page.scroll = "hidden"

    # use the custom fonts in the assets folder
    page.fonts = {"sf-simple": "/fonts/San-Francisco/SFUIDisplay-Light.ttf",
                  "sf-bold": "/fonts/San-Francisco/SFUIDisplay-Bold.ttf"}
    page.theme = ft.Theme(font_family="sf-simple")

    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark. A splash(progress bar) is also shown.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        page.update()

    def shorten(e: ft.ControlEvent):
        """Grabs the URL in the textfield, and displays shortened versions of it."""

        user_link = text_field.value  # retrieve the content of the textfield

        if user_link:  # if the textfield is not empty
            # if the entered text in the textfield is not a valid URl, the program may break,
            # hence the need to catch that in a try-except
            page.splash.visible = True
            page.update()
            page.add(ft.Text(f"Long URL: {text_field.value}", italic=False, weight=ft.FontWeight.BOLD))
            try:
                page.add(ShortLinkRow(shortener.tinyurl.short(text_field.value), "Source: tinyurl.com"))
                page.add(ShortLinkRow(shortener.chilpit.short(text_field.value), "Source: chilp.it"))
                page.add(ShortLinkRow(shortener.clckru.short(text_field.value), "Source: clck.ru"))
                page.add(ShortLinkRow(shortener.dagd.short(text_field.value), "Source: da.dg"))
                page.add(ShortLinkRow(shortener.isgd.short(text_field.value), "Source: is.gd"))
                page.add(ShortLinkRow(shortener.osdb.short(text_field.value), "Source: os.db"))

                # page.add(ShortLinkRow(shortener.gitio.short(url_field.value), "Source: git.io"),
                # page.add(ShortLinkRow(shortener.owly.short(url_field.value), "Source: ow.ly"),
                # page.add(ShortLinkRow(shortener.qpsru.short(url_field.value), "Source: qps.ru"),

            except Exception as exception:
                print(exception)
                # inform the user that an error has occurred
                e.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text(f"An error occurred. Please retry, or refresh the page."),
                        open=True
                    )
                )
                page.splash.visible = False
                page.update()

        else:  # if the textfield is empty (no text)
            # inform the user
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Please enter a URL in the field!"),
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
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            tooltip="View Code",
            on_click=lambda e: page.launch_url(
                "https://github.com/ndonkoHenri/Flet-Samples/tree/master/URL%20shortener")
        )
    )

    page.add(
        text_field := ft.TextField(
            value='https://github.com/ndonkoHenri', # a test link
            label="Long URL",
            hint_text="type long url here",
            max_length=200,
            width=800,
            keyboard_type=ft.KeyboardType.URL,
            # 'shorten' is the function to be called on occurrence of some events
            suffix=ft.FilledButton("Shorten!", on_click=shorten),  # event: button clicked
            on_submit=shorten  # event: 'enter' key pressed
        ),
        ft.Text("Generated URLs:", weight=ft.FontWeight.BOLD, size=23, font_family="sf-bold")
    )


ft.app(target=main, assets_dir="assets")    # view=ft.WEB_BROWSER
