# import all the controls: if the shader mask requires controls which are not imported, an error is raised
from flet import *
import flet as ft


# the content of the ShaderMask tab
class TabContentShaderMask(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.shader_mask_obj = ft.Ref[ft.ShaderMask]()

        # dropdown values for the blend_mode parameter
        self.bm_dropdown = ft.Dropdown(
            options=[
                ft.dropdown.Option("modulate"),
                ft.dropdown.Option("clear"),
                ft.dropdown.Option("color"),
                ft.dropdown.Option("colorBurn"),
                ft.dropdown.Option("colorDodge"),
                ft.dropdown.Option("darken"),
                ft.dropdown.Option("difference"),
                ft.dropdown.Option("dst"),
                ft.dropdown.Option("dstATop"),
                ft.dropdown.Option("dstIn"),
                ft.dropdown.Option("dstOut"),
                ft.dropdown.Option("dstOver"),
                ft.dropdown.Option("exclusion"),
                ft.dropdown.Option("hardLight"),
                ft.dropdown.Option("hue"),
                ft.dropdown.Option("lighten"),
                ft.dropdown.Option("luminosity"),
                ft.dropdown.Option("multiply"),
                ft.dropdown.Option("overlay"),
                ft.dropdown.Option("plus"),
                ft.dropdown.Option("saturation"),
                ft.dropdown.Option("screen"),
                ft.dropdown.Option("softLight"),
                ft.dropdown.Option("src"),
                ft.dropdown.Option("srcATop"),
                ft.dropdown.Option("srcIn"),
                ft.dropdown.Option("srcOut"),
                ft.dropdown.Option("srcOver"),
                ft.dropdown.Option("values"),
                ft.dropdown.Option("xor"),
            ],
            value="modulate",
            on_change=self.update_mask,
            width=150,
            helper_text="blend mode",
        )

        # text field for gradient property of the ShaderMask object
        self.field_shader = ft.TextField(
            label="shader",
            value="LinearGradient(begin=alignment.top_center, end=alignment.bottom_center, colors=[colors.BLUE_100,"
                  "colors.TRANSPARENT], stops=[0.5, 1.0])",
            on_submit=self.update_mask,
            keyboard_type=ft.KeyboardType.TEXT,
            on_blur=self.update_mask,
            hint_text="LinearGradient(.....)",
            helper_text="Linear/Radial/Sweep Gradient object"
        )

        # text field for the border radius property of the ShaderMask object
        self.field_border_radius = ft.TextField(
            label="border radius",
            value="border_radius.all(10)",
            on_submit=self.update_mask,
            on_blur=self.update_mask,
            keyboard_type=ft.KeyboardType.TEXT,
            hint_text="5,10,2,3",
            helper_text="BorderRadius object or (left, top, right, bottom)"
        )

        # text field for content property of the ShaderMask object
        self.field_content = ft.TextField(
            label="content",
            value="Image(src='https://picsum.photos/100/200?2')",
            on_submit=self.update_mask,
            on_blur=self.update_mask,
            keyboard_type=ft.KeyboardType.TEXT,
            helper_text="A control for the content",
            hint_text="Image(src='https://picsum.photos/100/200?2')",
        )

        self.border_radius = 10

        self.shader = ft.LinearGradient(
            begin=ft.alignment.top_center,
            end=ft.alignment.bottom_center,
            colors=[colors.BLACK, colors.TRANSPARENT],
            stops=[0.5, 1.0],
        )
        self.blend_mode = "dstIn"
        self.content = ft.Image(src="https://picsum.photos/100/200?2")

    def update_mask(self, e: ft.ControlEvent):
        """
        It updates the gradient of the container object.

        :param e: The event object
        """
        content = self.field_content.value.strip() if self.field_content.value.strip() else None
        b_radius = self.field_border_radius.value.strip() if self.field_border_radius.value.strip() else None
        shader = self.field_shader.value.strip() if self.field_shader.value.strip() else None
        blend_mode = self.bm_dropdown.value

        # border radius
        try:
            b_radius = eval(b_radius)
        except Exception as x:
            print(f"BorderRadius Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, right, "
                        "bottom). Please check your input."),
                    open=True)
            )
            return
        else:
            if not isinstance(b_radius, ft.BorderRadius) and \
                    not isinstance(b_radius, tuple):
                e.page.show_snack_bar(
                    ft.SnackBar(
                        ft.Text(
                            "ERROR: `border_radius` must be an BorderRadius object or in the form (left, top, "
                            "right, bottom). This could be gotten from the BorderRadius Tab here."
                        ),
                        open=True
                    )
                )
                return
            elif isinstance(b_radius, tuple) and len(b_radius) == 4:
                b_radius = eval(
                    f"BorderRadius({b_radius[0]}, {b_radius[1]},{b_radius[2]}, {b_radius[3]})")

        # shader
        try:
            shader = eval(shader)
            if shader is not None and not isinstance(shader, (ft.LinearGradient, ft.RadialGradient, ft.SweepGradient)):
                raise ValueError("Wrong Value")
        except Exception as x:
            print(f"Shader Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text("ERROR: `shader` must be a Gradient(LinearGradient,RadialGradient,SweepGradient) "
                            "object. Please check your input."),
                    open=True)
            )
            return

        # content
        try:
            content = eval(content)
            self.content = self.shader_mask_obj.current.content = content
        except Exception as x:
            print(f"Content Error: {x}")
            e.page.show_snack_bar(
                ft.SnackBar(
                    ft.Text(
                        "ERROR: `content` must be a valid Control object. Please check your input."),
                    open=True))
            return

        self.blend_mode = self.shader_mask_obj.current.blend_mode = blend_mode
        self.border_radius = self.shader_mask_obj.current.border_radius = b_radius
        self.shader = self.shader_mask_obj.current.shader = shader
        self.update()
        e.page.show_snack_bar(ft.SnackBar(ft.Text("Updated ShaderMask!"), open=True))

    def copy_to_clipboard(self, e: ft.ControlEvent):
        """
        It copies the gradient of the container to the clipboard.

        :param e: The event object
        """
        e.page.set_clipboard(
            f"ShaderMask(content={self.field_content.value.strip()}, blend_mode={self.blend_mode}, shader={self.shader}, border_radius={self.border_radius})")
        e.page.show_snack_bar(ft.SnackBar(ft.Text(
            f"Copied: ShaderMask(content={self.field_content.value.strip()}, blend_mode={self.blend_mode}, shader={self.shader}, border_radius={self.border_radius})"),
            open=True))

    def build(self):

        return ft.Column(
            [
                self.field_content,
                self.field_shader,
                ft.Row(
                    [self.field_border_radius, self.bm_dropdown],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                ft.Row(
                    [
                        ft.ShaderMask(
                            ft.Image(src="https://picsum.photos/100/200?2"),
                            blend_mode=ft.BlendMode.DST_IN,
                            shader=ft.LinearGradient(
                                begin=ft.alignment.top_center,
                                end=ft.alignment.bottom_center,
                                colors=[colors.BLACK, colors.TRANSPARENT],
                                stops=[0.5, 1.0],
                            ),
                            border_radius=10,
                            ref=self.shader_mask_obj
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER),
                ft.Row(
                    [
                        ft.FilledButton(
                            "Copy Value to Clipboard",
                            icon=icons.COPY,
                            on_click=self.copy_to_clipboard,
                        ),
                        ft.FilledTonalButton(
                            "Go to Docs",
                            icon=icons.DATASET_LINKED_OUTLINED,
                            on_click=lambda e: e.page.launch_url("https://flet.dev/docs/controls/shadermask")
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            scroll=ft.ScrollMode.HIDDEN,
        )


if __name__ == "__main__":
    def main(page: ft.Page):
        page.add(TabContentShaderMask())


    ft.app(main)
