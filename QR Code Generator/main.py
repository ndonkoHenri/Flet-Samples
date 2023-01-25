import os
import flet as ft
import pyqrcode


# todo: add filepicker for image save on desktop

def main(page: ft.Page):
    page.title = "QRcode Generator"
    page.theme_mode = "light"
    # page.window_always_on_top = True
    page.splash = ft.ProgressBar(visible=False)
    page.horizontal_alignment = "center"
    page.count = len(os.listdir("assets/generated-codes"))
    page.window_min_height = 658
    page.window_width = 521
    page.scroll = "hidden"

    def save(e):
        """saves the QR code as an SVG file(for PC) or opens a new tab for download(web)."""
        cancel_dialog(e)
        if qr_text.current.value.strip() and qr_image.current.src_base64:
            if page.web:
                page.launch_url(f"data:application/octet-stream;base64,{qr_image.current.src_base64}")
                return
            else:
                qr_code = pyqrcode.create(qr_text.current.value)
                qr_code.svg(f"assets/generated-codes/output_{page.count}.svg", scale=10, debug=True)
                page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text(
                            f"The file was saved successfully as 'assets/generated-codes/output_{page.count}.svg'!"),
                        open=True
                    )
                )
                page.count += 1
        else:
            page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("Did you forget to enter your Text/URL?"),
                    open=True
                )
            )

    def cancel_dialog(e):
        """closes the dialog box"""
        page.dialog.open = False
        page.update()

    def open_dialog(e):
        """opens the dialog box"""
        page.dialog = web_alert_dialog if page.web else pc_alert_dialog
        page.dialog.open = True
        page.update()

    pc_alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Confirm"),
        content=ft.Text("You are about to download the generated QR Code.\nDo you want to proceed?"),
        actions=[
            ft.TextButton("Yeah", on_click=save),
            ft.TextButton("Abort", on_click=cancel_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )

    web_alert_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Note"),
        content=ft.Text("You are about to download the generated QR Code.\n"
                        "Remember to save it with common image file formats such as: .png, .jpg, .jpeg, .bmp etc!"),
        actions=[
            ft.TextButton("Alright", on_click=save),
            ft.TextButton("Abort", on_click=cancel_dialog),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    page.dialog = web_alert_dialog

    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark. A splash(progress bar) is also shown.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        page.update()

    def generate_qr(e):
        try:
            if qr_text.current.value.strip():
                page.splash.visible = True
                page.update()
                # generating the code as base64, and setting the src_base64 property of the image to it
                qr_code = pyqrcode.create(qr_text.current.value)
                qr_image.current.src = None
                qr_image.current.src_base64 = qr_code.png_as_base64_str(scale=10)
                qr_image.current.update()

                page.splash.visible = False
                save_btn.current.disabled = False
                page.update()

                page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text(f"Updated QR Code!"),
                        open=True
                    )
                )
            else:
                save_btn.current.disabled = True
                page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text("No Text was entered!"),
                        open=False if qr_image.current.src_base64 else True
                    )
                )
        except Exception as e:
            page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(f"An Error occurred: {e}"),
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
            "QRcode Generator",
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
                "https://github.com/ndonkoHenri/Flet-Samples/tree/master/QR%20Code%20Generator")
        )
    )

    qr_image = ft.Ref[ft.Image]()
    qr_text = ft.Ref[ft.TextField]()
    save_btn = ft.Ref[ft.FilledButton]()

    page.add(
        ft.TextField(
            ref=qr_text,
            max_length=250,
            hint_text="enter text here..",
            label="QR Text Field",
            width=520,
            height=90,
            suffix=ft.FilledButton("Generate", on_click=generate_qr),
            on_change=generate_qr,
            autofocus=True
        ),
        ft.Divider(),
        ft.Container(
            ft.Image(
                ref=qr_image,
                src="/enter_text_meme.png",
                width=370,
                height=370,
            ),
            alignment=ft.Alignment(0, 0),
        ),
        ft.FilledButton("Save/Download", save_btn, icon=ft.icons.DOWNLOAD, on_click=open_dialog, disabled=True)
    )


if __name__ == "__main__":
    # flet.app(target=main, assets_dir="assets")
    ft.app(target=main, assets_dir="assets", view=ft.WEB_BROWSER)
