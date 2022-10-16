import math
import time
from itertools import islice
from flet import (colors, border_radius, icons, padding, border, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, IconButton, GridView, TextButton, Container, Icon, Column,
                  FloatingActionButton,
                  alignment, Tabs, Ref, ListView, Tab, FilledTonalButton, Slider, RadioGroup, Radio, Divider,
                  LinearGradient, RadialGradient, SweepGradient)
from flet.control_event import ControlEvent
from flet.types import BoxShape


# the content of the border radius tab
class TabContentBorderRadius(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_border_radius(e: ControlEvent):
            """
            It updates the border radius of the container object.

            :param e: The event object
            """

            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # if the value of the text field in focus is numeric or if it is empty...
                container_obj.current.border_radius = border_radius.BorderRadius(
                    int(field_tl.value.strip()) if field_tl.value.strip().isnumeric() else 0,
                    int(field_tr.value.strip()) if field_tr.value.strip().isnumeric() else 0,
                    int(field_bl.value.strip()) if field_bl.value.strip().isnumeric() else 0,
                    int(field_br.value.strip()) if field_br.value.strip().isnumeric() else 0, )
                container_text.current.value = f"{int(field_tl.value.strip()) if field_tl.value.strip().isnumeric() else 0}, {int(field_tr.value.strip()) if field_tr.value.strip().isnumeric() else 0}, {int(field_bl.value.strip()) if field_bl.value.strip().isnumeric() else 0}, {int(field_br.value.strip()) if field_br.value.strip().isnumeric() else 0} "
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated BorderRadius!"), open=True))

            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the border radius of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.border_radius}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.border_radius}"), open=True))

        container_obj = Ref[Container]()
        container_text = Ref[Text]()

        # text field for topLeft(tl) property of the BorderRadius object
        field_tl = TextField(
            label="topLeft",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for topRight(tr) property of the BorderRadius object
        field_tr = TextField(
            label="topRight",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for bottomLeft(bl) property of the BorderRadius object
        field_bl = TextField(
            label="bottomLeft",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # text field for bottomRight(br) property of the BorderRadius object
        field_br = TextField(
            label="bottomRight",
            value="",
            width=120,
            height=50,
            on_change=update_border_radius,
            keyboard_type="number"
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_tl, field_tr, field_bl, field_br
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Border Radius:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            content=Text(
                                "0, 0, 0, 0",
                                ref=container_text,
                                weight="bold",
                                size=18,
                                color="black"),
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#border_radius")
                        ),
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )


# the content of the padding tab
class TabContentPadding(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):

        def update_front_container_padding(e: ControlEvent):
            """
            It updates the padding of the container object.

            :param e: The event object
            """
            # if the value of the text field in focus is numeric or if it is empty...
            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # update the container's padding values
                container_back.current.padding = padding.Padding(
                    int(field_left.value.strip()) if field_left.value.strip().isnumeric() else 0,
                    int(field_top.value.strip()) if field_top.value.strip().isnumeric() else 0,
                    int(field_right.value.strip()) if field_right.value.strip().isnumeric() else 0,
                    int(field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0,
                )
                # update the text in the container
                container_text.current.value = f"{int(field_left.value.strip()) if field_left.value.strip().isnumeric() else 0}, {int(field_top.value.strip()) if field_top.value.strip().isnumeric() else 0}, {int(field_right.value.strip()) if field_right.value.strip().isnumeric() else 0}, {int(field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0} "
                self.update()
                # show a snackbar to account for the changes
                e.page.show_snack_bar(SnackBar(Text("Updated Padding!"), open=True))

            else:
                # Show a snackbar with an error message, in case the above condition is not met.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def update_front_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_front.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_front.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_front.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container's Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the padding of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_back.current.padding}")
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_back.current.padding}"), open=True))

        container_front = Ref[Container]()
        container_back = Ref[Container]()
        container_text = Ref[Text]()

        # text field for left parameter of the Padding object
        field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for top parameter of the Padding object
        field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for right parameter of the Padding object
        field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # text field for bottom parameter of the Padding object
        field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=update_front_container_padding,
            keyboard_type="number",
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_left, field_top, field_right, field_bottom
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_front_container_size,
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_front_container_size,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2),
                        Text("Container's Padding:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            content=Container(
                                Text(
                                    "0, 0, 0, 0",
                                    ref=container_text,
                                    weight="bold",
                                    size=18,
                                    color="black"
                                ),
                                ref=container_front,
                                bgcolor=colors.BLUE_700,
                                padding=padding.Padding(0, 0, 0, 0),
                                alignment=Alignment(0, 0),
                                width=float(field_width.value),
                                height=float(field_height.value),
                            ),
                            expand=True,
                            height=250,
                            ref=container_back,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(0, 0, 0, 0),
                            alignment=Alignment(0, 0),  # align its contents in the center
                            border_radius=border_radius.BorderRadius(0, 0, 0, 0),
                        )
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/padding")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden",
        )


