from itertools import islice

from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  TextField, IconButton, GridView, TextButton, Container, Icon, Column,
                  alignment, TextAlign, MainAxisAlignment, CrossAxisAlignment)


# the content of the Icons tab
class TabContentIcons(UserControl):
    # all this below was obtained from https://github.com/flet-dev/examples/tree/main/python/apps/icons-browser

    def __init__(self):
        super().__init__()

    def build(self):
        def batches(iterable, batch_size):
            """
            It takes an iterable and a batch size, and returns an iterator that yields batches of the iterable

            :param iterable: An iterable object (e.g. a list) that you want to split into batches
            :param batch_size: The number of items to process in each batch
            """
            iterator = iter(iterable)
            while batch := list(islice(iterator, batch_size)):
                yield batch

        # fetch all icon constants from icons.py module
        icons_list = []
        list_started = False
        for key, value in vars(icons).items():
            if key == "TEN_K":
                list_started = True
            if list_started:
                icons_list.append(value)

        # search field
        search_txt = TextField(
            expand=1,
            hint_text="Enter keyword and press search button",
            autofocus=True,
            on_submit=lambda e: display_icons(e.control.value),
        )

        def search_click(_):
            """
            It takes the value of the search box and passes it as parameter to the display_icons function

            :param _:
            :type _: The event that triggered the function
            """
            display_icons(search_txt.value)

        search_query = Row(
            [search_txt, IconButton(icon=icons.SEARCH, on_click=search_click)]
        )

        # the grid in which the results will be displayed
        search_results = GridView(
            expand=1,
            runs_count=10,
            max_extent=150,
            spacing=5,
            run_spacing=5,
            child_aspect_ratio=1,
        )
        status_bar = Text()

        def copy_to_clipboard(e):
            """
            When the user clicks on an icon, the icon's value is copied to the clipboard,
            and a snackbar is shown to account for the changes.

            :param e: The event object
            """
            icon_key = e.control.data
            print("Copy to clipboard:", icon_key)
            self.page.set_clipboard(e.control.data)
            self.page.show_snack_bar(SnackBar(Text(f"Copied: {icon_key}"), open=True))

        def search_icons(search_term: str):
            """
            It takes a search term and returns a generator object that yields the icon names that
            contain the search term

            :param search_term: The search term that the user entered
            :type search_term: str
            """
            for icon_name in icons_list:
                if search_term != "" and search_term in icon_name:
                    yield icon_name

        def display_icons(search_term: str):
            """
            It takes a search term, disables the search box, cleans the search results, and then loops through the
            search results in batches of 200, adding each icon to the search results(the displayed grid).

            :param search_term: str - the search term to use
            :type search_term: str
            """

            # clean search results
            search_query.disabled = True
            self.update()

            search_results.clean()

            for batch in batches(search_icons(search_term.lower()), 200):
                for icon_name in batch:
                    icon_key = f"icons.{icon_name.upper()}"
                    search_results.controls.append(
                        TextButton(
                            content=Container(
                                content=Column(
                                    [
                                        Icon(name=icon_name, size=30),
                                        Text(
                                            value=f"{icon_name}",
                                            size=12,
                                            width=100,
                                            no_wrap=True,
                                            text_align=TextAlign.CENTER,
                                            color=colors.ON_SURFACE_VARIANT,
                                        ),
                                    ],
                                    spacing=5,
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                ),
                                alignment=alignment.center,
                            ),
                            tooltip=f"{icon_key}\nClick to copy to a clipboard",
                            on_click=copy_to_clipboard,
                            data=icon_key,
                        )
                    )
                status_bar.value = f"Icons found: {len(search_results.controls)}"
                self.update()

            # if there are no results, a snackbar shows up to let the user be aware
            if len(search_results.controls) == 0:
                self.page.show_snack_bar(SnackBar(Text("No icons found"), open=True))
            search_query.disabled = False
            self.update()

        return Column(
            [
                search_query,
                search_results,
                status_bar,
            ],
            expand=True,
        )
