from dataclasses import dataclass

from codemonkeys.defs import MONKEYS_PATH

from monkeys.monkey import Monkey
from codemonkeys.types import OStr


@dataclass
class ConvertYamlMonkeys(Monkey):

    # File Iteration
    WORK_PATH: str = MONKEYS_PATH
    INCLUDE_EXTS: tuple = ('.py')

    # Main Prompts
    MAIN_PROMPT: str = \
        ("Please convert the following python 'monkey' class files to the new format, which is a yaml config file."
         " The yaml configs should contain all of the declared properties of the python class, formatted well.")

    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a yaml file, and nothing else."
    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Context / Summary
    # CONTEXT_FILE_PATH: OStr = f'{MONKEYS_PATH}/self_help.py'

    # Output
    OUTPUT_PATH: str = MONKEYS_PATH
    OUTPUT_EXT: OStr = '.yaml'
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0

    # Max Tokens
    MAIN_MAX_TOKENS: int = 5000
    SUMMARY_MAX_TOKENS: int = 5000
