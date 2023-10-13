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
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output strictly to the contents of the file, like this: ```complete contents of file```."

    # Output
    OUTPUT_PATH: str = "ROOT_PATH/stor/output"
    OUTPUT_EXT: str = ".py"
    OUTPUT_FILENAME_APPEND: str = ""
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Output Fixing
    OUTPUT_CHECK_PROMPT: OStr = 'Examine the following output and determine if it contains the contents of a python script. Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: int = 1

    # Models
    MAIN_MODEL: int = 4
    SUMMARY_MODEL: int = 4
    OUTPUT_CHECK_MODEL: int = 3

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    OUTPUT_CHECK_TEMP: float = .5