# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.
import pathlib
import sys
import os
import django

BASE_DIR = pathlib.Path(__file__).resolve().parents[2].resolve().as_posix()
REPORT = BASE_DIR + '/reports/'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'oc_lettings_site.settings')
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())
sys.path.insert(1, "/oc_lettings_site/")
sys.path.insert(1, "/lettings/")
sys.path.insert(1, "/profiles/")
sys.path.insert(1, os.path.abspath('.'))
sys.path.insert(1, os.path.abspath('../../'))
sys.path.insert(1, REPORT)

print(sys.path)

# Setup Django
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Orange County Lettings'
copyright = '2023, LECOMTE Thomas'
author = 'LECOMTE Thomas'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "myst_parser",
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode'
]

myst_enable_extensions = [

]

myst_all_links_external = True

autosummary_generate_overwrite = True
autodoc_typehints = "description"

coverage_show_missing_items = True

viewcode_follow_imported_members = True
viewcode_line_numbers = True

source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_logo = '_static/logo.png'
html_theme = 'pydata_sphinx_theme'
html_sidebars = {
    "**": ["sidebar-nav-bs.html"],
}
html_theme_options = {
    "collapse_navigation": True,
    "navigation_depth": 4,
    "show_nav_level": 4,
    "show_toc_level": 3,
    "show_prev_next": False,
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/Nathom78/Python-OC-Lettings-FR",
            # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fa-brands fa-square-github",
            # The type of image to be used (see below for details)
            "type": "fontawesome",
        },
        {
            "name": "Azure site",
            "url": "https://orange-county-lettings.azurewebsites.net/",
            "icon": "_static/Microsoft-Azure.png",
            "type": "local",
        }
    ]
}
html_static_path = ['_static']
