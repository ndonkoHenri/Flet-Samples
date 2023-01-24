import flet as ft
import utils


# todo: output as pdf | add error dialog to handle errors

def main(page: ft.Page):
    """
    App's entry point.

    :param page: The page object
    :type page: Page
    """
    page.title = "Markdown Editor"
    # page.window_always_on_top = True
    page.theme_mode = "dark"

    # set the minimum width and height of the window.
    page.window_min_width = 478
    page.window_min_height = 389

    # set the width and height of the window.
    page.window_width = 620
    page.window_height = 720

    # set the splash (a progress bar)
    page.splash = ft.ProgressBar(visible=False, color="yellow")

    page.file_picker = ft.FilePicker(on_result=utils.file_picker_result_import, on_upload=utils.on_upload_progress)
    # hide dialog in a overlay
    page.overlay.append(page.file_picker)

    # a dialog to be shown when saving/exporting (on web only)
    web_export_dialog = ft.AlertDialog(
        title=ft.Text("Save as..."),
        content=ft.Text("Choose a format for your file.\nTip: Press CANCEL to abort."),
        modal=True,
        actions_alignment=ft.MainAxisAlignment.CENTER,
        actions=[
            ft.ElevatedButton(".md", on_click=lambda e: get_file_format(".md")),  # .md = Markdown file format
            ft.ElevatedButton(".txt", on_click=lambda e: get_file_format(".txt")),  # .txt = ft.Text file format
            ft.ElevatedButton(".html", on_click=lambda e: get_file_format(".html")),  # .html = HTML file format
            # ft.TextButton(".pdf", on_click=lambda e: get_file_format(".pdf")),
            ft.TextButton("CANCEL", on_click=lambda e: get_file_format(None)),
        ],
    )

    def on_error(e):
        # page.dialog = utils.error_dialog
        # page.dialog.open = True
        # page.update()
        page.show_snack_bar(
            ft.SnackBar(ft.Text("Humm, seems like an error suddenly occurred! Please try again."), open=True),
        )

    page.on_error = on_error

    def get_file_format(file_format: str | None):
        """
        Closes the dialog, and calls the md_save with the file format specified by the user(in the alertdialog)

        :param file_format: The file format selected in the AlertDialog.

        Note:
            file_format=None, when the CANCEL button of the AlertDialog is triggered.
        """
        page.dialog.open = False
        page.update()
        if file_format is not None:
            md_save(file_format)
        else:
            page.show_snack_bar(ft.SnackBar(ft.Text("Operation cancelled successfully!"), open=True))

    def md_update(e):
        """
        Updates the markdown(preview) when the text in the Textfield changes.

        :param e: the event that triggered the function
        """
        page.md.value = page.text_field.value
        page.update()

    def export_markdown_to_file(e):
        if page.web:
            page.dialog = web_export_dialog
            page.dialog.open = True
            page.update()
        else:
            page.file_picker.save_file(
                dialog_title="Save As...",
                file_type=ft.FilePickerFileType.CUSTOM,
                file_name="untitled.md",
                allowed_extensions=["txt", "md", 'html']
            )

    def md_save(file_format):
        """
        It takes the Text from the textarea (Left hand side section), saves it as a file in the assets' folder
        with the specified file_format, and opens the saved file in a new browser tab using a rel-path to the assets.

        :param file_format: The file format to be used when saving
        """
        try:
            file_name = "untitled"
            # to save as HTML file, we convert the Markdown to html using 'markdown2' library
            with open(f"assets/untitled{file_format}", "w") as f:  # save it in the assets folder
                if file_format == ".html":
                    import markdown2  # pip install markdown2
                    f.write(markdown2.markdown(page.text_field.value))
                else:
                    f.write(page.text_field.value)

            page.launch_url(f"/{file_name}{file_format}")  # open the file (already in the assets folder)
            page.show_snack_bar(ft.SnackBar(ft.Text(f"Success: File was saved to assets as '{file_name}'!"),
                                            open=True if not page.web else False))
        except ImportError as exc:
            print(exc)
            print("To create an HTML output, install the markdown2 python library, using `pip install markdown2!`")
        except Exception as exc:
            print(exc)
            page.show_snack_bar(ft.SnackBar(ft.Text(f"Error: {exc}!"), open=True))

    def change_theme(e):
        """
        When the button(to change theme) is clicked, the theme is changed, and the page is updated.

        :param e: The event that triggered the function
        """
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        theme_icon_button.selected = not theme_icon_button.selected
        page.update()

    # button to change theme_mode (from dark to light mode, or the reverse)
    theme_icon_button = ft.IconButton(
        icon=ft.icons.LIGHT_MODE,
        selected_icon=ft.icons.DARK_MODE,
        icon_color=ft.colors.WHITE,
        selected_icon_color=ft.colors.BLACK,
        selected=False,
        icon_size=35,
        tooltip="change theme",
        on_click=change_theme,
    )

    page.appbar = ft.AppBar(
        title=ft.Text("Markdown Editor", color=ft.colors.WHITE),
        center_title=True,
        bgcolor=ft.colors.BLUE,
        actions=[theme_icon_button],
        elevation=5,
        leading=ft.IconButton(
            icon=ft.icons.CODE,
            icon_color=ft.colors.YELLOW_ACCENT,
            on_click=lambda e: page.launch_url("https://github.com/ndonkoHenri/Flet-Samples/tree/master/Markdown%20Editor")
        )
    )

    # you can move it to a file if you wish.
    md_test_string = """# Markdown
The following provides a quick reference to the most commonly used Markdown syntax.
Gotten from https://ashki23.github.io/markdown-latex.html

## Headers

### H3

#### H4

##### H5

###### H6

*Italic* and **Bold**
~~Scratched Text~~

## Lists
- Item 1
- Item 2
    - Item 2a (2 tabs)
    - Item 2b
        - Item 2b-1 (4 tabs)
        - Item 2b-2

Link: [Github](http://www.github.com/)

Quote:
> Imagination is more important than knowledge.
>
> Albert Einstein

## Tables

1st Header|2nd Header|3rd Header
---|:---:|---: 
col 1 is|left-aligned|1
col 2 is|center-aligned|2
col 3 is|right-aligned|3
"""

    # the LHS of the editor
    page.text_field = ft.TextField(
        value=md_test_string,
        multiline=True,
        on_change=md_update,
        expand=True,
        height=page.window_height,
        keyboard_type=ft.KeyboardType.TEXT,
        border_color=ft.colors.TRANSPARENT,
        hint_text="# Heading\n\n- Use bulleted lists\n- To better clarify\n- Your points",
    )
    # the RHS of the editor
    page.md = ft.Markdown(
        value=md_test_string,
        selectable=True,
        extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
        on_tap_link=lambda e: page.launch_url(e.data),
    )

    page.add(
        ft.Row(
            [
                ft.Text("Markdown", style=ft.TextThemeStyle.TITLE_LARGE),
                ft.FilledButton(
                    "Import",
                    on_click=lambda _: page.file_picker.pick_files(
                        dialog_title="Import File...",
                        file_type=ft.FilePickerFileType.CUSTOM,
                        allow_multiple=False,
                        allowed_extensions=["txt", "md", 'html']
                    ),
                    tooltip="load a file",
                    icon=ft.icons.UPLOAD_FILE_ROUNDED
                ),
                ft.FilledButton(
                    "Export",
                    on_click=export_markdown_to_file,
                    tooltip="save as ft.Text file",
                    icon=ft.icons.SIM_CARD_DOWNLOAD_ROUNDED
                ),
                ft.Text("Preview", style=ft.TextThemeStyle.TITLE_LARGE)
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND
        ),
        ft.Divider(thickness=1, color=ft.colors.RED_ACCENT_700),
        ft.Row(
            [
                page.text_field,
                ft.VerticalDivider(color=ft.colors.RED_ACCENT_700),
                ft.Container(
                    ft.Column(
                        [
                            page.md
                        ],
                        scroll=ft.ScrollMode.HIDDEN
                    ),
                    expand=True,
                    alignment=ft.alignment.top_left,
                    padding=ft.padding.Padding(0, 12, 0, 0),
                )
            ],
            expand=True,
        ),
        ft.Text(
            "Made with ❤ by @ndonkoHenri aka TheEthicalBoy!",
            style=ft.TextThemeStyle.LABEL_SMALL,
            weight=ft.FontWeight.BOLD,
            italic=True,
            color=ft.colors.BLUE_900,
        )
    )


# (running the app)
if __name__ == "__main__":
    ft.app(target=main, assets_dir="assets", upload_dir='assets/uploads')
