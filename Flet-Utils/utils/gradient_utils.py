import math

from flet import (colors, icons, padding, UserControl, SnackBar, Text, Alignment, Row,
                  FilledButton, TextField, Container, Column, MainAxisAlignment, FontWeight, KeyboardType,
                  Ref, FilledTonalButton, RadioGroup, Radio, Divider, GradientTileMode, ScrollMode,
                  LinearGradient, RadialGradient, SweepGradient, ControlEvent)
from flet import border


# the content of the LinearGradient tab
class TabContentLinearGradient(UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = Ref[Container]()

        # field for begin parameter of the LinearGradient object
        self.field_begin = TextField(
            label="begin",
            value='-1, 0.5',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=KeyboardType.TEXT,
        )
        # field for end parameter of the LinearGradient object
        self.field_end = TextField(
            label="end",
            value='Alignment(0, 1)',
            on_submit=self.update_gradient,
            width=200,
            hint_text="ex: Alignment(0, 1)",
            helper_text="Alignment object or x,y",
            keyboard_type=KeyboardType.TEXT,
        )
        # radio buttons for the tile_mode parameter
        self.radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment=MainAxisAlignment.CENTER,
            ),
            value="clamp",
            on_change=self.update_gradient,

        )

        # text field for colors property of the LinearGradient object
        self.field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the LinearGradient object
        self.field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for rotation property of the LinearGradient object
        self.field_rotation = TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ControlEvent):
        """
        It updates the gradient of the container object.

        :param e: The event object
        """

        begin = self.field_begin.value.strip() if self.field_begin.value.strip() else "alignment.center_left"
        end = self.field_end.value.strip() if self.field_end.value.strip() else "alignment.center_right"
        clrs = self.field_colors.value.strip().split("\n") if self.field_colors.value.strip() else []
        stops = self.field_stops.value.strip().split("\n") if self.field_stops.value.strip() else []
        rotation = self.field_rotation.value.strip() if self.field_rotation.value.strip() else None
        # tile_mode - How this gradient should tile the plane beyond in the region before begin and after end.
        tile_mode = self.radios.value

        # end - An instance of Alignment class. The offset at which stop 1.0 of the gradient is placed.
        try:
            end = eval(end)
            if not isinstance(end, Alignment) and not isinstance(end, tuple):
                raise ValueError("Wrong Value!")
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
                raise ValueError("Wrong Value!")
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
            self.container_obj.current.gradient = LinearGradient(colors=clrs, tile_mode=tile_mode, rotation=rotation,
                                                                 stops=stops, begin=begin, end=end)
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

    def update_container_size(self, e: ControlEvent):
        """
        The function updates the container size when the width or height values are changed.

        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_obj.current.height = int(
                self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else 160
            self.container_obj.current.width = int(
                self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else 160
            self.container_obj.current.update()
            e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):
        begin_stop_fields = Row(
            controls=[
                self.field_begin, self.field_end
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        all_textfields = Row(
            controls=[
                self.field_colors, self.field_stops, self.field_rotation
            ],
            alignment=MainAxisAlignment.CENTER
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight=FontWeight.BOLD, size=21),
                        Row(
                            [self.field_width, self.field_height],
                            alignment=MainAxisAlignment.CENTER
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Linear Gradient:", weight=FontWeight.BOLD, size=21),
                        all_textfields,
                        self.radios,
                        begin_stop_fields,
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
                Row(
                    [
                        Container(
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=Alignment(0, 0),
                            gradient=LinearGradient(colors=['redaccent', 'yellow'], tile_mode=GradientTileMode.MIRROR,
                                                    stops=[0.2, 0.7], begin=Alignment(x=-1, y=0.5), rotation=0,
                                                    end=Alignment(x=0, y=1), type='linear')
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=self.copy_to_clipboard,
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#lineargradient")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN,
        )


# the content of the RadialGradient tab
class TabContentRadialGradient(UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = Ref[Container]()

        # field for center parameter of the RadialGradient object
        self.field_center = TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=KeyboardType.TEXT,
        )
        # text field for focal property of the RadialGradient object
        self.field_focal = TextField(
            label="focal",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=KeyboardType.TEXT,
        )
        # text field for rotation property of the LinearGradient object
        self.field_rotation = TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # radio buttons for the tile_mode parameter
        self.radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            value="clamp",
            on_change=self.update_gradient,

        )

        # text field for colors property of the RadialGradient object
        self.field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the RadialGradient object
        self.field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for radius property of the RadialGradient object
        self.field_radius = TextField(
            label="radius",
            value="",
            width=90,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            hint_text="ex: 0.5",
        )
        # text field for focal radius property of the RadialGradient object
        self.field_focal_radius = TextField(
            label="focal radius",
            value="0.3",
            width=90,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            hint_text="ex: 0.5",
        )
        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ControlEvent):
        """
        It updates the gradient of the container object.

        :param e: The event object
        """

        center = self.field_center.value.strip() if self.field_center.value.strip() else "0,0"
        clrs = self.field_colors.value.strip().split("\n") if self.field_colors.value.strip() else []
        stops = self.field_stops.value.strip().split("\n") if self.field_stops.value.strip() else []
        radius = self.field_radius.value.strip() if self.field_radius.value.strip() else "0.5"
        focal = self.field_focal.value.strip() if self.field_focal.value.strip() else "None"
        focal_radius = self.field_focal_radius.value.strip() if self.field_focal_radius.value.strip() else "0.0"
        rotation = self.field_rotation.value.strip() if self.field_rotation.value.strip() else None
        tile_mode = self.radios.value

        # center - An instance of Alignment class.
        try:
            center = eval(center)
            if not isinstance(center, Alignment) and not isinstance(center, tuple):
                raise ValueError("Wrong Value!")
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
                raise ValueError("Wrong Value!")
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
            self.container_obj.current.gradient = RadialGradient(colors=clrs, tile_mode=tile_mode, radius=radius,
                                                                 stops=stops, center=center, focal=focal,
                                                                 focal_radius=focal_radius, rotation=rotation)
            print(self.container_obj.current.gradient)
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

    def update_container_size(self, e: ControlEvent):
        """
        The function updates the container size when the width or height values are changed.

        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_obj.current.height = int(
                self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else 160
            self.container_obj.current.width = int(
                self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else 160
            self.container_obj.current.update()
            e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):

        # a row containing all the fields created above
        center_focal_rotation_fields = Row(
            controls=[
                self.field_center, self.field_focal, self.field_rotation
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        # a row containing all the fields created above
        all_textfields = Row(
            controls=[
                self.field_colors, self.field_stops, self.field_radius, self.field_focal_radius
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight=FontWeight.BOLD, size=21),
                        Row(
                            [self.field_width, self.field_height],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Divider(height=2, thickness=2),
                        Text("Linear Gradient Builder:", weight=FontWeight.BOLD, size=21),
                        all_textfields,
                        self.radios,
                        center_focal_rotation_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=RadialGradient(colors=['redaccent', 'yellow'], stops=[0.2, 0.7], focal_radius=0.3)
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#radialgradient")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )


# the content of the SweepGradient tab
class TabContentSweepGradient(UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = Ref[Container]()

        # field for center parameter of the SweepGradient object
        self.field_center = TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=KeyboardType.TEXT,
        )
        # text field for start_angle property of the SweepGradient object
        self.field_start_angle = TextField(
            label="start angle",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # text field for end_angle property of the SweepGradient object
        self.field_end_angle = TextField(
            label="end angle",
            value="",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 320",
        )

        # text field for colors property of the SweepGradient object
        self.field_colors = TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the SweepGradient object
        self.field_stops = TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for rotation property of the SweepGradient object
        self.field_rotation = TextField(
            label="rotation",
            value="",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # radio buttons for the tile_mode parameter
        self.radios = RadioGroup(
            Row(
                [
                    Radio(value="clamp", label="clamp"),
                    Radio(value="decal", label="decal"),
                    Radio(value="mirror", label="mirror"),
                    Radio(value="repeated", label="repeated"),
                ],
                alignment=MainAxisAlignment.CENTER
            ),
            value="clamp",
            on_change=self.update_gradient,
        )

        # text field for the width property of the Container object
        self.field_width = TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ControlEvent):
        """
        It updates the gradient of the container object.

        :param e: The event object
        """

        center = self.field_center.value.strip() if self.field_center.value.strip() else "0,0"
        clrs = self.field_colors.value.strip().split("\n") if self.field_colors.value.strip() else []
        stops = self.field_stops.value.strip().split("\n") if self.field_stops.value.strip() else []
        start_angle = self.field_start_angle.value.strip() if self.field_start_angle.value.strip() else "0"
        end_angle = self.field_end_angle.value.strip() if self.field_end_angle.value.strip() else "180"
        rotation = self.field_rotation.value.strip() if self.field_rotation.value.strip() else None
        tile_mode = self.radios.value

        # center - An instance of Alignment class.
        try:
            center = eval(center)
            if not isinstance(center, Alignment) and not isinstance(center, tuple):
                raise ValueError("Wrong Value!")
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
            self.container_obj.current.gradient = SweepGradient(colors=clrs,
                                                                tile_mode=tile_mode,
                                                                start_angle=start_angle,
                                                                end_angle=end_angle,
                                                                stops=stops,
                                                                center=center,
                                                                rotation=rotation)
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

    def update_container_size(self, e: ControlEvent):
        """
        The function updates the container size when the width or height values are changed.

        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_obj.current.height = int(
                self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else 160
            self.container_obj.current.width = int(
                self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else 160
            self.container_obj.current.update()
            e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):
        center_focal_rotation_fields = Row(
            controls=[
                self.field_center, self.field_start_angle, self.field_end_angle
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        all_textfields = Row(
            controls=[
                self.field_colors, self.field_stops, self.field_rotation,
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight=FontWeight.BOLD, size=21),
                        Row(
                            [self.field_width, self.field_height],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Divider(height=2, thickness=2),
                        Text("Container's Sweep Gradient:", weight=FontWeight.BOLD, size=21),
                        all_textfields,
                        self.radios,
                        center_focal_rotation_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=SweepGradient(colors=['redaccent', 'yellow'], )
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=self.copy_to_clipboard
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#sweepgradient")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )
