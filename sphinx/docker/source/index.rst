.. meta::
   :description: Docker, No Tears
   :keywords: docker containerization swarm kubernetes devop devsecop noop serverless
   :robots: index, follow
   :abstract: A tutorial on Docker.
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

.. Docker, No Tears documentation master file, created by
   sphinx-quickstart on Wed Nov 27 09:19:08 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Docker, No Tears
================

Preface
=======

This book is a tutorial on ``Docker``. To follow along, install Docker Engine or Docker Desktop, then verify that the modern Compose and Buildx plugins are available.

* `Docker <https://docs.docker.com/get-started/get-docker/>`_
* `Docker Compose <https://docs.docker.com/compose/>`_
* `Docker Buildx <https://docs.docker.com/build/>`_
* `kubectl <https://kubernetes.io/docs/tasks/tools/>`_
* A local Kubernetes cluster such as `minikube <https://minikube.sigs.k8s.io/docs/start/>`_, `kind <https://kind.sigs.k8s.io/>`_, or Docker Desktop Kubernetes

The diagram below gives a quick map of how the book moves from single-container basics toward repeatable builds, orchestration, security, and cloud deployment targets.

.. uml::

   @startuml
   left to right direction
   skinparam shadowing false
   rectangle "Start Here" as start
   rectangle "Core Docker" as core
   rectangle "Build and\nSecurity" as build
   rectangle "Multi-Service and\nOrchestration" as orchestration
   rectangle "Platforms and\nWorkloads" as operations
   rectangle "ECR, ECS,\nSageMaker" as deployment
   start --> core
   core --> build
   build --> orchestration
   orchestration --> operations
   operations --> deployment
   @enduml

Read the diagram from left to right: first get Docker working locally, then learn core container workflows, harden the build path, orchestrate multiple services, and carry those patterns into specialized workloads and AWS deployments.

.. toctree::
   :maxdepth: 2
   :caption: Start Here

   preflight
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: Core Docker

   containerization
   cli
   runtime
   devops

.. toctree::
   :maxdepth: 2
   :caption: Build and Security

   buildkit
   build-checks
   image-hardening
   supply-chain

.. toctree::
   :maxdepth: 2
   :caption: Multi-Service and Orchestration

   compose
   swarm
   kubernetes

.. toctree::
   :maxdepth: 2
   :caption: Platforms and Workloads

   arm
   gpu
   encryption

.. toctree::
   :maxdepth: 2
   :caption: AWS Deployment

   ecr
   ecs
   sagemaker

.. toctree::
   :maxdepth: 2
   :caption: Reference

   references


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

    @misc{oneoffcoder_docker_2019, 
    title={Docker, No Tears}, 
    url={https://docker.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Nov}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>
