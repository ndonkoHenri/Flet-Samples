import flet as ft
from flet import padding


# the content of the padding tab
class TabContentPadding(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container_front = ft.Ref[ft.Container]()
        self.container_back = ft.Ref[ft.Container]()
        self.container_text = ft.Ref[ft.Text]()

        # text field for left parameter of the Padding object
        self.field_left = ft.TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        # text field for top parameter of the Padding object
        self.field_top = ft.TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        # text field for right parameter of the Padding object
        self.field_right = ft.TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        # text field for bottom parameter of the Padding object
        self.field_bottom = ft.TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=ft.KeyboardType.NUMBER,
        )
        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_front_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_front_container_size,
        )

    def update_front_container_padding(self, e: ft.ControlEvent):
        """
        It updates the padding of the container object.

        :param e: The event object
        """
        # if the value of the text field in focus is numeric or if it is empty...
        if e.control.value.strip().isnumeric() or not e.control.value.strip():
            # update the container's padding values
            self.container_back.current.padding = ft.padding.Padding(
                int(self.field_left.value.strip()) if self.field_left.value.strip().isnumeric() else 0,
                int(self.field_top.value.strip()) if self.field_top.value.strip().isnumeric() else 0,
                int(self.field_right.value.strip()) if self.field_right.value.strip().isnumeric() else 0,
                int(self.field_bottom.value.strip()) if self.field_bottom.value.strip().isnumeric() else 0,
            )
            # update the text in the container
            self.container_text.current.value = f"{int(self.field_left.value.strip()) if self.field_left.value.strip().isnumeric() else 0}, {int(self.field_top.value.strip()) if self.field_top.value.strip().isnumeric() else 0}, {int(self.field_right.value.strip()) if self.field_right.value.strip().isnumeric() else 0}, {int(self.field_bottom.value.strip()) if self.field_bottom.value.strip().isnumeric() else 0} "
            self.update()
            # show a snackbar to account for the changes
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Padding!"), open=True))

        else:
            # Show a snackbar with an error message, in case the above condition is not met.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def update_front_container_size(self, e: ft.ControlEvent):
        """
        The function updates the container size when the width or height values are changed.
        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_front.current.height = int(
                self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else 160
            self.container_front.current.width = int(
                self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else 160
            self.container_front.current.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container's Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the padding of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_back.current.padding}")
        # show a snackbar to account for the changes
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_back.current.padding}"), open=True))

    def build(self):
        all_fields = ft.Row(
            controls=[
                self.field_left, self.field_top, self.field_right, self.field_bottom
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
                        ft.Divider(height=2),
                        ft.Text("Container's Padding:", weight=ft.FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Container(
                                ft.Text(
                                    "0, 0, 0, 0",
                                    ref=self.container_text,
                                    weight=ft.FontWeight.BOLD,
                                    size=18,
                                    color="black"
                                ),
                                ref=self.container_front,
                                bgcolor=ft.colors.BLUE_700,
                                padding=ft.Padding(0, 0, 0, 0),
                                alignment=ft.Alignment(0, 0),
                                width=float(self.field_width.value),
                                height=float(self.field_height.value),
                            ),
                            expand=True,
                            height=250,
                            ref=self.container_back,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.Padding(0, 0, 0, 0),
                            alignment=ft.Alignment(0, 0),  # align its contents in the center
                            border_radius=ft.border_radius.BorderRadius(0, 0, 0, 0),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#padding")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentPadding())


    ft.app(main)
