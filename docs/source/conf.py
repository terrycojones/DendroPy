# -*- coding: utf-8 -*-
#
# DendroPy documentation build configuration file, created by
# sphinx-quickstart on Wed Mar 19 16:36:08 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os
import time
from sphinx.ext import autodoc
from dendropy import __version__ as PROJECT_VERSION

# -- Sphinx Hackery ------------------------------------------------

# Following allows for a docstring of a method to be inserted "nakedly"
# (without the signature etc.) into the current context by, for example::
#
#       .. autodocstringonly:: dendropy.dataio.newickreader.NewickReader.__init__
#
# Based on:
#
#   http://stackoverflow.com/questions/7825263/including-docstring-in-sphinx-documentation
class DocStringOnlyMethodDocumenter(autodoc.MethodDocumenter):
    objtype = "docstringonly"

    # do not indent the content
    content_indent = "    "

    # do not add a header to the docstring
    def add_directive_header(self, sig):
        pass

    # def add_line(self, line, source, *lineno):
    #     """Append one line of generated reST to the output."""
    #     print self.indent + line
    #     self.directive.result.append(self.indent + line, source, *lineno)

class KeywordArgumentsOnlyMethodDocumenter(autodoc.MethodDocumenter):
    objtype = "keywordargumentsonly"
    priority = 0 # do not override normal autodocumenter

    # do not indent the content
    content_indent = "    "

    # do not add a header to the docstring
    def add_directive_header(self, sig):
        pass

    def add_line(self, line, source, *lineno):
        if ":Keyword Arguments:" in line:
            line = line.replace(":Keyword Arguments:", "                   ")
            self._emit_line = True
        if getattr(self, "_emit_line", False):
            self.directive.result.append(self.indent + line, source, *lineno)

def setup(app):
#     app.add_autodocumenter(DocStringOnlyMethodDocumenter)
    app.add_autodocumenter(KeywordArgumentsOnlyMethodDocumenter)

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinxcontrib.napoleon', # requires: pip install sphinxcontrib-napoleon
    # 'numpydoc', # requires: pip install numpydoc
]

# If 'both', then class docstring and class.__init__() docstring combined for
# class documentation.
# If 'init', then only class.__init__() docstring shown for class documentation
# (class docstring omitted).
# If not specified, then only class docstring shown for class documentation
# (__init__ docstring omitted).
autoclass_content = 'both' # or 'init'

# numpydoc settings
# numpydoc_show_class_members = False
# numpydoc_class_members_toctree = False

# Napoleon settings
# napoleon_google_docstring = True
# napoleon_numpy_docstring = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
# napoleon_use_admonition_for_examples = False
# napoleon_use_admonition_for_notes = False
# napoleon_use_admonition_for_references = False
# napoleon_use_ivar = False
# napoleon_use_param = False
napoleon_use_rtype = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'DendroPy'
copyright = u'2009-{}, Jeet Sukumaran and Mark T. Holder'.format(time.strftime('%Y'))

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = PROJECT_VERSION
# The full version, including alpha/beta/rc tags.
release = PROJECT_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = False

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False

