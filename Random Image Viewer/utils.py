import base64
import random

import flet as ft
import requests


# todo: add grayscale and blur

class ImageCard(ft.Card):
    # elevation when this card is not hovered
    NORMAL_ELEVATION = 3
    # elevation when this card is hovered
    HOVERED_ELEVATION = 7

    def __init__(self, img_id: int):
        super(ImageCard, self).__init__(elevation=self.NORMAL_ELEVATION)
        self.img_id = str(img_id)
        self.random_id = random.randint(0, 1050)  # get a random number/id
        # images are gotten from https://picsum.photos | I hardcoded a size of 200x300
        self.random_img_url = f"https://picsum.photos/id/{self.random_id}/200/300"

        # defines the responsiveness of this card (what amount of space should be occupied) on different window sizes
        # see docs https://flet.dev/docs/controls/responsiverow/
        self.col = {"xs": 12, "sm": 6, "md": 5, "lg": 4, "xl": 3, "xxl": 2.4}

        # the content of this card
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        controls=[
                            ft.Text(
                                f"Image #{self.img_id} 📸",
                                weight=ft.FontWeight.BOLD,
                                font_family="SpaceGrotesk"
                            )
                        ],
                        alignment=ft.MainAxisAlignment.END
                    ),
                    ft.Row(
                        controls=[
                            ft.Image(
                                src=self.random_img_url,
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),
                    ft.Row(
                        [
                            ft.TextButton(
                                on_click=self.copy_img_url,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.COPY, color=ft.colors.GREEN_ACCENT_700),
                                        ft.Text("Copy URL", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_ACCENT_700)
                                    ],
                                )
                            ),
                            ft.TextButton(
                                on_click=self.launch_img_url,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.DOWNLOAD, color=ft.colors.GREEN_ACCENT_700),
                                        ft.Text("Download", weight=ft.FontWeight.BOLD, color=ft.colors.GREEN_ACCENT_700)
                                    ],
                                )
                            ),
                            ft.TextButton(
                                on_click=self.delete_img_card,
                                content=ft.Row(
                                    [
                                        ft.Icon(ft.icons.DELETE, color=ft.colors.RED_ACCENT_700),
                                        ft.Text("Delete", color=ft.colors.RED_ACCENT_700)
                                    ],
                                ),
                            ),
                        ],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        wrap=True
                    ),
                ],
            ),
            padding=10,
            on_hover=self.hover_elevation,
            # bgcolor=ft.colors.BLUE_GREY_100,
            border_radius=18,
        )

    def launch_img_url(self, e):
        """Opens the image in the browser, so the user downloads from there. See it as a way to avoid copyright issues."""
        self.page.launch_url(self.random_img_url)
        self.page.show_snack_bar(
            ft.SnackBar(
                ft.Text("Opened original Image. Download from there please.", font_family="SpaceGrotesk"),
                open=True
            )
        )

    def copy_img_url(self, e):
        """Copies the url of this image to the clipboard, and then shows a snackbar to notify the user."""
        self.page.set_clipboard(self.random_img_url)
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("Image URL copied to clipboard."), open=True)
        )

    def delete_img_card(self, e):
        """When the 'delete' btn is clicked, this card is deleted, and then shows a snackbar to notify the user."""
        self.page.images_row.controls.remove(self)
        self.update()
        self.page.update()
        self.page.show_snack_bar(
            ft.SnackBar(ft.Text("Deletion successful!"), open=True)
        )

    def hover_elevation(self, e):
        """When the card is hovered, increase the elevation and vice-versa."""
        self.elevation = self.HOVERED_ELEVATION if self.elevation == self.NORMAL_ELEVATION else self.NORMAL_ELEVATION
        self.update()


# not used
def get_root_url(base_url: str):
    """
    Takes a base url as an argument, makes a request to the server to get the image and
    returns the specific/precise url of this image.

    :param base_url: the url of the image you want to download
    :type base_url: str
    :return: The specific url of the image
    """
    r = requests.get(base_url)
    specific_image_url = r.url
    # print(base_url, specific_image_url)
    return specific_image_url
