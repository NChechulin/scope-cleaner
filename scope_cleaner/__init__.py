"""
An IPython cell magic to remove temporary variables.

Scope cleaner is a very simple IPython cell magic which allows one
to automatically remove temporary variables, so that they don't pollute
the scope and keep extra memory allocated.

The most common usecase is some variables used for EDA (Exploratory
data analysis), or when some statistic has to be printed.
"""

__version__ = "0.1.0.post4"

from typing import Any

from scope_cleaner.magic import cleanup_temporary_vars


def load_ipython_extension(ipython: Any) -> None:
    """
    Ipython function to load register magics.

    Args:
        ipython (Any): IPython object
    """
    ipython.register_magics(cleanup_temporary_vars)
