import time
import flet as ft
import requests


def main(page: ft.Page):
    page.title = "IP Revealer"
    page.window_center()
    page.window_always_on_top = True
    page.vertical_alignment = page.horizontal_alignment = "center"
    page.window_min_width, page.window_min_height = 312, 124
    page.window_width, page.window_height = 386, 201

    ip_text = ft.Ref[ft.Text]()

    def fetch_ip():
        """
        Query the ipify service (https://www.ipify.org) to retrieve this device's public IP address.

        :rtype: string
        :returns: The public IP address of the requesting device as a string.
        :raises: RequestError if the web request failed
        """
        error = ""
        try:
            resp = requests.get('https://api.ipify.org')
        except requests.RequestException:
            error = "The request failed, most likely due to an networking error. Check you Internet connection."
        else:
            if resp.status_code != 200:
                error = 'Received an invalid status code from ipify:' + str(
                    resp.status_code) + '. The service might be experiencing issues.'
            else:
                ip_text.current.value = resp.text
                page.update()

        if error:
            for i in [error, "Retrying in some few seconds..."]:
                print(i)
                page.show_snack_bar(
                    ft.SnackBar(
                        content=ft.Text(i),
                        open=True
                    )
                )
                time.sleep(9)

            # retry again
            fetch_ip()

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("</Your Public IP>", weight=ft.FontWeight.BOLD, size=15),
                    ft.Text("000.000.000", ref=ip_text, weight=ft.FontWeight.BOLD, size=25, color=ft.colors.WHITE)
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            # I came up with this gradient using Flutils - https://flutils.pages.dev
            gradient=ft.LinearGradient(
                colors=['white38', 'white12'],
                tile_mode=ft.GradientTileMode.CLAMP,
                rotation=4.712,
                stops=[0.01, 0.6],
                begin=ft.Alignment(x=-1, y=0),
                end=ft.Alignment(x=1, y=0),
                type='linear'
            ),
            width=270
        )
    )

    # go get the IP
    fetch_ip()


ft.app(main)
