# made by @ndonkoHenri aka TheEthicalBoy

import flet as ft
import utils


def main(page: ft.Page):
    def tile_clicked(e):
        """
        When a tile is clicked, if it's not a favorite, add it to the favorites page, otherwise remove it from the
        favorites page.
        """

        # tile item added to the favorites page (precisely into the list of favorites)
        if e.control.trailing.name == ft.icons.FAVORITE_BORDER:
            # change the icon and its color to reflect the event
            e.control.trailing.name = ft.icons.FAVORITE
            e.control.trailing.color = ft.colors.RED

            # addition to favorites page
            utils.favorites_view.controls[0].controls.append(
                ft.ListTile(
                    title=e.control.title
                )
            )

        # tile item removed from the favorites page (precisely from list of favorites)
        else:
            # change the icon and its color to reflect the event
            e.control.trailing.name = ft.icons.FAVORITE_BORDER
            e.control.trailing.color = None

            # removal from favorites page
            for fav_tile in utils.favorites_view.controls[0].controls:
                # check the type and content --- please use debug or add prints to better understand
                if isinstance(fav_tile, ft.ListTile) and fav_tile.title == e.control.title:
                    utils.favorites_view.controls[0].controls.remove(fav_tile)

        # update the page to reflect the current UI state
        page.update()

    def route_change(route):
        """
        Called whenever there's a change in the routes. (see https://flet.dev/docs/guides/python/navigation-and-routing)
        It clears the page's views and appends the main view (root view).
        If the route is /favorites, it appends the favorites view, and updates the page.
        """
        page.views.clear()
        page.views.append(main_view)

        if page.route == "/favorites":
            page.views.append(
                utils.favorites_view
            )
        page.update()

    def view_pop(view):
        """
        When the user clicks the back button, the current view is popped off the stack, and the previous view is loaded.
        """
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    # basic page settings
    page.title = "startup_namer"
    page.window_always_on_top = True
    page.fonts = {"San Fransisco": "/fonts/San-Francisco/SFUIDisplay-Light.ttf"}
    page.theme_mode = "light"
    page.theme = ft.Theme(
        font_family="San Fransisco",  # set as default font family
        use_material3=False,      # use material 2: this setting is mainly for the app-bar's elevation
    )

    # change the transition from one view to another to better mimic the Flutter example
    page.theme.page_transitions.windows = ft.PageTransitionTheme.CUPERTINO
    page.theme.page_transitions.macos = ft.PageTransitionTheme.CUPERTINO

    # set the callbacks for the navigation and routing of the app
    page.on_route_change = route_change
    page.on_view_pop = view_pop

    # Creating a list of tiles.
    for i in range(20):
        item_text = ft.Text(f"Name {i}")

        item_tile = ft.ListTile(
            title=item_text,
            on_click=tile_clicked,
            trailing=ft.Icon(
                ft.icons.FAVORITE_BORDER
            ),
        )

        # add the currently created tile to the listview (list of tiles)
        utils.main_listview.controls.append(item_tile)

    main_view = ft.View(
        "/",
        controls=page.controls,
    )

    page.add(
        utils.main_appbar,
        utils.main_listview
    )


ft.app(
    target=main,
    assets_dir="assets",  # https://flet.dev/docs/controls/image/#src
    route_url_strategy="path",  # https://flet.dev/docs/guides/python/navigation-and-routing#url-strategy-for-web
    # view=ft.WEB_BROWSER   # opens the app in the browser
)
