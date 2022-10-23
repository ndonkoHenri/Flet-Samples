import os
import time
import flet
from flet import (icons, colors, ProgressBar, Page, SnackBar, Text, AlertDialog, TextButton, IconButton, ButtonStyle,
                  AppBar, Image, FilledButton, TextField, Ref, Divider, Container, Alignment)
import pyqrcode


def main(page: Page):
    page.title = "QRcode Generator"
    page.theme_mode = "light"
    # page.window_always_on_top = True
    page.splash = ProgressBar(visible=False)
    page.horizontal_alignment = "center"
    page.count = len(os.listdir("assets/generated-codes"))
    page.window_min_height = 658
    page.window_width = 521

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
                    SnackBar(
                        Text(f"The file was saved successfully as 'assets/generated-codes/output_{page.count}.svg'!"),
                        open=True
                    )
                )
                page.count += 1
        else:
            page.show_snack_bar(
                SnackBar(
                    Text("Did you forget to enter your Text/URL?"),
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

    pc_alert_dialog = AlertDialog(
        modal=True,
        title=Text("Confirm"),
        content=Text("You are about to download the generated QR Code.\nDo you want to proceed?"),
        actions=[
            TextButton("Yeah", on_click=save),
            TextButton("Abort", on_click=cancel_dialog),
        ],
        actions_alignment="end",
    )

    web_alert_dialog = AlertDialog(
        modal=True,
        title=Text("Note"),
        content=Text("You are about to download the generated QR Code.\n"
                     "Remember to save it with common image file formats such as: .png, .jpg, .jpeg, .bmp etc!"),
        actions=[
            TextButton("Alright", on_click=save),
            TextButton("Abort", on_click=cancel_dialog),
        ],
        actions_alignment="end",
    )
    page.dialog = web_alert_dialog

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
        time.sleep(0.2)  # shows the progress bar for some time indicating that work is being done
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
                    SnackBar(
                        Text(f"Updated QR Code!"),
                        open=True
                    )
                )
            else:
                save_btn.current.disabled = True
                page.show_snack_bar(
                    SnackBar(
                        Text("No Text was entered!"),
                        open=False if qr_image.current.src_base64 else True
                    )
                )
        except Exception as e:
            page.show_snack_bar(
                SnackBar(
                    Text(f"An Error occurred: {e}"),
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
            "QRcode Generator",
            color="white"
        ),
        center_title=True,
        bgcolor="blue",
        actions=[theme_icon_button],
    )

    qr_image = Ref[Image]()
    qr_text = Ref[TextField]()
    save_btn = Ref[FilledButton]()

    page.add(
        TextField(
            ref=qr_text,
            max_length=250,
            hint_text="enter text here..",
            label="QR Text Field",
            width=520,
            height=90,
            suffix=FilledButton("Generate", on_click=generate_qr),
            on_change=generate_qr,
            autofocus=True
        ),
        Divider(),
        Container(
            Image(
                ref=qr_image,
                src="/enter_text_meme.png",
                width=370,
                height=370,
            ),
            alignment=Alignment(0, 0),
        ),
        FilledButton("Save/Download", save_btn, icon=icons.DOWNLOAD, on_click=open_dialog, disabled=True)
    )


if __name__ == "__main__":
    # flet.app(target=main, assets_dir="assets")
    flet.app(target=main, assets_dir="assets",)
