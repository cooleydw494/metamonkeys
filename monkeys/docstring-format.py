from dataclasses import dataclass
from monkeys.monkey import OStr, Monkey


@dataclass
class DocStringFormat(Monkey):
    # File Iteration
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys/commands"
    FILEPATH_MATCH_EXCLUDE: tuple = ('help', '__', 'defs.py', 'commands', 'example-automation.py', 'theme.py')
    FILTER_MAX_TOKENS: int = 6000

    # Main Prompts
    MAIN_PROMPT: str = \
        ('Your role is to read the contents of python files, and without changing anything else whatsoever, '
         'convert any docstrings not written in the reST style to be written in the reST style.')

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ('Limit your response to the verbatim contents of {the-file}, including all existing code and comments, '
         'as well as any docstring alterations to comply with the reST style. Add nothing else, and remove nothing.')

    OUTPUT_EXAMPLE_PROMPT: OStr = \
        ("Output should be in the following format with no additional context: [file-contents]"
         "Limit your response to the contents of a python class file, and nothing else."
         "Limit your output to file contents, like: ```<new file contents>```.")

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output Fixing
    OUTPUT_CHECK_PROMPT: OStr = None
    OUTPUT_TRIES: int = 1

    # Output
    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys/help/commands"
    SKIP_EXISTING_OUTPUT_FILES: bool = True
