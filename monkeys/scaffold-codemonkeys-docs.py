from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from monkeys.monkey import Monkey
from monkeys.scaffold import Scaffold


@dataclass
class ScaffoldCodemonkeysDocs(Scaffold):

    # Context / Summary
    CONTEXT_FILE_PATH: str = f"{STOR_PATH}/context/scaffold/codemonkeys-docs.txt"

    # Project Root Dir
    PROJECT_ROOT: str = '~/local-git/codemonkeys-docs'

    # Filepath Extraction
    FILE_EXTRACTION_PROMPT: str = ("Review the following architectural documentation for a codebase and extract a list "
                                   "of all the filepaths that need to be created to scaffold it. Always use absolute "
                                   f"paths, with the project root dir {PROJECT_ROOT} included.")
