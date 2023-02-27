from flet import *
import flet as ft


# todo: width, height

# the content of the progress ring tab
class TabContentProgressRing(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.ring_color = None
        self.ring_bgcolor = None
        self.ring_stroke_width = None
        self.ring_tooltip = None
        self.ring_value = None
        self.ring_width = None
        self.ring_height = None

        self.ring_opacity = None
        self.ring_rotate = None
        self.ring_scale = None
        self.ring_offset = None

        self.ring_obj = ft.Ref[ft.ProgressRing]()

        # text field for tooltip property of the Progress Ring object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_ring,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the Progress Ring object
        self.field_color = ft.TextField(
            label="color",
            value="",
            helper_text="Optional[str]",
            on_submit=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the bgcolor property of the Progress Ring object
        self.field_bgcolor = ft.TextField(
            label="bgcolor",
            value="",
            helper_text="Optional[str]",
            hint_text="colors.RED_50 or red50",
            on_submit=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1,
            # width=170,
        )

        # text field for the stroke_width property of the Progress Ring object
        self.field_stroke_width = ft.TextField(
            label="stroke_width",
            helper_text="Union[int, float]",
            value="",
            on_change=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the value property of the Progress Ring object
        self.field_value = ft.TextField(
            label="value",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the width property of the Progress Bar object
        self.field_width = ft.TextField(
            label="width",
            value="",
            helper_text="Union[int, float]",
            on_submit=self.update_ring,
            on_blur=self.update_ring,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the height property of the Progress Bar object
        self.field_height = ft.TextField(
            label="height",
            value="",
            helper_text="Union[int, float]",
            on_submit=self.update_ring,
            on_blur=self.update_ring,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the opacity property of the Progress Ring object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=170,
            expand=1
        )

        # text field for the offset property of the Progress Ring object
        self.field_offset = ft.TextField(
            label="offset",
            value="",
            helper_text="Optional[Offset, tuple]",
            on_submit=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the scale property of the Progress Ring object
        self.field_scale = ft.TextField(
            label="scale",
            value="",
            helper_text="Union[int, float, Scale]",
            on_submit=self.update_ring,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            # width=110,
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_value, self.field_stroke_width, self.field_opacity],
                ),
                ft.Row(
                    [self.field_bgcolor, self.field_color, self.field_tooltip],
                ),
                ft.Row(
                    [self.field_offset, self.field_scale, self.field_width, self.field_height],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11
        )

        return ft.Column(
            [
                ft.Text("Progress Ring Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.ProgressRing(
                            ref=self.ring_obj,
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/progressring")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30
        )

    def update_ring(self, e: ft.ControlEvent):
        """It updates the Progress Ring object."""
        self.ring_opacity = int(self.field_value.value.strip()) if self.field_value.value.strip().isnumeric() else None

        self.ring_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.ring_bgcolor = self.field_bgcolor.value.strip() if self.field_bgcolor.value.strip() else None
        self.ring_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        self.ring_offset = self.field_offset.value.strip() if self.field_offset.value.strip() else "None"
        self.ring_scale = self.field_scale.value.strip() if self.field_scale.value.strip() else "None"

        # value
        try:
            if self.field_value.value:
                self.ring_value = eval(self.field_value.value)
                assert isinstance(self.ring_value, (int, float)), "`value` must be either of type float or int !"
            else:
                self.ring_value = None
        except Exception as x:
            print(f"Value Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # stroke_width
        try:
            if self.field_stroke_width.value:
                self.ring_stroke_width = eval(self.field_stroke_width.value)
                assert isinstance(self.ring_stroke_width,
                                  (int, float)), "`stroke_width` must be either of type float or int !"
            else:
                self.ring_stroke_width = None
        except Exception as x:
            print(f"Stroke Width Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # width
        try:
            if self.field_width.value:
                self.ring_width = eval(self.field_width.value)
                assert isinstance(self.ring_width, (int, float)), "`width` must be either of type float or int !"
            else:
                self.ring_width = None
        except Exception as x:
            print(f"Width Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # height
        try:
            if self.field_height.value:
                self.ring_height = eval(self.field_height.value)
                assert isinstance(self.ring_height, (int, float)), "`height` must be either of type float or int !"
            else:
                self.ring_height = None
        except Exception as x:
            print(f"Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.ring_color is not None:
                self.ring_color = eval(self.ring_color) if '.' in self.ring_color else self.ring_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.ring_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # bgcolor
        try:
            if self.ring_bgcolor is not None:
                self.ring_bgcolor = eval(self.ring_bgcolor) if '.' in self.ring_bgcolor else self.ring_bgcolor.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.ring_bgcolor not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Bgcolor Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # offset
        try:
            self.ring_offset = eval(self.ring_offset)
            if not isinstance(self.ring_offset, ft.Offset) \
                    and not isinstance(self.ring_offset, tuple) \
                    and self.ring_offset is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.ring_offset, tuple) and len(self.ring_offset) == 2:
                self.ring_offset = eval(f"Offset({self.ring_offset[0]}, {self.ring_offset[1]})")

        except Exception as x:
            print(f"Offset Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `offset` must be an Offset object or in the form x,y. Please check your input."),
                    open=True))
            return

        # scale
        try:
            self.ring_scale = eval(self.ring_scale)
            if not isinstance(self.ring_scale, ft.Scale) \
                    and not isinstance(self.ring_scale, (int, float)) \
                    and self.ring_scale is not None:
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
                self.ring_opacity = eval(self.field_opacity.value)
                assert isinstance(self.ring_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.ring_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.ring_obj.current.color = self.ring_color
        self.ring_obj.current.bgcolor = self.ring_bgcolor
        self.ring_obj.current.tooltip = self.ring_tooltip
        self.ring_obj.current.value = self.ring_value
        self.ring_obj.current.stroke_width = self.ring_stroke_width
        self.ring_obj.current.width = self.ring_width
        self.ring_obj.current.height = self.ring_height
        self.ring_obj.current.opacity = self.ring_opacity
        self.ring_obj.current.scale = self.ring_scale
        self.ring_obj.current.offset = self.ring_offset

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Progress Ring!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.ring_opacity}"
        s = f", scale={self.ring_scale}"
        off = f", offset={self.ring_offset}"
        t = f", tooltip='{self.ring_tooltip}'"
        bg = f", bgcolor='{self.ring_bgcolor}'"
        c = f", color='{self.ring_color}'"
        w = f", width={self.ring_width}"
        h = f", height={self.ring_height}"
        sw = f", stroke_width={self.ring_stroke_width}"

        others = f"{sw if self.ring_stroke_width is not None else ''}{w if self.ring_width is not None else ''}{h if self.ring_height is not None else ''}{c if self.ring_color is not None else ''}{bg if self.ring_bgcolor is not None else ''}{t if self.ring_tooltip is not None else ''}{o if self.ring_opacity is not None else ''}{s if self.ring_scale is not None else ''}{off if self.ring_offset is not None else ''}"
        val = f"ProgressRing(value={self.ring_value}{others if others else ''})"
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.add(TabContentProgressRing())


    ft.app(main)
