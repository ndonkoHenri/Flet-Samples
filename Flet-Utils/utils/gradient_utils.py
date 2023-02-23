import math

import flet as ft


# the content of the LinearGradient tab
class TabContentLinearGradient(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = ft.Ref[ft.Container]()

        # field for begin parameter of the LinearGradient object
        self.field_begin = ft.TextField(
            label="begin",
            value='-1, 0.5',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # field for end parameter of the LinearGradient object
        self.field_end = ft.TextField(
            label="end",
            value='Alignment(0, 1)',
            on_submit=self.update_gradient,
            width=200,
            hint_text="ex: Alignment(0, 1)",
            helper_text="Alignment object or x,y",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # radio buttons for the tile_mode parameter
        self.tile_mode_radio_group = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="clamp", label="clamp"),
                    ft.Radio(value="decal", label="decal"),
                    ft.Radio(value="mirror", label="mirror"),
                    ft.Radio(value="repeated", label="repeated"),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            value="clamp",
            on_change=self.update_gradient,

        )

        # text field for colors property of the LinearGradient object
        self.field_colors = ft.TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the LinearGradient object
        self.field_stops = ft.TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for rotation property of the LinearGradient object
        self.field_rotation = ft.TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ft.ControlEvent):
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
        tile_mode = self.tile_mode_radio_group.value

        # end - An instance of Alignment class. The offset at which stop 1.0 of the gradient is placed.
        try:
            end = eval(end)
            if not isinstance(end, ft.Alignment) and not isinstance(end, tuple):
                raise ValueError("Wrong Value!")
            elif isinstance(end, tuple) and len(end) == 2:
                end = eval(f"Alignment({end[0]}, {end[1]})")
        except Exception as x:
            print(f"End Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `end` must be an Alignment object or in the form x,y. Please check your input."),
                    open=True))
            return

        # begin - An instance of Alignment class. The offset at which stop 0.0 of the gradient is placed.
        try:
            begin = eval(begin)
            if not isinstance(begin, ft.Alignment) and not isinstance(begin, tuple):
                raise ValueError("Wrong Value!")
            elif isinstance(begin, tuple) and len(begin) == 2:
                begin = eval(f"Alignment({begin[0]}, {begin[1]})")
        except Exception as x:
            print(f"Begin Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `begin` must be an Alignment object or in the form x,y. Please check your input."),
                    open=True))
            return

        # rotation: rotation - rotation for the gradient, in radians, around the center-point of its bounding box.
        try:
            if rotation is not None:
                rotation = round((math.pi * float(rotation)) / 180, 3)  # convert to rads
        except Exception as x:
            print(f"Rotation Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: For simplicity, `rotation` must be in degrees! It will be "
                        "converted to radians internally."),
                    open=True))
            return

        # colors: must have at least two colors in it (otherwise, it's not a gradient!).
        if len(clrs) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
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
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                for i in clrs:
                    if i not in all_flet_colors:
                        raise ValueError("Entered color was not found! See the colors browser for help!")

            except Exception as x:
                print(f"Colors Error: {x}")
                e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
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
                    ft.SnackBar(
                        ft.Text(
                            "ERROR: There seems to be an error with your stops. Please check your entries and "
                            "make sure they are between 0.0 and 1.0!"),
                        open=True))
                return
        elif stops and len(stops) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
                    "ERROR: `stops` is either empty or has a number of values(between 0.0 and 1.0) equal to those "
                    "in `colors`. This could be gotten from the Colors V1/V2 Tab here."),
                    open=True))
            return

        # compare colors and stops
        if stops and len(clrs) != len(stops):
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                    open=True))
            return

        # make the gradient visible
        try:
            self.container_obj.current.gradient = ft.LinearGradient(
                colors=clrs,
                tile_mode=tile_mode,
                rotation=rotation,
                stops=stops,
                begin=begin,
                end=end
            )
            self.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Gradient!"), open=True))
        except Exception as x:
            print(f"Display Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text("ERROR: Display error!"), open=True))
            return

    def update_container_size(self, e: ft.ControlEvent):
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
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):
        begin_stop_fields = ft.Row(
            controls=[
                self.field_begin, self.field_end
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        all_textfields = ft.Row(
            controls=[
                self.field_colors, self.field_stops, self.field_rotation
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Size:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Row(
                            [self.field_width, self.field_height],
                            alignment=ft.MainAxisAlignment.CENTER
                        ),
                        ft.Divider(height=2, thickness=2),
                        ft.Text("Linear Gradient Builder:", weight=ft.FontWeight.BOLD, size=21),
                        all_textfields,
                        self.tile_mode_radio_group,
                        begin_stop_fields,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        ft.Container(
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            alignment=ft.Alignment(0, 0),
                            gradient=ft.LinearGradient(
                                colors=['redaccent', 'yellow'],
                                tile_mode=ft.GradientTileMode.MIRROR,
                                stops=[0.2, 0.7],
                                begin=ft.Alignment(x=-1, y=0.5),
                                rotation=0,
                                end=ft.Alignment(x=0, y=1), type='linear'
                            )
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Copy Value to Clipboard",
                            icon=ft.icons.COPY,
                            on_click=self.copy_to_clipboard,
                        ),
                        ft.FilledTonalButton(
                            "Go to Docs",
                            icon=ft.icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#lineargradient")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )


# the content of the RadialGradient tab
class TabContentRadialGradient(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = ft.Ref[ft.Container]()

        # field for center parameter of the RadialGradient object
        self.field_center = ft.TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # text field for focal property of the RadialGradient object
        self.field_focal = ft.TextField(
            label="focal",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # text field for rotation property of the LinearGradient object
        self.field_rotation = ft.TextField(
            label="rotation",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # radio buttons for the tile_mode parameter
        self.tile_mode_radio_group = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="clamp", label="clamp"),
                    ft.Radio(value="decal", label="decal"),
                    ft.Radio(value="mirror", label="mirror"),
                    ft.Radio(value="repeated", label="repeated"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            value="clamp",
            on_change=self.update_gradient,

        )

        # text field for colors property of the RadialGradient object
        self.field_colors = ft.TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )
        # text field for stops property of the RadialGradient object
        self.field_stops = ft.TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )
        # text field for radius property of the RadialGradient object
        self.field_radius = ft.TextField(
            label="radius",
            value="",
            width=90,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="ex: 0.5",
        )
        # text field for focal radius property of the RadialGradient object
        self.field_focal_radius = ft.TextField(
            label="focal radius",
            value="0.3",
            width=90,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="ex: 0.5",
        )
        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ft.ControlEvent):
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
        tile_mode = self.tile_mode_radio_group.value

        # center - An instance of Alignment class.
        try:
            center = eval(center)
            if not isinstance(center, ft.Alignment) and not isinstance(center, tuple):
                raise ValueError("Wrong Value!")
            elif isinstance(center, tuple) and len(center) == 2:
                center = eval(f"Alignment({center[0]}, {center[1]})")
        except Exception as x:
            print(f"center Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `center` must be an Alignment object or in the form x,y. Please check your input."),
                    open=True))
            return

        # radius: The radius of the gradient, as a fraction of the shortest side of the paint box.
        try:
            radius = float(radius)
        except Exception as x:
            print(f"Radius Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: There seems to be an error. Please check your entry for `radius`!"),
                    open=True))
            return

        # colors: must have at least two colors in it (otherwise, it's not a gradient!).
        if len(clrs) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
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
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                for i in clrs:
                    if i not in all_flet_colors:
                        raise ValueError("Entered color was not found! See the colors browser for help!")

            except Exception as x:
                print(f"Colors Error: {x}")
                e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
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
                    ft.SnackBar(
                        ft.Text(
                            "ERROR: There seems to be an error with your stops. Please check your entries and "
                            "make sure they are between 0.0 and 1.0!"),
                        open=True))
                return
        elif stops and len(stops) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
                    "ERROR: `stops` is either empty or has a number of values(between 0.0 and 1.0) equal to those "
                    "in `colors`. This could be gotten from the Colors V1/V2 "
                    "Tab here."),
                    open=True))
            return

        # focal - The focal point of the gradient.
        try:
            focal = eval(focal)
            if not isinstance(focal, ft.Alignment) and not isinstance(focal, tuple):
                raise ValueError("Wrong Value!")
            elif isinstance(focal, tuple) and len(focal) == 2:
                focal = eval(f"Alignment({focal[0]}, {focal[1]})")
        except Exception as x:
            print(f"Focal Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `focal` must be an Alignment object or in the form x,y. Please check your input."),
                    open=True))
            return

        # focal_radius - The radius of the focal point of gradient.
        try:
            focal_radius = float(focal_radius)
        except Exception as x:
            print(f"Focal Radius Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
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
                ft.SnackBar(
                    ft.Text(
                        "ERROR: For simplicity, `rotation` must be in degrees! It will be "
                        "converted to radians internally."),
                    open=True))
            return

        # compare colors and stops
        if stops and len(clrs) != len(stops):
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                    open=True))
            return

        # make the gradient visible
        try:
            self.container_obj.current.gradient = ft.RadialGradient(
                colors=clrs,
                tile_mode=tile_mode,
                radius=radius,
                stops=stops,
                center=center,
                focal=focal,
                focal_radius=focal_radius,
                rotation=rotation
            )
            print(self.container_obj.current.gradient)
            self.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Gradient!"), open=True))
        except Exception as x:
            print(f"Display Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text("ERROR: Display error!"), open=True))
            return

    def update_container_size(self, e: ft.ControlEvent):
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
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):

        # a row containing all the fields created above
        center_focal_rotation_fields = ft.Row(
            controls=[
                self.field_center, self.field_focal, self.field_rotation
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        # a row containing all the fields created above
        all_textfields = ft.Row(
            controls=[
                self.field_colors, self.field_stops, self.field_radius, self.field_focal_radius
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Size:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Row(
                            [self.field_width, self.field_height],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=2, thickness=2),
                        ft.Text("Radial Gradient Builder:", weight=ft.FontWeight.BOLD, size=21),
                        all_textfields,
                        self.tile_mode_radio_group,
                        center_focal_rotation_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=ft.RadialGradient(colors=['redaccent', 'yellow'], stops=[0.2, 0.7],
                                                       focal_radius=0.3)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
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
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#radialgradient")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )


# the content of the SweepGradient tab
class TabContentSweepGradient(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.container_obj = ft.Ref[ft.Container]()

        # field for center parameter of the SweepGradient object
        self.field_center = ft.TextField(
            label="center",
            value='0,0',
            width=200,
            on_submit=self.update_gradient,
            hint_text="ex: -1, 0.5",
            helper_text="Alignment object or x,y",
            keyboard_type=ft.KeyboardType.TEXT,
        )
        # text field for start_angle property of the SweepGradient object
        self.field_start_angle = ft.TextField(
            label="start angle",
            value="0",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )
        # text field for end_angle property of the SweepGradient object
        self.field_end_angle = ft.TextField(
            label="end angle",
            value="",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 320",
        )

        # text field for colors property of the SweepGradient object
        self.field_colors = ft.TextField(
            label="colors",
            value="colors.RED_ACCENT\nYellow",
            width=190,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.TEXT,
            multiline=True,
            shift_enter=True,
            min_lines=2,
            hint_text="colors.RED_50\npurple"
        )

        # text field for stops property of the SweepGradient object
        self.field_stops = ft.TextField(
            label="stops",
            value="0.2\n0.7",
            width=90,
            on_submit=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            shift_enter=True,
            min_lines=2,
            hint_text="0.2\n0.7"
        )

        # text field for rotation property of the SweepGradient object
        self.field_rotation = ft.TextField(
            label="rotation",
            value="",
            width=110,
            on_change=self.update_gradient,
            keyboard_type=ft.KeyboardType.NUMBER,
            suffix_text="°",
            helper_text="In degrees",
            hint_text="ex: 180",
        )

        # radio buttons for the tile_mode parameter
        self.tile_mode_radio_group = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="clamp", label="clamp"),
                    ft.Radio(value="decal", label="decal"),
                    ft.Radio(value="mirror", label="mirror"),
                    ft.Radio(value="repeated", label="repeated"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            value="clamp",
            on_change=self.update_gradient,
        )

        # text field for the width property of the Container object
        self.field_width = ft.TextField(
            label="Width",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )
        # text field for the height property of the Container object
        self.field_height = ft.TextField(
            label="Height",
            hint_text=f"default=160",
            value="160",
            width=120,
            height=50,
            on_submit=self.update_container_size,
        )

    def update_gradient(self, e: ft.ControlEvent):
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
        tile_mode = self.tile_mode_radio_group.value

        # center - An instance of Alignment class.
        try:
            center = eval(center)
            if not isinstance(center, ft.Alignment) and not isinstance(center, tuple):
                raise ValueError("Wrong Value!")
            elif isinstance(center, tuple) and len(center) == 2:
                center = eval(f"Alignment({center[0]}, {center[1]})")
        except Exception as x:
            print(f"center Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `center` must be an Alignment object or in the form x,y. Please check your input."),
                    open=True))
            return

        # colors: must have at least two colors in it (otherwise, it's not a gradient!).
        if len(clrs) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
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
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                for i in clrs:
                    if i not in all_flet_colors:
                        raise ValueError("Entered color was not found! See the colors browser for help!")

            except Exception as x:
                print(f"Colors Error: {x}")
                e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
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
                    ft.SnackBar(
                        ft.Text(
                            "ERROR: There seems to be an error with your stops. Please check your entries and "
                            "make sure they are between 0.0 and 1.0!"),
                        open=True))
                return
        elif stops and len(stops) < 2:
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text(
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
                ft.SnackBar(
                    ft.Text(
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
                ft.SnackBar(
                    ft.Text(
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
                ft.SnackBar(
                    ft.Text(
                        "ERROR: For simplicity, `end_angle` must be in degrees! It will be "
                        "converted to radians internally."),
                    open=True))
            return

        # compare colors and stops
        if stops and len(clrs) != len(stops):
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: The number of values in `colors` must be equal to that in `stops`!"),
                    open=True))
            return

        # make the gradient visible
        try:
            self.container_obj.current.gradient = ft.SweepGradient(
                colors=clrs,
                tile_mode=tile_mode,
                start_angle=start_angle,
                end_angle=end_angle,
                stops=stops,
                center=center,
                rotation=rotation
            )
            self.update()
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Gradient!"), open=True))
        except Exception as x:
            print(f"Display Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: Display error!"),
                    open=True))
            return

    def update_container_size(self, e: ft.ControlEvent):
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
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(f"{self.container_obj.current.gradient}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {self.container_obj.current.gradient}"), open=True))

    def build(self):
        center_focal_rotation_fields = ft.Row(
            controls=[
                self.field_center, self.field_start_angle, self.field_end_angle
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        all_textfields = ft.Row(
            controls=[
                self.field_colors, self.field_stops, self.field_rotation,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Size:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Row(
                            [self.field_width, self.field_height],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=2, thickness=2),
                        ft.Text("Sweep Gradient Builder:", weight=ft.FontWeight.BOLD, size=21),
                        all_textfields,
                        self.tile_mode_radio_group,
                        center_focal_rotation_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=ft.padding.Padding(15, 0, 15, 0),
                            width=160,
                            height=160,
                            gradient=ft.SweepGradient(colors=['redaccent', 'yellow'], )
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
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
                            on_click=lambda e: e.page.launch_url(
                                "https://flet.dev/docs/controls/container#sweepgradient")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.scroll = ft.ScrollMode.HIDDEN
        page.add(
            TabContentLinearGradient(),
            TabContentRadialGradient(),
            TabContentSweepGradient()
        )


    ft.app(main)
