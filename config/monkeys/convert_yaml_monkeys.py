from dataclasses import dataclass

from codemonkeys.defs import MONKEYS_PATH

from config.monkeys.monkey import Monkey
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
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    # CONTEXT_FILE_PATH: OStr = f'{MONKEYS_PATH}/self_help.py'

    # Output Checks
    FIX_OUTPUT_PROMPT: OStr = 'The finalized output should include nothing more than the contents of a yaml file.'

    # Output
    OUTPUT_PATH: str = MONKEYS_PATH
    OUTPUT_EXT: OStr = '.yaml'
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'
    OUTPUT_CHECK_MODEL: str = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    OUTPUT_CHECK_TEMP: float = 0.5

    # Max Tokens
    MAIN_MAX_TOKENS: int = 5000
    SUMMARY_MAX_TOKENS: int = 5000
    OUTPUT_CHECK_MAX_TOKENS: int = 3000
