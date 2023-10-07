from dataclasses import dataclass

from config.monkeys.monkey import Monkey, OStr


@dataclass
class IDEDocumentation(Monkey):
    # General
    WORK_PATH: str = '~/local-git/codemonkeys/codemonkeys/commands'
    FILEPATH_MATCH_EXCLUDE: tuple = ('help', '__', 'defs.py', 'commands')
    FILE_SELECT_MAX_TOKENS: int = 6000

    # Main Prompts
    MAIN_PROMPT: str = (
        'Your role is to read the contents of python files, and without changing anything else whatsoever, add doc-blocks '
        'providineg concise documentation for IDEs. Rather than altering the file in any other way, return exactly the verbatim '
        'original file with only docstring that help IDEs understand the purpose of the code added. Only add docstring where they '
        'are genuinely useful, rather than adding them just because you can. If there are no docblock additions that are genuinely '
        'helpful, return the original file contents verbatim.')
    MAIN_PROMPT_ULTIMATUM: OStr = (
        'Limit your response to the verbatim contents of {the-file}, including all existing code and comments, as well as any new docstring. '
        'Always write docstring in the Google style, notating params/returns in a way IDEs understand. Add nothing else, and remove nothing.')

    OUTPUT_EXAMPLE_PROMPT: OStr = 'Output should be in the following format with no additional context: [file-contents]'

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output Checks
    OUTPUT_CHECK_PROMPT: OStr = None
    OUTPUT_TRIES: int = 1

    # Output
    OUTPUT_PATH: str = '~/local-git/codemonkeys/codemonkeys/help/commands'
    SKIP_EXISTING_OUTPUT_FILES: bool = True