# the content of the Icons tab
class TabContentIcons(UserControl):
    # all this below was obtained from https://github.com/flet-dev/examples/tree/main/python/apps/icons-browser

    def __init__(self):
        super().__init__(expand=True)

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
                                            text_align="center",
                                            color=colors.ON_SURFACE_VARIANT,
                                        ),
                                    ],
                                    spacing=5,
                                    alignment="center",
                                    horizontal_alignment="center",
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


# the content of the ColorV1 tab
class TabContentColors1(UserControl):
    # all this below was obtained from https://github.com/ndonkoHenri/Flet-Color-Browser

    def __init__(self, expand=True, height=500):
        """
        If the expand parameter is set to True, then the expand attribute of the object is set to True. Otherwise, the
        height attribute of the object is set to the value of the height parameter.

        :param expand: If True, the widget will expand to fill its parent, defaults to True (optional)
        :param height: The height of the widget, defaults to 500 (optional)
        """
        super().__init__()
        if expand:
            self.expand = expand
        else:
            self.height = height

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
                                            no_wrap=True, text_align="center", color=colors_dict[color_key],
                                        ),
                                    ],
                                    spacing=5,
                                    alignment="center",
                                    horizontal_alignment="center",
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
        self.text = Text(tile_text, text_align="center", weight="bold", italic=True, )
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
                                 keyboard_type="text", capitalization="characters", )

        return Column(
            controls=[
                search_field,
                Tabs(ref=self.displayed_tabs, expand=True,
                     tabs=create_tabs(self.original_tab_names))
            ]
        )


