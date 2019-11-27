.. meta::
   :description: R, No Tears
   :keywords: r statistical programming data science
   :robots: index, follow
   :abstract: A tutorial on programming R.
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

.. R, No Tears documentation master file, created by
   sphinx-quickstart on Thu Nov 21 17:03:41 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

R, No Tears
===========

Preface
=======

This book is a tutorial on programming ``R``. To follow along and execute the code samples, you will need `Docker <https://www.docker.com/>`_ installed. The Docker container is located on `Docker Hub <https://hub.docker.com/r/oneoffcoder/book-r-intro>`_. After you have installed Docker, you may run the container as follows.

.. code-block:: bash

   docker run -it \
    -p 8888:8888 \
    -v $HOME/git/books/sphinx/r-intro/source:/root/ipynb \
    oneoffcoder/book-r-intro
    
Note that this Docker container has `Jupyter Lab <https://jupyter.org/>`_ running on port ``8888``. You may access Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_ when the Docker container is running.


.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Core
   
   data-types
   data-structures
   control-structures
   functions
   functional
   oop
   
.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Statistics
   
   data-manipulation
   descriptive
   distribution
   hypothesis
   
.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Graphs
   
   plot
   ggplot2
   
.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Data Science
   
   regression
   logistic
   classification
   clustering
   missing
   validation
   
.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Other
   
   misc

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
    The full source code is available on <a href="https://github.com/oneoffcoder/books" target="_blank">GitHub</a>.
    <br />
    <br />
    </embed>

Cite this book as follows.::

    @misc{oneoffcoder_r_programming_2019, 
    title={R, No Tears}, 
    url={https://r.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Nov}}

Author
======

Jee Vang, Ph.D.
