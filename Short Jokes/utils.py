import flet as ft


class JokeCard(ft.Card):
    # elevation when this card is not hovered
    NORMAL_ELEVATION = 3
    # elevation when this card is hovered
    HOVERED_ELEVATION = 7

    def __init__(self, joke_id: int, joke: str = "This is a Joke bro. Haha!"):
        super(JokeCard, self).__init__(elevation=self.NORMAL_ELEVATION)
        self.joke_id = str(joke_id)
        self.joke = joke
        self.col = {"sm": 6, "md": 4}

    def _build(self):
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text(
                        f"Joke #{self.joke_id} 😂",
                        weight=ft.FontWeight.BOLD,
                        font_family="SpaceGrotesk"
                    ),
                    ft.Text(
                        self.joke,
                        weight=ft.FontWeight.BOLD,
                        font_family="Kalam",
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                on_click=self.copy_joke,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.COPY, color=ft.colors.GREEN_ACCENT_700),
                                        ft.Text("Copy", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_ACCENT_700)
                                    ],
                                )
                            ),
                            ft.TextButton(
                                on_click=self.delete_joke_card,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.DELETE, color=ft.colors.RED_ACCENT_700),
                                        ft.Text("Delete", color=ft.colors.RED_ACCENT_700)
                                    ],
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                ],
            ),
            width=400,
            padding=10,
            on_hover=self.hover_elevation,
            # bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=18,
        )

    def copy_joke(self, e):
        """When the 'copy' btn is clicked, copy the joke."""
        self.page.set_clipboard(self.joke)
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text(f"Copied Joke to Clipboard!", font_family="SpaceGrotesk"),
                open=True
            )
        )

    def delete_joke_card(self, e):
        """When the 'delete' btn is clicked, delete this card."""
        self.page.jokes_row.controls.remove(self)
        self.update()
        self.page.update()
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text(f"Joke was successfully deleted!", font_family="SpaceGrotesk"),
                open=True
            )
        )

    def hover_elevation(self, e):
        """When the card is hovered, increase the elevation."""
        self.elevation = self.HOVERED_ELEVATION if self.elevation == self.NORMAL_ELEVATION else self.NORMAL_ELEVATION
        self.update()


ethical_signature = ft.Text(
    "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
    style=ft.TextThemeStyle.LABEL_SMALL,
    weight=ft.FontWeight.BOLD,
    color=ft.colors.BLUE_900,
)

