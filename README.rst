bigstack
========

*python decorator that increases the stack size for the function. This is useful
for highly recursive function (albeit highly recursive function are bad).*

Description
-----------

This decorator increases the stack size for the function and its recursion
limit. The function runs in a separated thread with a stack size specified
by the ``stacksize`` parameter (``default: 128MiB``). Also the recursion
limit can be modified by the ``recursionlimit`` parameter (``default: 1M``),
but be aware that this is a variable shared by the whole python environment,
so a subsequent invocation of a decorated function may change it.

.. code:: python

    @bigstack
    def function(...):
        """Highly recursive function."""
        ...

.. code:: python

    @bigstack(stacksize=2 ** 30)    # stack size = 1GB
    def function(...):
        """Highly recursive function."""
        ...

Installation
------------

The package has been uploaded to `PyPI`_, so you can install it with pip:

    pip install bigstack


.. _PyPI: https://pypi.python.org/pypi/bigstack