# the content of the alignment tab
class TabContentAlignment(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_alignment(e: ControlEvent):
            """
            It updates the alignment of the container object.

            :param e: The event object
            """
            # round the values from the sliders to 2 decimals to avoid long values, and store result in variables
            x = round(float(slider_x.value), 2)
            y = round(float(slider_y.value), 2)
            # update container's alignment
            container_obj.current.alignment = alignment.Alignment(x, y)
            # update the text of the button in the container
            container_button.current.text = f"Pos: {x},{y}"
            self.update()
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text("Updated Alignment!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the alignment used by the container to the clipboard.

            :param e: The event object
            """
            # update the text in the clipboard
            e.page.set_clipboard(f"{container_obj.current.alignment}")
            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.alignment}"), open=True))

        container_button = Ref[FilledTonalButton]()
        container_obj = Ref[Container]()

        # slider for x parameter of the Alignment object
        slider_x = Slider(
            label="x",
            value=0,
            on_change=update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )
        # slider for y parameter of the Alignment object
        slider_y = Slider(
            label="y",
            value=0,
            on_change=update_alignment,
            min=-1,
            max=1,
            divisions=100,
        )

        # a row containing all the sliders created above
        all_sliders = Row(
            controls=[
                slider_x,
                slider_y
            ],
            # alignment="center",
            wrap=True
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Alignment:", weight="bold", size=21),
                        Text("CheatSheet:\ntopLeft = (-1,-1) | topCenter = (0,1) | topRight = (1,-1)\ncenterLeft = ("
                             "-1,0) | Center = (0,0) | centerRight = (1,0)\nbottomLeft = (-1,1) | bottomCenter = ("
                             "0,1) | bottomRight = (1,1)", italic=True, ),
                        all_sliders
                    ],
                    alignment="center"),
                Row(
                    [
                        Container(
                            content=FilledTonalButton("Pos: 0.0,0.0", container_button, disabled=True),
                            expand=True,
                            ref=container_obj,
                            bgcolor=colors.DEEP_PURPLE_ACCENT_700,
                            width=160,
                            height=160,
                            alignment=alignment.Alignment(0, 0),  # align its contents in the center
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/alignment")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )


# the content of the Shape tab
class TabContentShape(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        def update_shape(e: ControlEvent):
            """
            It updates the Shape of the container object.

            :param e: The event object
            """
            _shape = radios.value

            # update container's shape
            container_obj.current.shape = BoxShape(_shape)
            self.update()

            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text("Updated Shape!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the shape used by the container to the clipboard.

            :param e: The event object
            """
            # update the text in the clipboard
            e.page.set_clipboard(f"BoxShape('{container_obj.current.shape}')")

            # show a snackbar to account for the changes
            e.page.show_snack_bar(SnackBar(Text(f"Copied: BoxShape('{container_obj.current.shape}')"), open=True))

        container_obj = Ref[Container]()

        # radio buttons for the Shape object
        radios = RadioGroup(
            Row(
                [
                    Radio(value="rectangle", label="Rectangle"),
                    Radio(value="circle", label="Circle")
                ],
                alignment="center",
            ),
            value="rectangle",
            on_change=update_shape,

        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Shape:", weight="bold", size=21),
                        radios
                    ],
                    alignment="spaceBetween",

                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.GREEN,
                            width=180,
                            height=180,
                            shape=BoxShape("rectangle"),
                        )
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/shape")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )


# the content of the border tab
class TabContentBorder(UserControl):
    # border = border.only(BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"), BorderSide(2, "blue"),)

    def build(self):
        def update_border(e: ControlEvent):
            """
            It updates the border radius of the container object.

            :param e: The event object
            """
            left, right, top, bottom = int(
                field_left.value.strip()) if field_left.value.strip().isnumeric() else 0, int(
                field_right.value.strip()) if field_right.value.strip().isnumeric() else 0, int(
                field_top.value.strip()) if field_top.value.strip().isnumeric() else 0, int(
                field_bottom.value.strip()) if field_bottom.value.strip().isnumeric() else 0

            if e.control.value.strip().isnumeric() or not e.control.value.strip():
                # if the value of the text field in focus is numeric or if it is empty...
                container_obj.current.border = border.only(border.BorderSide(left, colors.TEAL_900),
                                                           border.BorderSide(top, colors.TEAL_900),
                                                           border.BorderSide(right, colors.TEAL_900),
                                                           border.BorderSide(bottom, colors.TEAL_900))
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Border!"), open=True))

            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the border radius of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.border}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.border}"), open=True))

        container_obj = Ref[Container]()

        # text field for left property of the Border object
        field_left = TextField(
            label="left",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for right property of the Border object
        field_right = TextField(
            label="right",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for top property of the Border object
        field_top = TextField(
            label="top",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # text field for bottom property of the Border object
        field_bottom = TextField(
            label="bottom",
            value="",
            width=120,
            height=50,
            on_change=update_border,
            keyboard_type="number"
        )
        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                field_left, field_right, field_top, field_bottom
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Border:", weight="bold", size=21),
                        all_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            border=border.all(0, colors.TRANSPARENT),
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/container/border")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )


# the content of the LinearGradient tab
class TabContentLinearGradient(UserControl):

    def build(self):
        def update_gradient(e: ControlEvent):
            """
            It updates the gradient of the container object.

            :param e: The event object
            """

            begin = field_begin.value.strip() if field_begin.value.strip() else "alignment.center_left"
            end = field_end.value.strip() if field_end.value.strip() else "alignment.center_right"
            clrs = field_colors.value.strip().split("\n") if field_colors.value.strip() else []
            stops = field_stops.value.strip().split("\n") if field_stops.value.strip() else []
            rotation = field_rotation.value.strip() if field_rotation.value.strip() else None
            # tile_mode - How this gradient should tile the plane beyond in the region before begin and after end.
            tile_mode = radios.value

            # end - An instance of Alignment class. The offset at which stop 1.0 of the gradient is placed.
            try:
                end = eval(end)
                if not isinstance(end, Alignment) and not isinstance(end, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `end` must be an Alignment object or in the form x,y. This could be gotten from "
                            "the Alignment Tab here."),
                            open=True))
                    return
                elif isinstance(end, tuple) and len(end) == 2:
                    end = eval(f"Alignment({end[0]}, {end[1]})")
            except Exception as x:
                print(f"End Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text("ERROR: `end` must be an Alignment object or in the form x,y. Please check your input."),
                        open=True))
                return

            # begin - An instance of Alignment class. The offset at which stop 0.0 of the gradient is placed.
            try:
                begin = eval(begin)
                if not isinstance(begin, Alignment) and not isinstance(begin, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `begin` must be an Alignment object or in the form x,y. This could be gotten from "
                            "the Alignment Tab here."),
                            open=True))
                    return
                elif isinstance(begin, tuple) and len(begin) == 2:
                    begin = eval(f"Alignment({begin[0]}, {begin[1]})")
            except Exception as x:
                print(f"Begin Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text("ERROR: `begin` must be an Alignment object or in the form x,y. Please check your input."),
                        open=True))
                return

            # rotation: rotation - rotation for the gradient, in radians, around the center-point of its bounding box.
            try:
                if rotation is not None:
                    rotation = round((math.pi * float(rotation)) / 180, 3)  # convert to rads
            except Exception as x:
                print(f"Rotation Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: For simplicity, `rotation` must be in degrees! It will be "
                            "converted to radians internally."),
                        open=True))
                return

            # colors: must have at least two colors in it (otherwise, it's not a gradient!).
            if len(clrs) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `colors` must have at least two colors. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return
            elif len(clrs) >= 2:
                try:
                    clrs = [eval(c) if '.' in c else c.lower() for c in clrs]

                    # Getting all the colors from the flet.colors module.
                    list_started = False
                    all_flet_colors = list()
                    for value in vars(colors).values():
                        if value == "primary":
                            list_started = True
                        if list_started:
                            all_flet_colors.append(value)

                    # checking if all the entered colors exist in flet
                    for i in clrs:
                        if i not in all_flet_colors:
                            e.page.show_snack_bar(
                                SnackBar(
                                    Text(
                                        f"ERROR: Color `{i}` is not a valid color! Check the Colors V1/V2 tabs for "
                                        f"help with color-choosing."),
                                    open=True)
                            )

                            return

                except Exception as x:
                    print(f"Colors Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your colors. Please check your entries and "
                                "make sure they exist in the flet.colors!"),
                            open=True))
                    return

            # stops:  must have the same length as colors.
            if stops and len(stops) >= 2:
                try:
                    stops = [eval(s) for s in stops]
                    is_not_range = True if list(filter(lambda a: not 0.0 <= a <= 1.0, stops)) else False
                    print(f"{stops=}")
                    if is_not_range: raise ValueError("Some values are out of the specified range(0.0 - 1.0)!")
                except Exception as x:
                    print(f"Stops Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your stops. Please check your entries and "
                                "make sure they are between 0.0 and 1.0!"),
                            open=True))
                    return
            elif stops and len(stops) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `stops` is either empty or has a number of values(between 0.0 and 1.0) equal to those "
                        "in `colors`. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return

            # compare colors and stops
            if stops and len(clrs) != len(stops):
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                        open=True))
                return

            # make the gradient visible
            try:
                container_obj.current.gradient = LinearGradient(colors=clrs, tile_mode=tile_mode, rotation=rotation,
                                                                stops=stops, begin=begin, end=end)
                print(container_obj.current.gradient)
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Gradient!"), open=True))
            except Exception as x:
                print(f"Display Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: Display error!"),
                        open=True))
                return

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the gradient of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.gradient}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.gradient}"), open=True))

        container_obj = Ref[Container]()

        # field for begin parameter of the LinearGradient object
        field_begin = TextField(
            label="begin",
            value='-1, 0.5',
            width=200,
            on_submit=update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type="text",
        )
        # field for end parameter of the LinearGradient object
        field_end = TextField(
            label="end",
            value='Alignment(0, 1)',
            on_submit=update_gradient,
            width=200,
            hint_text="ex: Alignment(0, 1)",
            helper_text="Alignment object or x,y",
            keyboard_type="text",
        )

        # a row containing all the fields created above
        begin_stop_fields = Row(
            controls=[
                field_begin, field_end
            ],
            alignment="center",
        )

        # radio buttons for the tile_mode parameter
        radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment="center"
            ),
            value="clamp",
            on_change=update_gradient,

        )

        # text field for colors property of the LinearGradient object
        field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=update_gradient,
            keyboard_type="text",
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the LinearGradient object
        field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=update_gradient,
            keyboard_type="number",
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for rotation property of the LinearGradient object
        field_rotation = TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=update_gradient,
            keyboard_type="number",
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # a row containing all the fields created above
        all_textfields = Row(
            controls=[
                field_colors, field_stops, field_rotation
            ],
            alignment="center"
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center"
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Linear Gradient:", weight="bold", size=21),
                        all_textfields,
                        radios,
                        begin_stop_fields,
                    ],
                    alignment="center",
                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            gradient=LinearGradient(colors=['redaccent', 'yellow'], tile_mode='mirror', rotation=0,
                                                    stops=[0.2, 0.7], begin=Alignment(x=-1, y=0.5),
                                                    end=Alignment(x=0, y=1), type='linear')
                        ),
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard,
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#lineargradient")
                        )
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            scroll="hidden",
        )


