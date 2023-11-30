from dataclasses import dataclass

from mixins.example_workspace import ExampleWorkspace
from monkeys.monkey import Monkey, OStr


@dataclass
class IdeDocumentation(Monkey):

    mixins = (
        ExampleWorkspace,
    )

    # Main Prompts
    MAIN_PROMPT: str = (
        'Your role is to read the contents of Python files, and without changing anything else, '
        'add/improve docstrings/documentation for IDE and Sphinx autodoc purposes, following the reST Documentation '
        'Guide for Assistant. Exercise judgement in determining what is useful information. '
        'If there are no docblock additions that are genuinely helpful, return the original file contents verbatim. '
        'Use the following reST formatting guide and CodeMonkeys project context to guide your understanding:\n\n'
        '{cop:~/local-git/metamonkeys/stor/context/rest-guide.md}\n\n')

    MAIN_PROMPT_ULTIMATUM: OStr = (
        'Limit your response to the verbatim contents of {the-file}, including all existing code and comments, '
        'as well as any new docstring, following the reST documentation guide closely. Add nothing else, and remove '
        'nothing.')

    OUTPUT_PROMPT: OStr = "Output should be the unabridged contents of the updated file."
