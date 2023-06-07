import time
import flet as ft


def main(page: ft.Page):
    page.title = "IP Revealer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = page.horizontal_alignment = "center"
    page.fonts = {
        "PJS": "/fonts/Plus_Jakarta_Sans/PlusJakartaSans-VariableFont_wght.ttf",
        "Stick": "/fonts/Stick/Stick-Regular.ttf"
    }
    page.theme = ft.Theme(font_family="PJS")

    # in desktop mode
    if not page.web:
        page.window_center()
        # page.window_always_on_top = True
        page.window_min_width, page.window_min_height = 312, 124
        page.window_width, page.window_height = 386, 201

    def reveal_ip(e):
        """
        The reveal_ip function is called when the user clicks on the eye icon.
        It hides both the eye and blur containers, which makes it so that only the IP address is visible.
        """
        eye_container.visible = False
        blur_container.visible = False
        page.update()

    def copy_ip(e):
        """
        Copies the IP value to clipboard.
        """
        page.set_clipboard(page.client_ip)

        copy_button.selected = True
        page.update()

        time.sleep(2)

        copy_button.selected = False
        page.update()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("</Your Public IP>", weight=ft.FontWeight.BOLD, size=25, selectable=True),
                    ft.Stack(
                        [
                            ft.Container(
                                ft.Row(
                                    [
                                        ft.Text(
                                            page.client_ip if page.client_ip else "No IP found :(",
                                            weight=ft.FontWeight.BOLD,
                                            font_family="Stick",
                                            size=40,
                                            selectable=True
                                        ),
                                        copy_button := ft.IconButton(
                                            ft.icons.COPY_ROUNDED,
                                            icon_color=ft.colors.BLUE,
                                            icon_size=15,
                                            on_click=copy_ip,
                                            visible=page.client_ip is not None,
                                            selected_icon=ft.icons.CHECK_CIRCLE_ROUNDED,
                                            selected_icon_color=ft.colors.GREEN
                                        )
                                    ],
                                    spacing=0,
                                    alignment=ft.MainAxisAlignment.CENTER,
                                    vertical_alignment=ft.CrossAxisAlignment.END
                                ),
                                alignment=ft.alignment.center,
                            ),
                            blur_container := ft.Container(
                                width=410,
                                height=65,
                                blur=ft.Blur(15, 15),
                            ),
                            eye_container := ft.Container(
                                content=ft.IconButton(
                                    ft.icons.REMOVE_RED_EYE,
                                    on_click=reveal_ip
                                ),
                                alignment=ft.alignment.bottom_center,
                                padding=ft.Padding(0, 7.5, 0, 0)
                            ),
                        ],
                    ),
                    ft.Container(
                        content=ft.Text(
                            "Made with ❤ by the ",
                            spans=[
                                ft.TextSpan(
                                    "@TheEthicalBoy",
                                    ft.TextStyle(
                                        color=ft.colors.BLUE,
                                        decoration=ft.TextDecoration.UNDERLINE,
                                        decoration_color=ft.colors.BLUE,
                                        decoration_thickness=0.5,
                                    ),
                                    url="https://github.com/ndonkoHenri",
                                )
                            ],
                            selectable=True,
                            size=10
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20
            ),
            width=500,
        )
    )


ft.app(
    main,
    view=ft.WEB_BROWSER,
    # web_renderer="html",
    assets_dir="assets",
    # use_color_emoji=True
)
