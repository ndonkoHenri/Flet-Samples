from flet import *
import flet as ft


# the content of the icon tab
class TabContentIcon(UserControl):

    def __init__(self):
        super().__init__()
        self.icon_color = "cake_rounded"
        self.icon_name = None
        self.icon_size = 65
        self.icon_tooltip = None

        self.icon_obj = Ref[Icon]()

        # text field for message property of the Icon object
        self.field_tooltip = TextField(
            label="tooltip",
            value="",
            on_change=self.update_icon,
            keyboard_type=KeyboardType.TEXT,
            expand=2
        )

        # text field for bgcolor property of the Icon object
        self.field_color = TextField(
            label="color",
            value="red900",
            on_submit=self.update_icon,
            on_blur=self.update_icon,
            keyboard_type=KeyboardType.TEXT,
            hint_text="colors.RED_50 or red50",
            expand=1
        )

        # text field for the show_duration property of the Icon object
        self.field_size = TextField(
            label="size",
            value="65",
            on_change=self.update_icon,
            keyboard_type=KeyboardType.NUMBER,
            hint_text="2000",
            # width=125,
            expand=1
        )

        # text field for the vertical_offset property of the Icon object
        self.field_name = TextField(
            label="name",
            hint_text="ft.icons.COPY or COPY or copy",
            value="cake_rounded",
            on_submit=self.update_icon,
            on_blur=self.update_icon,
            keyboard_type=KeyboardType.TEXT,
            expand=2
        )

    def build(self):

        all_fields = Column(
            controls=[
                Row(
                    [self.field_name, self.field_color],
                ),
                Row(
                    [self.field_tooltip, self.field_size],
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )

        return Column(
            [
                Text("Icon Builder:", weight=FontWeight.BOLD, size=21),
                all_fields,
                Row(
                    [
                        Icon(
                            ref=self.icon_obj,
                            name="cake_rounded",
                            size=65,
                            tooltip=self.icon_tooltip,
                            color="red900"
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
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
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/icon")
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
            scroll=ScrollMode.HIDDEN,
            spacing=20
        )

    def update_icon(self, e: ControlEvent):
        """
        It updates the Icon object.
        :param e: The event object
        """
        self.icon_size = int(self.field_size.value.strip()) if self.field_size.value.strip().isnumeric() else 50
        self.icon_color = self.field_color.value.strip() if self.field_color.value.strip() else None
        self.icon_name = self.field_name.value.strip() if self.field_name.value.strip() else "cake_rounded"
        self.icon_tooltip = self.field_tooltip.value.strip() if self.field_tooltip.value.strip() else None

        # name
        try:
            if self.icon_name is not None:
                self.icon_name = eval(self.icon_name) if '.' in self.icon_name else self.icon_name.lower()

                # Getting all the icons from flet's icons module
                list_started = False
                all_flet_icons = list()
                for value in vars(icons).values():
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
                SnackBar(
                    Text(
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
                for value in vars(colors).values():
                    if value == "primary":
                        list_started = True
                    if list_started:
                        all_flet_colors.append(value)

                # checking if all the entered colors exist in flet
                if self.icon_color not in all_flet_colors:
                    raise ValueError("Wrong Value!")
        except Exception as x:
            print(f"Color Error: {x}")
            e.page.show_snack_bar(
                SnackBar(
                    Text(
                        "ERROR: There seems to be an error with your colors. Check the Colors V1/V2 tabs for "
                        f"help with color-choosing.!"),
                    open=True))
            return

        self.icon_obj.current.color = self.icon_color
        self.icon_obj.current.tooltip = self.icon_tooltip
        self.icon_obj.current.name = self.icon_name
        self.icon_obj.current.size = self.icon_size

        self.update()
        e.page.show_snack_bar(SnackBar(Text("Updated Tooltip!"), open=True))

    def copy_to_clipboard(self, e: ControlEvent):
        """
        It copies the tooltip object/instance to the clipboard.

        :param e: The event object
        """
        t = f'Icon(name={self.icon_name}, color="{self.icon_color}", size={self.icon_size}, tooltip="{self.icon_tooltip}")'
        e.page.set_clipboard(t)
        e.page.show_snack_bar(SnackBar(Text(f"Copied: {t}"), open=True))
        print(t)
