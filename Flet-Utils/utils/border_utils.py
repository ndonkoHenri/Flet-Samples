from flet import (colors, icons, padding, border, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column,
                  Ref, FilledTonalButton, Divider)
from flet.control_event import ControlEvent


# the content of the border tab
class TabContentBorder(UserControl):
    # border = border.only(BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"),)

    def build(self):
        def update_border(e: ControlEvent):
            """
            It updates the border radius of the container object.

            :param e: The event object
            """
            left, right, top, bottom = int(
                field_left.value.strip()) if field_left.value.strip().isnumeric() else 0, int(
                field_right.value.strip()) if field_right.value.strip().isnumeric() else 0, int(
                field_top.value.strip()) if field_top.value.strip().isnumeric() else 0, int(
                field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0

            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # if the value of the text field in focus is numeric or if it is empty...
                container_obj.current.border = border.only(border.BorderSide(left, colors.TEAL_900),
                                                           border.BorderSide(top, colors.TEAL_900),
                                                           border.BorderSide(right, colors.TEAL_900),
                                                           border.BorderSide(bottom, colors.TEAL_900))
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Border!"), open=True))

            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the border radius of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.border}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.border}"), open=True))

        container_obj = Ref[Container]()

        # text field for left property of the Border object
        field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for right property of the Border object
        field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for top property of the Border object
        field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for bottom property of the Border object
        field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_left, field_right, field_top, field_bottom
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Border:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border=border.all(0, colors.TRANSPARENT),
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#border")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )
