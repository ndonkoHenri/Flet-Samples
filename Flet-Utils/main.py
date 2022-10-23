import time

import flet
from flet import icons, colors, Page, ProgressBar, IconButton, ButtonStyle, AppBar, Text, Tab, Tabs
from utils.padding_utils import TabContentPadding
from utils.alignment_utils import TabContentAlignment
from utils.border_utils import TabContentBorder
from utils.border_radius_utils import TabContentBorderRadius
from utils.colors_utils import TabContentColors1, TabContentColors2
from utils.icons_utils import TabContentIcons
from utils.gradient_utils import TabContentLinearGradient, TabContentSweepGradient, TabContentRadialGradient
from utils.shadermask_utils import TabContentShaderMask
from utils.shape_utils import TabContentShape


def main(page: Page):
    page.title = "Flet Utilities"
    page.theme_mode = "light"  # by default, page.theme_mode=None
    # page.window_always_on_top = True
    page.splash = ProgressBar(visible=False)
    page.vertical_alignment = "start"
    # set the width and height of the window.
    page.window_width = 572
    page.window_height = 720

    # page.horizontal_alignment = "center"

    def change_theme(e):
        """
        Changes the app's theme_mode, from dark to light or light to dark. A splash(progress bar) is also shown.

        :param e: The event that triggered the function
        :type e: ControlEvent
        """
        page.splash.visible = True
        page.update()
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"  # changes the page's theme_mode
        page.splash.visible = False
        theme_icon_button.selected = not theme_icon_button.selected  # changes the icon
        time.sleep(0.2)  # shows the progress bar for a second indicating that work is being done..
        page.update()

    theme_icon_button = IconButton(
        icons.DARK_MODE,
        selected=False,
        selected_icon=icons.LIGHT_MODE,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
        style=ButtonStyle(color={"": colors.BLACK, "selected": colors.WHITE}, ),
    )

    page.appbar = AppBar(
        title=Text(
            "Flet Utilities",
            color="white"
        ),
        center_title=True,
        bgcolor="blue",
        actions=[theme_icon_button],
    )

    border_radius_content = TabContentBorderRadius()
    padding_content = TabContentPadding()
    icons_content = TabContentIcons()
    colors1_content = TabContentColors1()
    colors2_content = TabContentColors2(page)
    alignment_content = TabContentAlignment()
    shape_content = TabContentShape()
    border_content = TabContentBorder()
    linear_gradient_content = TabContentLinearGradient()
    radial_gradient_content = TabContentRadialGradient()
    sweep_gradient_content = TabContentSweepGradient()
    shader_mask_content = TabContentShaderMask()

    page.add(
        Tabs(
            expand=True,
            selected_index=11,
            tabs=[
                Tab(
                    text="BorderRadius",
                    content=border_radius_content
                ),
                Tab(
                    text="Padding",
                    content=padding_content
                ),
                Tab(
                    text="Icons",
                    content=icons_content
                ),
                Tab(
                    text="Colors V1",
                    content=colors1_content
                ),
                Tab(
                    text="Colors V2",
                    content=colors2_content
                ),
                Tab(
                    text="Alignment",
                    content=alignment_content
                ),
                Tab(
                    text="Shape",
                    content=shape_content
                ),
                Tab(
                    text="Border",
                    content=border_content
                ),
                Tab(
                    text="Linear Gradient",
                    content=linear_gradient_content
                ),
                Tab(
                    text="Radial Gradient",
                    content=radial_gradient_content
                ),
                Tab(
                    text="Sweep Gradient",
                    content=sweep_gradient_content
                ),
                Tab(
                    text="Shader Mask",
                    content=shader_mask_content
                ),
            ]
        ),
        Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style="labelSmall",
            weight="bold",
            italic=True,
            color=colors.BLUE_900,
        )
    )


flet.app(target=main)