# the content of the RadialGradient tab
class TabContentRadialGradient(UserControl):

    def build(self):
        def update_gradient(e: ControlEvent):
            """
            It updates the gradient of the container object.

            :param e: The event object
            """

            center = field_center.value.strip() if field_center.value.strip() else "0,0"
            clrs = field_colors.value.strip().split("\n") if field_colors.value.strip() else []
            stops = field_stops.value.strip().split("\n") if field_stops.value.strip() else []
            radius = field_radius.value.strip() if field_radius.value.strip() else "0.5"
            focal = field_focal.value.strip() if field_focal.value.strip() else "None"
            focal_radius = field_focal_radius.value.strip() if field_focal_radius.value.strip() else "0.0"
            rotation = field_rotation.value.strip() if field_rotation.value.strip() else None
            tile_mode = radios.value

            # center - An instance of Alignment class.
            try:
                center = eval(center)
                if not isinstance(center, Alignment) and not isinstance(center, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `center` must be an Alignment object or in the form x,y. This could be gotten "
                            "from the Alignment Tab here."),
                            open=True))
                    return
                elif isinstance(center, tuple) and len(center) == 2:
                    center = eval(f"Alignment({center[0]}, {center[1]})")
            except Exception as x:
                print(f"center Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: `center` must be an Alignment object or in the form x,y. Please check your input."),
                        open=True))
                return

            # radius: The radius of the gradient, as a fraction of the shortest side of the paint box.
            try:
                radius = float(radius)
            except Exception as x:
                print(f"Radius Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: There seems to be an error. Please check your entry for `radius`!"),
                        open=True))
                return

            # colors: must have at least two colors in it (otherwise, it's not a gradient!).
            if len(clrs) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `colors` must have at least two colors. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return
            elif len(clrs) >= 2:
                try:
                    clrs = [eval(c) if '.' in c else c.lower() for c in clrs]

                    # Getting all the colors from the flet.colors module.
                    list_started = False
                    all_flet_colors = list()
                    for value in vars(colors).values():
                        if value == "primary":
                            list_started = True
                        if list_started:
                            all_flet_colors.append(value)

                    # checking if all the entered colors exist in flet
                    for i in clrs:
                        if i not in all_flet_colors:
                            e.page.show_snack_bar(
                                SnackBar(
                                    Text(
                                        f"ERROR: Color `{i}` is not a valid color! Check the Colors V1/V2 tabs for "
                                        f"help with color-choosing."),
                                    open=True)
                            )

                            return

                except Exception as x:
                    print(f"Colors Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your colors. Please check your entries and "
                                "make sure they exist in the flet.colors!"),
                            open=True))
                    return

            # stops:  must have the same length as colors.
            if stops and len(stops) >= 2:
                try:
                    stops = [eval(s) for s in stops]
                    is_not_range = True if list(filter(lambda a: not 0.0 <= a <= 1.0, stops)) else False
                    print(f"{stops=}")
                    if is_not_range: raise ValueError("Some values are out of the specified range(0.0 - 1.0)!")
                except Exception as x:
                    print(f"Stops Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your stops. Please check your entries and "
                                "make sure they are between 0.0 and 1.0!"),
                            open=True))
                    return
            elif stops and len(stops) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `stops` is either empty or has a number of values(between 0.0 and 1.0) equal to those "
                        "in `colors`. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return

            # focal - The focal point of the gradient.
            try:
                focal = eval(focal)
                if not isinstance(focal, Alignment) and not isinstance(focal, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `center` must be an Alignment object or in the form x,y. This could be gotten "
                            "from the Alignment Tab here."),
                            open=True))
                    return
                elif isinstance(focal, tuple) and len(focal) == 2:
                    focal = eval(f"Alignment({focal[0]}, {focal[1]})")
            except Exception as x:
                print(f"Focal Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text("ERROR: `focal` must be an Alignment object or in the form x,y. Please check your input."),
                        open=True))
                return

            # focal_radius - The radius of the focal point of gradient.
            try:
                focal_radius = float(focal_radius)
            except Exception as x:
                print(f"Focal Radius Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: There seems to be an error. Please check your entry for `focal_radius`!"),
                        open=True))
                return

            # rotation: rotation - rotation for the gradient, in radians, around the center-point of its bounding box.
            try:
                if rotation is not None:
                    rotation = round((math.pi * float(rotation)) / 180, 3)  # convert to rads
            except Exception as x:
                print(f"Rotation Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: For simplicity, `rotation` must be in degrees! It will be "
                            "converted to radians internally."),
                        open=True))
                return

            # compare colors and stops
            if stops and len(clrs) != len(stops):
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                        open=True))
                return

            # make the gradient visible
            try:
                container_obj.current.gradient = RadialGradient(colors=clrs, tile_mode=tile_mode, radius=radius,
                                                                stops=stops, center=center, focal=focal,
                                                                focal_radius=focal_radius, rotation=rotation)
                print(container_obj.current.gradient)
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Gradient!"), open=True))
            except Exception as x:
                print(f"Display Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: Display error!"),
                        open=True))
                return

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the gradient of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.gradient}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.gradient}"), open=True))

        container_obj = Ref[Container]()

        # field for center parameter of the RadialGradient object
        field_center = TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type="text",
        )
        # text field for focal property of the RadialGradient object
        field_focal = TextField(
            label="focal",
            value='0,0',
            width=200,
            on_submit=update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type="text",
        )
        # text field for rotation property of the LinearGradient object
        field_rotation = TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=update_gradient,
            keyboard_type="number",
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # a row containing all the fields created above
        center_focal_rotation_fields = Row(
            controls=[
                field_center, field_focal, field_rotation
            ],
            alignment="center",
        )

        # radio buttons for the tile_mode parameter
        radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment="center"
            ),
            value="clamp",
            on_change=update_gradient,

        )

        # text field for colors property of the RadialGradient object
        field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=update_gradient,
            keyboard_type="text",
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the RadialGradient object
        field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=update_gradient,
            keyboard_type="number",
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for radius property of the RadialGradient object
        field_radius = TextField(
            label="radius",
            value="",
            width=90,
            on_change=update_gradient,
            keyboard_type="number",
            hint_text="ex: 0.5",
        )
        # text field for focal radius property of the RadialGradient object
        field_focal_radius = TextField(
            label="focal radius",
            value="0.3",
            width=90,
            on_change=update_gradient,
            keyboard_type="number",
            hint_text="ex: 0.5",
        )

        # a row containing all the fields created above
        all_textfields = Row(
            controls=[
                field_colors, field_stops, field_radius, field_focal_radius
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Linear Gradient:", weight="bold", size=21),
                        all_textfields,
                        radios,
                        center_focal_rotation_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=RadialGradient(colors=['redaccent', 'yellow'], stops=[0.2, 0.7], focal_radius=0.3)
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#radialgradient")
                        )
                    ],
                    alignment="center",
                )
            ],
            alignment="center",
            scroll="hidden"
        )


# the content of the SweepGradient tab
class TabContentSweepGradient(UserControl):

    def build(self):
        def update_gradient(e: ControlEvent):
            """
            It updates the gradient of the container object.

            :param e: The event object
            """

            center = field_center.value.strip() if field_center.value.strip() else "0,0"
            clrs = field_colors.value.strip().split("\n") if field_colors.value.strip() else []
            stops = field_stops.value.strip().split("\n") if field_stops.value.strip() else []
            start_angle = field_start_angle.value.strip() if field_start_angle.value.strip() else "0"
            end_angle = field_end_angle.value.strip() if field_end_angle.value.strip() else "180"
            rotation = field_rotation.value.strip() if field_rotation.value.strip() else None
            tile_mode = radios.value

            # center - An instance of Alignment class.
            try:
                center = eval(center)
                if not isinstance(center, Alignment) and not isinstance(center, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `center` must be an Alignment object or in the form x,y. This could be gotten "
                            "from the Alignment Tab here."),
                            open=True))
                    return
                elif isinstance(center, tuple) and len(center) == 2:
                    center = eval(f"Alignment({center[0]}, {center[1]})")
            except Exception as x:
                print(f"center Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: `center` must be an Alignment object or in the form x,y. Please check your input."),
                        open=True))
                return

            # colors: must have at least two colors in it (otherwise, it's not a gradient!).
            if len(clrs) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `colors` must have at least two colors. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return
            elif len(clrs) >= 2:
                try:
                    clrs = [eval(c) if '.' in c else c.lower() for c in clrs]

                    # Getting all the colors from the flet.colors module.
                    list_started = False
                    all_flet_colors = list()
                    for value in vars(colors).values():
                        if value == "primary":
                            list_started = True
                        if list_started:
                            all_flet_colors.append(value)

                    # checking if all the entered colors exist in flet
                    for i in clrs:
                        if i not in all_flet_colors:
                            e.page.show_snack_bar(
                                SnackBar(
                                    Text(
                                        f"ERROR: Color `{i}` is not a valid color! Check the Colors V1/V2 tabs for "
                                        f"help with color-choosing."),
                                    open=True)
                            )

                            return

                except Exception as x:
                    print(f"Colors Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your colors. Please check your entries and "
                                "make sure they exist in the flet.colors!"),
                            open=True))
                    return

            # stops:  must have the same length as colors.
            if stops and len(stops) >= 2:
                try:
                    stops = [eval(s) for s in stops]
                    is_not_range = True if list(filter(lambda a: not 0.0 <= a <= 1.0, stops)) else False
                    print(f"{stops=}")
                    if is_not_range: raise ValueError("Some values are out of the specified range(0.0 - 1.0)!")
                except Exception as x:
                    print(f"Stops Error: {x}")
                    e.page.show_snack_bar(
                        SnackBar(
                            Text(
                                "ERROR: There seems to be an error with your stops. Please check your entries and "
                                "make sure they are between 0.0 and 1.0!"),
                            open=True))
                    return
            elif stops and len(stops) < 2:
                e.page.show_snack_bar(
                    SnackBar(Text(
                        "ERROR: `stops` is either empty or has a number of values(between 0.0 and 1.0) equal to those "
                        "in `colors`. This could be gotten from the Colors V1/V2 "
                        "Tab here."),
                        open=True))
                return

            # rotation: rotation - rotation for the gradient, in radians, around the center-point of its bounding box.
            try:
                if rotation is not None:
                    rotation = round((math.pi * float(rotation)) / 180, 3)  # convert to rads
            except Exception as x:
                print(f"Rotation Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: For simplicity, `rotation` must be in degrees! It will be "
                            "converted to radians internally."),
                        open=True))
                return

            # start_angle : The angle in radians at which stop 0.0 of the gradient is placed. Defaults to 0.0.
            try:
                if start_angle is not None:
                    start_angle = round((math.pi * float(start_angle)) / 180, 3)  # convert to rads
            except Exception as x:
                print(f"Start_angle Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: For simplicity, `start_angle` must be in degrees! It will be "
                            "converted to radians internally."),
                        open=True))
                return

            # end_angle : The angle in radians at which stop 1.0 of the gradient is placed. Defaults to math.pi * 2.
            try:
                if end_angle is not None:
                    end_angle = round((math.pi * float(end_angle)) / 180, 3)  # convert to rads

            except Exception as x:
                print(f"End_angle Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: For simplicity, `end_angle` must be in degrees! It will be "
                            "converted to radians internally."),
                        open=True))
                return

            # compare colors and stops
            if stops and len(clrs) != len(stops):
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                        open=True))
                return

            # make the gradient visible
            try:
                container_obj.current.gradient = SweepGradient(colors=clrs,
                                                               tile_mode=tile_mode,
                                                               start_angle=start_angle,
                                                               end_angle=end_angle,
                                                               stops=stops,
                                                               center=center,
                                                               rotation=rotation)
                print(container_obj.current.gradient)
                self.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Gradient!"), open=True))
            except Exception as x:
                print(f"Display Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: Display error!"),
                        open=True))
                return

        def update_container_size(e: ControlEvent):
            """
            The function updates the container size when the width or height values are changed.

            :param e: The event object
            """
            if e.control.value.strip().isnumeric():
                # if the value of the text field in focus is numeric...
                container_obj.current.height = int(
                    field_height.value.strip()) if field_height.value.strip().isnumeric() else 160
                container_obj.current.width = int(
                    field_width.value.strip()) if field_width.value.strip().isnumeric() else 160
                container_obj.current.update()
                e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
            else:
                # Show a snackbar with the error message.
                e.page.show_snack_bar(
                    SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the gradient of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(f"{container_obj.current.gradient}")
            e.page.show_snack_bar(SnackBar(Text(f"Copied: {container_obj.current.gradient}"), open=True))

        container_obj = Ref[Container]()

        # field for center parameter of the SweepGradient object
        field_center = TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type="text",
        )
        # text field for start_angle property of the SweepGradient object
        field_start_angle = TextField(
            label="start angle",
            value="0",
            width=110,
            on_change=update_gradient,
            keyboard_type="number",
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # text field for end_angle property of the SweepGradient object
        field_end_angle = TextField(
            label="end angle",
            value="",
            width=110,
            on_change=update_gradient,
            keyboard_type="number",
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 320",
        )

        # a row containing all the fields created above
        center_focal_rotation_fields = Row(
            controls=[
                field_center, field_start_angle, field_end_angle
            ],
            alignment="center",
        )

        # radio buttons for the tile_mode parameter
        radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment="center"
            ),
            value="clamp",
            on_change=update_gradient,

        )

        # text field for colors property of the SweepGradient object
        field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=update_gradient,
            keyboard_type="text",
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the SweepGradient object
        field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=update_gradient,
            keyboard_type="number",
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for rotation property of the SweepGradient object
        field_rotation = TextField(
            label="rotation",
            value="",
            width=110,
            on_change=update_gradient,
            keyboard_type="number",
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # a row containing all the fields created above
        all_textfields = Row(
            controls=[
                field_colors, field_stops, field_rotation,
            ],
            alignment="center",
        )
        # text field for the width property of the Container object
        field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )
        # text field for the height property of the Container object
        field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=update_container_size,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight="bold", size=21),
                        Row(
                            [field_width, field_height],
                            alignment="center",
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Sweep Gradient:", weight="bold", size=21),
                        all_textfields,
                        radios,
                        center_focal_rotation_fields
                    ],
                    alignment="center"
                ),
                Row(
                    [
                        Container(
                            ref=container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=SweepGradient(colors=['redaccent', 'yellow'], )
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#sweepgradient")
                        )
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            scroll="hidden"
        )
