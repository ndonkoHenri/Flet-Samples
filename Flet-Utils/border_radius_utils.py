from flet import (colors, border_radius, icons, padding, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column,
                  Ref, FilledTonalButton, Divider)
from flet.control_event import ControlEvent


# the content of the border radius tab
class TabContentBorderRadius(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_border_radius(e: ControlEvent):
            """
            It updates the border radius of the container object.

            :param e: The event object
            """

            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # if the value of the text field in focus is numeric or if it is empty...
                container_obj.current.border_radius = border_radius.BorderRadius(
                    int(field_tl.value.strip()) if field_tl.value.strip().isnumeric() else 0,
                    int(field_tr.value.strip()) if field_tr.value.strip().isnumeric() else 0,
                    int(field_bl.value.strip()) if field_bl.value.strip().isnumeric() else 0,
                    int(field_br.value.strip()) if field_br.value.strip().isnumeric() else 0, )
                container_text.current.value = f"{int(field_tl.value.strip()) if field_tl.value.strip().isnumeric() else 0}, {int(field_tr.value.strip()) if field_tr.value.strip().isnumeric() else 0}, {int(field_bl.value.strip()) if field_bl.value.strip().isnumeric() else 0}, {int(field_br.value.strip()) if field_br.value.strip().isnumeric() else 0} "
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated BorderRadius!"), open=True))

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
            e.page.set_clipboard(f"{container_obj.current.border_radius}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.border_radius}"), open=True))

        container_obj = Ref[Container]()
        container_text = Ref[Text]()

        # text field for topLeft(tl) property of the BorderRadius object
        field_tl = TextField(
            label="topLeft",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for topRight(tr) property of the BorderRadius object
        field_tr = TextField(
            label="topRight",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for bottomLeft(bl) property of the BorderRadius object
        field_bl = TextField(
            label="bottomLeft",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for bottomRight(br) property of the BorderRadius object
        field_br = TextField(
            label="bottomRight",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_tl, field_tr, field_bl, field_br
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
                        Text("Container's Border Radius:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            content=Text(
                                "0, 0, 0, 0",
                                ref=container_text,
                                weight="bold",
                                size=18,
                                color="black"),
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
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
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#border_radius")
                        ),
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )
