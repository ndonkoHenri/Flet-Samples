import math
import flet as ft
from flet import *
from flet import border_radius, border, padding, margin, alignment


# the content of the tooltip tab
class TabContentTooltip(ft.UserControl):

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
        self.content_property = ft.Text("Hover me to see tooltip")
        self.margin_property = margin.all(0)
        self.padding_property = padding.all(10)
        self.gradient_property = ft.LinearGradient(
            begin=ft.Alignment(-1, -1),
            end=ft.Alignment(0.8, 1),
            colors=[
                "red",
                "yellow",
            ],
            tile_mode=ft.GradientTileMode.MIRROR,
            rotation=math.pi / 3,
        )
        self.border_property = None
        self.bgcolor = None
        self.border_radius_property = border_radius.all(10)
        self.text_style_property = ft.TextStyle(size=20, color=ft.colors.WHITE)

        self.container_obj = ft.Ref[ft.Container]()
        self.tooltip_obj = ft.Ref[ft.Tooltip]()

        # text field for the width property of the Container object
        self.container_width = ft.TextField(
            label="Width",
            hint_text="default=200",
            value="200",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

        # text field for the height property of the Container object
        self.container_height = ft.TextField(
            label="Height",
            hint_text="default=200",
            value="200",
            width=120,
            height=50,
            content_padding=9,
            on_submit=self.update_container_size
        )

        # text field for message property of the Tooltip object
        self.field_message = ft.TextField(
            label="message",
            value="This is tooltip",
            on_change=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=2
        )

        # text field for bgcolor property of the Tooltip object
        self.field_bgcolor = ft.TextField(
            label="bgcolor",
            value="",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for text_style property of the Tooltip object
        self.field_text_style = ft.TextField(
            label="text_style",
            value="TextStyle(size=20, color=colors.WHITE)",
            helper_text="TextStyle instance",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the border radius property of the Tooltip object
        self.field_border_radius = ft.TextField(
            label="border radius",
            value="BorderRadius(10, 10, 10, 10)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="5,10,2,3",
            helper_text="BorderRadius instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the border property of the Tooltip object
        self.field_border = ft.TextField(
            label="border",
            value="",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="5,10,2,3",
            helper_text="Border instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for gradient property of the Tooltip object
        self.field_gradient = ft.TextField(
            label="gradient",
            value="LinearGradient(begin=Alignment(-1, -1), end=Alignment(0.8, 1), colors=['red','yellow',], tile_mode=GradientTileMode.MIRROR, rotation=math.pi / 3)",
            on_submit=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="LinearGradient(.....)",
            helper_text="Linear, Radial or Sweep Gradient instance",
            expand=2
        )

        # text field for the height property of the Tooltip object
        self.field_height = ft.TextField(
            label="height",
            hint_text="160",
            value="",
            width=120,
            height=50,
            content_padding=9,
            on_change=self.update_tooltip,
            keyboard_type=ft.KeyboardType.NUMBER,
            # on_blur=update_tooltip,
        )

        # text field for the margin property of the Tooltip object
        self.field_margin = ft.TextField(
            label="margin",
            value="margin.all(0)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="margin.all(10)",
            helper_text="Margin instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the padding property of the Tooltip object
        self.field_padding = ft.TextField(
            label="padding",
            value="padding.all(10)",
            on_submit=self.update_tooltip,
            on_blur=self.update_tooltip,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="padding.symmetric(horizontal=10)",
            helper_text="Padding instance or (left, top, right, bottom)",
            expand=1
        )

        # text field for the show_duration property of the Tooltip object
        self.field_show_duration = ft.TextField(
            label="show_duration",
            value="",
            on_change=self.update_tooltip,
            # on_blur=update_tooltip,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="2000",
            width=125,
            height=60,
            content_padding=9
        )

        # text field for the vertical_offset property of the Tooltip object
        self.field_vertical_offset = ft.TextField(
            label="vertical_offset",
            hint_text="160",
            value="",
            width=127,
            height=60,
            on_change=self.update_tooltip,
            content_padding=9,
            keyboard_type=ft.KeyboardType.NUMBER,
            # on_blur=update_tooltip,
        )

        # text field for the wait_duration property of the Tooltip object
        self.field_wait_duration = ft.TextField(
            label="wait_duration",
            value="",
            on_change=self.update_tooltip,
            # on_blur=update_tooltip,
            keyboard_type=ft.KeyboardType.NUMBER,
            hint_text="1000",
            width=120,
            height=60,
            content_padding=9
        )

        # dropdown values for the prefer_below parameter
        self.prefer_below_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("True"),
                ft.dropdown.Option("False"),
            ],
            value="True",
            on_change=self.update_tooltip,
            width=100,
            label="prefer_below",
            content_padding=9,
            height=60
        )

        # dropdown values for the shape parameter
        self.shape_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("circle"),
                ft.dropdown.Option("rectangle"),
            ],
            value="rectangle",
            on_change=self.update_tooltip,
            width=100,
            label="shape",
            content_padding=9,
            height=60
        )

        # dropdown values for the enable_feedback parameter
        self.enable_feedback_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("True"),
                ft.dropdown.Option("False"),
            ],
            value="True",
            on_change=self.update_tooltip,
            width=115,
            label="enable_feedback",
            content_padding=9,
            height=60
        )

        # dropdown values for the text_align parameter
        self.text_align_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("left"),
                ft.dropdown.Option("right"),
                ft.dropdown.Option("center"),
                ft.dropdown.Option("justify"),
                ft.dropdown.Option("start"),
                ft.dropdown.Option("end")
            ],
            value="left",
            on_change=self.update_tooltip,
            width=100,
            label="text_align",
            content_padding=9,
            height=60
        )

    def build(self):
        all_fields = ft.Row(
            controls=[
                ft.Row(
                    [self.field_message, self.field_bgcolor],
                ),
                ft.Row(
                    [self.field_border, self.field_border_radius],
                ),
                ft.Row(
                    [self.field_margin, self.field_padding],
                ),
                ft.Row(
                    [self.field_gradient, self.field_text_style],
                ),
                self.field_vertical_offset, self.field_show_duration, self.field_wait_duration,
                self.text_align_dropdown,
                self.prefer_below_dropdown, self.shape_dropdown, self.enable_feedback_dropdown
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            wrap=True
        )

        return ft.Column(
            [
                ft.Column(
                    [
                        ft.Text("Container's Size:", weight=ft.FontWeight.BOLD, size=21),
                        ft.Row(
                            [self.container_width, self.container_height],
                            alignment=ft.MainAxisAlignment.CENTER,
                        ),
                        ft.Divider(height=2, thickness=2),
                        ft.Text("Tooltip Builder:", weight=ft.FontWeight.BOLD, size=21),
                        all_fields
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.Container(
                            ft.Tooltip(
                                ref=self.tooltip_obj,
                                message="This is tooltip",
                                content=ft.Text("Hover me to see tooltip"),
                                padding=padding.all(10),
                                border_radius=10,
                                margin=margin.all(10),
                                text_style=ft.TextStyle(size=20, color=ft.colors.WHITE),
                                gradient=ft.LinearGradient(
                                    begin=ft.Alignment(-1, -1),
                                    end=ft.Alignment(0.8, 1),
                                    colors=[
                                        'red',
                                        'yellow',
                                    ],
                                    tile_mode=ft.GradientTileMode.MIRROR,
                                    rotation=math.pi / 3,
                                ),
                            ),
                            ref=self.container_obj,
                            bgcolor=ft.colors.RED_ACCENT_700,
                            padding=padding.Padding(15, 0, 15, 0),
                            width=200,
                            height=200,
                            alignment=ft.Alignment(0, 0),
                            border=border.all(0, ft.colors.TRANSPARENT),
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
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
                            url="https://flet.dev/docs/controls/tooltip"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN
        )

    def update_tooltip(self, e: ft.ControlEvent):
        """
        It updates the tooltip object.
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
                    not isinstance(self.border_property, ft.Border) and \
                    not isinstance(self.border_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.border_property, tuple) and len(self.border_property) == 4:
                border_property = eval(
                    f"Border({self.border_property[0]}, {self.border_property[1]},{self.border_property[2]}, {self.border_property[3]})")
        except Exception as x:
            print(f"BorderRadius Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `border` must be an Border object or in the form (left, top, right, "
                            "bottom). Please check your input."),
                    open=True)
            )
            return

        # border radius
        try:
            self.border_radius_property = eval(self.border_radius_property)
            if self.border_radius_property is not None and \
                    not isinstance(self.border_radius_property, (border_radius.BorderRadius, ft.BorderRadius)) and \
                    not isinstance(self.border_radius_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.border_radius_property, tuple) and len(self.border_radius_property) == 4:
                self.border_radius_property = eval(
                    f"BorderRadius({self.border_radius_property[0]}, {self.border_radius_property[1]},{self.border_radius_property[2]}, {self.border_radius_property[3]})")
        except Exception as x:
            print(f"BorderRadius Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True)
            )
            return

        # margin
        try:
            self.margin_property = eval(self.margin_property)
            if self.margin_property is not None and \
                    not isinstance(self.margin_property, ft.Margin) and \
                    not isinstance(self.margin_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.margin_property, tuple) and len(self.margin_property) == 4:
                self.margin_property = eval(
                    f"Margin({self.margin_property[0]}, {self.margin_property[1]},{self.margin_property[2]}, {self.margin_property[3]})")

        except Exception as x:
            print(f"Margin Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `margin` must be an Margin object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True))
            return

        # padding
        try:
            self.padding_property = eval(self.padding_property)
            if self.padding_property is not None and \
                    not isinstance(self.padding_property, ft.Padding) and \
                    not isinstance(self.padding_property, tuple):
                raise ValueError("Wrong Value")
            elif isinstance(self.padding_property, tuple) and len(self.padding_property) == 4:
                self.padding_property = eval(
                    f"Padding({self.padding_property[0]}, {self.padding_property[1]},{self.padding_property[2]}, {self.padding_property[3]})")
        except Exception as x:
            print(f"Padding Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `padding` must be an Padding object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True)
            )
            return

        # gradient
        try:
            self.gradient_property = eval(self.gradient_property)
            if self.gradient_property is not None and not isinstance(self.gradient_property,
                                                                     (ft.LinearGradient, ft.RadialGradient,
                                                                      ft.SweepGradient)):
                raise ValueError("Wrong Value")
        except Exception as x:
            print(f"Gradient Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `gradient` must be a Gradient(LinearGradient,RadialGradient,SweepGradient) "
                            "object. Please check your input."),
                    open=True)
            )
            return

        # text style
        try:
            self.text_style_property = eval(self.text_style_property)
            if self.text_style_property is not None and \
                    not isinstance(self.text_style_property, ft.TextStyle):
                raise ValueError("Wrong Value")
        except Exception as x:
            print(f"TextStyle Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `text_style` must be a TextStyle object. Please check your input."),
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
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.bgcolor not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Bgcolor Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
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
        self.tooltip_obj.current.shape = ft.BoxShape(self.shape)
        self.tooltip_obj.current.text_align = self.text_align
        self.tooltip_obj.current.border_radius = self.border_radius_property
        self.tooltip_obj.current.border = self.border_property
        self.tooltip_obj.current.margin = self.margin_property
        self.tooltip_obj.current.padding = self.padding_property
        self.tooltip_obj.current.gradient = self.gradient_property

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Tooltip!"), open=True))

    def update_container_size(self, e: ft.ControlEvent):
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
            e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Container Size!"), open=True))
        else:
            # Show a snackbar with the error message.
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: The value(ex: non-integer) entered is not valid!"), open=True)
            )

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the tooltip object/instance to the clipboard.

        :param e: The event object
        """

        t = f"Tooltip(enable_feedback={self.enable_feedback}, height={self.height}, vertical_offset={self.vertical_offset}, margin={self.margin_property}, padding={self.padding_property}, bgcolor={self.bgcolor}, gradient={self.gradient_property}, border={self.border_property}, border_radius={self.border_radius_property}, shape=BoxShape('{self.shape}'), message='{self.message}', text_style={self.text_style_property}, text_align={self.text_align}, prefer_below={self.prefer_below}, show_duration={self.show_duration}, wait_duration={self.wait_duration})"
        e.page.set_clipboard(f"{t}")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {t}"), open=True))
        print(t)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentTooltip())


    ft.app(main)
