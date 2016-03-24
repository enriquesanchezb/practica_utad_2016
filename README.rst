=========================
 Words Project
=========================

.. image:: https://travis-ci.org/enriquesanchezb/practica_utad_2016.svg?branch=master
    :target: https://travis-ci.org/enriquesanchezb/practica_utad_2016

Synopsis
========

Read words from a font and show it.


Installation
============

#. Clone the repo and install and create a new environmet using virtualenv_::

    source venv/bin/activate

#. Once you have created and activated the environment you have to install the dependencies::

    pip install -r requirements.txt

.. _virtualenv: https://github.com/pypa/virtualenv

#. Install the stopwords package::

    python -m nltk.downloader stopwords


Tests
=====

All the tests are into ``tests`` directory. You can run them using::

    paver test
    paver test_all

Run the tests means: lint the code using PEP8 and pass all the tests

If you want to know the coverage you can use paver too::

    paver coverage

Continuos Integration
=====================

To pass all the test into a system like Jenkins_ you can use tox_.

.. _Jenkins: http://jenkins-ci.org/
.. _tox: https://pypi.python.org/pypi/tox

Contributors
============

* Enrique Sánchez-Bayuela (`@EnriqueSanchezB`_)

.. _@EnriqueSanchezB: http://twitter.com/EnriqueSanchezB

License
=======

All the rights reserved (C) 2016