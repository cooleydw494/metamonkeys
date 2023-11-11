from dataclasses import dataclass

from mixins.codemonkeys_workspace import CodemonkeysWorkspace
from mixins.gpt_ultra import GptFourPreview
from monkeys.monkey import OStr, Monkey


@dataclass
class Commenter(Monkey):

    mixins = (
        CodemonkeysWorkspace,
        GptFourPreview,
    )

    # Prompts
    MAIN_PROMPT: str = \
        ("Please add code comments to document the following file: {the-file}. Use PEP8 style docstrings for functions "
         "and classes, and single-line comments for other code. Focus on readability and clarity. Rather than include "
         "verbose comments, try to make comments elegant and concise. You may add new comments, new docstrings, and "
         "edit existing comments. You may also re-order code, but do not add or remove code. If there is no value to "
         "adding/altering comments, return the original file verbatim.")

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ("Limit your response to the verbatim contents of {the-file}, including all existing code and comments, "
         "as well as any new or altered comments you add. Do not add comments that are not genuinely helpful.")

    OUTPUT_PROMPT: str = "Output should be nothing more than the updated file contents."
