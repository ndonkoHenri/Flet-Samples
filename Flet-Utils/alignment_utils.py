from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  FilledButton, Container, Column,
                  alignment, Ref, FilledTonalButton, Slider)
from flet.control_event import ControlEvent


# the content of the alignment tab
class TabContentAlignment(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_alignment(e: ControlEvent):
            """
            It updates the alignment of the container object.

            :param e: The event object
            """
            # round the values from the sliders to 2 decimals to avoid long values, and store result in variables
            x = round(float(slider_x.value), 2)
            y = round(float(slider_y.value), 2)
            # update container's alignment
            container_obj.current.alignment = alignment.Alignment(x, y)
            # update the text of the button in the container
            container_button.current.text = f"Pos: {x},{y}"
            self.update()
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text("Updated Alignment!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the alignment used by the container to the clipboard.

            :param e: The event object
            """
            # update the text in the clipboard
            e.page.set_clipboard(f"{container_obj.current.alignment}")
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.alignment}"), open=True))

        container_button = Ref[FilledTonalButton]()
        container_obj = Ref[Container]()

        # slider for x parameter of the Alignment object
        slider_x = Slider(
            label="x",
            value=0,
            on_change=update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )
        # slider for y parameter of the Alignment object
        slider_y = Slider(
            label="y",
            value=0,
            on_change=update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )

        # a row containing all the sliders created above
        all_sliders = Row(
            controls=[
                slider_x,
                slider_y
            ],
            # alignment="center",
            wrap=True
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Alignment:", weight="bold", size=21),
                        Text("CheatSheet:\ntopLeft = (-1,-1) | topCenter = (0,1) | topRight = (1,-1)\ncenterLeft = ("
                             "-1,0) | Center = (0,0) | centerRight = (1,0)\nbottomLeft = (-1,1) | bottomCenter = ("
                             "0,1) | bottomRight = (1,1)", italic=True, ),
                        all_sliders
                    ],
                    alignment="center"),
                Row(
                    [
                        Container(
                            content=FilledTonalButton("Pos: 0.0,0.0", container_button, disabled=True),
                            expand=True,
                            ref=container_obj,
                            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
                            width=160,
                            height=160,
                            alignment=alignment.Alignment(0, 0),  # align its contents in the center
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#alignment")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )
