from flet import *
import flet as ft


# the content of the progress bar tab
class TabContentProgressBar(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.bar_color = "green"
        self.bar_bgcolor = None
        self.bar_bar_height = None
        self.bar_tooltip = None
        self.bar_value = None
        self.bar_width = None
        self.bar_height = None

        self.bar_opacity = None
        self.bar_rotate = None
        self.bar_scale = None
        self.bar_offset = None

        self.bar_obj = ft.Ref[ft.ProgressBar]()

        # text field for tooltip property of the Progress Bar object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_bar,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the Progress Bar object
        self.field_color = ft.TextField(
            label="color",
            value="green",
            helper_text="Optional[str]",
            on_submit=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the bgcolor property of the Progress Bar object
        self.field_bgcolor = ft.TextField(
            label="bgcolor",
            value="",
            helper_text="Optional[str]",
            hint_text="colors.RED_50 or red50",
            on_submit=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1,
            # width=170,
        )

        # text field for the bar_height property of the Progress Bar object
        self.field_bar_height = ft.TextField(
            label="bar_height",
            helper_text="Union[int, float]",
            # value="4",
            on_change=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the value property of the Progress Bar object
        self.field_value = ft.TextField(
            label="value",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the width property of the Progress Bar object
        self.field_width = ft.TextField(
            label="width",
            value="420",
            helper_text="Union[int, float]",
            on_submit=self.update_bar,
            on_blur=self.update_bar,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the height property of the Progress Bar object
        self.field_height = ft.TextField(
            label="height",
            value="",
            helper_text="Union[int, float]",
            on_submit=self.update_bar,
            on_blur=self.update_bar,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the opacity property of the Progress Bar object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=170,
            expand=1
        )

        # text field for the offset property of the Progress Bar object
        self.field_offset = ft.TextField(
            label="offset",
            value="",
            helper_text="Optional[Offset, tuple]",
            on_submit=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the scale property of the Progress Bar object
        self.field_scale = ft.TextField(
            label="scale",
            value="",
            helper_text="Union[int, float, Scale]",
            on_submit=self.update_bar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            # width=110,
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_value, self.field_bar_height, self.field_opacity],
                ),
                ft.Row(
                    [self.field_bgcolor, self.field_color, self.field_tooltip],
                ),
                ft.Row(
                    [self.field_offset, self.field_scale, self.field_height, self.field_width],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11
        )

        return ft.Column(
            [
                ft.Text("Progress Bar Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.ProgressBar(
                            ref=self.bar_obj,
                            color="green",
                            # bar_height=4,
                            width=420
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
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
                            url="https://flet.dev/docs/controls/progressbar"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30
        )

    def update_bar(self, e: ft.ControlEvent):
        """It updates the Progress Bar object."""
        self.bar_opacity = int(self.field_value.value.strip()) if self.field_value.value.strip().isnumeric() else None

        self.bar_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.bar_bgcolor = self.field_bgcolor.value.strip() if self.field_bgcolor.value.strip() else None
        self.bar_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        self.bar_offset = self.field_offset.value.strip() if self.field_offset.value.strip() else "None"
        self.bar_scale = self.field_scale.value.strip() if self.field_scale.value.strip() else "None"

        # value
        try:
            if self.field_value.value:
                self.bar_value = eval(self.field_value.value)
                assert isinstance(self.bar_value, (int, float)), "`value` must be either of type float or int !"
            else:
                self.bar_value = None
        except Exception as x:
            print(f"Value Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"),open=True))
            return

        # bar_height
        try:
            if self.field_bar_height.value:
                self.bar_bar_height = eval(self.field_bar_height.value)
                assert isinstance(self.bar_bar_height, (int, float)), "`bar_height` must be either of type float or int !"
            else:
                self.bar_bar_height = None
        except Exception as x:
            print(f"Bar Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # width
        try:
            if self.field_width.value:
                self.bar_width = eval(self.field_width.value)
                assert isinstance(self.bar_width, (int, float)), "`width` must be either of type float or int !"
            else:
                self.bar_width = None
        except Exception as x:
            print(f"Width Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # height
        try:
            if self.field_height.value:
                self.bar_height = eval(self.field_height.value)
                assert isinstance(self.bar_height, (int, float)), "`height` must be either of type float or int !"
            else:
                self.bar_height = None
        except Exception as x:
            print(f"Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.bar_color is not None:
                self.bar_color = eval(self.bar_color) if '.' in self.bar_color else self.bar_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.bar_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # bgcolor
        try:
            if self.bar_bgcolor is not None:
                self.bar_bgcolor = eval(self.bar_bgcolor) if '.' in self.bar_bgcolor else self.bar_bgcolor.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.bar_bgcolor not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Bgcolor Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # offset
        try:
            self.bar_offset = eval(self.bar_offset)
            if not isinstance(self.bar_offset, ft.Offset) \
                    and not isinstance(self.bar_offset, tuple) \
                    and self.bar_offset is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.bar_offset, tuple) and len(self.bar_offset) == 2:
                self.bar_offset = eval(f"Offset({self.bar_offset[0]}, {self.bar_offset[1]})")
        except Exception as x:
            print(f"Offset Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `offset` must be an Offset object or in the form x,y. Please check your input."),
                    open=True))
            return

        # scale
        try:
            self.bar_scale = eval(self.bar_scale)
            if not isinstance(self.bar_scale, ft.Scale) \
                    and not isinstance(self.bar_scale, (int, float)) \
                    and self.bar_scale is not None:
                raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Scale Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `scale` must be an Scale object. Please check your input."),
                    open=True))
            return

        # opacity
        try:
            if self.field_opacity.value:
                self.bar_opacity = eval(self.field_opacity.value)
                assert isinstance(self.bar_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.bar_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.bar_obj.current.color = self.bar_color
        self.bar_obj.current.bgcolor = self.bar_bgcolor
        self.bar_obj.current.tooltip = self.bar_tooltip
        self.bar_obj.current.value = self.bar_value
        self.bar_obj.current.bar_height = self.bar_bar_height
        self.bar_obj.current.width = self.bar_width
        self.bar_obj.current.height = self.bar_height
        self.bar_obj.current.opacity = self.bar_opacity
        self.bar_obj.current.scale = self.bar_scale
        self.bar_obj.current.offset = self.bar_offset

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Progress Bar!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.bar_opacity}"
        s = f", scale={self.bar_scale}"
        off = f", offset={self.bar_offset}"
        t = f", tooltip='{self.bar_tooltip}'"
        bg= f", bgcolor='{self.bar_bgcolor}'"
        c = f", color='{self.bar_color}'"
        w = f", width={self.bar_width}"
        h = f", height={self.bar_height}"

        others = f"{w if self.bar_width is not None else ''}{h if self.bar_height is not None else ''}{c if self.bar_color is not None else ''}{bg if self.bar_bgcolor is not None else ''}{t if self.bar_tooltip is not None else ''}{o if self.bar_opacity is not None else ''}{s if self.bar_scale is not None else ''}{off if self.bar_offset is not None else ''}"
        val = f"Progressbar(value={self.bar_value}, bar_height={self.bar_bar_height}{others if others else ''})"
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.add(TabContentProgressBar())


    ft.app(main)
