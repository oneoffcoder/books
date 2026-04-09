.. meta::
   :description: Robotics Programming with Makeblock
   :keywords: robot robots robotics programming makeblock scratch
   :robots: index, follow
   :abstract: A tutorial on programming Makeblock's robots.
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

.. Makeblock Programming documentation master file, created by
   sphinx-quickstart on Mon Nov 18 14:06:41 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Robotics Programming with Makeblock
===================================

Preface
=======

This book is a tutorial on programming ``Makeblock`` robots. In particular, we will demonstrate how to program with the ``Codey Rocky`` (or just ``Codey`` for short) and ``mBot`` robots. To follow along, you will need to `install mBlock and mLink <https://www.mblock.cc/en-us/download>`_. It is advised to use mBlock version ``5.1.0`` or higher and mLink version ``1.3.0`` or higher.

The diagram below shows how the book is organized around the mBlock toolchain first, then the robot-specific blocks, and finally the code-oriented chapters for moving beyond drag-and-drop programming.

.. uml::

   @startuml
   left to right direction
   skinparam shadowing false
   rectangle "IDE Setup" as ide
   rectangle "Codey Blocks" as codey_blocks
   rectangle "mBot Blocks" as mbot_blocks
   rectangle "Shared Blocks" as common_blocks
   rectangle "Codey Coding" as codey_code
   rectangle "mBot Coding" as mbot_code
   rectangle "Resources" as resources
   ide --> codey_blocks
   ide --> mbot_blocks
   ide --> common_blocks
   codey_blocks --> codey_code
   mbot_blocks --> mbot_code
   common_blocks --> codey_code
   common_blocks --> mbot_code
   codey_code --> resources
   mbot_code --> resources
   @enduml

In other words, readers learn the environment and block vocabulary before they are asked to reason about full robot programs, which makes the later coding chapters much easier to follow.

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: mBlock

   ide
   blocks-codey
   blocks-mbot
   blocks-common

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Coding

   code-codey
   code-mbot

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Miscellaneous

   resources

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

    @misc{oneoffcoder_robotics_programming_makeblock_2019, 
    title={Robotics Programming with Makeblock}, 
    url={https://makeblock.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Nov}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>
