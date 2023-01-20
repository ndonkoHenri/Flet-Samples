# from flet import (colors, icons, padding, border, UserControl, SnackBar, Text, Alignment, Row,
#                   FilledButton, TextField, Container, Column,
#                   Ref, FilledTonalButton, Divider, KeyboardType)
import math
import flet as ft
from flet import *
from flet import border_radius, border, padding, margin, alignment


# the content of the tooltip tab
class TabContentTooltip(UserControl):

    def __init__(self):
        super().__init__()
        self.vertical_offset = None
        self.wait_duration = None
        self.show_duration = None
        self.text_align = None
        self.prefer_below = None
        self.message = "This is tooltip"
        self.shape = None
        self.enable_feedback = None
        self.content_property = Text("Hover me to see tooltip")
        self.margin_property = margin.all(0)
        self.padding_property = padding.all(10)
        self.gradient_property = LinearGradient(
                                    begin=Alignment(-1, -1),
                                    end=Alignment(0.8, 1),
                                    colors=[
                                        "red",
                                        "yellow",
                                    ],
                                    tile_mode=GradientTileMode.MIRROR,
                                    rotation=math.pi / 3,
                                )
        self.border_property = None
        self.bgcolor = None
        self.border_radius_property = border_radius.all(10)
        self.text_style_property = TextStyle(size=20, color=colors.WHITE)

        self.container_obj = Ref[Container]()
        self.tooltip_obj = Ref[Tooltip]()

        # text field for the width property of the Container object
        self.container_width = TextField(
            label="Width",
            hint_text="default=200",
            value="200",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

        # text field for the height property of the Container object
        self.container_height = TextField(
            label="Height",
            hint_text="default=200",
            value="200",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

        # text field for message property of the Tooltip object
        self.field_message = TextField(
            label="message",
            value="This is tooltip",
            on_change=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            expand=2
        )

        # text field for bgcolor property of the Tooltip object
        self.field_bgcolor = TextField(
            label="bgcolor",
            value="",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for text_style property of the Tooltip object
        self.field_text_style = TextField(
            label="text_style",
            value="TextStyle(size=20, color=colors.WHITE)",
            helper_text="TextStyle instance",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            expand=1
        )

        # text field for the border radius property of the Tooltip object
        self.field_border_radius = TextField(
            label="border radius",
            value="BorderRadius(topLeft=10, topRight=10, bottomLeft=10, bottomRight=10)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="5,10,2,3",
            helper_text="BorderRadius instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the border property of the Tooltip object
        self.field_border = TextField(
            label="border",
            value="",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="5,10,2,3",
            helper_text="Border instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for gradient property of the Tooltip object
        self.field_gradient = TextField(
            label="gradient",
            value="LinearGradient(begin=Alignment(-1, -1), end=Alignment(0.8, 1), colors=['red','yellow',], tile_mode=GradientTileMode.MIRROR, rotation=math.pi / 3)",
            on_submit=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="LinearGradient(.....)",
            helper_text="Linear, Radial or Sweep Gradient instance",
            expand=2
        )

        # text field for the height property of the Tooltip object
        self.field_height = TextField(
            label="height",
            hint_text="160",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_tooltip,
            keyboard_type=KeyboardType.NUMBER,
            # on_blur=update_tooltip,
        )

        # text field for the margin property of the Tooltip object
        self.field_margin = TextField(
            label="margin",
            value="margin.all(0)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="margin.all(10)",
            helper_text="Margin instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the padding property of the Tooltip object
        self.field_padding = TextField(
            label="padding",
            value="padding.all(10)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=KeyboardType.TEXT,
            hint_text="padding.symmetric(horizontal=10)",
            helper_text="Padding instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the show_duration property of the Tooltip object
        self.field_show_duration = TextField(
            label="show_duration",
            value="",
            on_change=self.update_tooltip,
            # on_blur=update_tooltip,
            keyboard_type=KeyboardType.NUMBER,
            hint_text="2000",
            width=125,
            height=60,
            content_padding=9
        )

        # text field for the vertical_offset property of the Tooltip object
        self.field_vertical_offset = TextField(
            label="vertical_offset",
            hint_text="160",
            value="",
            width=127,
            height=60,
            on_change=self.update_tooltip,
            content_padding=9,
            keyboard_type=KeyboardType.NUMBER,
            # on_blur=update_tooltip,
        )

        # text field for the wait_duration property of the Tooltip object
        self.field_wait_duration = TextField(
            label="wait_duration",
            value="",
            on_change=self.update_tooltip,
            # on_blur=update_tooltip,
            keyboard_type=KeyboardType.NUMBER,
            hint_text="1000",
            width=120,
            height=60,
            content_padding=9
        )

        # dropdown values for the prefer_below parameter
        self.prefer_below_dropdown = Dropdown(
            options=[
                dropdown.Option("True"),
                dropdown.Option("False"),
            ],
            value="True",
            on_change=self.update_tooltip,
            width=100,
            label="prefer_below",
            content_padding=9,
            height=60
        )

        # dropdown values for the shape parameter
        self.shape_dropdown = Dropdown(
            options=[
                dropdown.Option("circle"),
                dropdown.Option("rectangle"),
            ],
            value="rectangle",
            on_change=self.update_tooltip,
            width=100,
            label="shape",
            content_padding=9,
            height=60
        )

        # dropdown values for the enable_feedback parameter
        self.enable_feedback_dropdown = Dropdown(
            options=[
                dropdown.Option("True"),
                dropdown.Option("False"),
            ],
            value="True",
            on_change=self.update_tooltip,
            width=115,
            label="enable_feedback",
            content_padding=9,
            height=60
        )

        # dropdown values for the text_align parameter
        self.text_align_dropdown = Dropdown(
            options=[
                dropdown.Option("left"),
                dropdown.Option("right"),
                dropdown.Option("center"),
                dropdown.Option("justify"),
                dropdown.Option("start"),
                dropdown.Option("end")
            ],
            value="left",
            on_change=self.update_tooltip,
            width=100,
            label="text_align",
            content_padding=9,
            height=60
        )

    def build(self):

        # a row containing all the fields created above
        all_fields = Row(
            controls=[
                Row(
                    [self.field_message, self.field_bgcolor],
                ),
                Row(
                    [self.field_border, self.field_border_radius],
                ),
                Row(
                    [self.field_margin, self.field_padding],
                ),
                Row(
                    [self.field_gradient, self.field_text_style],
                ),
                self.field_vertical_offset, self.field_show_duration, self.field_wait_duration,
                self.text_align_dropdown,
                self.prefer_below_dropdown, self.shape_dropdown, self.enable_feedback_dropdown
            ],
            alignment=MainAxisAlignment.CENTER,
            wrap=True
        )

        return Column(
            [
                Column(
                    [
                        Text("Container's Size:", weight=FontWeight.BOLD, size=21),
                        Row(
                            [self.container_width, self.container_height],
                            alignment=MainAxisAlignment.CENTER,
                        ),
                        Divider(height=2, thickness=2),
                        Text("Tooltip Builder:", weight=FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    [
                        Container(
                            Tooltip(
                                ref=self.tooltip_obj,
                                message="This is tooltip",
                                content=Text("Hover me to see tooltip"),
                                padding=padding.all(10),
                                border_radius=10,
                                margin=margin.all(10),
                                text_style=TextStyle(size=20, color=colors.WHITE),
                                gradient=LinearGradient(
                                    begin=Alignment(-1, -1),
                                    end=Alignment(0.8, 1),
                                    colors=[
                                        'red',
                                        'yellow',
                                    ],
                                    tile_mode=GradientTileMode.MIRROR,
                                    rotation=math.pi / 3,
                                ),
                            ),
                            ref=self.container_obj,
                            bgcolor=colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=200,
                            height=200,
                            alignment=Alignment(0, 0),
                            border=border.all(0, colors.TRANSPARENT),
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/tooltip")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN
        )

    def update_tooltip(self, e: ControlEvent):
        """
        It updates the border radius of the container object.
        :param e: The event object
        """
        self.wait_duration, self.show_duration, self.height, self.vertical_offset = (
            int(self.field_wait_duration.value.strip()) if self.field_wait_duration.value.strip().isnumeric() else None,
            int(self.field_show_duration.value.strip()) if self.field_show_duration.value.strip().isnumeric() else None,
            int(self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else None,
            int(self.field_vertical_offset.value.strip()) if self.field_vertical_offset.value.strip().isnumeric() else None
        )

        self.enable_feedback = self.enable_feedback_dropdown.value
        self.shape = self.shape_dropdown.value
        self.message = self.field_message.value.strip()
        self.prefer_below = self.prefer_below_dropdown.value
        self.text_align = self.text_align_dropdown.value
        self.bgcolor = self.field_bgcolor.value.strip() if self.field_bgcolor.value.strip() else None
        self.border_radius_property = self.field_border_radius.value.strip() if self.field_border_radius.value.strip() else "None"
        self.border_property = self.field_border.value.strip() if self.field_border.value.strip() else "None"
        self.text_style_property = self.field_text_style.value.strip() if self.field_text_style.value.strip() else "None"
        self.margin_property = self.field_margin.value.strip() if self.field_margin.value.strip() else "None"
        self.padding_property = self.field_padding.value.strip() if self.field_padding.value.strip() else "None"
        self.gradient_property = self.field_gradient.value.strip() if self.field_gradient.value.strip() else "None"

        # border
        try:
            self.border_property = eval(self.border_property)
            if self.border_property is not None and \
                    not isinstance(self.border_property, Border) and \
                    not isinstance(self.border_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.border_property, tuple) and len(self.border_property) == 4:
                border_property = eval(
                    f"Border({self.border_property[0]}, {self.border_property[1]},{self.border_property[2]}, {self.border_property[3]})")
        except Exception as x:
            print(f"BorderRadius Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text("ERROR: `border` must be an Border object or in the form (left, top, right, "
                         "bottom). Please check your input."),
                    open=True)
            )
            return

        # border radius
        try:
            self.border_radius_property = eval(self.border_radius_property)
            if self.border_radius_property is not None and \
                    not isinstance(self.border_radius_property, (border_radius.BorderRadius, BorderRadius)) and \
                    not isinstance(self.border_radius_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.border_radius_property, tuple) and len(self.border_radius_property) == 4:
                self.border_radius_property = eval(
                    f"BorderRadius({self.border_radius_property[0]}, {self.border_radius_property[1]},{self.border_radius_property[2]}, {self.border_radius_property[3]})")
        except Exception as x:
            print(f"BorderRadius Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text(
                        "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True)
            )
            return

        # margin
        try:
            self.margin_property = eval(self.margin_property)
            if self.margin_property is not None and \
                    not isinstance(self.margin_property, Margin) and \
                    not isinstance(self.margin_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.margin_property, tuple) and len(self.margin_property) == 4:
                self.margin_property = eval(
                    f"Margin({self.margin_property[0]}, {self.margin_property[1]},{self.margin_property[2]}, {self.margin_property[3]})")

        except Exception as x:
            print(f"Margin Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text(
                        "ERROR: `margin` must be an Margin object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True))
            return

        # padding
        try:
            self.padding_property = eval(self.padding_property)
            if self.padding_property is not None and \
                    not isinstance(self.padding_property, Padding) and \
                    not isinstance(self.padding_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.padding_property, tuple) and len(self.padding_property) == 4:
                self.padding_property = eval(
                    f"Padding({self.padding_property[0]}, {self.padding_property[1]},{self.padding_property[2]}, {self.padding_property[3]})")
        except Exception as x:
            print(f"Padding Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text(
                        "ERROR: `padding` must be an Padding object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True)
            )
            return

        # gradient
        try:
            self.gradient_property = eval(self.gradient_property)
            if self.gradient_property is not None and not isinstance(self.gradient_property,
                                                                     (LinearGradient, RadialGradient, SweepGradient)):
                raise ValueError("Wrong Value")
        except Exception as x:
            print(f"Gradient Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text("ERROR: `gradient` must be a Gradient(LinearGradient,RadialGradient,SweepGradient) "
                         "object. Please check your input."),
                    open=True)
            )
            return

        # text style
        try:
            self.text_style_property = eval(self.text_style_property)
            if self.text_style_property is not None and \
                    not isinstance(self.text_style_property, TextStyle):
                raise ValueError("Wrong Value")
        except Exception as x:
            print(f"TextStyle Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text("ERROR: `text_style` must be a TextStyle object. Please check your input."),
                    open=True)
            )
            return

        # bgcolor
        try:
            if self.bgcolor is not None:
                self.bgcolor = eval(self.bgcolor) if '.' in self.bgcolor else self.bgcolor.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.bgcolor not in all_flet_colors:
                    raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Bgcolor Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text(
                        "ERROR: There seems to be an error with your colors. Check the Colors V1/V2 tabs for "
                        f"help with color-choosing.!"),
                    open=True))
            return

        self.tooltip_obj.current.bgcolor = self.bgcolor
        self.tooltip_obj.current.text_style = self.text_style_property
        self.tooltip_obj.current.enable_feedback = self.enable_feedback
        self.tooltip_obj.current.message = self.message
        self.tooltip_obj.current.wait_duration = self.wait_duration
        self.tooltip_obj.current.show_duration = self.show_duration
        self.tooltip_obj.current.height = self.height
        self.tooltip_obj.current.vertical_offset = self.vertical_offset
        self.tooltip_obj.current.prefer_below = self.prefer_below
        self.tooltip_obj.current.shape = BoxShape(self.shape)
        self.tooltip_obj.current.text_align = self.text_align
        self.tooltip_obj.current.border_radius = self.border_radius_property
        self.tooltip_obj.current.border = self.border_property
        self.tooltip_obj.current.margin = self.margin_property
        self.tooltip_obj.current.padding = self.padding_property
        self.tooltip_obj.current.gradient = self.gradient_property

        self.update()
        e.page.show_snack_bar(SnackBar(Text("Updated Tooltip!"), open=True))

    def update_container_size(self, e: ControlEvent):
        """
        The function updates the container size when the width or height values are changed.

        :param e: The event object
        """
        if e.control.value.strip().isnumeric():
            # if the value of the text field in focus is numeric...
            self.container_obj.current.height = int(
                self.container_height.value.strip()) if self.container_height.value.strip().isnumeric() else 160
            self.container_obj.current.width = int(
                self.container_width.value.strip()) if self.container_width.value.strip().isnumeric() else 160
            self.container_obj.current.update()
            e.page.show_snack_bar(SnackBar(Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                SnackBar(Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True)
            )

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the tooltip object/instance to the clipboard.

        :param e: The event object
        """

        t = f"Tooltip(enable_feedback={self.enable_feedback}, height={self.height}, vertical_offset={self.vertical_offset}, margin={self.margin_property}, padding={self.padding_property}, bgcolor={self.bgcolor}, gradient={self.gradient_property}, border={self.border_property}, border_radius={self.border_radius_property}, shape=BoxShape('{self.shape}'), message='{self.message}', text_style={self.text_style_property}, text_align={self.text_align}, prefer_below={self.prefer_below}, show_duration={self.show_duration}, wait_duration={self.wait_duration})"
        e.page.set_clipboard(f"{t}")
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {t}"), open=True))
        print(t)
