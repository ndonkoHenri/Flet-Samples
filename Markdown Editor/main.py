import flet
from flet import (colors, icons, Text, IconButton, AppBar, Page, Row, Theme, padding, SnackBar, Divider, Ref,
                  VerticalDivider, alignment, Container, Markdown, TextField, Column, TextStyle)


def main(page: Page):
    """
    App's entry point.

    :param page: The page object
    :type page: Page
    """
    page.title = "Markdown Editor"
    # page.window_always_on_top = True
    page.theme_mode = "dark"
    # Appbar.elevation only works in material2
    page.theme = Theme(use_material3=False)
    page.dark_theme = Theme(use_material3=False, )

    # set the minimum width and height of the window.
    page.window_min_width = 478
    page.window_min_height = 389

    # set the width and height of the window.
    page.window_width = 620
    page.window_height = 720

    def md_update(e):
        """
        Updates the markdown(preview) when the text in the textfield changes.

        :param e: the event that triggered the function
        """
        md.value = md_field.value
        page.update()

    def md_save(e):
        """
        It takes the text from the textarea and saves it to a file in the assets folder

        :param e: The event that triggered the function
        """
        try:
            file_name = filename_field.current.value.strip()
            if not file_name:
                file_name = "untitled.md"
            file_name = file_name if '.' in file_name else f"{file_name}.md"
            with open(f"assets/{file_name}", "w") as f:
                f.write(md_field.value)
            page.show_snack_bar(SnackBar(Text(f"Success: File was saved to assets as '{file_name}'!"), open=True))
        except Exception as exc:
            print(exc)
            page.show_snack_bar(SnackBar(Text(f"Error: {exc}!"), open=True))

    def change_theme(e):
        """
        When the button(to change theme) is clicked, the progress bar is made visible, the theme is changed,
        the progress bar is made invisible, and the page is updated

        :param e: The event that triggered the function
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        theme_icon_button.icon = icons.DARK_MODE if theme_icon_button.icon == icons.LIGHT_MODE else icons.LIGHT_MODE
        theme_icon_button.icon_color = colors.BLACK if theme_icon_button.icon_color == colors.WHITE else colors.WHITE
        page.update()

    # button to change theme_mode (from dark to light mode, or the reverse)
    theme_icon_button = IconButton(
        icons.LIGHT_MODE,
        icon_color=colors.WHITE,
        selected=True,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
    )

    page.appbar = AppBar(
        title=Text("Markdown Editor", color=colors.WHITE),
        center_title=True,
        bgcolor=colors.BLUE,
        actions=[theme_icon_button],
        elevation=5,
    )

    md_test_str = """# Markdown Example
> Markdown allows you to easily include formatted text, images, and even formatted Dart code in your app.

## Titles

Setext-style

This is an H1
=============

This is an H2
-------------

Atx-style

# This is an H1

## This is an H2

###### This is an H6

Select the valid headers:

- [x] `# hello`
- [ ] `#hello`

## Links

[inline-style](https://www.google.com)

## Images

![Image from Flet assets](/icons/icon-192.png)

![Test image](https://picsum.photos/200/300)

## Tables

|Syntax                                 |Result                               |
|---------------------------------------|-------------------------------------|
|`*italic 1*`                           |*italic 1*                           |
|`_italic 2_`                           | _italic 2_                          |
|`**bold 1**`                           |**bold 1**                           |
|`__bold 2__`                           |__bold 2__                           |
|`This is a ~~strikethrough~~`          |This is a ~~strikethrough~~          |
|`***italic bold 1***`                  |***italic bold 1***                  |
|`___italic bold 2___`                  |___italic bold 2___                  |
|`***~~italic bold strikethrough 1~~***`|***~~italic bold strikethrough 1~~***|
|`~~***italic bold strikethrough 2***~~`|~~***italic bold strikethrough 2***~~|

## Styling

Style text as _italic_, __bold__, ~~strikethrough~~, or `inline code`.

- Use bulleted lists
- To better clarify
- Your points

## Code blocks

Formatted Dart code looks really pretty too:

```
void main() {
  runApp(MaterialApp(
    home: Scaffold(
      body: Markdown(data: markdownData),
    ),
  ));
}
```"""

    md_field = TextField(
        value=md_test_str,
        multiline=True,
        min_lines=10,
        on_change=md_update,
        expand=1,
        height=page.window_height,
        keyboard_type="text",
        border_color=colors.TRANSPARENT,
        hint_text="# Heading\n\n- Use bulleted lists\n- To better clarify\n- Your points",
        tooltip="enter your md text here"

    )
    md = Markdown(
        value=md_test_str,
        selectable=True,
        extension_set="gitHubWeb",
        on_tap_link=lambda e: page.launch_url(e.data),
    )

    filename_field = Ref[TextField]()
    page.add(
        Row(
            [
                Text("Markdown", style='titleLarge'),
                TextField(
                    filename_field,
                    value="untitled",
                    suffix=IconButton(icon=icons.DOWNLOAD, on_click=md_save, icon_size=15),
                    tooltip="your file name",
                    label="File name",
                    hint_text="untitled",
                    width=180,
                    height=60,
                    border="outline",
                    filled=True,
                    label_style=TextStyle(italic=True, color=colors.GREEN, size=17)

                ),
                Text("Preview", style='titleLarge')
            ],
            alignment="spaceAround"
        ),
        Divider(thickness=1, color=colors.RED_ACCENT_700),
        Row(
            [
                md_field,
                VerticalDivider(width=1, thickness=1, color=colors.RED_ACCENT_700),
                Container(
                    Column(
                        [
                            md
                        ],
                        scroll="hidden"
                    ),
                    expand=1,
                    alignment=alignment.top_left,
                    padding=padding.Padding(0, 12, 0, 0),
                )
            ],
            expand=True,
        ),
        Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style="labelSmall",
            weight="bold",
            italic=True,
            color=colors.BLUE_900,
        )
    )


# (running the app)
if __name__ == "__main__":
    flet.app(target=main, assets_dir="assets")
