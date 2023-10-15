from dataclasses import dataclass

from monkeys.self_help import SelfHelp


@dataclass
class FinishFiles(SelfHelp):

    # File Iteration
    INCLUDE_EXTS: str = ".py"
    FILEPATH_MATCH_EXCLUDE: tuple = ('help.py', '__init__.py')

    # Main Prompts
    MAIN_PROMPT: str = \
        'Read the contents of {the-file} and write a fully implemented version of whatever is described.'

    MAIN_PROMPT_ULTIMATUM: OStr = \
        'Return only the contents of a script/module that meets the requirements of the description existing within {the-file}.'

    OUTPUT_PROMPT: str = "Output should be nothing more than the updated file contents."
    
    # Output Fixing
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script/module only. Respond with only one word: "True" or "False".'

    OUTPUT_TRIES: int = 2

    # Output
    OUTPUT_EXT: str = ''
    OUTPUT_FILENAME_APPEND: str = ''
    SKIP_EXISTING_OUTPUT_FILES: bool = False

    # Models
    MAIN_MODEL: int = 4
    OUTPUT_CHECK_MODEL: int = 3
    
    # Temps
    MAIN_TEMP: float = 1.0
    OUTPUT_CHECK_TEMP: float = .5