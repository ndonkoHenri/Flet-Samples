import flet as ft


# the content of the alignment tab
class TabContentAlignment(ft.UserControl):
    def __init__(self):
        super().__init__()
        # slider for x parameter of the Alignment object
        self.slider_x = ft.Slider(
            label="x",
            value=0,
            on_change=self.update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )
        # slider for y parameter of the Alignment object
        self.slider_y = ft.Slider(
            label="y",
            value=0,
            on_change=self.update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )

        self.container_button = ft.Ref[ft.FilledTonalButton]()
        self.container_obj = ft.Ref[ft.Container]()

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the alignment used by the container to the clipboard.
        :param e: The event object
        """
        # update the text in the clipboard
        e.page.set_clipboard(f"{self.container_obj.current.alignment}")
        # show a snackbar to account for the changes
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.alignment}"), open=True))

    def update_alignment(self, e: ft.ControlEvent):
        """
        It updates the alignment of the container object.
        :param e: The event object
        """
        # round the values from the sliders to 2 decimals to avoid long values, and store result in variables
        x = round(float(self.slider_x.value), 2)
        y = round(float(self.slider_y.value), 2)
        # update container's alignment
        self.container_obj.current.alignment = ft.Alignment(x, y)
        # update the text of the button in the container
        self.container_button.current.text = f"Pos: {x},{y}"
        self.update()
        # show a snackbar to account for the changes
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Alignment!"), open=True))

    def build(self):
        all_sliders = ft.Row(
            controls=[
                self.slider_x,
                self.slider_y
            ],
            wrap=True
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Alignment Builder:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Text(
                            "CheatSheet:\ntopLeft = (-1,-1) | topCenter = (0,-1) | topRight = (1,-1)\ncenterLeft = ("
                            "-1,0) | Center = (0,0) | centerRight = (1,0)\nbottomLeft = (-1,1) | bottomCenter = ("
                            "0,1) | bottomRight = (1,1)", italic=True, ),
                        all_sliders
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.FilledTonalButton(
                                content=ft.Text(
                                    "Pos: 0.0,0.0",
                                    weight=ft.FontWeight.BOLD
                                ),
                                ref=self.container_button,
                                disabled=True
                            ),
                            expand=True,
                            ref=self.container_obj,
                            bgcolor=ft.colors.DEEP_PURPLE_ACCENT_700,
                            width=160,
                            height=160,
                            alignment=ft.Alignment(0, 0),  # align its contents in the center
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Copy Value to Clipboard",
                            icon=ft.icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        ft.FilledTonalButton(
                            "Go to Docs",
                            icon=ft.icons.DATASET_LINKED_OUTLINED,
                            url="https://flet.dev/docs/controls/container/#alignment"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentAlignment())


    ft.app(main)
