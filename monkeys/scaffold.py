from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from monkeys.monkey import Monkey

@dataclass
class Scaffold(Monkey):

    # Main Prompts
    MAIN_PROMPT: str = ("Review the following architectural documentation for a codebase, and write the best "
                        "implementation of the specified file as possible, with close attention to other usable"
                        " elements declared in the architecture overview (classes, functions, etc).")

    MAIN_PROMPT_ULTIMATUM: str = ("Take your time carefully considering architecture information and how it affects"
                                  " implementation of each file, ensuring among other things, that naming and imports"
                                  " are correct.")

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold/twitter_poster.txt"

    # Project Root Dir
    PROJECT_ROOT: str = '~/local-git/twitter_poster'

    # Filepath Extraction
    FILE_EXTRACTION_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                                   "of all the filepaths that need to be created to scaffold it. Always use absolute "
                                   f"paths, with the project root dir {PROJECT_ROOT} included.")

    # Output
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Git
    GPT_GIT_COMMITS: bool = True
    GIT_REPO_PATH: str = PROJECT_ROOT

    # Models
    MAIN_MODEL: str = 'gpt-4'
    FILE_EXTRACTION_MODEL: str = 'gpt-4'

    # Temps
    MAIN_TEMP: float = 1.0
    FILE_EXTRACTION_TEMP: float = 0.8

    # Max Tokens
    MAIN_MAX_TOKENS: int = 6000
    FILE_EXTRACTION_MAX_TOKENS: int = 3000
