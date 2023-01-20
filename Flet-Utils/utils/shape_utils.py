from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  FilledButton, Container, Column, MainAxisAlignment, FontWeight, ScrollMode,
                  Ref, FilledTonalButton, RadioGroup, Radio, BoxShape, ControlEvent)


# the content of the Shape tab
class TabContentShape(UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = Ref[Container]()

        self.radios = RadioGroup(
            Row(
                [
                    Radio(value="rectangle", label="Rectangle"),
                    Radio(value="circle", label="Circle")
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            value="rectangle",
            on_change=self.update_shape,

        )

    def update_shape(self, e: ControlEvent):
        """
        It updates the Shape of the container object.

        :param e: The event object
        """
        _shape = self.radios.value

        # update container's shape
        self.container_obj.current.shape = BoxShape(_shape)
        self.update()

        # show a snackbar to account for the changes
        e.page.show_snack_bar(SnackBar(Text("Updated Shape!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the shape used by the container to the clipboard.

        :param e: The event object
        """
        # update the text in the clipboard
        e.page.set_clipboard(f"BoxShape('{self.container_obj.current.shape}')")

        # show a snackbar to account for the changes
        e.page.show_snack_bar(SnackBar(Text(f"Copied: BoxShape('{self.container_obj.current.shape}')"), open=True))

    def build(self):

        return Column(
            [
                Column(
                    [
                        Text("Container's Shape:", weight=FontWeight.BOLD, size=21),
                        self.radios
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN,

                ),
                Row(
                    [
                        Container(
                            ref=self.container_obj,
                            bgcolor=colors.GREEN,
                            width=180,
                            height=180,
                            shape=BoxShape("rectangle"),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#shape")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )
