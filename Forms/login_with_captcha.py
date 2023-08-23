import flet as ft
from login_utils import LoginWithCaptcha


def main(page: ft.Page):
    page.title = "Forms"
    # page.window_always_on_top = True
    page.theme_mode = "light"
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.window_width, page.window_height = 425, 700
    page.window_center()
    page.window_visible = True
    page.on_error = lambda e: print("Error: ", e.data)

    page.appbar = ft.AppBar(
        title=ft.Text("Login Form + Captcha", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        elevation=5,
    )

    def handle_success():
        print("Handling Success...")

    def handle_error():
        print("Handling Error...")

    page.add(
        LoginWithCaptcha(
            on_success=handle_success,
            on_error=handle_error
        )
    )


if __name__ == "__main__":
    ft.app(target=main, view=ft.FLET_APP_HIDDEN)
