==================
Oops All Itertools
==================

Python's ``more-itertools`` is a fantastic compliment to ``itertools`` but it's
inconvenient to have to constantly look up which itertool is in which library.
Oops All Itertools heaps them together into a loose pile in a single namespace.

Inspired by `more-itertools issue 681 <https://github.com/more-itertools/more-itertools/issues/681>`_

|Build Status|

.. |Build Status| image:: https://github.com/lonnen/oops-all-itertools/actions/workflows/test.yml/badge.svg?branch=main
   :target: https://github.com/lonnen/oops-all-itertools/actions/workflows/test.yml

:Code:          https://github.com/lonnen/oops-all-itertools
:Issues:        https://github.com/lonnen/oops-all-itertools/issues
:Releases:      https://pypi.org/project/oops_all_itertools/#history
:License:       MIT; See LICENSE

Install
=======

To get started, install the library with `pip <https://pip.pypa.io/en/stable/>`_:

.. code-block:: shell

    $ pip install oops-all-itertools


Usage
=====

.. code-block:: python

    >>> from oops_all_itertools import chain, chunked

    >>> list(chain.from_iterable(chunked(range(6), 3)))
    [0, 1, 2, 3, 4, 5]


For the full list of functions, see the `itertools API documentation <https://docs.python.org/3/library/itertools.html>`_
and the `more-itertools API documentation <https://more-itertools.readthedocs.io/en/stable/api.html>`_.