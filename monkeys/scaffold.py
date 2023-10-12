from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from monkeys.monkey import Monkey


@dataclass
class Scaffold(Monkey):

    # Main Prompts
    MAIN_PROMPT: str = ("Review the following architectural documentation for a codebase, and write the best "
                        "implementation of the specified file as possible, with close attention to other usable"
                        " elements declared in the architecture overview (classes, functions, etc).")

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold.txt"

    # Filepath Extraction
    FILE_EXTRACTION_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                                   "of all the filepaths that need to be created to scaffold it. Use absolute paths, "
                                   "with the project root dir located within ~/local-git.")

    # Output
    SKIP_EXISTING_OUTPUT_FILES = True
    ALLOW_MULTIPLE_FILES_PER_PROMPT = False

    # Git
    GPT_GIT_COMMITS: bool = False

    # Models
    MAIN_MODEL: str = 'gpt-4'
    FILE_EXTRACTION_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    FILE_EXTRACTION_TEMP: float = 0.8

    # Max Tokens
    MAIN_MAX_TOKENS: int = 6000
    FILE_EXTRACTION_MAX_TOKENS: int = 3000
