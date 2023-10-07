from dataclasses import dataclass

from codemonkeys.config.monkey import OStr, Monkey as BaseMonkey


@dataclass
class Monkey(BaseMonkey):

    # General
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    FILE_TYPES_INCLUDED: tuple = ('.py')
    FILEPATH_MATCH_INCLUDE: tuple = ()
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'help', '__', 'defs.py')
    FILE_SELECT_MAX_TOKENS: int = 3000

    # Main Prompts
    MAIN_PROMPT: str = "Please generate code for the following task..."
    MAIN_PROMPT_ULTIMATUM: OStr = "Limit your response to the contents of a python script, and nothing else."
    OUTPUT_EXAMPLE_PROMPT: OStr = "Limit your output to file contents, like: ```<new file contents>```."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = \
        'Examine the following output and determine if it contains the contents of a python script.' \
        ' Respond with only one word: "True" or "False".'
    OUTPUT_TRIES: int = 1

    # Output
    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    OUTPUT_EXT: OStr = None
    OUTPUT_FILENAME_APPEND: OStr = None
    OUTPUT_REMOVE_STRINGS: tuple = ('```python\n', '```python,```')
    SKIP_EXISTING_OUTPUT_FILES: bool = True

    # Editor
    EDITOR_PROMPT: OStr = None
    EDITOR_PROMPT_ULTIMATUM: OStr = None

    # Output Splitting
    OUTPUT_SPLIT_PATH: OStr = None
    OUTPUT_SPLIT_TAG: str = '[SPLIT]'

    # Git
    COMMIT_STYLE: OStr = None
    STATIC_COMMIT_MESSAGE: str = 'File updated with CodeMonkeys.'

    # Models
    MAIN_MODEL: str = 'gpt-4'
    SUMMARY_MODEL: str = 'gpt-4'
    OUTPUT_CHECK_MODEL: str = 'gpt-3.5-turbo'

    # Temps
    MAIN_TEMP: float = 1.0
    SUMMARY_TEMP: float = 1.0
    OUTPUT_CHECK_TEMP: float = 0.7

    # Max Tokens
    MAIN_MAX_TOKENS: int = 5000
    SUMMARY_MAX_TOKENS: int = 5000
    OUTPUT_CHECK_MAX_TOKENS: int = 3000
