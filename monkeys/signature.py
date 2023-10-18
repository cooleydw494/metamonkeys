from dataclasses import dataclass

from monkeys.monkey import OStr, Monkey


@dataclass
class Signature(Monkey):

    # File Iteration
    WORK_PATH: str = '~/local-git/twitter_poster'
    FILEPATH_MATCH_EXCLUDE: tuple = ('help', '__', 'defs.py', 'commands')
    FILTER_MAX_TOKENS: int = 6000

    # Main Prompts
    MAIN_PROMPT: str = \
        ("Your role is to read the contents of python files, and without changing anything else whatsoever, "
         "update method signatures to have correct type-hinting for parameters and returns. Rather than altering "
         "the file in any other way, return exactly the verbatim original file with only the type-hinting additions. "
         "Add type-hints only if they don't already exists, or if the existing type-hints are incorrect. "
         "If there are no type-hint additions necessary, return the original file contents verbatim.")

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ("Limit your response to the verbatim contents of {the-file}, including all existing code and comments, "
         "as well as any new type-hinting. Add nothing else, and remove nothing.")

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents for writing."

    # Output
    OUTPUT_PATH: str = '~/local-git/twitter_poster'
    SKIP_EXISTING_OUTPUT_FILES: bool = False
    RELATIVE_OUTPUT_PATHS = True
