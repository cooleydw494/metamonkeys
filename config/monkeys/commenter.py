from dataclasses import dataclass

from config.monkeys.monkey import OStr, Monkey


@dataclass
class Commenter(Monkey):

    # File Iteration
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys/commands"
    PATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'commenter', '__', 'defs.py')
    FILTER_MAX_TOKENS: int = 6000

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

    OUTPUT_EXAMPLE_PROMPT: OStr = \
        ("Limit your output strictly to the updated contents of the file, including nothing else, like this: [complete "
         "contents of file]")

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        ('Examine the following output and determine if it is limited to the contents of a commented python file. '
         'Respond with only one word: "True" or "False".')
    OUTPUT_TRIES: int = 3

    # Output
    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys/commenter/commands"
    SKIP_EXISTING_OUTPUT_FILES: bool = True
