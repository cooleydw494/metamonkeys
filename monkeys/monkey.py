from dataclasses import dataclass

from codemonkeys.entities.monkey import Monkey as Base
from codemonkeys.types import OStr


@dataclass
class Monkey(Base):

    # File Iteration
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    INCLUDE_EXTS: tuple = ('.py')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'help', '__', 'defs.py')
    FILTER_MAX_TOKENS: int = 3000

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    OUTPUT_EXT: OStr = None
    OUTPUT_FILENAME_APPEND: OStr = None
    SKIP_EXISTING_OUTPUT_FILES: bool = False

    # Editor
    EDITOR_PROMPT: OStr = None
    EDITOR_PROMPT_ULTIMATUM: OStr = None

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: OStr = None

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0

    # Max Tokens
    MAIN_MAX_TOKENS: int = 5000
    SUMMARY_MAX_TOKENS: int = 5000
