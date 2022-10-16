"""Contains utility procedures for interacting with IPython kernel."""


import io
import tokenize
from typing import List, Set


def tokenize_code(code: str) -> List[tokenize.TokenInfo]:
    """
    Parse python code into a list of tokens.

    Args:
        code (str): Program code

    Returns:
        List[tokenize.TokenInfo]: List of code tokens
    """
    stream = io.StringIO(code)
    return list(tokenize.generate_tokens(stream.readline))


def extract_assigned_vars(tokens: List[tokenize.TokenInfo]) -> Set[str]:
    """
    Take variable names out of tokenized code.

    Args:
        tokens (List[tokenize.TokenInfo]): Tokenized cell code

    Returns:
        Set[str]: Set of variable names
    """
    var_names: Set[str] = set()

    for ind, cur_token in enumerate(tokens[1:], start=1):
        prev_token = tokens[ind - 1]

        cur_is_asgn = cur_token.type == tokenize.OP and cur_token.string == "="

        if prev_token.type == tokenize.NAME and cur_is_asgn:
            var_names.add(prev_token.string)

    return var_names


def get_variables_from_code(cell_code: str, global_vars: Set[str]) -> List[str]:
    """
    Extract all variables which have been assigned a value from python cell code.

    Args:
        cell_code (str): Python cell code.
        global_vars (Set[str]): Set of variables from global scope.
        Used for validation of parsed variables.

    Returns:
        List[str]: List of variable names.
    """
    cell_tokens = tokenize_code(cell_code)
    cell_assigned_vars = extract_assigned_vars(cell_tokens)

    # At this point, `cell_assigned_vars` contains all the variables that have been
    # assigned a value in current cell. This means that it might contain
    # false-positives. For example, variables from functions defined in the cell.
    # What we need to do is to ask IPython to give us all global variables and find
    # the intersection of global variables and cell ones.

    return list(cell_assigned_vars.intersection(global_vars))
