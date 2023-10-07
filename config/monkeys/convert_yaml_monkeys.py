from dataclasses import dataclass

from codemonkeys.defs import MONKEYS_PATH

from config.monkeys.monkey import Monkey
from codemonkeys.types import OStr


@dataclass
class ConvertYamlMonkeys(Monkey):

    # General
    WORK_PATH: str = MONKEYS_PATH
    FILE_TYPES_INCLUDED: tuple = ('.yaml')

    # Main Prompts
    MAIN_PROMPT: str = \
        ("Please convert the following yaml 'monkey' configuration file to the new format, which is a python class "
         "using inheritance for defaults. Use the SelfHelp class as an example, understanding that different configs "
         "will require different properties to be overridden.")

    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python class file, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f'{MONKEYS_PATH}/self_help.py'

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script.' \
        ' Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: int = 3

    # Output
    OUTPUT_PATH: str = MONKEYS_PATH
    OUTPUT_EXT: OStr = '.py'
    OUTPUT_REMOVE_STRINGS: tuple = ('```python\n', '```python,```')
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
