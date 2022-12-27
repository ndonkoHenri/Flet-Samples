# I pushed some stuffs into here to make th main.py file cleaner

import flet as ft

# the list view for the main page
main_listview = ft.ListView(
    expand=True,
    spacing=1,
    divider_thickness=0.2,
    first_item_prototype=True
)

# the appbar to be shown on the main/entry page
main_appbar = ft.AppBar(
    title=ft.Text(
        "Startup Name Generator",
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        size=18
    ),
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    center_title=True,
    actions=[
        ft.IconButton(
            ft.icons.LIST,
            tooltip='Saved Suggestions',
            icon_color=ft.colors.BLACK,
            on_click=lambda e: e.page.go("/favorites"),     # if pressed, move to the favorites page
        )
    ],
    elevation=4  # will only be seen when Theme.use_material3=False
)

# the appbar to be shown on the favorites page
favorites_appbar = ft.AppBar(
    title=ft.Text(
        "Saved Suggestions",
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        size=18
    ),
    bgcolor=ft.colors.WHITE,
    color=ft.colors.BLACK,
    center_title=True,
    elevation=4  # will only be seen when Theme.use_material3=False
)

favorites_view = ft.View(
    "/favorites",
    controls=[
        ft.ListView(
            expand=True,
            spacing=1,
            divider_thickness=0.2,
            first_item_prototype=True
        )
    ],
    appbar=favorites_appbar,
    bgcolor=ft.colors.WHITE
)
