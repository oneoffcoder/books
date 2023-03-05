.. meta::
   :description: Data Science Topics
   :keywords: data science pytorch deep learning machine learning artificial intelligence
   :robots: index, follow
   :abstract: A data science book.
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

.. Data Science Topics documentation master file, created by
   sphinx-quickstart on Wed Nov  6 12:03:40 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Data Science Topics
===================

Preface
=======

This book is to teach students specialized areas and topics of ``Data Science``. To follow along and execute the code samples, you will need `Docker <https://www.docker.com/>`_ installed. The Docker container is located on `Docker Hub <https://hub.docker.com/r/oneoffcoder/book-datascience>`_. After you have installed Docker, you may run the container as follows.

.. code-block:: bash

   docker run -it \
    -p 8888:8888 \
    -p 6006:6006 \
    --gpus all \
    oneoffcoder/book-datascience

Note that this Docker container has `Jupyter Lab <https://jupyter.org/>`_ running on port ``8888``. You may access Jupyter Lab at `http://localhost:8888 <http://localhost:8888>`_ when the Docker container is running.

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: General

   missing-data
   pca
   lda
   mvn-conditional
   bivariate-cond-gaussian
   multivariate-cond-gaussian
   normalized-entropy-mi
   mi-gaussian
   cmi-gaussian
   partial-correlation
   precision-recall-roc
   kalman-filter
   kalman-filter-ii
   gaussian-hmm
   ipf
   ipf-ii
   
.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Distributions

   generate-gaussian-distributed-values
   kullback-leibler-divergence
   dirichlet-multinomial-distribution
   scheduling-distributions
   gmm
   gmm-dirichlet
   gmm-data-discretization
   kmc-bic-aic
   pdf-cdf
   s-curve
   markov-chain-stationary-distribution

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Regression
   
   regression-errors
   psuedo-r-squared-logistic-regression
   simple-mcfadden
   logistic-nb
   estimating-standard-error-coefficients
   logreg-y-probability
   lasso-safe-strong
   log-linear-model
   log-linear-graphical
   lmm
   irwls
   
.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Survival Analysis
   
   survival-functions
   survival-mva

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Rating and Ranking
   
   btl-model
   massey-method
   massey-method-ii
   colley-method
   keener-method
   markov-method
   reordering-method
   
.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Gradient Descent

   gradient-descent
   autograd-regression-gradient-descent
   autograd-logistic-regression-gradient-descent
   autograd-poisson-regression-gradient-descent
   neural-network-gradient-descent
   online-sgd

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Natural Language Processing

   latent-semantic-analysis
   topic-modeling-gensim
   
.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Deep Learning

   neural-network-handcraft
   restricted-boltzmann-machine
   rnn-classify-signals
   pose-estimation
   autoencoder-anomaly
   autoencoder-data-imputation
   autoencoder-malicious-urls

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: COVID-19
      
   covid-patient-level
   covid-diagnosis

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Chernoff Faces

   chernoff-faces
   chernoff-deeplearning
   chernoff-classification
   chernoff-inception_v3

.. toctree::
   :maxdepth: 1
   :numbered:
   :caption: Causality

   simpson-paradox
   generate-random-bbn
   creating-junction-tree
   gaussian-network-inference
   causal-inference
   dbn-markov-chain
   dbn-hmm
   psm

.. toctree::
   :maxdepth: 1
   :caption: References

   zzz-bib
   

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

    @misc{oneoffcoder_datascience_topics_2019, 
    title={Data Science Topics}, 
    url={https://datascience.oneoffcoder.com}, 
    author={One-Off Coder}, 
    year={2019}, 
    month={Nov}}

Author
======

Jee Vang, Ph.D.

- |Patreon_Link|

.. |Patreon_Link| raw:: html

   <a href="https://www.patreon.com/vangj" target="_blank">Patreon</a>