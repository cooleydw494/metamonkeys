from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from mixins.codemonkeys_workspace import CodemonkeysWorkspace
from mixins.example_workspace import ExampleWorkspace
from monkeys.monkey import Monkey, OStr


@dataclass
class MinifyCode(Monkey):

    mixins = (
        ExampleWorkspace,
    )

    # Main Prompts
    MAIN_PROMPT: str = (
        'Read files and minify the code, removing all comments and docstrings')
    MAIN_PROMPT_ULTIMATUM: OStr = (
        'Return only minified contents of {the-file}, excluding all comments and docstrings.')

    OUTPUT_PROMPT: OStr = "Output should be the unabridged contents of the minified file."
