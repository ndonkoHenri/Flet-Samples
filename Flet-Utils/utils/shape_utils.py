from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  FilledButton, Container, Column,
                  Ref, FilledTonalButton, RadioGroup, Radio)
from flet.control_event import ControlEvent
from flet.types import BoxShape


# the content of the Shape tab
class TabContentShape(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_shape(e: ControlEvent):
            """
            It updates the Shape of the container object.

            :param e: The event object
            """
            _shape = radios.value

            # update container's shape
            container_obj.current.shape = BoxShape(_shape)
            self.update()

            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text("Updated Shape!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the shape used by the container to the clipboard.

            :param e: The event object
            """
            # update the text in the clipboard
            e.page.set_clipboard(f"BoxShape('{container_obj.current.shape}')")

            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: BoxShape('{container_obj.current.shape}')"), open=True))

        container_obj = Ref[Container]()

        # radio buttons for the Shape object
        radios = RadioGroup(
            Row(
                [
                    Radio(value="rectangle", label="Rectangle"),
                    Radio(value="circle", label="Circle")
                ],
                alignment="center",
            ),
            value="rectangle",
            on_change=update_shape,

        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Shape:", weight="bold", size=21),
                        radios
                    ],
                    alignment="spaceBetween",

                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.GREEN,
                            width=180,
                            height=180,
                            shape=BoxShape("rectangle"),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#shape")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )