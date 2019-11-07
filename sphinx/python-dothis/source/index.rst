.. meta::
   :description: Python: Do This, Not That!
   :keywords: python
   :robots: index, follow
   :abstract: A book showing how to write beautiful, idiomatic Python code.
   :author: One-Off Coder
   :contact: info@oneoffcoder.com
   :copyright: One-Off Coder
   :content: global
   :generator: Sphinx
   :language: English
   :rating: general
   :reply-to: info@oneoffcoder.com
   :web_author: One-Off Coder
   :revisit-after: 1 days

.. Python: Do This, Not That! documentation master file, created by
   sphinx-quickstart on Wed Oct 16 19:28:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Python: Do This, Not That!
==========================

Preface
=======

This book shows how to write beautiful, idiomatic Python code with simple, effective examples. There are no long explanations, but the intention is to **show** and **demonstrate** preferred ways of writing code in Python. As such, the intended audience is for intermediate Python programmers looking to improve ways to write and express their code in a readable way while still preserving computational efficiency and effectiveness. 

Under each major section, you will see two sub-sections: `Don't Do This` and `Do This`. Code under `Don't Do This` are discouraged, and following the adjective of |JeffKnupp_Link| :cite:`JeKn19`, are harmful. Code under `Do This` are the encouraged, beautiful and idiomatic Pythonic way to write the code instead. All examples are geared for Python 3 (specifically, v3.7) and higher (though a lot of examples may work for Python 2).

Ideas and code examples are borrowed from :cite:`RaHe19b,JeKn19,YaKh19`.

.. |JeffKnupp_Link| raw:: html

   <a href="https://jeffknupp.com/writing-idiomatic-python-ebook/" target="_blank">Jeff Knupp</a>

Table of Contents
=================

.. toctree::
   :maxdepth: 1
   :numbered:

   basic-chained-comparison
   basic-falsy-truthy
   basic-ternary-operator
   looping-range-numbers
   looping-backward
   looping-collection
   looping-collection-indices
   looping-two-collections
   list-generator
   list-filtering
   dictionary-defaultdict
   dictionary-get
   dictionary-updating
   dictionary-merging
   dictionary-counting
   dictionary-comprehension
   set-comprehension
   tuple-unpacking
   tuple-ignoring
   tuple-namedtuple
   string-concatenation
   string-interpolation
   string-dry
   function-clarification
   function-lambda
   function-generator
   class-new-vs-old
   class-dunder
   class-enumeration
   data-map-filter-reduce
   data-flattening
   data-caching
   file-reading
   file-delete
   file-filtering
   file-serde-shelve
   iter-combination
   iter-cycling
   iter-product
   misc-simultaneous-state-updates
   misc-pandas

About
=====

.. image:: _static/images/logo.png
   :alt: One-Off Coder logo.

One-Off Coder is an educational, service and product company. Please visit us online to discover how we may help you achieve life-long success in your personal coding career or with your company's business goals and objectives.

- |Website_Link|
- |Facebook_Link|
- |Twitter_Link|
- |Instagram_Link|
- |YouTube_Link|
- |LinkedIn_Link|

.. |Website_Link| raw:: html

   <a href="https://www.oneoffcoder.com" target="_blank">Website</a>

.. |Facebook_Link| raw:: html

   <a href="https://www.facebook.com/One-Off-Coder-309817926496801/" target="_blank">Facebook</a>

.. |Twitter_Link| raw:: html

   <a href="https://twitter.com/oneoffcoder" target="_blank">Twitter</a>

.. |Instagram_Link| raw:: html

   <a href="https://www.instagram.com/oneoffcoder/" target="_blank">Instagram</a>

.. |YouTube_Link| raw:: html

   <a href="https://www.youtube.com/channel/UCCCv8Glpb2dq2mhUj5mcHCQ" target="_blank">YouTube</a>

.. |LinkedIn_Link| raw:: html

   <a href="https://www.linkedin.com/company/one-off-coder/" target="_blank">LinkedIn</a>

Copyright
=========

.. raw:: html

    <embed>
    This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">Creative Commons Attribution 4.0 International License</a> by <a href="https://www.oneoffcoder.com" target="_blank">One-Off Coder</a>.
    <br />
    <br />
    <a rel="license" href="http://creativecommons.org/licenses/by/4.0/" target="_blank">
        <img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" />
    </a>
    <br />
    <br />
    The full source code is available on <a href="https://github.com/oneoffcoder/python-dothis" target="_blank">GitHub</a>.
    <br />
    <br />
    </embed>

Cite this book as follows.::

    @misc{oneoffcoder_python_dothis_2019, 
    title={Python: Do This, Not That!}, 
    url={https://python.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Oct}}

Bibliography
============

.. bibliography:: references.bib
   :style: alpha

Author
======

Jee Vang, Ph.D.