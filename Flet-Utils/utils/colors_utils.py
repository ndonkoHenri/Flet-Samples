import time
from itertools import islice

from flet import (colors, icons, UserControl, SnackBar, Text, Row, TextCapitalization,
                  TextField, IconButton, GridView, TextButton, Container, Icon, Column,
                  FloatingActionButton, TextAlign, FontWeight, MainAxisAlignment, KeyboardType,
                  alignment, Tabs, Ref, ListView, Tab, CrossAxisAlignment, ControlEvent)


# the content of the ColorV1 tab
class TabContentColors1(UserControl):
    # all this below was obtained from https://github.com/ndonkoHenri/Flet-Color-Browser

    def __init__(self, expand=True):
        """
        If the expand parameter is set to True, then the expand attribute of the object is set to True. Otherwise, the
        height attribute of the object is set to the value of the height parameter.

        :param expand: If True, the widget will expand to fill its parent, defaults to True (optional)
        """
        super().__init__(expand=expand)

    def build(self):
        def batches(iterable, batch_size):
            """
            It takes an iterable and a batch size, and returns an iterator that yields batches of the iterable

            :param iterable: An iterable object (e.g. a list)
            :param batch_size: The number of items to process in each batch
            """
            iterator = iter(iterable)
            while batch := list(islice(iterator, batch_size)):
                yield batch

        # fetch all icon constants from colors.py module and store them in a dict(colors_dict)
        colors_dict = dict()
        list_started = False
        for key, value in vars(colors).items():
            if key == "PRIMARY":
                # 'PRIMARY' is the first color-variable (our starting point)
                list_started = True
            if list_started:
                # when this list_started is True, we create new key-value pair in our dictionary
                colors_dict[key] = value

        # Creating a text field
        search_txt = TextField(
            expand=1, hint_text="Enter keyword and press search button", autofocus=True,
            on_submit=lambda e: display_colors(e.control.value), tooltip="search field", label="Color Search Field"
        )

        def search_click(_):
            """
            Called when the search button is pressed, it displays the colors.
            """
            display_colors(search_txt.value)

        # Creating a row with a search text field and a search button.
        search_query = Row(
            [search_txt, FloatingActionButton(icon=icons.SEARCH, on_click=search_click, tooltip="search")]
        )

        # Creating a grid view with 10 columns and 150 pixels as the maximum extent of each column.
        search_results = GridView(
            expand=1, runs_count=10, max_extent=150, spacing=5, run_spacing=5, child_aspect_ratio=1,
        )
        status_bar = Text()

        def copy_to_clipboard(e):
            """
            When the user clicks on a color, copy the color key to the clipboard

            :param e: The event object
            """

            color_key = e.control.data
            print("Copied to clipboard:", color_key)
            self.page.set_clipboard(e.control.data)
            self.page.show_snack_bar(SnackBar(Text(f"Copied: {color_key}"), open=True))

        def search_colors(search_term: str):
            """
            It takes a search term as an argument, and then loops through the colors_dict dictionary,
            checking if the search term is in the color name or the color value. If it is, it yields the color key

            :param search_term: The search term that the user entered
            :return color_key: str
            """

            for color_key, color_value in colors_dict.items():
                # the color_key has underscores while the color_value doesn't. We take this into consideration
                if search_term and (search_term in color_value or search_term in color_key.lower()):
                    yield color_key

        def display_colors(search_term: str):
            """
            It takes a search term, disables the search box, cleans the search results(grid view),
            and then loops through the search results in batches of 40, adding each color to the search results

            :param search_term: str
            """

            # disable the text field and the search button, and clean search results
            search_query.disabled = True
            self.update()
            search_results.clean()

            # Adding the colors to the grid view in batches of 40.
            for batch in batches(search_colors(search_term.lower()), 40):
                for color_key in batch:
                    flet_color_key = f"colors.{color_key}"

                    search_results.controls.append(
                        TextButton(
                            content=Container(
                                content=Column(
                                    [
                                        Icon(name=icons.RECTANGLE, size=38, color=colors_dict[color_key], ),
                                        Text(
                                            value=f"{colors_dict[color_key]}", size=14, width=100,
                                            no_wrap=True, text_align=TextAlign.CENTER, color=colors_dict[color_key],
                                        ),
                                    ],
                                    spacing=5,
                                    alignment=MainAxisAlignment.CENTER,
                                    horizontal_alignment=CrossAxisAlignment.CENTER,
                                ),
                                alignment=alignment.center,
                            ),
                            tooltip=f"{flet_color_key}\nClick to copy to a clipboard",
                            on_click=copy_to_clipboard,
                            data=flet_color_key,
                        )
                    )
                status_bar.value = f"Colors found: {len(search_results.controls)}"
                self.update()

            # It checks if the search results are empty, and if they are, it shows a snack bar some message
            if len(search_results.controls) == 0:
                # if no color was found containing the user's search term
                self.page.show_snack_bar(SnackBar(Text("No colors found"), open=True))
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


