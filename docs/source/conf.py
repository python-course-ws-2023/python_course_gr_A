# Configuration file for the Sphinx documentation builder.
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
sys.path.insert(0, os.path.abspath('/Users/bekzodamonov/Library/CloudStorage/GoogleDrive-bekzod.amonov.study@gmail.com/My Drive/TU DORTMUND/Introduction with Python/final-project-submit/titanic_survival_package/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'titanic_survival_package'
copyright = '2024, Bekzod Amonov, Trung Anh Ha'
author = 'Bekzod Amonov, Trung Anh Ha'
release = '27.03.2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.viewcode",    # Add links to highlighted source code
    "sphinx.ext.githubpages", # Publish HTML docs in GitHub Pages
    "sphinx.ext.autodoc",     # Include documentation from docstrings
    "numpydoc",               # Support NumPy style docstrings
    "myst_nb",                # For compiling Jupyter Notebooks into high quality documentation formats
    "sphinx.ext.coverage",    # Collect doc coverage stats
    "sphinx.ext.mathjax",     # Allow support for algebra
    'sphinx.ext.napoleon',    # Support for Google and NumPy style docstrings
    'sphinx.ext.autosummary', # For automatic generation of stub files for Sphinx's autosummary extension
]

templates_path = ['_templates']
language = 'English'
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for

html_theme = 'sphinx_rtd_theme'
html_title = "Titanic Survival Package"
html_static_path = ['_static']

# do not execute jupyter notebooks when building docs
nb_execution_mode = "off"

# download notebooks as .ipynb and not as .ipynb.txt
html_sourcelink_suffix = ""


