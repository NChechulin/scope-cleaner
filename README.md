# Scope cleaner

An IPython cell magic to remove temporary variables.
I wrote this package because I didn't like by global scope to be cluttered with variables I used in 1 cell only during EDA (Exploratory Data Analysis).

## Installation

ToDo

## Usage

Firstly, one needs to import the package: `import scope_cleaner`.
Then a new magic becomes available: `%%cleanup_temporary_vars <optional_prefix>`.
Optional prefix is a parameter which helps to filter out the temporary variables introduced in current cell.
If it's not set, the prefix defaults to `_`.

Example:
Consider the following IPython cells:

**Cell 2**
```python
%%cleanup_temporary_vars tmp

a = 10
b = 15

tmp_1 = 123
tmp_2 = 234

print("tmp", tmp_1, tmp_2)  # Out: tmp 123 234
tmp_1 + tmp_2  # Out: 357
```

So all the variables from current cell work correctly.

**Cell 3**
```python
a + b  # Out: 25
tmp_1  # Error: no such variable
```

As we can see, the temporary variable was automatically deleted by `%%cleanup_temporary_vars` in the end of previous cell (because its name starts with `tmp`).

