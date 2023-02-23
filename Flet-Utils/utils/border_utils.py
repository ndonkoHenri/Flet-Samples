import flet as ft


# todo: add respective colors to each

# the content of the border tab
class TabContentBorder(ft.UserControl):
    # border = border.only(BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"),)
    def __init__(self):
        super().__init__()
        self.container_obj = ft.Ref[ft.Container]()

        # text field for left property of the Border object
        self.field_left = ft.TextField(
            label="left",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for right property of the Border object
        self.field_right = ft.TextField(
            label="right",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for top property of the Border object
        self.field_top = ft.TextField(
            label="top",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for bottom property of the Border object
        self.field_bottom = ft.TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=ft.KeyboardType.NUMBER
        )

        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

    def update_border(self, e: ft.ControlEvent):
        """
        It updates the border radius of the container object.
        :param e: The event object
        """
        left, right, top, bottom = int(
            self.field_left.value.strip()) if self.field_left.value.strip().isnumeric() else 0, int(
            self.field_right.value.strip()) if self.field_right.value.strip().isnumeric() else 0, int(
            self.field_top.value.strip()) if self.field_top.value.strip().isnumeric() else 0, int(
            self.field_bottom.value.strip()) if self.field_bottom.value.strip().isnumeric() else 0

        if e.control.value.strip().isnumeric() or not e.control.value.strip():
            # if the value of the text field in focus is numeric or if it is empty...
            self.container_obj.current.border = ft.border.only(
                ft.BorderSide(left, ft.colors.GREEN_700),
                ft.BorderSide(top, ft.colors.GREEN_700),
                ft.BorderSide(right, ft.colors.GREEN_700),
                ft.BorderSide(bottom, ft.colors.GREEN_700)
            )
            self.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Border!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def update_container_size(self, e: ft.ControlEvent):
        """
        The function updates the container size when the width or height values are changed.

        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_obj.current.height = int(
                self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else 160
            self.container_obj.current.width = int(
                self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else 160
            self.container_obj.current.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the border radius of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.border}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.border}"), open=True))

    def build(self):
        all_fields = ft.Row(
            controls=[
                self.field_left, self.field_right, self.field_top, self.field_bottom
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Size:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Row(
                            [self.field_width, self.field_height],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=2, thickness=2),
                        ft.Text("Container's Border:", weight=ft.FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=ft.Alignment(0, 0),
                            border=ft.border.all(0, ft.colors.TRANSPARENT),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#border")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentBorder())


    ft.app(main)
