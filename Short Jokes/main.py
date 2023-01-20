import flet as ft
from utils import JokeCard, ethical_signature
from joke import return_joke



def main(page: ft.Page):
    page.title = "Short Jokes"
    page.theme_mode = "light"
    # page.window_always_on_top = True
    page.jokes_id_counter = 0
    page.splash = ft.ProgressBar(visible=False)
    page.fonts = {
        "Kalam": "/fonts/Kalam/Kalam-Regular.ttf",
        "JetBrainsMono": "/fonts/JetBrains_Mono/JetBrainsMono-VariableFont_wght.ttf",
        "SpaceGrotesk": "/fonts/Space_Grotesk/SpaceGrotesk-VariableFont_wght.ttf"
    }
    page.theme = ft.Theme(font_family="JetBrainsMono")
    page.dark_theme = ft.Theme(font_family="JetBrainsMono")

    def close_dlg(e):
        page.dialog.open = False
        page.update()

    def close_banner(e):
        """Close the banner."""
        page.banner.open = False
        page.update()

    def open_banner(e):
        """Open the banner."""
        page.banner.open = True
        page.update()

    def change_theme(e):
        """
        When the button(to change theme) is clicked, the theme is changed, and the page is updated.

        :param e: The event that triggered the function
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()

    def generate(e):
        # make sure the banner is closed
        close_banner(None)

        # make the progress bar visible and disable the btn: indicating to the user, that we are trying to get the joke
        page.splash.visible = True
        joke_gen_btn.disabled = True
        page.update()

        # if the returned value is a valid Joke(not None), then we add a new card to the Row of jokes
        if (fetched_joke := return_joke()) is not None:
            page.jokes_id_counter += 1
            page.jokes_row.controls.append(JokeCard(joke_id=page.jokes_id_counter, joke=fetched_joke))
        else:
            open_banner(None)

        # make the progress bar invisible and enable the button: indicating
        page.splash.visible = False
        joke_gen_btn.disabled = False
        page.update()

    page.dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Disclaimer 📝", weight=ft.FontWeight.BOLD),
        content=ft.Text("This app fetches Joke's from an API and I tried my best to make the fetched jokes safe for "
                        "everyone. Nevertheless, it might still happen that a joke isn't of your likings. Please, "
                        "feel free to use the 'Delete' button at your disposal.\nThanks for your comprehension. 😉"),
        actions=[
            ft.TextButton("Alright!", on_click=close_dlg),
        ],
        actions_alignment=ft.MainAxisAlignment.END
    )

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to fetch the Joke. Please make sure you are connected to the "
            "internet. What would you like me to do? "
        ),
        actions=[
            ft.TextButton("Retry", on_click=generate),
            ft.TextButton("Ignore", on_click=close_banner),
        ],
    )

    theme_icon_button = ft.IconButton(
        icon=ft.icons.DARK_MODE,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_color=ft.colors.BLACK,
        selected_icon_color=ft.colors.WHITE,
        selected=False,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
    )

    page.appbar = ft.AppBar(
        title=ft.Text("Short Jokes"),
        center_title=True,
        bgcolor="blue",
        color="yellow",
        actions=[theme_icon_button],
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            tooltip="View Code",
            on_click=lambda e: page.launch_url(
                "https://github.com/ndonkoHenri/Flet-Samples/tree/master/Short%20Jokes")
        )
    )

    page.jokes_row = ft.ResponsiveRow(
        [
            JokeCard(
                page.jokes_id_counter,
                ">> why do python programmers wear glasses? \n\n>> Because they can't C."
            ),
        ],
    )

    page.add(
        ft.Row(
            controls=[
                joke_gen_btn := ft.FilledButton(
                    on_click=generate,
                    content=ft.Row(
                        [
                            ft.Icon(ft.icons.RESTART_ALT),
                            ft.Text("Generate a Joke!", font_family="SpaceGrotesk", weight=ft.FontWeight.BOLD)
                        ]
                    )
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        ft.Column(
            [page.jokes_row],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
        ),
        ethical_signature
    )

    # open the disclaimer dialog
    page.dialog.open = True
    page.update()


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
