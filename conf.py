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
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/ast'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/client'))
sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/core'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/data'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/evaluation'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/mechanisms'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/metadata'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/models'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/reader'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/sql'))
# sys.path.insert(0, os.path.abspath('venv/lib/python3.8/site-packages/opendp/smartnoise/synthesizers'))

# -- Project information -----------------------------------------------------

project = 'OpenDP'
copyright = '2021, Joshua Allen, Ethan Cowan, Christian Covington, Eduardo de Leon, Ira Globus-Harris, James Honaker, Jason Huang, Ellen Kraffmiller, Saniya Movahed, Michael Phelan, Raman Prasad, Michael Shoemate, Robert Treacy'
author = 'Joshua Allen, Ethan Cowan, Christian Covington, Eduardo de Leon, Ira Globus-Harris, James Honaker, Jason Huang, Ellen Kraffmiller, Saniya Movahed, Michael Phelan, Raman Prasad, Michael Shoemate, Robert Treacy'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.autosummary']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
