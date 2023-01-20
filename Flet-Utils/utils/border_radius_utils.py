from flet import (colors, border_radius, icons, padding, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column, KeyboardType,
                  Ref, FilledTonalButton, Divider, MainAxisAlignment, ControlEvent, FontWeight, ScrollMode)


# the content of the border radius tab
class TabContentBorderRadius(UserControl):
    def __init__(self):
        super().__init__()
        # text field for topLeft(tl) property of the BorderRadius object
        self.field_tl = TextField(
            label="topLeft",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for topRight(tr) property of the BorderRadius object
        self.field_tr = TextField(
            label="topRight",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for bottomLeft(bl) property of the BorderRadius object
        self.field_bl = TextField(
            label="bottomLeft",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for bottomRight(br) property of the BorderRadius object
        self.field_br = TextField(
            label="bottomRight",
            value="",
            width=120,
            height=50,
            on_change=self.update_border_radius,
            keyboard_type=KeyboardType.NUMBER
        )
        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size
        )

        self.container_obj = Ref[Container]()
        self.container_text = Ref[Text]()

    def update_border_radius(self, e: ControlEvent):
        """
        It updates the border radius of the container object.

        :param e: The event object
        """

        if e.control.value.strip().isnumeric() or not e.control.value.strip():
            # if the value of the text field in focus is numeric or if it is empty...
            self.container_obj.current.border_radius = border_radius.BorderRadius(
                int(self.field_tl.value.strip()) if self.field_tl.value.strip().isnumeric() else 0,
                int(self.field_tr.value.strip()) if self.field_tr.value.strip().isnumeric() else 0,
                int(self.field_bl.value.strip()) if self.field_bl.value.strip().isnumeric() else 0,
                int(self.field_br.value.strip()) if self.field_br.value.strip().isnumeric() else 0, )
            self.container_text.current.value = f"{int(self.field_tl.value.strip()) if self.field_tl.value.strip().isnumeric() else 0}, {int(self.field_tr.value.strip()) if self.field_tr.value.strip().isnumeric() else 0}, {int(self.field_bl.value.strip()) if self.field_bl.value.strip().isnumeric() else 0}, {int(self.field_br.value.strip()) if self.field_br.value.strip().isnumeric() else 0} "
            self.update()
            e.page.show_snack_bar(SnackBar(Text("Updated BorderRadius!"), open=True))

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
        e.page.set_clipboard(f"{self.container_obj.current.border_radius}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.border_radius}"), open=True))

    def build(self):

        all_fields = Row(
            controls=[
                self.field_tl, self.field_tr, self.field_bl, self.field_br
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
                        Text("BorderRadius Builder:", weight=FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            content=Text(
                                "0, 0, 0, 0",
                                ref=self.container_text,
                                weight=FontWeight.BOLD,
                                size=18,
                                color="black"),
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
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
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#border_radius")
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )
