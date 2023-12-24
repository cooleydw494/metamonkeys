from dataclasses import dataclass

from monkeys.monkey import Monkey
from codemonkeys.types import OStr


@dataclass
class Translate(Monkey):

    # File Iteration
    WORK_PATH: str = "~/local-git/cm-examples/english-to-spanish"
    INCLUDE_EXTS: tuple = ()

    # Main Prompts
    MAIN_PROMPT: str = "Please translate the following text from English to Spanish from {the-file}:"

    # Output
    OUTPUT_PATH: str = "~/local-git/cm-examples/english-to-spanish"

    # Models
    MAIN_MODEL: str = 'gpt-4-1106-preview'
    SUMMARY_MODEL: str = 'gpt-4-1106-preview'
    FILE_SELECT_MODEL: str = 'gpt-4-1106-preview'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    FILE_SELECT_TEMP: float = 0.8

    # Max Tokens
    MAIN_MAX_TOKENS: int = 5000
    SUMMARY_MAX_TOKENS: int = 5000
    FILE_SELECT_MAX_TOKENS: int = 4000

    RELATIVE_OUTPUT_PATHS: bool = True
