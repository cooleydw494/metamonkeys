from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from mixins.x_poster_workspace import XPosterWorkspace
from monkeys.monkey import Monkey


@dataclass
class Scaffold(Monkey):

    mixins = (
        XPosterWorkspace,
    )

    # Filepath Extraction
    FILE_SELECT_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                                   "of all the filepaths that need to be created to scaffold it. Always use absolute "
                                   f"paths, with the project root dir {XPosterWorkspace.WORK_PATH} included.")

    # Main Prompts
    MAIN_PROMPT: str = ("Review the following architectural documentation for a codebase, and write the best "
                        "implementation of the specified file as possible, with close attention to other usable "
                        "elements declared in the architecture overview (classes, functions, etc).")

    MAIN_PROMPT_ULTIMATUM: str = ("Take your time carefully considering architecture information and how it affects "
                                  "implementation of each file, ensuring among other things, that naming and imports "
                                  "are correct.")

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold/x_poster.txt"

    MAIN_MAX_TOKENS = 4000
    SUMMARY_MAX_TOKENS = 4000
    FILE_SELECT_MAX_TOKENS = 4000
    FILTER_MAX_TOKENS = 4000
