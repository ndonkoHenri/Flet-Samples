import flet as ft


# the content of the border radius tab
class TabContentBorderRadius(ft.UserControl):
    def __init__(self):
        super().__init__()
        # text field for topLeft(tl) property of the BorderRadius object
        self.field_tl = ft.TextField(
            label="topLeft",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for topRight(tr) property of the BorderRadius object
        self.field_tr = ft.TextField(
            label="topRight",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for bottomLeft(bl) property of the BorderRadius object
        self.field_bl = ft.TextField(
            label="bottomLeft",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for bottomRight(br) property of the BorderRadius object
        self.field_br = ft.TextField(
            label="bottomRight",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=ft.KeyboardType.NUMBER
        )
        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size
        )

        self.container_obj = ft.Ref[ft.Container]()
        self.container_text = ft.Ref[ft.Text]()

    def update_border_radius(self, e: ft.ControlEvent):
        """
        It updates the border radius of the container object.

        :param e: The event object
        """

        if e.control.value.strip().isnumeric() or not e.control.value.strip():
            # if the value of the text field in focus is numeric or if it is empty...
            self.container_obj.current.border_radius = ft.border_radius.BorderRadius(
                int(self.field_tl.value.strip()) if self.field_tl.value.strip().isnumeric() else 0,
                int(self.field_tr.value.strip()) if self.field_tr.value.strip().isnumeric() else 0,
                int(self.field_bl.value.strip()) if self.field_bl.value.strip().isnumeric() else 0,
                int(self.field_br.value.strip()) if self.field_br.value.strip().isnumeric() else 0, )
            self.container_text.current.value = f"{int(self.field_tl.value.strip()) if self.field_tl.value.strip().isnumeric() else 0}, {int(self.field_tr.value.strip()) if self.field_tr.value.strip().isnumeric() else 0}, {int(self.field_bl.value.strip()) if self.field_bl.value.strip().isnumeric() else 0}, {int(self.field_br.value.strip()) if self.field_br.value.strip().isnumeric() else 0} "
            self.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated BorderRadius!"), open=True))

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
        e.page.set_clipboard(f"{self.container_obj.current.border_radius}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.border_radius}"), open=True))

    def build(self):

        all_fields = ft.Row(
            controls=[
                self.field_tl, self.field_tr, self.field_bl, self.field_br
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
                        ft.Text("BorderRadius Builder:", weight=ft.FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "0, 0, 0, 0",
                                ref=self.container_text,
                                weight=ft.FontWeight.BOLD,
                                size=18,
                                color="black"),
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=ft.Alignment(0, 0),
                            border_radius=ft.BorderRadius(0, 0, 0, 0),
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
                            url="https://flet.dev/docs/controls/container#border_radius"
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentBorderRadius())


    ft.app(main)
