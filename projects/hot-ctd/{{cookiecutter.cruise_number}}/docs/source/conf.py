# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'HOT-{{cookiecutter.cruise_number}} CTD Data Processing Report'
copyright = f'{datetime.now().year}, Hawaii Ocean Time-series (HOT)'
author = '{{cookiecutter.processor_first_name}} {{cookiecutter.processor_last_name}}'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_nb",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx_design",
    "sphinx_thebe",
]

# Enable some MyST extensions.
myst_enable_extensions = [
    "colon_fence",
    "amsmath",
]

intersphinx_mapping = {
    "cchdo-website": ("https://exchange-format.readthedocs.io/en/latest/", None),
}

myst_url_schemes = ["http", "https", ]

# Added cross reference for headings
myst_heading_anchors = 3

# Jupyter notebook
nb_execution_mode = "auto"

thebe_config = {
    "always_load": True,
}

# Add numbered roles
numfig = True

# Make sure the explicity target is unique
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = {
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
    '.md': 'myst-nb',
}

master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store', '.env', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/_images/logo_HOT.png"
html_title = "HOT-{{cookiecutter.cruise_number}}"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/hot-dogs/hot{{cookiecutter.cruise_number}}-data-report",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": False,
}

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/_images/logo_HOT.png"

latex_additional_files = [
    "latex_templates/maketitle.sty",
    "latex_templates/mystyle.sty",
]

latex_elements = {
    'papersize': 'a4paper',
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage[Bjornstrup]{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    'figure_align': 'htbp',
    'pointsize': '10pt',

    # ===================== PREAMBLE ======================================
    'preamble': r'''
      \input{mystyle.sty}
    ''',
    # ============== COVER PAGE + TABLE OF CONTENTS  ======================
    'maketitle': r''' 
      \input{maketitle.sty}
    ''',

    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}, \
        HeaderFamily=\\rmfamily\\bfseries, \
        InnerLinkColor={rgb}{0,0,1}, \
        OuterLinkColor={rgb}{0,0,1}',
    'tableofcontents': ' ',

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'hot-{{cookiecutter.cruise_number}}-ctd-data-report.tex',
     u'HOT-{{cookiecutter.cruise_number}}: CTD Data Processing Report',
     u'{{cookiecutter.processor_first_name}}{{cookiecutter.processor_last_name}} ', 'manual'),
]


# If false, no module index is generated.
latex_domain_indices = True

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     ('index', 'whots-manual-page-test', u'whots-manual-page-test',
#      [u'Fernando Carvalho Pacheco'], 1)
# ]
#
# latex_logo = "../source/_static/_images/logo_HOT.jpg"
