from flet import (colors, icons, UserControl, SnackBar, Text, Row,
                  FilledButton, TextField, Column,
                  Ref, FilledTonalButton, LinearGradient, RadialGradient, SweepGradient, dropdown, Dropdown, ShaderMask,
                  Image, alignment, Alignment, border_radius)
from flet.border_radius import BorderRadius
from flet.control_event import ControlEvent


# the content of the ShaderMask tab
class TabContentShaderMask(UserControl):
    def __init__(self):
        super().__init__()
        self.border_radius = 10
        self.shader = LinearGradient(
            begin=alignment.top_center,
            end=alignment.bottom_center,
            colors=[colors.BLACK, colors.TRANSPARENT],
            stops=[0.5, 1.0],
        )
        self.blend_mode = "dstIn"
        self.content = Image(src="https://picsum.photos/100/200?2")

    def build(self):
        def update_mask(e: ControlEvent):
            """
            It updates the gradient of the container object.

            :param e: The event object
            """
            content = field_content.value.strip() if field_content.value.strip() else None
            b_radius = field_border_radius.value.strip() if field_border_radius.value.strip() else None
            shader = field_shader.value.strip() if field_shader.value.strip() else None
            blend_mode = bm_dropdown.value

            # border radius
            try:
                b_radius = eval(b_radius)
                if not isinstance(b_radius, BorderRadius) and not isinstance(b_radius, tuple):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, right, "
                            "bottom). This could be gotten from "
                            "the BorderRadius Tab here."),
                            open=True))
                    return
                elif isinstance(b_radius, tuple) and len(b_radius) == 4:
                    b_radius = eval(
                        f"BorderRadius({b_radius[0]}, {b_radius[1]},{b_radius[2]}, {b_radius[3]})")
            except Exception as x:
                print(f"BorderRadius Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, right, "
                            "bottom). Please check your input."),
                        open=True))
                return

            # shader
            try:
                shader = eval(shader)
                if not isinstance(shader, (LinearGradient, RadialGradient, SweepGradient)):
                    e.page.show_snack_bar(
                        SnackBar(Text(
                            "ERROR: `gradient` must be a Gradient(LinearGradient,RadialGradient,SweepGradient) "
                            "object. This could be gotten from "
                            "the Gradient Tabs here."),
                            open=True))
                    return
            except Exception as x:
                print(f"Shader Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: `gradient` must be a Gradient(LinearGradient,RadialGradient,SweepGradient) "
                            "object. Please check your input."),
                        open=True))
                return

            # content
            try:
                content = eval(content)
                self.content = shader_mask_obj.current.content = content
            except Exception as x:
                print(f"Content Error: {x}")
                e.page.show_snack_bar(
                    SnackBar(
                        Text(
                            "ERROR: `content` must be a valid Control object. Please check your input."),
                        open=True))
                return

            self.blend_mode = shader_mask_obj.current.blend_mode = blend_mode
            self.border_radius = shader_mask_obj.current.border_radius = b_radius
            self.shader = shader_mask_obj.current.shader = shader
            self.update()
            e.page.show_snack_bar(SnackBar(Text("Updated ShaderMask!"), open=True))

        def copy_to_clipboard(e: ControlEvent):
            """
            It copies the gradient of the container to the clipboard.

            :param e: The event object
            """
            e.page.set_clipboard(
                f"ShaderMask(content={field_content.value.strip()}, blend_mode={self.blend_mode}, shader={self.shader}, border_radius={self.border_radius})")
            e.page.show_snack_bar(SnackBar(Text(
                f"Copied: ShaderMask(content={field_content.value.strip()}, blend_mode={self.blend_mode}, shader={self.shader}, border_radius={self.border_radius})"),
                open=True))

        shader_mask_obj = Ref[ShaderMask]()

        # dropdown values for the blend_mode parameter
        bm_dropdown = Dropdown(
            options=[
                dropdown.Option("modulate"),
                dropdown.Option("clear"),
                dropdown.Option("color"),
                dropdown.Option("colorBurn"),
                dropdown.Option("colorDodge"),
                dropdown.Option("darken"),
                dropdown.Option("difference"),
                dropdown.Option("dst"),
                dropdown.Option("dstATop"),
                dropdown.Option("dstIn"),
                dropdown.Option("dstOut"),
                dropdown.Option("dstOver"),
                dropdown.Option("exclusion"),
                dropdown.Option("hardLight"),
                dropdown.Option("hue"),
                dropdown.Option("lighten"),
                dropdown.Option("luminosity"),
                dropdown.Option("multiply"),
                dropdown.Option("overlay"),
                dropdown.Option("plus"),
                dropdown.Option("saturation"),
                dropdown.Option("screen"),
                dropdown.Option("softLight"),
                dropdown.Option("src"),
                dropdown.Option("srcATop"),
                dropdown.Option("srcIn"),
                dropdown.Option("srcOut"),
                dropdown.Option("srcOver"),
                dropdown.Option("values"),
                dropdown.Option("xor"),
            ],
            value="modulate",
            on_change=update_mask,
            width=150,
            helper_text="blend mode",
        )

        # text field for gradient property of the ShaderMask object
        field_shader = TextField(
            label="shader",
            value="LinearGradient(begin=alignment.top_center, end=alignment.bottom_center, colors=[colors.BLACK,"
                  "colors.TRANSPARENT], stops=[0.5, 1.0])",
            on_submit=update_mask,
            keyboard_type="text",
            on_blur=update_mask,
            hint_text="LinearGradient(.....)",
            helper_text="Linear/Radial/Sweep Gradient object"
        )

        # text field for the border radius property of the ShaderMask object
        field_border_radius = TextField(
            label="border radius",
            value="border.all(10)",
            on_submit=update_mask,
            on_blur=update_mask,
            keyboard_type="text",
            hint_text="5,10,2,3",
            helper_text="BorderRadius object or (left, top, right, bottom)"
        )

        # text field for content property of the ShaderMask object
        field_content = TextField(
            label="content",
            value="Image(src='https://picsum.photos/100/200?2')",
            on_submit=update_mask,
            on_blur=update_mask,
            keyboard_type="text",
            helper_text="A control for the content",
            hint_text="Image(src='https://picsum.photos/100/200?2')",
        )

        return Column(
            [
                field_content,
                field_shader,
                Row(
                    [field_border_radius, bm_dropdown],
                    alignment="center"
                ),
                Row(
                    [
                        ShaderMask(
                            Image(src="https://picsum.photos/100/200?2"),
                            blend_mode="dstIn",
                            shader=LinearGradient(
                                begin=alignment.top_center,
                                end=alignment.bottom_center,
                                colors=[colors.BLACK, colors.TRANSPARENT],
                                stops=[0.5, 1.0],
                            ),
                            border_radius=10,
                            ref=shader_mask_obj
                        )
                    ],
                    alignment="center"),
                Row(
                    [
                        FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=copy_to_clipboard,
                        ),
                        FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/shadermask")
                        )
                    ],
                    alignment="center",
                ),
            ],
            alignment="center",
            scroll="hidden",
        )
