from flet import (colors, icons, padding, border, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column, FontWeight, ScrollMode,
                  Ref, FilledTonalButton, Divider, MainAxisAlignment, KeyboardType, ControlEvent, BorderSide)


# todo: add respective colors to each

# the content of the border tab
class TabContentBorder(UserControl):
    # border = border.only(BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"),)
    def __init__(self):
        super().__init__()
        self.container_obj = Ref[Container]()

        # text field for left property of the Border object
        self.field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for right property of the Border object
        self.field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for top property of the Border object
        self.field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for bottom property of the Border object
        self.field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_border,
            keyboard_type=KeyboardType.NUMBER
        )

        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

    def update_border(self, e: ControlEvent):
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
            self.container_obj.current.border = border.only(BorderSide(left, colors.GREEN_700),
                                                            BorderSide(top, colors.GREEN_700),
                                                            BorderSide(right, colors.GREEN_700),
                                                            BorderSide(bottom, colors.GREEN_700))
            self.update()
            e.page.show_snack_bar(SnackBar(Text("Updated Border!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def update_container_size(self, e: ControlEvent):
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
            e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the border radius of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.border}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.border}"), open=True))

    def build(self):
        all_fields = Row(
            controls=[
                self.field_left, self.field_right, self.field_top, self.field_bottom
            ],
            alignment=MainAxisAlignment.CENTER,
        )
        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight=FontWeight.BOLD, size=21),
                        Row(
                            [self.field_width, self.field_height],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Border:", weight=FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border=border.all(0, colors.TRANSPARENT),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#border")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )
