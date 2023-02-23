import flet as ft


# the content of the Shape tab
class TabContentShape(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = ft.Ref[ft.Container]()

        self.radios = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="rectangle", label="Rectangle"),
                    ft.Radio(value="circle", label="Circle")
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            value="rectangle",
            on_change=self.update_shape,

        )

    def update_shape(self, e: ft.ControlEvent):
        """
        It updates the Shape of the container object.

        :param e: The event object
        """
        _shape = self.radios.value

        # update container's shape
        self.container_obj.current.shape = ft.BoxShape(_shape)
        self.update()

        # show a snackbar to account for the changes
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Shape!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the shape used by the container to the clipboard.

        :param e: The event object
        """
        # update the text in the clipboard
        e.page.set_clipboard(f"BoxShape('{self.container_obj.current.shape}')")

        # show a snackbar to account for the changes
        e.page.show_snack_bar(
            ft.SnackBar(ft.Text(f"Copied: BoxShape('{self.container_obj.current.shape}')"), open=True))

    def build(self):
        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Shape:", weight=ft.FontWeight.BOLD, size=21),
                        self.radios
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,

                ),
                ft.Row(
                    [
                        ft.Container(
                            ref=self.container_obj,
                            bgcolor=ft.colors.GREEN,
                            width=180,
                            height=180,
                            shape=ft.BoxShape("rectangle"),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/#shape")
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
        page.add(TabContentShape())


    ft.app(main)
