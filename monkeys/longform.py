from dataclasses import dataclass

from monkeys.monkey import OStr, Monkey


@dataclass
class LongForm(Monkey):

    # File Iteration
    WORK_PATH: str = "ROOT_PATH/stor/work_path"
    INCLUDE_EXTS: str = ".js,.vue,.php"
    FILEPATH_MATCH_EXCLUDE: str = ".config,.md,.git,migrations,vite,webpack,.txt"
    FILTER_MAX_TOKENS: int = 3000
    #  CONTEXT_FILE_PATH: OStr = "help.py"

    # Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    CONTEXT_SUMMARY_PROMPT: str = "Provide a summary of this file..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the full contents of a python script, and nothing else."
    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents."

    # Output
    OUTPUT_PATH: str = "ROOT_PATH/stor/output"
    OUTPUT_EXT: str = ".py"
    OUTPUT_FILENAME_APPEND: str = ""
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Models
    MAIN_MODEL: int = 4
    SUMMARY_MODEL: int = 4

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
