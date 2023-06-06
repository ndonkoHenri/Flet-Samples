from flet import *
import flet as ft


# the content of the vertical_divider tab
class TabContentVerticalDivider(ft.UserControl):

    def __init__(self):
        super().__init__()

        self.vertical_divider_color = "green"
        self.vertical_divider_tooltip = None
        self.vertical_divider_thickness = 4
        self.vertical_divider_width = None
        self.vertical_divider_opacity = None

        self.left_con_obj = ft.Ref[ft.Container]()
        self.vertical_divider_obj = ft.Ref[ft.VerticalDivider]()
        self.right_con_obj = ft.Ref[ft.Container]()

        # text field for tooltip property of the VerticalDivider object
        self.field_tooltip = ft.TextField(
            label="tooltip",
            value="",
            helper_text="Optional[str]",
            on_change=self.update_vertical_divider,
            keyboard_type=ft.KeyboardType.TEXT,
            expand=1
        )

        # text field for color property of the VerticalDivider object
        self.field_color = ft.TextField(
            label="color",
            value="green",
            helper_text="Optional[str]",
            on_submit=self.update_vertical_divider,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the thickness property of the VerticalDivider object
        self.field_thickness = ft.TextField(
            label="thickness",
            helper_text="Union[int, float]",
            value="4",
            on_change=self.update_vertical_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the width property of the VerticalDivider object
        self.field_width = ft.TextField(
            label="width",
            value="10",
            helper_text="Union[int, float]",
            on_change=self.update_vertical_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # text field for the opacity property of the VerticalDivider object
        self.field_opacity = ft.TextField(
            label="opacity",
            value="",
            helper_text="Union[int, float]",
            on_change=self.update_vertical_divider,
            keyboard_type=ft.KeyboardType.NUMBER,
            expand=1
        )

        # checkbox
        self.containers_checkbox = ft.Checkbox(
            label="Don't show left and right containers.",
            on_change=self.update_vertical_divider,
        )

    def build(self):
        all_fields = ft.Column(
            controls=[
                ft.Row(
                    [self.field_thickness, self.field_width, self.field_opacity]
                ),
                ft.Row(
                    [self.field_color, self.field_tooltip],
                ),
                self.containers_checkbox
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=11,
        )

        w, h = 125, 200

        return ft.Column(
            [
                ft.Text("VerticalDivider Builder:", weight=ft.FontWeight.BOLD, size=21),
                all_fields,
                ft.Row(
                    [
                        ft.Container(
                            ref=self.left_con_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=w,
                            height=h,
                        ),
                        ft.VerticalDivider(
                            ref=self.vertical_divider_obj,
                            width=10,
                            thickness=4,
                            color="green"
                        ),
                        ft.Container(
                            ref=self.right_con_obj,
                            bgcolor=ft.colors.AMBER,
                            alignment=ft.alignment.center,
                            width=w,
                            height=h,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    # spacing=0,
                    height=h,
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
            # horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
            spacing=30,
            expand=True
        )

    def update_vertical_divider(self, e: ft.ControlEvent):
        """It updates the VerticalDivider object."""
        self.vertical_divider_opacity, self.vertical_divider_thickness, self.vertical_divider_width = (
            int(self.field_opacity.value.strip()) if self.field_opacity.value.strip().isnumeric() else None,
            int(self.field_thickness.value.strip()) if self.field_thickness.value.strip().isnumeric() else None,
            int(self.field_width.value.strip()) if self.field_width.value.strip().isnumeric() else None,
        )

        self.vertical_divider_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.vertical_divider_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        # thickness
        try:
            if self.field_thickness.value:
                self.vertical_divider_thickness = eval(self.field_thickness.value)
                assert isinstance(self.vertical_divider_thickness,
                                  (int, float)), "`thickness` must be either of type float or int !"
            else:
                self.vertical_divider_thickness = None
        except Exception as x:
            print(f"Thickness Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # width
        try:
            if self.field_width.value:
                self.vertical_divider_width = eval(self.field_width.value)
                assert isinstance(self.vertical_divider_width, (int, float)), "`width` must be either of type float or int !"
            else:
                self.vertical_divider_width = None
        except Exception as x:
            print(f"Height Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # color
        try:
            if self.vertical_divider_color is not None:
                self.vertical_divider_color = eval(self.vertical_divider_color) if '.' in self.vertical_divider_color else self.vertical_divider_color.lower()

                # Getting all the colors from flet's colors module
                list_started = False
                all_flet_colors = list()
                for value in vars(ft.colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.vertical_divider_color not in all_flet_colors:
                    raise ValueError("Entered color was not found! See the colors browser for help!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        # opacity
        try:
            if self.field_opacity.value:
                self.vertical_divider_opacity = eval(self.field_opacity.value)
                assert isinstance(self.vertical_divider_opacity, (int, float)), "`opacity` must be either of type float or int !"
            else:
                self.vertical_divider_opacity = None
        except Exception as x:
            print(f"Opacity Error: {x}")
            e.page.show_snack_bar(ft.SnackBar(ft.Text(f"ERROR: {x}"), open=True))
            return

        self.vertical_divider_obj.current.color = self.vertical_divider_color
        self.vertical_divider_obj.current.tooltip = self.vertical_divider_tooltip
        self.vertical_divider_obj.current.thickness = self.vertical_divider_thickness
        self.vertical_divider_obj.current.width = self.vertical_divider_width
        self.vertical_divider_obj.current.opacity = self.vertical_divider_opacity

        self.left_con_obj.current.visible = not self.containers_checkbox.value
        self.right_con_obj.current.visible = not self.containers_checkbox.value

        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated VerticalDivider!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """It copies the tooltip object/instance to the clipboard."""
        o = f", opacity={self.vertical_divider_opacity}"
        t = f", tooltip='{self.vertical_divider_tooltip}'"
        c = f", color='{self.vertical_divider_color}'"
        th = f", thickness={self.vertical_divider_thickness}"

        others = f"{th if self.vertical_divider_thickness is not None else ''}{c if self.vertical_divider_color is not None else ''}{t if self.vertical_divider_tooltip else ''}{o if self.vertical_divider_opacity is not None else ''}"
        val = f"VerticalDivider(width={self.vertical_divider_width}{others if others else ''})"

        e.page.set_clipboard(val)
        e.page.show_snack_bar(ft.SnackBar(ft.Text(f"Copied: {val}"), open=True))
        print(val)


if __name__ == "__main__":
    def main(page: ft.Page):
        page.theme_mode = ft.ThemeMode.LIGHT
        # page.horizontal_alignment = "center"
        page.window_always_on_top = True
        page.add(TabContentVerticalDivider())


    ft.app(main)
