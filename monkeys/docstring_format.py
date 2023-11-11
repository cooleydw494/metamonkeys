from dataclasses import dataclass

from mixins.x_poster_workspace import XPosterWorkspace
from monkeys.monkey import OStr, Monkey


@dataclass
class DocstringFormat(Monkey):

    mixins = (
        XPosterWorkspace,
    )

    # Main Prompts
    MAIN_PROMPT: str = \
        ('Your role is to read the contents of python files, and without changing anything else whatsoever, '
         'convert any docstrings not written in the reST style to be written in the reST style.')

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ('Limit your response to the verbatim contents of {the-file}, including all existing code and comments, '
         'as well as any docstring alterations to comply with the reST style. Add nothing else, and remove nothing.')

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None
