from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from mixins.codemonkeys_workspace import CodemonkeysWorkspace
from monkeys.monkey import Monkey, OStr


@dataclass
class IdeDocumentation(Monkey):

    mixins = (
        CodemonkeysWorkspace,
    )

    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys/builders"
    OUTPUT_PATH = "~/local-git/codemonkeys/codemonkeys/builders"

    # Main Prompts
    MAIN_PROMPT: str = (
        'Your role is to read the contents of Python files, and without changing anything else whatsoever, '
        'add/improve docstrings/documentation for IDE and Sphinx autodoc purposes. '
        'Exercise judgement in determining what is useful information. '
        'If there are no docblock additions that are genuinely helpful, return the original file contents verbatim. '
        'Use the following reST formatting guide and project context to assist having a full understanding:\n\n'
        '{cop:~/local-git/metamonkeys/stor/context/rest-guide.md}\n\n')
    MAIN_PROMPT_ULTIMATUM: OStr = (
        'Limit your response to the verbatim contents of {the-file}, including all existing code and comments, '
        'as well as any new docstring, following the reST documentation guide closely. Add nothing else, and remove '
        'nothing.')

    OUTPUT_PROMPT: OStr = "Output should be the unabridged contents of the updated file."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f'{STOR_PATH}/context/codemonkeys-docs.md'