# the tiles used in the ColorV2 tab
class Tile(Container):

    # all this below was obtained from https://github.com/ndonkoHenri/Flet-Color-Browser

    def __init__(self, tile_text, color, page):
        super().__init__()
        self.text = Text(tile_text, text_align=TextAlign.CENTER, weight=FontWeight.BOLD, italic=True, )
        self.color_text = f"colors.{tile_text}"
        self.bgcolor = color
        self.expand = True
        self.height = 40
        self.content = self.text
        self.page = page
        self.tooltip = "Click to copy to Clipboard"

    def _build(self):
        def click_event(_):
            """
            It copies the color's text to the clipboard.

            :param _: The event that triggered the function
            """
            print("Copied to clipboard:", self.color_text)
            self.page.set_clipboard(self.color_text)
            self.page.show_snack_bar(SnackBar(Text(f"Copied: {self.color_text}!"), open=True))

        self.on_click = click_event

        return self


# the content of the ColorV2 tab
class TabContentColors2(UserControl):
    # all this below was obtained from https://github.com/ndonkoHenri/Flet-Color-Browser

    def __init__(self, page):
        """
        The function creates a reference to the Tabs object that will be created later, and creates a list of colors
        that will be used to create the tabs.

        :param page: This is a reference to the page object that is passed to the constructor of the class
        """

        super().__init__(expand=True)

        # A reference to the page object that is passed to the constructor of the class.
        self.page = page

        # Creating a reference to the Tabs object that will be created later.
        self.displayed_tabs = Ref[Tabs]()

        # A list of colors that will be used to create the tabs.
        self.original_tab_names = ['RED', "BLACK", "WHITE", 'PINK', 'PURPLE', 'DEEP_PURPLE', 'INDIGO', 'BLUE',
                                   'LIGHT_BLUE',
                                   'CYAN', 'TEAL', 'GREEN', 'LIGHT_GREEN', 'LIME', 'YELLOW', 'AMBER', "ORANGE",
                                   'DEEP_ORANGE',
                                   'BROWN', 'BLUE_GREY']

    def build(self):

        # Getting all the colors from the colors' module.
        list_started = False
        all_flet_colors = list()
        for key in vars(colors).keys():
            if key == "PRIMARY":
                list_started = True
            if list_started:
                all_flet_colors.append(key)

        def create_tabs(tab_names: list) -> list:
            """
            It takes a list of strings where each string represents the name of a tab to be shown, and returns a list
            of tabs, each tab containing a list of tiles(containers) having a specific background color associated
            with the text in it.

            :param tab_names: list of strings that will be used to create the tabs
            :type tab_names: list
            :return: A list of tabs
            """
            created_tabs = []
            found = []
            # iterate over the tab_names(list containing the tabs to be shown)
            for tab_name in tab_names:
                tab_content = ListView()
                for color in all_flet_colors:
                    tile_bgcolor = color.lower().replace("_", "")
                    tile_content = Tile(color, tile_bgcolor, self.page)
                    # Checking if the color starts with the tab_name and if the tab_name is in the color.
                    if (tab_name in color) and color.startswith(tab_name):
                        tab_content.controls.append(tile_content)
                        found.append(color)

                # Add a tab with the name of the color and the content of the tab is a list of tiles.
                # Also remove underscores from the tab's name.
                created_tabs.append(Tab(tab_name.replace("_", " "), content=tab_content, ))

            # Creating a tab called "OTHERS" and adding all the colors that were not added to any other tab to it.
            others = [i for i in all_flet_colors if i not in found]
            others_content = ListView(controls=[Tile(x, x.lower().replace("_", ""), self.page) for x in others])
            created_tabs.append(Tab("OTHERS", content=others_content))

            return created_tabs

        # self.displayed_tabs.current.tabs = create_tabs(self.original_tab_names)

        def filter_tabs(_):
            """
            If the text in the search field is "ALL", show all tabs. If the search field is not empty, show only the
            tabs that contain the search term.

            :param _: ControlEvent
            :type _: ControlEvent
            """
            # Making the progress bar visible.
            self.page.splash.visible = True
            self.page.update()
            filtered_tab_names = []

            if search_field.value and search_field.value.lower().strip() == "all":
                filtered_tab_names = self.original_tab_names
            else:
                for tab_name in self.original_tab_names:
                    if search_field.value and search_field.value.lower().strip() in tab_name.lower().replace("_", " "):
                        filtered_tab_names.append(tab_name)

            if filtered_tab_names:
                # Removing all the tabs from the Tabs object.
                self.displayed_tabs.current.clean()

                # Showing a progress bar for 1 second and then hiding it.
                self.page.splash.visible = False
                time.sleep(0.4)
                self.page.update()

                # Updating the tabs of the Tabs object.
                self.displayed_tabs.current.tabs = create_tabs(filtered_tab_names)
                self.displayed_tabs.current.update()
                return

            # Showing a progress bar for 1 second and then hiding it.
            self.page.splash.visible = False
            time.sleep(1)
            self.page.update()

        # creating a field which will t=help the user search for specific tabs
        search_field = TextField(label="Search Tabs...", prefix_icon=icons.SEARCH, on_submit=filter_tabs,
                                 border_radius=50, suffix=IconButton(icon=icons.CHECK, bgcolor=colors.INVERSE_PRIMARY,
                                                                     icon_color=colors.ERROR, on_click=filter_tabs),
                                 helper_text="Tip: Enter 'ALL' to show all the tabs", height=70, width=450,
                                 keyboard_type=KeyboardType.TEXT, capitalization=TextCapitalization.CHARACTERS, )

        return Column(
            controls=[
                search_field,
                Tabs(ref=self.displayed_tabs, expand=True,
                     tabs=create_tabs(self.original_tab_names))
            ]
        )
