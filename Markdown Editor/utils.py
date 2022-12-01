import flet as ft

file_path = None
error_code = None


# dialog
def close_dialog(e):
    """Closes the Alert Dialog."""
    e.page.dialog.open = False
    e.page.update()


# dialog
def open_dialog(e):
    """Opens the Alert Dialog."""
    e.page.dialog.open = True
    e.page.update()


# progress bar / page.splash
def show_progress(e):
    """makes the progress bar visible, indicating we are loading up some stuffs"""
    e.page.splash.visible = True
    e.page.update()


# progress bar / page.splash
def unshow_progress(e):
    e.page.splash.visible = False
    e.page.update()


# import
def file_picker_result_import(e: ft.FilePickerResultEvent):
    # Note: e.path is None when using pick_files or when FilePicker is closed by user
    global file_path

    # IMPORT / FILE LOAD (WEB and DESKTOP)
    if e.files is not None and e.path is None:
        if not e.page.web:
            file_path = e.files[0].path
            e.page.dialog = import_dialog
        else:
            e.page.dialog = upload_dialog
        open_dialog(e)

    # SAVE / FILE EXPORT (DESKTOP only)
    if e.path is not None:  # e.path has a value only when using save_files or get_directory_path
        with open(e.path if e.path.split('\\')[-1].split(".")[-1] in ["html", "md", 'txt'] else f'{e.path}.md', 'wt') as f:
            if e.path.split('\\')[-1].split(".")[-1] == 'html':
                import markdown2  # pip install markdown2
                f.write(markdown2.markdown(e.page.text_field.value))
            else:
                f.write(e.page.text_field.value)

        e.page.show_snack_bar(
            ft.SnackBar(ft.Text("File saved successfully!"), open=True),
        )


# web upload
def on_upload_progress(e: ft.FilePickerUploadEvent):
    if e.error:
        e.page.show_snack_bar(
            ft.SnackBar(ft.Text("Sorry, but an error occurred! Try again."), open=True),
        )
        return
    show_progress(e)

    if e.progress == 1:
        overwrite_textfield_and_md(e.page, e.page.file_picker.result.files[0].name)
        unshow_progress(e)


# web upload
def upload_file(e):
    if e.page.file_picker.result is not None and e.page.file_picker.result.files is not None:
        file_name = e.page.file_picker.result.files[0].name

        e.page.file_picker.upload(
            [
                ft.FilePickerUploadFile(
                    file_name,
                    upload_url=e.page.get_upload_url(file_name, 600),
                )
            ]
        )

        close_dialog(e)
        show_progress(e)


# textfield and markdown
def overwrite_textfield_and_md(page, file_name_or_path, is_web=True):
    """updates the content of the LHS and RHS"""

    global file_path

    file_path = f'assets/uploads/{file_name_or_path}' if is_web else file_name_or_path
    try:
        with open(file_path, 'rt') as f:
            text = f.read()
    except Exception as exc:
        # page.dialog = error_dialog
        # page.dialog.open = True
        # page.update()
        print(exc)
        page.show_snack_bar(
            ft.SnackBar(ft.Text(f"Humm, seems like an error suddenly occurred! Please try again."), open=True),
        )
        return

    page.text_field.value = text    # update the content of the Textfield (LHS)
    page.md.value = text            # update the content of the Markdown (RHS)
    page.update()

    page.dialog.open = False
    page.show_snack_bar(
        ft.SnackBar(ft.Text(f"File uploaded successfully!"), open=True),
    )


# a dialog to be shown when uploading a file (on WEB only)
upload_dialog = ft.AlertDialog(
    title=ft.Text("Confirm file upload"),
    content=ft.Column(
        [
            ft.Text("Do you really want me to upload this file?\n"
                    "Remember, the content of the input box will be deleted!\n"
                    "Tip: Press CANCEL to abort."),
        ]
    ),
    modal=True,
    actions_alignment="center",
    actions=[
        ft.ElevatedButton("UPLOAD", on_click=upload_file),
        ft.TextButton("CANCEL", on_click=close_dialog),
    ],
)

# a dialog to be shown when importing a file on DESKTOP only
import_dialog = ft.AlertDialog(
    title=ft.Text("Confirm file import"),
    content=ft.Text("Do you really want me to import this file?\n"
                    "Remember, the current Markdown will be deleted/overwritten!\n"
                    "Tip: Press CANCEL to abort."),
    modal=True,
    actions_alignment="center",
    actions=[
        ft.ElevatedButton("IMPORT", on_click=lambda e: overwrite_textfield_and_md(e.page, file_path, is_web=False)),
        ft.TextButton("CANCEL", on_click=close_dialog),
    ],
)

# a dialog to be shown when there is an error
error_dialog = ft.AlertDialog(
    title=ft.Text("An Error occurred!"),
    content=ft.Text("Please try again, and if it persists, report on GitHub.\n"
                    "I will take an immediate look at it!"),
    modal=True,
    actions_alignment="end",
    actions=[
        ft.ElevatedButton("REPORT", on_click=lambda e: e.page.launch_url("https://github.com/ndonkoHenri/Flet-Samples/issues")),
        ft.TextButton("CANCEL", on_click=close_dialog),
    ],
)
