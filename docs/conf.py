# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PygameShader'
copyright = '2024, Yoann Berenguer'
author = 'Yoann Berenguer'
release = '1.0.11'
languages = ['en', 'fr', 'es']
# language = ['fr']
# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


templates_path = ['_templates']
exclude_patterns = ['Thumbs.db', '.DS_Store']

extensions = ['sphinxcontrib.youtube','sphinxcontrib.video', 'sphinx.ext.autodoc',
              'sphinx.ext.viewcode', 'sphinx.ext.intersphinx']

locale_dirs = ['locale/']  # Path where translations will be stored
gettext_compact = False    # Ensures messages are stored in individual files per document

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


html_theme = 'bizstyle' #'traditional' # 'agogo' #'classic'
html_static_path = ['_static']
#html_css_files = ["custom.css"]  # Load your custom CSS

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
# html_css_files = [
#      'hack.css'
#      ]
