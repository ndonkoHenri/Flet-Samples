import flet as ft
from utils.padding_utils import TabContentPadding
from utils.alignment_utils import TabContentAlignment
from utils.border_utils import TabContentBorder
from utils.border_radius_utils import TabContentBorderRadius
from utils.colors_utils import TabContentColors1, TabContentColors2
from utils.icons_browser_utils import TabContentIconsBrowser
from utils.gradient_utils import TabContentLinearGradient, TabContentSweepGradient, TabContentRadialGradient
from utils.shadermask_utils import TabContentShaderMask
from utils.shape_utils import TabContentShape
from utils.tooltip_utils import TabContentTooltip
from utils.icon_utils import TabContentIcon
from utils.progress_ring_utils import TabContentProgressRing
from utils.progress_bar_utils import TabContentProgressBar
from utils.divider_utils import TabContentDivider
from utils.vertical_divider_utils import TabContentVerticalDivider
from utils.circle_avatar_utils import TabContentCircleAvatar
from utils.shadow_utils import TabContentShadow
from utils.blur_utils import TabContentBlur


def main(page: ft.Page):
    page.title = "Flet Utilities"
    page.theme_mode = "light"
    # page.window_always_on_top = True
    page.vertical_alignment = "start"

    # set the width and height of the window.
    page.window_width = 640
    page.window_height = 750

    # page.horizontal_alignment = "center"

    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        page.update()

    theme_icon_button = ft.IconButton(
        ft.icons.DARK_MODE,
        selected=False,
        selected_icon=ft.icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ft.ButtonStyle(color={"": ft.colors.BLACK, "selected": ft.colors.WHITE}, ),
    )

    page.appbar = ft.AppBar(
        title=ft.Text(
            "Flet Utilities",
            color="white"
        ),
        center_title=True,
        bgcolor="blue",
        actions=[theme_icon_button],
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            on_click=lambda e: page.launch_url(
                "https://github.com/ndonkoHenri/Flet-Samples/tree/master/Flet-Utils"),
            tooltip="View Code"
        ),
    )

    icon_content = TabContentIcon()
    tooltip_content = TabContentTooltip()
    progress_ring_content = TabContentProgressRing()
    progress_bar_content = TabContentProgressBar()
    divider_content = TabContentDivider()
    vertical_divider_content = TabContentVerticalDivider()
    circle_avatar_content = TabContentCircleAvatar()
    border_radius_content = TabContentBorderRadius()
    padding_content = TabContentPadding()
    icons_browser_content = TabContentIconsBrowser()
    colors1_content = TabContentColors1()
    colors2_content = TabContentColors2(page)
    alignment_content = TabContentAlignment()
    shape_content = TabContentShape()
    shadow_content = TabContentShadow()
    blur_content = TabContentBlur()
    border_content = TabContentBorder()
    linear_gradient_content = TabContentLinearGradient()
    radial_gradient_content = TabContentRadialGradient()
    sweep_gradient_content = TabContentSweepGradient()
    shader_mask_content = TabContentShaderMask()

    page.add(
        ft.Tabs(
            expand=True,
            selected_index=0,
            tabs=[
                ft.Tab(
                    text="Icon",
                    content=icon_content
                ),
                ft.Tab(
                    text="Tooltip",
                    content=tooltip_content
                ),
                ft.Tab(
                    text="ProgressRing",
                    content=progress_ring_content
                ),
                ft.Tab(
                    text="ProgressBar",
                    content=progress_bar_content
                ),
                ft.Tab(
                    text="Divider",
                    content=divider_content
                ),
                ft.Tab(
                    text="VerticalDivider",
                    content=vertical_divider_content
                ),
                ft.Tab(
                    text="CircleAvatar",
                    content=circle_avatar_content
                ),
                ft.Tab(
                    text="Shadow",
                    content=shadow_content
                ),
                ft.Tab(
                    text="Blur",
                    content=blur_content
                ),
                ft.Tab(
                    text="BorderRadius",
                    content=border_radius_content
                ),
                ft.Tab(
                    text="Padding",
                    content=padding_content
                ),
                ft.Tab(
                    text="Icons Browser",
                    content=icons_browser_content
                ),
                ft.Tab(
                    text="Colors V1",
                    content=colors1_content
                ),
                ft.Tab(
                    text="Colors V2",
                    content=colors2_content
                ),
                ft.Tab(
                    text="Alignment",
                    content=alignment_content
                ),
                ft.Tab(
                    text="Shape",
                    content=shape_content
                ),
                ft.Tab(
                    text="Border",
                    content=border_content
                ),
                ft.Tab(
                    text="Linear Gradient",
                    content=linear_gradient_content
                ),
                ft.Tab(
                    text="Radial Gradient",
                    content=radial_gradient_content
                ),
                ft.Tab(
                    text="Sweep Gradient",
                    content=sweep_gradient_content
                ),
                ft.Tab(
                    text="Shader Mask",
                    content=shader_mask_content
                ),
            ]
        ),
        ft.Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style=ft.TextThemeStyle.LABEL_SMALL,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color=ft.colors.BLUE_900,
        )
    )


ft.app(
    target=main,
    route_url_strategy="path",
    assets_dir="assets",
    view=ft.WEB_BROWSER
)
