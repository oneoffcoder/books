.. meta::
   :description: AWS Certified Developer
   :keywords: aws certified developer 
   :robots: index, follow
   :abstract: A tutorial on AWS development.
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

.. AWS Developer documentation master file, created by
   sphinx-quickstart on Sun Dec  1 16:12:54 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

AWS Certified Developer
=======================

Preface
=======

This book is to teach students how to develop applications and solutions using the Amazon Web Services ``AWS`` platform. There is a companion ``Docker`` image that you may use as follows. Note that you will have to override the following values: ``AWS_REGION``, ``AWS_ACCESS_KEY`` and ``AWS_SECRET_KEY``.

.. code-block:: bash
    :linenos:

    docker run -it \
        -p 8888:8888 \
        -v `pwd`/ipynb:/root/ipynb \
        -e NOTEBOOK_PASSWORD=sha1:6676da7235c8:9c7d402c01e330b9368fa9e1637233748be11cc5 \
        -e AWS_REGION="us-east-1" \
        -e AWS_ACCESS_KEY="<set>" \
        -e AWS_SECRET_KEY="<set>" \
        oneoffcoder/book-aws-developer:latest

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   intro
   ec2



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

    @misc{oneoffcoder_aws_developer_2019, 
    title={AWS Certified Developer}, 
    url={https://aws-developer.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Dec}}

Author
======

Jee Vang, Ph.D.