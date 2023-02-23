from flet import *
import flet as ft


# todo: change  link to docs

# the content of the blur tab
class TabContentBlur(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.blur_sigma_y = None
        self.blur_sigma_x = None

        self.blur_tile_mode = None

        self.blur_obj = ft.Ref[ft.Blur]()

        # text field for the sigma x property of the Blur object
        self.field_sigma_x = ft.TextField(
            label="sigma_x",
            helper_text="Union[int, float]",
            value="",
            on_change=self.update_blur,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the sigma_y property of the Blur object
        self.field_sigma_y = ft.TextField(
            label="sigma_y",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_blur,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # radio buttons for the tile_mode parameter
        self.tile_mode_radio_group = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="clamp", label="clamp"),
                    ft.Radio(value="decal", label="decal"),
                    ft.Radio(value="mirror", label="mirror"),
                    ft.Radio(value="repeated", label="repeated"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            value="clamp",
            on_change=self.update_blur,
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_sigma_x, self.field_sigma_y]
                ),
                self.tile_mode_radio_group,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11,
        )

        return ft.Column(
            [
                ft.Text("Blur Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.Container(
                            ref=self.blur_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=150,
                            height=150,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Copy Value to Clipboard",
                            icon=ft.icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        ft.FilledTonalButton(
                            "Go to Docs",
                            icon=ft.icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/verticaldivider/")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30,
            expand=True
        )

    def update_blur(self, e: ft.ControlEvent):
        """It updates the blur object."""
        self.blur_sigma_x, self.blur_sigma_y = (
            int(self.field_sigma_x.value.strip()) if self.field_sigma_x.value.strip().isnumeric() else None,
            int(self.field_sigma_y.value.strip()) if self.field_sigma_y.value.strip().isnumeric() else None,
        )
        self.blur_tile_mode = self.tile_mode_radio_group.value

        # sigma_y
        try:
            if self.field_sigma_y.value:
                self.blur_sigma_y = eval(self.field_sigma_y.value)
                assert isinstance(self.blur_sigma_y,
                                  (int, float)), "`sigma_y` must be either of type float or int !"
            else:
                self.blur_sigma_y = None
        except Exception as x:
            print(f"Sigma Y Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # sigma_x
        try:
            if self.field_sigma_x.value:
                self.blur_sigma_x = eval(self.field_sigma_x.value)
                assert isinstance(self.blur_sigma_x,
                                  (int, float)), "`sigma_x` must be either of type float or int !"
            else:
                self.blur_sigma_x = None
        except Exception as x:
            print(f"Sigma X Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.blur_obj.current.blur.sigma_y = self.blur_sigma_y
        self.blur_obj.current.blur.sigma_x = self.blur_sigma_x
        self.blur_obj.current.blur.tile_mode = self.blur_tile_mode

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Blur!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the blur object/instance to the clipboard."""
        val = self.blur_obj.current.blur
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_always_on_top = True
        page.add(TabContentBlur())


    ft.app(main)
