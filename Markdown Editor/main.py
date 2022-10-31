import flet
from flet import (colors, icons, Text, IconButton, AppBar, Page, Row, Theme, padding, SnackBar, Divider, Ref,
                  VerticalDivider, alignment, Container, Markdown, TextField, Column, TextStyle, AlertDialog,
                  TextButton, ElevatedButton, FilledButton)


def main(page: Page):
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

    # a dialog to be shown when saving the file (on web only)
    page.dialog = AlertDialog(
        title=Text("Save as..."),
        content=Text("Choose a format for your file.\nTip: Press CANCEL to abort."),
        modal=True,
        actions_alignment="center",
        actions=[
            ElevatedButton(".md", on_click=lambda e: get_file_format(".md")),   # .md = Markdown file format
            ElevatedButton(".txt", on_click=lambda e: get_file_format(".txt")),   # .txt = Text file format
            ElevatedButton(".html", on_click=lambda e: get_file_format(".html")),     # .html = HTML file format
            # TextButton(".pdf", on_click=lambda e: get_file_format(".pdf")),
            TextButton("CANCEL", on_click=lambda e: get_file_format(None)),
        ],
    )

    def close_dialog():
        """Closes the Alert Dialog."""
        page.dialog.open = False
        page.update()

    def open_dialog():
        """Opens the Alert Dialog."""
        page.dialog.open = True
        page.update()

    def get_file_format(file_format: str | None):
        """
        Closes the dialog, and calls the md_save with the file format specified by the user(in the alertdialog)

        :param file_format: The file format selected in the AlertDialog.

        Note:
            file_format=None, when the CANCEL button of the AlertDialog is triggered.
        """
        close_dialog()
        if file_format is not None:
            md_save(file_format)
        else:
            page.show_snack_bar(SnackBar(Text("Operation cancelled successfully!"), open=True))

    def md_update(e):
        """
        Updates the markdown(preview) when the text in the textfield changes.

        :param e: the event that triggered the function
        """
        md.value = md_field.value
        page.update()

    def md_save(file_format):
        """
        It takes the text from the textarea, saves it as a file in the assets' folder with the specified file_format,
        and opens the saved file in a new browser tab.

        :param file_format: The file format to be used when saving
        """
        try:
            file_name = "untitled"

            # to save as HTML file, we convert the Markdown to html using 'markdown2' library
            with open(f"assets/{file_name}{file_format}", "w") as f:
                if file_format == ".html":
                    import markdown2    # pip install markdown2
                    f.write(markdown2.markdown(md_field.value))
                else:
                    f.write(md_field.value)

            page.show_snack_bar(SnackBar(Text(f"Success: File was saved to assets as '{file_name}'!"), open=True if not page.web else False))
            page.launch_url(f"/{file_name}{file_format}")
        except ImportError as exc:
            print(exc)
            print("To create an HTML output, install the markdown2 python library, using `pip install markdown2!`")
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

    # a markdown example with basic syntax gotten from https://github.com/mxstbr/markdown-test-file/blob/master/TEST.md
    # you can move it to a file if you wish.
    md_test_str = """
# Markdown: Syntax

----

## Overview

### Philosophy

Markdown is intended to be as easy-to-read and easy-to-write as is feasible.

Readability, however, is emphasized above all else. A Markdown-formatted
document should be publishable as-is, as plain text, without looking
like it's been marked up with tags or formatting instructions. While
Markdown's syntax has been influenced by several existing text-to-HTML
filters -- including [Setext](http://docutils.sourceforge.net/mirror/setext.html), [atx](http://www.aaronsw.com/2002/atx/), [Textile](http://textism.com/tools/textile/), [reStructuredText](http://docutils.sourceforge.net/rst.html),
[Grutatext](http://www.triptico.com/software/grutatxt.html), and [EtText](http://ettext.taint.org/doc/) -- the single biggest source of
inspiration for Markdown's syntax is the format of plain text email.

## Block Elements

### Paragraphs and Line Breaks

A paragraph is simply one or more consecutive lines of text, separated
by one or more blank lines. (A blank line is any line that looks like a
blank line -- a line containing nothing but spaces or tabs is considered
blank.) Normal paragraphs should not be indented with spaces or tabs.

The implication of the "one or more consecutive lines of text" rule is
that Markdown supports "hard-wrapped" text paragraphs. This differs
significantly from most other text-to-HTML formatters (including Movable
Type's "Convert Line Breaks" option) which translate every line break
character in a paragraph into a `<br />` tag.

When you *do* want to insert a `<br />` break tag using Markdown, you
end a line with two or more spaces, then type return.

### Headers

Markdown supports two styles of headers, [Setext] [1] and [atx] [2].

Optionally, you may "close" atx-style headers. This is purely
cosmetic -- you can use this if you think it looks better. The
closing hashes don't even need to match the number of hashes
used to open the header. (The number of opening hashes
determines the header level.)


### Blockquotes

Markdown uses email-style `>` characters for blockquoting. If you're
familiar with quoting passages of text in an email message, then you
know how to create a blockquote in Markdown. It looks best if you hard
wrap the text and put a `>` before every line:

> This is a blockquote with two paragraphs. Lorem ipsum dolor sit amet,
> consectetuer adipiscing elit. Aliquam hendrerit mi posuere lectus.
> Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.
> 
> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
> id sem consectetuer libero luctus adipiscing.

Markdown allows you to be lazy and only put the `>` before the first
line of a hard-wrapped paragraph:

> This is a blockquote. Aliquam hendrerit mi posuere lectus.
Vestibulum enim wisi, viverra nec, fringilla in, laoreet vitae, risus.

> Donec sit amet nisl. Aliquam semper ipsum sit amet velit. Suspendisse
id sem consectetuer libero luctus adipiscing.

Blockquotes can be nested (i.e. a blockquote-in-a-blockquote) by
adding additional levels of `>`:

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

Blockquotes can contain other Markdown elements, including headers, lists,
and code blocks:

> ## This is a header.
> 
> 1.   This is the first list item.
> 2.   This is the second list item.
> 
> Here's some example code:
> 
>     return shell_exec("echo $input | $markdown_script");

Any decent text editor should make email-style quoting easy. For
example, with BBEdit, you can make a selection and choose Increase
Quote Level from the Text menu.


### Lists

Markdown supports ordered (numbered) and unordered (bulleted) lists.

Unordered lists use asterisks, pluses, and hyphens -- interchangably
-- as list markers:

*   Red
*   Green
*   Blue

is equivalent to:

+   Red
+   Green
+   Blue

and:

-   Red
-   Green
-   Blue

Ordered lists use numbers followed by periods:

1.  Bird
2.  McHale
3.  Parish

It's important to note that the actual numbers you use to mark the
list have no effect on the HTML output Markdown produces. The HTML
Markdown produces from the above list is:

If you instead wrote the list in Markdown like this:

1.  Bird
1.  McHale
1.  Parish

or even:

3. Bird
1. McHale
8. Parish

you'd get the exact same HTML output. The point is, if you want to,
you can use ordinal numbers in your ordered Markdown lists, so that
the numbers in your source match the numbers in your published HTML.
But if you want to be lazy, you don't have to.

To make lists look nice, you can wrap items with hanging indents:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
    Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
    viverra, risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
    Suspendisse libero luctus adipiscing.

But if you want to be lazy, you don't have to:

*   Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
Aliquam hendrerit mi posuere lectus. Vestibulum enim wisi,
viverra risus.
*   Donec sit amet nisl. Aliquam semper ipsum sit amet velit.
Suspendisse luctus adipiscing.

List items may consist of multiple paragraphs. Each subsequent
paragraph in a list item must be indented by either 4 spaces
or one tab:

1.  This is a list item with two paragraphs. Lorem ipsum dolor
    sit amet, elit. Aliquam hendrerit
    mi posuere lectus.

    Vestibulum enim wisi, viverra nec, fringilla in, laoreet
    vitae, risus. Donec sit amet nisl. Aliquam semper ipsum
    sit amet velit.

2.  Suspendisse id sem consectetuer libero luctus adipiscing.

It looks nice if you indent every line of the subsequent
paragraphs, but here again, Markdown will allow you to be
lazy:

*   This is a list item with two paragraphs.

    This is the second paragraph in the list item. You're
only required to indent the first line. Lorem ipsum dolor
sit amet, consectetuer adipiscing elit.

*   Another item in the same list.

To put a blockquote within a list item, the blockquote's `>`
delimiters need to be indented:

*   A list item with a blockquote:

    > This is a blockquote
    > inside a list item.

To put a code block within a list item, the code block needs
to be indented *twice* -- 8 spaces or two tabs:

*   A list item with a code block:

        <code goes here>

### Code Blocks

Pre-formatted code blocks are used for writing about programming or
markup source code. Rather than forming normal paragraphs, the lines
of a code block are interpreted literally. Markdown wraps a code block
in both `<pre>` and `<code>` tags.

To produce a code block in Markdown, simply indent every line of the
block by at least 4 spaces or 1 tab.

This is a normal paragraph:

    This is a code block.

Here is an example of AppleScript:

    tell application "Foo"
        beep
    end tell

A code block continues until it reaches a line that is not indented
(or the end of the article).

Within a code block, ampersands (`&`) and angle brackets (`<` and `>`)
are automatically converted into HTML entities. This makes it very
easy to include example HTML source code using Markdown -- just paste
it and indent it, and Markdown will handle the hassle of encoding the
ampersands and angle brackets. For example, this:

    <div class="footer">
        &copy; 2004 Foo Corporation
    </div>

Regular Markdown syntax is not processed within code blocks. E.g.,
asterisks are just literal asterisks within a code block. This means
it's also easy to use Markdown to write about Markdown's own syntax.

```
tell application "Foo"
    beep
end tell
```

## Span Elements

### Links

Markdown supports two style of links: *inline* and *reference*.

In both styles, the link text is delimited by [square brackets].

To create an inline link, use a set of regular parentheses immediately
after the link text's closing square bracket. Inside the parentheses,
put the URL where you want the link to point, along with an *optional*
title for the link, surrounded in quotes. For example:

This is [an example](http://example.com/) inline link.

[This link](http://example.net/) has no title attribute.

### Emphasis

Markdown treats asterisks (`*`) and underscores (`_`) as indicators of
emphasis. Text wrapped with one `*` or `_` will be wrapped with an
HTML `<em>` tag; double `*`'s or `_`'s will be wrapped with an HTML
`<strong>` tag. E.g., this input:

*single asterisks*

_single underscores_

**double asterisks**

__double underscores__

### Code

To indicate a span of code, wrap it with backtick quotes (`` ` ``).
Unlike a pre-formatted code block, a code span indicates code within a
normal paragraph. For example:

Use the `printf()` function.
"""

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

    page.add(
        Row(
            [
                Text("Markdown", style='titleLarge'),
                FilledButton(
                    "SAVE",
                    on_click=lambda e: open_dialog(),
                    tooltip="download file",
                    icon=icons.DOWNLOAD_SHARP
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
    flet.app(target=main, assets_dir="assets", view=flet.WEB_BROWSER)
