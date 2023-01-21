from flet import (colors, border_radius, icons, padding, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column, ScrollMode,
                  Ref, FilledTonalButton, Divider, MainAxisAlignment, FontWeight, KeyboardType, ControlEvent)


# the content of the padding tab
class TabContentPadding(UserControl):
    def __init__(self):
        super().__init__()
        self.container_front = Ref[Container]()
        self.container_back = Ref[Container]()
        self.container_text = Ref[Text]()

        # text field for left parameter of the Padding object
        self.field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=KeyboardType.NUMBER,
        )
        # text field for top parameter of the Padding object
        self.field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=KeyboardType.NUMBER,
        )
        # text field for right parameter of the Padding object
        self.field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=KeyboardType.NUMBER,
        )
        # text field for bottom parameter of the Padding object
        self.field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=self.update_front_container_padding,
            keyboard_type=KeyboardType.NUMBER,
        )
        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_front_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_front_container_size,
        )

    def update_front_container_padding(self, e: ControlEvent):
        """
        It updates the padding of the container object.

        :param e: The event object
        """
        # if the value of the text field in focus is numeric or if it is empty...
        if e.control.value.strip().isnumeric() or not e.control.value.strip():
            # update the container's padding values
            self.container_back.current.padding = padding.Padding(
                int(self.field_left.value.strip()) if self.field_left.value.strip().isnumeric() else 0,
                int(self.field_top.value.strip()) if self.field_top.value.strip().isnumeric() else 0,
                int(self.field_right.value.strip()) if self.field_right.value.strip().isnumeric() else 0,
                int(self.field_bottom.value.strip()) if self.field_bottom.value.strip().isnumeric() else 0,
            )
            # update the text in the container
            self.container_text.current.value = f"{int(self.field_left.value.strip()) if self.field_left.value.strip().isnumeric() else 0}, {int(self.field_top.value.strip()) if self.field_top.value.strip().isnumeric() else 0}, {int(self.field_right.value.strip()) if self.field_right.value.strip().isnumeric() else 0}, {int(self.field_bottom.value.strip()) if self.field_bottom.value.strip().isnumeric() else 0} "
            self.update()
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text("Updated Padding!"), open=True))

        else:
            # Show a snackbar with an error message, in case the above condition is not met.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def update_front_container_size(self, e: ControlEvent):
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
            e.page.show_snack_bar(SnackBar(Text("Updated Container's Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the padding of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_back.current.padding}")
        # show a snackbar to account for the changes
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_back.current.padding}"), open=True))

    def build(self):
        all_fields = Row(
            controls=[
                self.field_left, self.field_top, self.field_right, self.field_bottom
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
                        Divider(height=2),
                        Text("Container's Padding:", weight=FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            content=Container(
                                Text(
                                    "0, 0, 0, 0",
                                    ref=self.container_text,
                                    weight=FontWeight.BOLD,
                                    size=18,
                                    color="black"
                                ),
                                ref=self.container_front,
                                bgcolor=colors.BLUE_700,
                                padding=padding.Padding(0, 0, 0, 0),
                                alignment=Alignment(0, 0),
                                width=float(self.field_width.value),
                                height=float(self.field_height.value),
                            ),
                            expand=True,
                            height=250,
                            ref=self.container_back,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(0, 0, 0, 0),
                            alignment=Alignment(0, 0),  # align its contents in the center
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#padding")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN,
        )
