import base64
import os
import random
import string
from typing import Callable

import flet as ft
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


class LoginWithCaptcha(ft.Column):
    def __init__(self, on_success: Callable = None, on_error: Callable = None, width=500):
        """
        :param on_success: Callable: Handle success
        :param on_error: Callable: Handle errors
        """
        super().__init__()

        self.width = width
        self.on_success = on_success
        self.on_error = on_error

        self.audio_state = "completed"
        self.captcha_text = None

        # create a captcha string of random digits - you might want to encrypt the returned value :)
        self.generate_captcha_text = lambda length: ''.join(random.choices(string.digits, k=length))

        self.email_field_ref = ft.Ref[ft.TextField]()
        self.pwd_field_ref = ft.Ref[ft.TextField]()
        self.captcha_field_ref = ft.Ref[ft.TextField]()
        self.captcha_image_ref = ft.Ref[ft.Image]()
        self.audio = ft.Audio(
            src=f"/captcha-audio-{self.captcha_text}.wav",
            autoplay=False,
            release_mode=ft.audio.ReleaseMode.STOP,
            volume=1,
            balance=0,
            # on_loaded=lambda _: print("Audio Control Loaded"),
            on_state_changed=self.handle_audio_state_change,
        )

        self.controls = [
            ft.SafeArea(
                content=ft.Column(
                    controls=[
                        ft.Container(
                            content=ft.Image(
                                src=r"/images/login.png",
                                error_content=ft.ProgressRing()
                            ),
                            height=160,
                            alignment=ft.alignment.top_center,
                        ),
                        ft.Column(
                            alignment=ft.MainAxisAlignment.START,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            controls=[
                                ft.Container(
                                    padding=ft.padding.symmetric(horizontal=16),
                                    content=ft.Column(
                                        spacing=0,
                                        alignment=ft.MainAxisAlignment.START,
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        controls=[
                                            ft.TextField(
                                                ref=self.email_field_ref,
                                                label="E-mail",
                                                hint_text="example@xyz.com",
                                                border=ft.InputBorder.UNDERLINE,
                                                on_change=self.handle_textfield_change
                                            ),
                                            ft.TextField(
                                                ref=self.pwd_field_ref,
                                                label="Password",
                                                hint_text="ex: D/s4-YcG#5",
                                                password=True,
                                                border=ft.InputBorder.UNDERLINE,
                                                on_change=self.handle_textfield_change
                                            ),
                                            ft.Divider(height=15, color=ft.colors.TRANSPARENT),
                                            ft.Column(
                                                spacing=5,
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                        tight=True,
                                                        controls=[
                                                            ft.Image(
                                                                ref=self.captcha_image_ref,
                                                                src="assets/images/captcha-image-test.png",
                                                                error_content=ft.ProgressRing(),
                                                                gapless_playback=True
                                                            ),
                                                            ft.Column(
                                                                alignment=ft.MainAxisAlignment.CENTER,
                                                                spacing=0,
                                                                controls=[
                                                                    ft.IconButton(
                                                                        ft.icons.AUDIOTRACK,
                                                                        tooltip="play/stop audio",
                                                                        icon_color=ft.colors.ORANGE_ACCENT_700,
                                                                        on_click=self.handle_audio
                                                                    ),
                                                                    ft.IconButton(
                                                                        ft.icons.REFRESH,
                                                                        tooltip="new captcha",
                                                                        icon_color=ft.colors.GREEN,
                                                                        on_click=self.generate_new_captcha
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    ft.Row(
                                                        alignment=ft.MainAxisAlignment.CENTER,
                                                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                        controls=[
                                                            ft.TextField(
                                                                ref=self.captcha_field_ref,
                                                                height=40,
                                                                width=110,
                                                                content_padding=ft.Padding(7, 7, 7, 7),
                                                                text_align=ft.TextAlign.CENTER
                                                            ),
                                                        ]
                                                    )
                                                ]
                                            ),
                                            ft.Divider(height=25, color=ft.colors.TRANSPARENT),
                                            ft.Row(
                                                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                                                controls=[
                                                    ft.ElevatedButton(
                                                        "LOGIN",
                                                        icon=ft.icons.EMAIL,
                                                        width=185,
                                                        height=40,
                                                        color=ft.colors.WHITE,
                                                        bgcolor=ft.colors.BLUE_700,
                                                        style=ft.ButtonStyle(
                                                            shape=ft.CountinuosRectangleBorder(radius=20),
                                                        ),
                                                        on_click=self.handle_login
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                )
                            ]
                        ),
                    ],
                ),
            )
        ]

    def update(self):
        """
        Updates the page, and this control itself.
        Calling self.update() becomes a "one stone two birds" operation.
        """
        self.page.update()
        super().update()

    def did_mount(self):
        """
        Called when this control is added to the page.
        It adds the Audio control to the page's overlay, then generates a new captcha.
        """
        self.page.overlay.append(self.audio)
        self.generate_new_captcha()

    def will_unmount(self):
        """
        Called when this control is about to be removed from the page.
        It removes/unloads the Audio control from the page's overlay and
        deletes any existing audio files in the 'assets/audios' directory.
        """
        # remove the Audio from the page's overlay
        self.page.overlay.remove(self.audio)

        # Delete all existing audio files in the assets directory
        for file_name in os.listdir("./assets/audios"):
            if file_name.endswith(".wav"):
                os.remove(os.path.join("assets", "audios", file_name))
                print("Deleted file: ", file_name)

    def handle_textfield_change(self, e):
        """
        Called when the textfield value changes (user is typing).
        If the field's value is empty, the appropriate error message is shown.
        """
        e.control.error_text = "Required!" if not e.data else None
        self.update()

    def handle_fields_validation(self):
        """
        Checks if the email and password fields are empty.
        If they are not empty, proceed by checking the captcha field too.

        :return: True if the email and password fields are not empty,
        :rtype: bool
        """
        if "@" in self.email_field_ref.current.value.strip() \
                and self.pwd_field_ref.current.value.strip():

            if self.captcha_field_ref.current.value.strip():
                self.show_snackbar_message("No field is empty!!")
                return True
            else:
                self.show_snackbar_message("Error: Please solve the captcha!")
        else:
            self.show_snackbar_message("Error: Check your entries!")

        return False

    def handle_login(self, e):
        """
        Called when the user clicks on the login button.
        It checks if all fields are valid(contain some text), and also if the captcha was correctly solved.
        """
        if not self.handle_fields_validation():
            if self.on_error:
                self.on_error()
            return

        if self.captcha_field_ref.current.value.strip() == self.captcha_text:
            self.show_snackbar_message("SUCCESS!")
            if self.on_success:
                self.on_success()
        else:
            self.show_snackbar_message("Captcha is incorrect!")
            if self.on_error:
                self.on_error()

    def generate_captcha(self, length: int = 4):
        """
        Generates a random captcha text, generates a corresponding image, converts the image to base64 encoding,
        and returns the base64 string. Using Base64 strings makes it possible to avoid saving the images locally.
        An audio captcha of the random text is also created.

        :return: a base64 string of the Captcha image
        :rtype: str
        """
        image_captcha = ImageCaptcha()
        audio_captcha = AudioCaptcha()

        # try to delete the lastly created audio file (not more needed, as we will be creating a new one)
        if self.captcha_text:
            try:
                os.remove(os.path.join("assets", "audios", f"captcha-audio-{self.captcha_text}.wav"))
            except FileNotFoundError as ex:
                self.show_snackbar_message(str(ex))

        self.captcha_text = self.generate_captcha_text(length)

        audio_path = f"/audios/captcha-audio-{self.captcha_text}.wav"
        try:
            audio_captcha.write(self.captcha_text, f'./assets{audio_path}')
        except Exception as ex:
            self.show_snackbar_message(str(ex))

        # Generate the CAPTCHA image as bytes
        image_bytes = image_captcha.generate(self.captcha_text)

        # Convert bytes to base64-encoded string
        image_base64 = base64.b64encode(image_bytes.read()).decode('utf-8')

        return image_base64, audio_path

    def generate_new_captcha(self, e=None):
        """
        Stop/Release any playing audio, then generates a new captcha code and
        updates the image and audio files accordingly.
        """
        if self.audio_state == "playing":
            self.audio.release()
        self.captcha_image_ref.current.src_base64, self.audio.src = self.generate_captcha()
        self.update()

    def handle_audio_state_change(self, e):
        """
        Called when the audio state changes.
        It updates the audio_state variable to reflect this change.

        :return: The audio state of the device
        """
        self.audio_state = e.data

    def handle_audio(self, e):
        """
        The handle_audio function is called when the user clicks on the audio-icon-button.
        Depending on the audio state at that moment, the captcha audio file will either be played or released/stopped.
        """
        if self.audio_state in ["completed", "stopped", "disposed"]:
            self.audio.play()
        elif self.audio_state == "playing":
            self.audio.release()

    def show_snackbar_message(self, text: str = "Message:", duration: int = 6000):
        """
        Helper function that displays a snackbar message to the user.

        :param text: str: the text of the snackbar message
        :param duration: int: the duration of the snackbar message
        """
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text(text),
                duration=duration,
                show_close_icon=True,
                behavior=ft.SnackBarBehavior.FLOATING,
                dismiss_direction=ft.DismissDirection.DOWN
            )
        )
        # print(text)
