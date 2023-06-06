from flet import *
import flet as ft


# todo: "rotate" from icon_utils

# the content of the circle avatar tab
class TabContentCircleAvatar(ft.UserControl):

    def __init__(self):
        super().__init__()

        self.avatar_background_image_url = None
        self.avatar_foreground_image_url = None
        self.avatar_content = None
        self.avatar_radius = None
        self.avatar_color = None
        self.avatar_bgcolor = None
        self.avatar_tooltip = None
        self.avatar_min_radius = None
        self.avatar_max_radius = None
        self.avatar_width = None
        self.avatar_height = None

        self.avatar_opacity = None
        self.avatar_rotate = None
        self.avatar_scale = None
        self.avatar_offset = None

        self.avatar_obj = ft.Ref[ft.CircleAvatar]()

        # text field for tooltip property of the CircleAvatar object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_avatar,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the CircleAvatar object
        self.field_color = ft.TextField(
            label="color",
            value="",
            helper_text="Optional[str]",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the bgcolor property of the CircleAvatar object
        self.field_bgcolor = ft.TextField(
            label="bgcolor",
            value="",
            helper_text="Optional[str]",
            hint_text="colors.RED_50 or red50",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1,
            # width=170,
        )

        # text field for background_image_url property of the CircleAvatar object
        self.field_background_image_url = ft.TextField(
            label="background_image_url",
            value="",
            helper_text="Optional[str]",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="",
            expand=1,
            text_style=ft.TextStyle(color=ft.colors.BLUE)
        )

        # text field for foreground_image_url property of the CircleAvatar object
        self.field_foreground_image_url = ft.TextField(
            label="foreground_image_url",
            value="https://avatars.githubusercontent.com/u/5041459?s=88&v=4",
            helper_text="Optional[str]",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="",
            expand=1,
            text_style=ft.TextStyle(color=ft.colors.BLUE)
        )

        # text field for the radius property of the CircleAvatar object
        self.field_radius = ft.TextField(
            label="radius",
            helper_text="Union[int, float]",
            # value="4",
            on_change=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the max_radius property of the CircleAvatar object
        self.field_max_radius = ft.TextField(
            label="max_radius",
            helper_text="Union[int, float]",
            # value="4",
            on_change=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the min_radius property of the CircleAvatar object
        self.field_min_radius = ft.TextField(
            label="min_radius",
            helper_text="Union[int, float]",
            # value="4",
            on_change=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the content property of the CircleAvatar object
        self.field_content = ft.TextField(
            label="content",
            value="",
            helper_text="Optional[Control]",
            hint_text="Text('Hello')",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            # width=80,
            expand=1
        )

        # text field for the width property of the CircleAvatar object
        self.field_width = ft.TextField(
            label="width",
            value="",
            helper_text="Union[int, float]",
            on_submit=self.update_avatar,
            on_blur=self.update_avatar,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the height property of the CircleAvatar object
        self.field_height = ft.TextField(
            label="height",
            value="",
            helper_text="Union[int, float]",
            on_submit=self.update_avatar,
            on_blur=self.update_avatar,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=80,
            expand=1
        )

        # text field for the opacity property of the CircleAvatar object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.NUMBER,
            # width=170,
            expand=1
        )

        # text field for the offset property of the CircleAvatar object
        self.field_offset = ft.TextField(
            label="offset",
            value="",
            helper_text="Optional[Offset, tuple]",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for the scale property of the CircleAvatar object
        self.field_scale = ft.TextField(
            label="scale",
            value="",
            helper_text="Union[int, float, Scale]",
            on_submit=self.update_avatar,
            # on_blur=self.update_icon,
            keyboard_type=ft.KeyboardType.TEXT,
            # width=110,
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_content, self.field_foreground_image_url, self.field_background_image_url],
                ),
                ft.Row(
                    [self.field_bgcolor, self.field_color, self.field_radius, self.field_min_radius, self.field_max_radius, self.field_opacity]
                ),
                ft.Row(
                    [self.field_height, self.field_width, self.field_offset, self.field_scale, self.field_tooltip, ],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11
        )

        return ft.Column(
            [
                ft.Text("Circle Avatar Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.CircleAvatar(
                            ref=self.avatar_obj,
                            foreground_image_url="https://avatars.githubusercontent.com/u/5041459?s=88&v=4"
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
                            url="https://flet.dev/docs/controls/circleavatar"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30
        )

    def update_avatar(self, e: ft.ControlEvent):
        """It updates the CircleAvatar object."""
        self.avatar_opacity, self.avatar_radius, self.avatar_min_radius, self.avatar_max_radius = (
            int(self.field_opacity.value.strip()) if self.field_opacity.value.strip().isnumeric() else None,
            int(self.field_radius.value.strip()) if self.field_radius.value.strip().isnumeric() else None,
            int(self.field_min_radius.value.strip()) if self.field_min_radius.value.strip().isnumeric() else None,
            int(self.field_max_radius.value.strip()) if self.field_max_radius.value.strip().isnumeric() else None
        )
        self.avatar_foreground_image_url, self.avatar_background_image_url = self.field_foreground_image_url.value, self.field_background_image_url.value

        self.avatar_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.avatar_bgcolor = self.field_bgcolor.value.strip() if self.field_bgcolor.value.strip() else None
        self.avatar_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        self.avatar_offset = self.field_offset.value.strip() if self.field_offset.value.strip() else "None"
        self.avatar_scale = self.field_scale.value.strip() if self.field_scale.value.strip() else "None"

        # content
        try:
            if self.field_content.value:
                self.avatar_content = eval(self.field_content.value)
                assert isinstance(self.avatar_content, ft.Control), "`content` must be a flet Control !"
            else:
                self.avatar_content = None
        except Exception as x:
            print(f"Content Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # radius
        try:
            if self.field_radius.value:
                self.avatar_radius = eval(self.field_radius.value)
                assert isinstance(self.avatar_radius,
                                  (int, float)), "`radius` must be either of type float or int !"
            else:
                self.avatar_radius = None
        except Exception as x:
            print(f"Radius Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # min_radius
        try:
            if self.field_min_radius.value:
                self.avatar_min_radius = eval(self.field_min_radius.value)
                assert isinstance(self.avatar_min_radius,
                                  (int, float)), "`min_radius` must be either of type float or int !"
            else:
                self.avatar_min_radius = None
        except Exception as x:
            print(f"Min Radius Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # max_radius
        try:
            if self.field_max_radius.value:
                self.avatar_max_radius = eval(self.field_max_radius.value)
                assert isinstance(self.avatar_max_radius,
                                  (int, float)), "`max_radius` must be either of type float or int !"
            else:
                self.avatar_max_radius = None
        except Exception as x:
            print(f"Max Radius Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # width
        try:
            if self.field_width.value:
                self.avatar_width = eval(self.field_width.value)
                assert isinstance(self.avatar_width, (int, float)), "`width` must be either of type float or int !"
            else:
                self.avatar_width = None
        except Exception as x:
            print(f"Width Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # height
        try:
            if self.field_height.value:
                self.avatar_height = eval(self.field_height.value)
                assert isinstance(self.avatar_height, (int, float)), "`height` must be either of type float or int !"
            else:
                self.avatar_height = None
        except Exception as x:
            print(f"Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.avatar_color is not None:
                self.avatar_color = eval(self.avatar_color) if '.' in self.avatar_color else self.avatar_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.avatar_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # bgcolor
        try:
            if self.avatar_bgcolor is not None:
                self.avatar_bgcolor = eval(
                    self.avatar_bgcolor) if '.' in self.avatar_bgcolor else self.avatar_bgcolor.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.avatar_bgcolor not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Bgcolor Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # offset
        try:
            self.avatar_offset = eval(self.avatar_offset)
            if not isinstance(self.avatar_offset, ft.Offset) \
                    and not isinstance(self.avatar_offset, tuple) \
                    and self.avatar_offset is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.avatar_offset, tuple) and len(self.avatar_offset) == 2:
                self.avatar_offset = eval(f"Offset({self.avatar_offset[0]}, {self.avatar_offset[1]})")
        except Exception as x:
            print(f"Offset Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `offset` must be an Offset object or in the form x,y. Please check your input."),
                    open=True))
            return

        # scale
        try:
            self.avatar_scale = eval(self.avatar_scale)
            if not isinstance(self.avatar_scale, ft.Scale) \
                    and not isinstance(self.avatar_scale, (int, float)) \
                    and self.avatar_scale is not None:
                raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Scale Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(ft.Text("ERROR: `scale` must be an Scale object. Please check your input."), open=True))
            return

        # opacity
        try:
            if self.field_opacity.value:
                self.avatar_opacity = eval(self.field_opacity.value)
                assert isinstance(self.avatar_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.avatar_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.avatar_obj.current.color = self.avatar_color
        self.avatar_obj.current.bgcolor = self.avatar_bgcolor
        self.avatar_obj.current.tooltip = self.avatar_tooltip
        self.avatar_obj.current.foreground_image_url = self.avatar_foreground_image_url
        self.avatar_obj.current.background_image_url = self.avatar_background_image_url
        self.avatar_obj.current.content = self.avatar_content
        self.avatar_obj.current.radius = self.avatar_radius
        self.avatar_obj.current.min_radius = self.avatar_min_radius
        self.avatar_obj.current.max_radius = self.avatar_max_radius

        self.avatar_obj.current.width = self.avatar_width
        self.avatar_obj.current.height = self.avatar_height

        self.avatar_obj.current.opacity = self.avatar_opacity
        self.avatar_obj.current.scale = self.avatar_scale
        self.avatar_obj.current.offset = self.avatar_offset
        # todo self.avatar_obj.current.rotate = self.avatar_rotate

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated CircleAvatar!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.avatar_opacity}"
        s = f", scale={self.avatar_scale}"
        off = f", offset={self.avatar_offset}"
        t = f", tooltip='{self.avatar_tooltip}'"
        bg = f", bgcolor='{self.avatar_bgcolor}'"
        c = f", color='{self.avatar_color}'"
        w = f", width={self.avatar_width}"
        h = f", height={self.avatar_height}"

        r = f", radius={self.avatar_radius}"
        minr = f", min_radius={self.avatar_min_radius}"
        maxr = f", max_radius={self.avatar_max_radius}"

        burl = f", background_image_url='{self.avatar_background_image_url}'"
        furl = f", foreground_image_url='{self.avatar_foreground_image_url}'"

        others = f"{maxr if self.avatar_max_radius is not None else ''}{minr if self.avatar_min_radius is not None else ''}{furl if self.avatar_foreground_image_url else ''}{burl if self.avatar_background_image_url else ''}{r if self.avatar_radius is not None else ''}{w if self.avatar_width is not None else ''}{h if self.avatar_height is not None else ''}{c if self.avatar_color is not None else ''}{bg if self.avatar_bgcolor is not None else ''}{t if self.avatar_tooltip else ''}{o if self.avatar_opacity is not None else ''}{s if self.avatar_scale is not None else ''}{off if self.avatar_offset is not None else ''}"
        val = f"CircleAvatar(radius={self.avatar_radius}{others if others else ''})"
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.add(TabContentCircleAvatar())


    ft.app(main)
