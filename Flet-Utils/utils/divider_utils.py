from flet import *
import flet as ft


# the content of the divider tab
class TabContentDivider(ft.UserControl):

    def __init__(self):
        super().__init__()

        self.divider_color = "green"
        self.divider_tooltip = None
        self.divider_thickness = 4
        self.divider_height = None
        self.divider_opacity = None

        self.top_con_obj = ft.Ref[ft.Container]()
        self.divider_obj = ft.Ref[ft.Divider]()
        self.bottom_con_obj = ft.Ref[ft.Container]()

        # text field for tooltip property of the Divider object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_divider,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the Divider object
        self.field_color = ft.TextField(
            label="color",
            value="green",
            helper_text="Optional[str]",
            on_submit=self.update_divider,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the thickness property of the Divider object
        self.field_thickness = ft.TextField(
            label="thickness",
            helper_text="Union[int, float]",
            value="4",
            on_change=self.update_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the height property of the Divider object
        self.field_height = ft.TextField(
            label="height",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the opacity property of the Divider object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # checkbox
        self.containers_checkbox = ft.Checkbox(
            label="Don't show top and bottom containers.",
            on_change=self.update_divider,
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_thickness, self.field_height, self.field_opacity]
                ),
                ft.Row(
                    [self.field_color, self.field_tooltip, ],
                ),
                self.containers_checkbox
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11,
        )

        w, h = 300, 50

        return ft.Column(
            [
                ft.Text("Divider Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Column(
                    [
                        ft.Container(
                            ref=self.top_con_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=w,
                            height=h,
                        ),
                        ft.Divider(
                            ref=self.divider_obj,
                            thickness=4,
                            color="green"
                        ),
                        ft.Container(
                            ref=self.bottom_con_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=w,
                            height=h,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=0,
                    width=w
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/divider/")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )

            ],
            alignment=ft.MainAxisAlignment.CENTER,
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30,
            expand=True
        )

    def update_divider(self, e: ft.ControlEvent):
        """It updates the Divider object."""
        self.divider_opacity, self.divider_thickness, self.divider_height = (
            int(self.field_opacity.value.strip()) if self.field_opacity.value.strip().isnumeric() else None,
            int(self.field_thickness.value.strip()) if self.field_thickness.value.strip().isnumeric() else None,
            int(self.field_height.value.strip()) if self.field_height.value.strip().isnumeric() else None,
        )

        self.divider_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.divider_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        # thickness
        try:
            if self.field_thickness.value:
                self.divider_thickness = eval(self.field_thickness.value)
                assert isinstance(self.divider_thickness,
                                  (int, float)), "`thickness` must be either of type float or int !"
            else:
                self.divider_thickness = None
        except Exception as x:
            print(f"Thickness Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # height
        try:
            if self.field_height.value:
                self.divider_height = eval(self.field_height.value)
                assert isinstance(self.divider_height, (int, float)), "`height` must be either of type float or int !"
            else:
                self.divider_height = None
        except Exception as x:
            print(f"Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.divider_color is not None:
                self.divider_color = eval(self.divider_color) if '.' in self.divider_color else self.divider_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.divider_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # opacity
        try:
            if self.field_opacity.value:
                self.divider_opacity = eval(self.field_opacity.value)
                assert isinstance(self.divider_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.divider_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.divider_obj.current.color = self.divider_color
        self.divider_obj.current.tooltip = self.divider_tooltip
        self.divider_obj.current.thickness = self.divider_thickness
        self.divider_obj.current.height = self.divider_height
        self.divider_obj.current.opacity = self.divider_opacity

        self.top_con_obj.current.visible = not self.containers_checkbox.value
        self.bottom_con_obj.current.visible = not self.containers_checkbox.value

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated Divider!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.divider_opacity}"
        t = f", tooltip='{self.divider_tooltip}'"
        c = f", color='{self.divider_color}'"
        th = f", thickness={self.divider_thickness}"

        others = f"{th if self.divider_thickness is not None else ''}{c if self.divider_color is not None else ''}{t if self.divider_tooltip else ''}{o if self.divider_opacity is not None else ''}"
        val = f"Divider(height={self.divider_height}{others if others else ''})"

        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        page.window_always_on_top = True
        page.add(TabContentDivider())


    ft.app(main)
