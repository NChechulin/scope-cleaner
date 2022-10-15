"""
This module contains an IPython magic to cleanup variables with a given prefix.
"""


from typing import Any, List

from IPython import get_ipython
from IPython.core.magic import needs_local_scope, register_cell_magic

from scope_cleaner.variable_extraction import get_variables_from_code


def generate_delete_statement(variables: List[str]) -> str:
    """
    Generate a Python del statement which will be executed by IPython.

    Args:
        variables (List[str]): List of variables names.

    Returns:
        str: Delete statement, or empty string if variables is empty.
    """
    return f"del {', '.join(variables)}" if variables else ""


@register_cell_magic
@needs_local_scope
def cleanup_temporary_vars(
    line: str,
    cell: str,
    local_ns: dict[str, Any],
) -> None:
    """
    Remove temporary variables introduced in current cell.

    Args:
        line (str): IPython argument containing variable prefix
        cell (str): Code of the cell
        global_ns (dict[str, Any]): Python namespace containing all variables.

    Returns:
        Tuple[str, str]: `line` and `cell`
    """
    prefix = line.strip()
    if not prefix:
        prefix = "_"

    ipy = get_ipython()
    ipy.run_cell(cell)

    var_names = get_variables_from_code(cell, global_vars=set(local_ns.keys()))
    to_delete = list(
        filter(
            lambda var_name: var_name.startswith(prefix),
            var_names,
        )
    )

    delete_statement = generate_delete_statement(to_delete)
    ipy.ex(delete_statement)
