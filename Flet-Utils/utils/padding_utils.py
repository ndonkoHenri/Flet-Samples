from flet import (colors, border_radius, icons, padding, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column,
                  Ref, FilledTonalButton, Divider)
from flet.control_event import ControlEvent


# the content of the padding tab
class TabContentPadding(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):

        def update_front_container_padding(e: ControlEvent):
            """
            It updates the padding of the container object.

            :param e: The event object
            """
            # if the value of the text field in focus is numeric or if it is empty...
            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # update the container's padding values
                container_back.current.padding = padding.Padding(
                    int(field_left.value.strip()) if field_left.value.strip().isnumeric() else 0,
                    int(field_top.value.strip()) if field_top.value.strip().isnumeric() else 0,
                    int(field_right.value.strip()) if field_right.value.strip().isnumeric() else 0,
                    int(field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0,
                )
                # update the text in the container
                container_text.current.value = f"{int(field_left.value.strip()) if field_left.value.strip().isnumeric() else 0}, {int(field_top.value.strip()) if field_top.value.strip().isnumeric() else 0}, {int(field_right.value.strip()) if field_right.value.strip().isnumeric() else 0}, {int(field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0} "
                self.update()
                # show a snackbar to account for the changes
                e.page.show_snack_bar(SnackBar(Text("Updated Padding!"), open=True))

            else:
                # Show a snackbar with an error message, in case the above condition is not met.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def update_front_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_front.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_front.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_front.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container's Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the padding of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_back.current.padding}")
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_back.current.padding}"), open=True))

        container_front = Ref[Container]()
        container_back = Ref[Container]()
        container_text = Ref[Text]()

        # text field for left parameter of the Padding object
        field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for top parameter of the Padding object
        field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for right parameter of the Padding object
        field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for bottom parameter of the Padding object
        field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_left, field_top, field_right, field_bottom
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
            on_submit=update_front_container_size,
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_front_container_size,
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
                        Divider(height=2),
                        Text("Container's Padding:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            content=Container(
                                Text(
                                    "0, 0, 0, 0",
                                    ref=container_text,
                                    weight="bold",
                                    size=18,
                                    color="black"
                                ),
                                ref=container_front,
                                bgcolor=colors.BLUE_700,
                                padding=padding.Padding(0, 0, 0, 0),
                                alignment=Alignment(0, 0),
                                width=float(field_width.value),
                                height=float(field_height.value),
                            ),
                            expand=True,
                            height=250,
                            ref=container_back,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(0, 0, 0, 0),
                            alignment=Alignment(0, 0),  # align its contents in the center
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
                        )
                    ],
                    alignment="center"
                ),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#padding")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden",
        )
