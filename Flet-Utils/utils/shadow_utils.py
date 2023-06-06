from flet import *
import flet as ft


# todo: change  link to docs

# the content of the shadow tab
class TabContentShadow(ft.UserControl):

    def __init__(self):
        super().__init__()
        self.shadow_color = None
        self.shadow_offset = None
        self.shadow_blur_radius = None
        self.shadow_spread_radius = None
        self.shadow_blur_style = None

        self.container_bgcolor = None

        self.shadow_obj = ft.Ref[ft.Container]()

        # text field for offset property of the BoxShadow object
        self.field_offset = ft.TextField(
            label="offset",
            value="",
            helper_text="Optional[Offset, tuple]",
            on_submit=self.update_shadow,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the BoxShadow object
        self.field_color = ft.TextField(
            label="color",
            value="",
            helper_text="Optional[str]",
            on_submit=self.update_shadow,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the spread_radius property of the BoxShadow object
        self.field_spread_radius = ft.TextField(
            label="spread_radius",
            helper_text="Union[int, float]",
            value="",
            on_change=self.update_shadow,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the blur_radius property of the BoxShadow object
        self.field_blur_radius = ft.TextField(
            label="blur_radius",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_shadow,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # radio buttons for the blur_style parameter
        self.blur_style_radio_group = ft.RadioGroup(
            ft.Row(
                [
                    ft.Radio(value="normal", label="normal"),
                    ft.Radio(value="solid", label="solid"),
                    ft.Radio(value="outer", label="outer"),
                    ft.Radio(value="inner", label="inner"),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            ),
            value="normal",
            on_change=self.update_shadow,
        )

        # text field for bgcolor property of the shown container
        self.field_container_bgcolor = ft.TextField(
            label="bgcolor",
            value="amber",
            helper_text="Optional[str]",
            on_submit=self.update_shadow,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_spread_radius, self.field_blur_radius]
                ),
                self.blur_style_radio_group,
                ft.Row(
                    [self.field_color, self.field_offset, self.field_container_bgcolor],
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11,
        )

        return ft.Column(
            [
                ft.Text("BoxShadow Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.Container(
                            ref=self.shadow_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=150,
                            height=150,
                        ),
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
                            url="https://flet.dev/docs/controls/verticaldivider/"
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30,
            expand=True
        )

    def update_shadow(self, e: ft.ControlEvent):
        """It updates the Shadow object."""
        self.shadow_blur_radius, self.shadow_spread_radius = (
            int(self.field_spread_radius.value.strip()) if self.field_spread_radius.value.strip().isnumeric() else None,
            int(self.field_blur_radius.value.strip()) if self.field_blur_radius.value.strip().isnumeric() else None,
        )

        self.shadow_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.shadow_offset = self.field_offset.value.strip() if self.field_offset.value.strip() else None
        self.shadow_blur_style = self.blur_style_radio_group.value
        
        self.container_bgcolor = self.field_container_bgcolor.value.strip() if self.field_container_bgcolor.value.strip() else None

        # spread_radius
        try:
            if self.field_spread_radius.value:
                self.shadow_blur_radius = eval(self.field_spread_radius.value)
                assert isinstance(self.shadow_blur_radius,
                                  (int, float)), "`spread_radius` must be either of type float or int !"
            else:
                self.shadow_blur_radius = None
        except Exception as x:
            print(f"Spread Radius Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # blur_radius
        try:
            if self.field_blur_radius.value:
                self.shadow_spread_radius = eval(self.field_blur_radius.value)
                assert isinstance(self.shadow_spread_radius,
                                  (int, float)), "`blur_radius` must be either of type float or int !"
            else:
                self.shadow_spread_radius = None
        except Exception as x:
            print(f"Blur Radius Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.shadow_color is not None:
                self.shadow_color = eval(self.shadow_color) if '.' in self.shadow_color else self.shadow_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.shadow_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # container bgcolor
        try:
            if self.container_bgcolor is not None:
                self.container_bgcolor = eval(
                    self.container_bgcolor) if '.' in self.container_bgcolor else self.container_bgcolor.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.container_bgcolor not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"BgColor Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # offset
        try:
            if self.shadow_offset is not None:
                self.shadow_offset = eval(self.shadow_offset)
            if not isinstance(self.shadow_offset, ft.Offset) \
                    and not isinstance(self.shadow_offset, tuple) \
                    and self.shadow_offset is not None:
                raise ValueError("Wrong Value!")
            elif isinstance(self.shadow_offset, tuple) and len(self.shadow_offset) == 2:
                self.shadow_offset = eval(f"Offset({self.shadow_offset[0]}, {self.shadow_offset[1]})")
        except Exception as x:
            print(f"Offset Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `offset` must be an Offset object or in the form x,y. Please check your input."),
                    open=True))
            return

        self.shadow_obj.current.shadow = ft.BoxShadow(self.shadow_spread_radius, self.shadow_blur_radius, self.shadow_color, self.shadow_offset, self.shadow_blur_style)
        self.shadow_obj.current.bgcolor = self.container_bgcolor

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated BoxShadow!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the Shadow object/instance to the clipboard."""
        val = self.shadow_obj.current.shadow
        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_always_on_top = True
        page.add(TabContentShadow())


    ft.app(main)