rst_prolog = """
.. |js| replace:: Jeet Sukumaran
.. _js: http://www.jeetworks.org/about
.. |mth| replace:: Mark T. Holder
.. _mth: http://people.ku.edu/~mtholder

.. |DendroPy| replace:: DendroPy
.. _DendroPy: https://jeetsukumaran.github.io/DendroPy/
.. |dendropy_homepage_url| replace::https://jeetsukumaran.github.io/DendroPy/
.. |dendropy_primer_url| replace::https://jeetsukumaran.github.io/DendroPy/primer/index.html
.. |dendropy_library_url| replace::https://jeetsukumaran.github.io/DendroPy/library/index.html
.. |dendropy_download_url| replace:: http://pypi.python.org/pypi/DendroPy
.. |dendropy_public_repo_url| replace:: http://github.com/jeetsukumaran/DendroPy

.. |Python| replace:: Python
.. _Python: http://www.python.org/
.. |Python26| replace:: Python 2.6
.. _Python 2.6: http://www.python.org/download/releases/2.6/
.. |Python27| replace:: Python 2.7
.. _Python 2.7: http://www.python.org/download/releases/2.7/
.. |Python34| replace:: Python 3.4.0
.. _Python 3.4.0: https://www.python.org/download/releases/3.4.0/
.. |Python2| replace:: Python 2
.. _Python 2: http://www.python.org/download/releases/2.7/
.. |Python3| replace:: Python 3
.. _Python 3: https://www.python.org/download/releases/3.4.0/
.. |setuptools| replace:: setuptools
.. _setuptools: http://pypi.python.org/pypi/setuptools
.. |pip| replace:: pip
.. _pip: http://pypi.python.org/pypi/pip
.. |Git| replace:: Git
.. _Git: http://git-scm.com/

.. |dendropy_logo| replace:: /_static/dendropy_logo.png
.. |dendropy_library_doc| replace:: /library/index
.. |dendropy_primer_doc| replace:: /primer/index
.. |sumtrees_doc| replace:: /programs/sumtrees

.. |dendropy_announce| replace:: DendroPy Announcements
.. _dendropy_announce: http://groups.google.com/group/dendropy-announce
.. |dendropy_users| replace:: DendroPy Users
.. _dendropy_users: http://groups.google.com/group/dendropy-users
.. |dendropy_issues| replace:: DendroPy Issues
.. _dendropy_issues: https://github.com/jeetsukumaran/DendroPy/issues

.. |Taxon| replace:: :class:`~dendropy.datamodel.taxonmodel.Taxon`
.. |TaxonNamespace| replace:: :class:`~dendropy.datamodel.taxonmodel.TaxonNamespace`
.. |TaxonNamespaceMapping| replace:: :class:`~dendropy.datamodel.taxonmodel.TaxonNamespaceMapping`
.. |Tree| replace:: :class:`~dendropy.datamodel.treemodel.Tree`
.. |Node| replace:: :class:`~dendropy.datamodel.treemodel.Node`
.. |Edge| replace:: :class:`~dendropy.datamodel.treemodel.Edge`
.. |Bipartition| replace:: :class:`~dendropy.datamodel.treemodel.Bipartition`
.. |TreeList| replace:: :class:`~dendropy.datamodel.treecollectionmodel.TreeList`
.. |TreeArray| replace:: :class:`~dendropy.datamodel.treecollectionmodel.TreeArray`
.. |SplitDistribution| replace:: :class:`~dendropy.datamodel.treecollectionmodel.SplitDistribution`
.. |SplitDistributionSummarizer| replace:: :class:`~dendropy.datamodel.treecollectionmodel.SplitDistributionSummarizer`
.. |DataSet| replace:: :class:`~dendropy.datamodel.datasetmodel.DataSet`
.. |StateIdentity| replace:: :class:`~dendropy.datamodel.charstatemodel.StateIdentity`
.. |StateAlphabet| replace:: :class:`~dendropy.datamodel.charstatemodel.StateAlphabet`
.. |CharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.CharacterMatrix`
.. |DnaCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix`
.. |RnaCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.RnaCharacterMatrix`
.. |ProteinCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.ProteinCharacterMatrix`
.. |InfiniteSitesCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.InfiniteSitesCharacterMatrix`
.. |RestrictionSitesCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.RestrictionSitesCharacterMatrix`
.. |StandardCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.StandardCharacterMatrix`
.. |ContinuousCharacterMatrix| replace:: :class:`~dendropy.datamodel.charmatrixmodel.ContinuousCharacterMatrix`
.. |CharacterDataSequence| replace:: :class:`~dendropy.datamodel.charmatrixmodel.CharacterDataSequence`
.. |ContinuousCharacterDataSequence| replace:: :class:`~dendropy.datamodel.charmatrixmodel.ContinuousCharacterDataSequence`
.. |DnaCharacterDataSequence| replace:: :class:`~dendropy.datamodel.charmatrixmodel.DnaCharacterDataSequence`
.. |CharacterType| replace:: :class:`~dendropy.datamodel.charmatrixmodel.CharacterType`
.. |Annotation| replace:: :class:`~dendropy.datamodel.basemodel.Annotation`
.. |AnnotationSet| replace:: :class:`~dendropy.datamodel.basemodel.AnnotationSet`
.. |Annotable| replace:: :class:`~dendropy.datamodel.basemodel.Annotable`
.. |PhylogeneticDistanceMatrix| replace:: :class:`~dendropy.calculate.phylogeneticdistance.PhylogeneticDistanceMatrix`
.. |AsciiTreePlot| replace:: :class:`~dendropy.datamodel.treemodel.AsciiTreePlot`

.. |get| replace::  :py:meth:`get`
.. |put| replace::  :py:meth:`put`
.. |read| replace::  :py:meth:`read`
.. |write| replace::  :py:meth:`write`

.. |get_from_methods| replace::  :py:meth:`get_from_*() <get_from_*>`
.. |read_from_methods| replace::  :py:meth:`read_from_*() <read_from_*>`
.. |write_to_methods| replace::  :py:meth:`write_to_*() <read_from_*>`

.. |True| replace:: ``True``
.. |False| replace:: ``False``
.. |None| replace:: ``None``

.. |FigTree| replace:: FigTree
.. _FigTree: http://tree.bio.ed.ac.uk/software/figtree/
.. |RAxML| replace:: RAxML
.. _RAxML: http://sco.h-its.org/exelixis/software.html
.. |SeqGen| replace:: Seq-Gen
.. _SeqGen: http://tree.bio.ed.ac.uk/software/seqgen/
.. |GenBank| replace:: GenBank
.. _GenBank: http://www.ncbi.nlm.nih.gov/genbank/

.. |Schemas| replace:: :doc:`/schemas/index`
.. |FASTA| replace:: :doc:`/schemas/fasta`
.. |Newick| replace:: :doc:`/schemas/newick`
.. |Nexus| replace:: :doc:`/schemas/nexus`
.. |NeXML| replace:: :doc:`/schemas/nexml`
.. |Phylip| replace:: :doc:`/schemas/phylip`

"""

