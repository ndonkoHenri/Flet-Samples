import flet as ft
from utils import ImageCard


def main(page: ft.Page):
    # little configurations
    page.title = "Random Image Viewer"
    page.horizontal_alignment = "center"  # center the controls in the page - just for a beautiful UI
    page.theme_mode = "light"
    page.img_id_counter = 1

    # some custom fonts found in the assets folder
    page.fonts = {
        "Kalam": "/fonts/Kalam/Kalam-Regular.ttf",
        "JetBrainsMono": "/fonts/JetBrains_Mono/JetBrainsMono-VariableFont_wght.ttf",
        "SpaceGrotesk": "/fonts/Space_Grotesk/SpaceGrotesk-VariableFont_wght.ttf"
    }
    # set the default font_family for light and dark theme modes
    page.theme = ft.Theme(font_family="JetBrainsMono")
    page.dark_theme = ft.Theme(font_family="JetBrainsMono")

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

        # button to change theme_mode (from dark to light mode, or the reverse)

    def generate_image(e):
        # make sure the banner is closed
        close_banner(None)

        img_gen_btn.disabled = True
        page.update()

        try:
            page.img_id_counter += 1
            page.images_row.controls.append(ImageCard(img_id=page.img_id_counter))
        except Exception as error:
            print(error)
            open_banner(None)

        img_gen_btn.disabled = False
        page.update()

    page.banner = ft.Banner(
        bgcolor=ft.colors.AMBER_100,
        leading=ft.Icon(ft.icons.WARNING_AMBER_ROUNDED, color=ft.colors.AMBER, size=40),
        content=ft.Text(
            "Oops, there were some errors while trying to fetch the Image. Please make sure you are connected to the "
            "internet. What would you like me to do? "
        ),
        actions=[
            ft.TextButton("Retry", on_click=generate_image),
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
        title=ft.Text("Random Image Viewer"),
        center_title=True,
        bgcolor="blue",
        color="yellow",
        actions=[theme_icon_button],
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            tooltip="View Code",
            on_click=lambda e: page.launch_url(
                "https://github.com/ndonkoHenri/Flet-Samples/tree/master/Random%20Image%Viewer")
        )
    )

    page.images_row = ft.ResponsiveRow([ImageCard(page.img_id_counter)])

    img_gen_btn = ft.FilledButton(
        text="Generate a Random Image",
        on_click=generate_image,
        content=ft.Row(
            [
                ft.Icon(ft.icons.RESTART_ALT),
                ft.Text("Generate a Random Image!", font_family="SpaceGrotesk", weight=ft.FontWeight.BOLD)
            ]
        )
    )

    page.add(
        img_gen_btn,
        ft.Column(
            [page.images_row],
            scroll=ft.ScrollMode.HIDDEN,
            expand=True
        ),
        ft.Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style=ft.TextThemeStyle.LABEL_SMALL,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLUE_900,
        )
    )


ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
