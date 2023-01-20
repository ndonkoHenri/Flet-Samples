from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  FilledButton, Container, Column,
                  alignment, Ref, FilledTonalButton, Slider, ControlEvent, MainAxisAlignment, FontWeight, ScrollMode)


# the content of the alignment tab
class TabContentAlignment(UserControl):
    def __init__(self):
        super().__init__()
        # slider for x parameter of the Alignment object
        self.slider_x = Slider(
            label="x",
            value=0,
            on_change=self.update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )
        # slider for y parameter of the Alignment object
        self.slider_y = Slider(
            label="y",
            value=0,
            on_change=self.update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )

        self.container_button = Ref[FilledTonalButton]()
        self.container_obj = Ref[Container]()

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the alignment used by the container to the clipboard.
        :param e: The event object
        """
        # update the text in the clipboard
        e.page.set_clipboard(f"{self.container_obj.current.alignment}")
        # show a snackbar to account for the changes
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.alignment}"), open=True))

    def update_alignment(self, e: ControlEvent):
        """
        It updates the alignment of the container object.
        :param e: The event object
        """
        # round the values from the sliders to 2 decimals to avoid long values, and store result in variables
        x = round(float(self.slider_x.value), 2)
        y = round(float(self.slider_y.value), 2)
        # update container's alignment
        self.container_obj.current.alignment = alignment.Alignment(x, y)
        # update the text of the button in the container
        self.container_button.current.text = f"Pos: {x},{y}"
        self.update()
        # show a snackbar to account for the changes
        e.page.show_snack_bar(SnackBar(Text("Updated Alignment!"), open=True))

    def build(self):
        all_sliders = Row(
            controls=[
                self.slider_x,
                self.slider_y
            ],
            wrap=True
        )

        return Column(
            [
                Column(
                    [
                        Text("Alignment Builder:", weight=FontWeight.BOLD, size=21),
                        Text("CheatSheet:\ntopLeft = (-1,-1) | topCenter = (0,1) | topRight = (1,-1)\ncenterLeft = ("
                             "-1,0) | Center = (0,0) | centerRight = (1,0)\nbottomLeft = (-1,1) | bottomCenter = ("
                             "0,1) | bottomRight = (1,1)", italic=True, ),
                        all_sliders
                    ],
                    alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        Container(
                            content=FilledTonalButton("Pos: 0.0,0.0", self.container_button, disabled=True),
                            expand=True,
                            ref=self.container_obj,
                            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
                            width=160,
                            height=160,
                            alignment=alignment.Alignment(0, 0),  # align its contents in the center
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#alignment")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )
