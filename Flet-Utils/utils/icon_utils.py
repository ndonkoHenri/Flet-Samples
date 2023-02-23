import math
from flet import *
import flet as ft


# the content of the icon tab
class TabContentIcon(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.icon_color = "red900"
        self.icon_name = "cake_rounded"
        self.icon_size = 65
        self.icon_tooltip = None
        self.icon_opacity = None
        self.icon_rotate = None
        self.icon_scale = None
        self.icon_offset = None

        self.icon_obj = ft.Ref[ft.Icon]()

        # text field for tooltip property of the Icon object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the Icon object
        self.field_color = ft.TextField(
            label="color",
            value="red900",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the size property of the Icon object
        self.field_size = ft.TextField(
            label="size",
            value="65",
            helper_text="Union[int, float]",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # expand=1
            width=170,
        )

        # text field for the name property of the Icon object
        self.field_name = ft.TextField(
            label="name",
            hint_text="ft.icons.COPY or COPY or copy",
            value="cake_rounded",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=2
        )

        # text field for the opacity property of the Icon object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            width=170,
            # expand=1
        )

        # text field for the rotate property of the Icon object
        self.field_rotate = ft.TextField(
            label="rotate | angle in degrees",
            value="",
            helper_text="Union[int, float, Rotate]",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the offset property of the Icon object
        self.field_offset = ft.TextField(
            label="offset",
            value="",
            helper_text="Optional[Offset]",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the scale property of the Icon object
        self.field_scale = ft.TextField(
            label="scale",
            value="",
            helper_text="Union[int, float, Scale]",
            on_submit=self.update_icon,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            # width=110,
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_name, self.field_color],
                ),
                ft.Row(
                    [self.field_tooltip, self.field_scale],
                ),
                ft.Row(
                    [self.field_rotate, self.field_offset],
                ),
                ft.Row(
                    [self.field_size, self.field_opacity],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11
        )

        return ft.Column(
            [
                ft.Text("Icon Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.Icon(
                            ref=self.icon_obj,
                            name="cake_rounded",
                            size=65,
                            color="red900"
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/icon")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=25
        )

    def update_icon(self, e: ft.ControlEvent):
        """
        It updates the Icon object.
        :param e: The event object
        """

        self.icon_size= int(self.field_size.value.strip()) if self.field_size.value.strip().isnumeric() else 65

        self.icon_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.icon_name = self.field_name.value.strip() if self.field_name.value.strip() else "cake_rounded"
        self.icon_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        self.icon_offset = self.field_offset.value.strip() if self.field_offset.value.strip() else "None"
        self.icon_rotate = self.field_rotate.value.strip() if self.field_rotate.value.strip() else "None"
        self.icon_scale = self.field_scale.value.strip() if self.field_scale.value.strip() else "None"

        # name
        try:
            if self.icon_name is not None:
                self.icon_name = eval(self.icon_name) if '.' in self.icon_name else self.icon_name.lower()

                # Getting all the icons from flet's icons module
                list_started = False
                all_flet_icons = list()
                for value in vars(ft.icons).values():
                    if value == "ten_k":
                        list_started = True
                    if list_started:
                        all_flet_icons.append(value)

                # checking if all the entered icons exist in flet
                if self.icon_name not in all_flet_icons:
                    raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Name Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: There seems to be an error with your icon's name. See the Icon tabs for "
                        f"help with choosing an icon name!"),
                    open=True))
            return

        # color
        try:
            if self.icon_color is not None:
                self.icon_color = eval(self.icon_color) if '.' in self.icon_color else self.icon_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.icon_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # offset
        try:
            self.icon_offset = eval(self.icon_offset)
            if not isinstance(self.icon_offset, ft.Offset) \
                    and not isinstance(self.icon_offset, tuple) \
                    and self.icon_offset is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.icon_offset, tuple) and len(self.icon_offset) == 2:
                self.icon_offset = eval(f"Offset({self.icon_offset[0]}, {self.icon_offset[1]})")
        except Exception as x:
            print(f"Offset Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `offset` must be an Offset object or in the form x,y. Please check your input."),
                    open=True))
            return

        # rotate - input is assumed to be in degrees (which is in turn converted to rads internally)
        try:
            self.icon_rotate = eval(self.icon_rotate)
            deg_to_rads = lambda d: round((math.pi * float(d)) / 180, 3)
            if not isinstance(self.icon_rotate, ft.Rotate) \
                    and not isinstance(self.icon_rotate, (int, float)) \
                    and self.icon_rotate is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.icon_rotate, ft.Rotate):
                self.icon_rotate.angle = deg_to_rads(self.icon_rotate.angle)
            elif isinstance(self.icon_rotate, (int, float)):
                self.icon_rotate = deg_to_rads(self.icon_rotate)
            elif isinstance(self.icon_rotate, tuple) and len(self.icon_rotate) == 2:
                self.icon_rotate = eval(f"Rotate({deg_to_rads(self.icon_rotate[0])}, {self.icon_rotate[1]})")
        except Exception as x:
            print(f"Rotate Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `rotate` must be an Rotate object or in the form angle,alignment. Please check your input."),
                    open=True))
            return

        # scale
        try:
            self.icon_scale = eval(self.icon_scale)
            if not isinstance(self.icon_scale, ft.Scale) \
                    and not isinstance(self.icon_scale, (int, float)) \
                    and self.icon_scale is not None:
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
                self.icon_opacity = eval(self.field_opacity.value)
                assert isinstance(self.icon_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.icon_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.icon_obj.current.color = self.icon_color
        self.icon_obj.current.tooltip = self.icon_tooltip
        self.icon_obj.current.name = self.icon_name
        self.icon_obj.current.size = self.icon_size
        self.icon_obj.current.opacity = self.icon_opacity
        self.icon_obj.current.scale = self.icon_scale
        self.icon_obj.current.rotate = self.icon_rotate
        self.icon_obj.current.offset = self.icon_offset

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Icon!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.icon_opacity}"
        s = f", scale={self.icon_scale}"
        r = f", rotate={self.icon_rotate}"
        off = f", offset={self.icon_offset}"
        t = f", tooltip='{self.icon_tooltip}'"
        c = f", color='{self.icon_color}'"

        others = f"{c if self.icon_color is not None else ''}{t if self.icon_tooltip is not None else ''}{o if self.icon_opacity is not None else ''}{s if self.icon_scale is not None else ''}{off if self.icon_offset is not None else ''}{r if self.icon_rotate is not None else ''}"
        val = f"Icon(name='{self.icon_name}', size={self.icon_size}{others if others else ''})"
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentIcon())


    ft.app(main)
