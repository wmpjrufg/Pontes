# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "Pontes"
copyright = "2026, Wanderlei Malaquias Pereira Jr."
author = "Wanderlei Malaquias Pereira Jr."

language = "pt_BR"

extensions = [
    "myst_parser",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "colon_fence",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "repository_url": "https://github.com/wmpjrufg/Pontes",
    "use_repository_button": True,
    "use_download_button": False,
    "home_page_in_toc": True,
}

html_title = "Pontes"