rst_prolog += """\
.. |dendropy_source_archive_url| replace:: http://pypi.python.org/packages/source/D/DendroPy/DendroPy-%s.tar.gz
.. |dendropy_source_archive| replace:: DendroPy source code archive
.. _dendropy_source_archive: http://pypi.python.org/packages/source/D/DendroPy/DendroPy-%s.tar.gz
""" % (version, version)

rst_prolog += """\
.. |dendropy_citation| replace:: Moreno, M. A., Sukumaran, J., and M. T. Holder. 2024. DendroPy 5: a mature Python library for phylogenetic computing. arXiv preprint arXiv:2405.14120. https://doi.org/10.48550/arXiv.2405.14120
.. |dendropy_copyright| replace:: Copyright {copyright}. All rights reserved.
.. |
""".format(copyright=copyright)

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_dendropy_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_themes"]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = "_static/dendropy_logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    "**" : ["logo.html",
            "cleardiv.html",
            "searchbox.html",
            "cleardiv.html",
            "localtoc.html",
            "cleardiv.html",
            "relations.html",
            "cleardiv.html",
            "side_supplemental.html"],
        }

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'DendroPydoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#   ('index', 'DendroPy.tex', u'DendroPy Documentation',
#    u'Jeet Sukumaran and Mark T. Holder', 'manual'),
# ]
latex_documents = [
  ('index', 'DendroPy.tex', u'DendroPy Documentation',
   u'Jeet Sukumaran and Mark T. Holder', 'manual'),
  ('primer/index', 'DendroPy-Primer.tex', u'DendroPy Primer',
   u'Jeet Sukumaran and Mark T. Holder', 'manual'),
  ('library/index', 'DendroPy-Library-API.tex', u'DendroPy Library API Reference',
   u'Jeet Sukumaran and Mark T. Holder', 'manual'),
  ('programs/sumtrees', 'DendroPy-SumTrees.tex', u'SumTrees User Manual',
   u'Jeet Sukumaran and Mark T. Holder', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    # ('index', 'dendropy', u'DendroPy Documentation',
    #  [u'Jeet Sukumaran and Mark T. Holder'], 1),
    ('library/index', 'dendropy', u'DendroPy Library API Reference',
     [u'Jeet Sukumaran and Mark T. Holder'], 1),
    ('primer/index', 'dendropy-primer', u'DendroPy Primer',
     [u'Jeet Sukumaran and Mark T. Holder'], 1),
    ('programs/sumtrees', 'sumtrees', u'SumTrees User Manual',
     [u'Jeet Sukumaran and Mark T. Holder'], 1),
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('library/index', 'DendroPy', u'DendroPy Documentation',
   u'Jeet Sukumaran and Mark T. Holder', 'DendroPy', 'Python library for phylogenetic computing',
   'Miscellaneous'),
  ('primer/index', 'DendroPy-Primer', u'DendroPy Primer',
   u'Jeet Sukumaran and Mark T. Holder', 'DendroPy', 'Python library for phylogenetic computing',
   'Miscellaneous'),
  ('programs/sumtrees', 'SumTrees', u'SumTrees Documentation',
   u'Jeet Sukumaran and Mark T. Holder', 'DendroPy', 'Python library for phylogenetic computing',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False


# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'DendroPy'
epub_author = u'Jeet Sukumaran and Mark T. Holder'
epub_publisher = u'Jeet Sukumaran and Mark T. Holder'
epub_copyright = u'2015, Jeet Sukumaran and Mark T. Holder'

# The basename for the epub file. It defaults to the project name.
#epub_basename = u'DendroPy'

# The HTML theme for the epub output. Since the default themes are not optimized
# for small screen space, using the same theme for HTML and epub output is
# usually not wise. This defaults to 'epub', a theme designed to save visual
# space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the PIL.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}
