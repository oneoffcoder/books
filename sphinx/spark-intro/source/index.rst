.. meta::
   :description: Spark, No Tears
   :keywords: spark massively parallel programming hadoop hdfs databricks
   :robots: index, follow
   :abstract: A Spark tutorial book.
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

.. Spark, No Tears documentation master file, created by
   sphinx-quickstart on Tue Oct 22 17:50:17 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Spark, No Tears
===============

Preface
=======

This book is to teach students how program in `Apache Spark <https://spark.apache.org>`_. To follow along and execute the code samples, you will need `Docker <https://www.docker.com/>`_ installed. The Docker container is located on `Docker Hub <https://hub.docker.com/r/oneoffcoder/book-spark-intro>`_. After you have installed Docker, you may run the container as follows.

.. code-block:: bash

   docker run -it \
    -p 8888:8888 \
    -e PYSPARK_MASTER=spark://localhost:7077 \
    oneoffcoder/book-spark-intro

Note that this Docker container has `Jupyter Lab <https://jupyter.org/>`_ running on port ``8888``. You may access Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_ when the Docker container is running.

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Contents
   
   rdd
   dataframes
   sparksql
   io
   dstreams
   graphs
   machine-learning

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

    @misc{oneoffcoder_spark_intro_2019, 
    title={Spark, No Tears}, 
    url={https://learn-spark.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Oct}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>