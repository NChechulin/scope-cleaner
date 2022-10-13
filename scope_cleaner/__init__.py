"""
An IPython cell magic to remove temporary variables.

Scope cleaner is a very simple IPython cell magic which allows one
to automatically remove temporary variables, so that they don't pollute
the scope and keep extra memory allocated.

The most common usecase is some variables used for EDA (Exploratory
data analysis), or when some statistic has to be printed.
"""
