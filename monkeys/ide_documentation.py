from dataclasses import dataclass

from codemonkeys.defs import STOR_PATH

from monkeys.monkey import Monkey, OStr


@dataclass
class IdeDocumentation(Monkey):
    # File Iteration
    WORK_PATH: str = '~/local-git/nousrss'
    INCLUDE_EXTS = ('.py',)
    FILEPATH_MATCH_EXCLUDE: tuple = ('help', '__', 'defs.py', 'commands')
    FILTER_MAX_TOKENS: int = 6000

    # Main Prompts
    MAIN_PROMPT: str = (
        'Your role is to read the contents of python files, and without changing anything else whatsoever, add doc-blocks '
        'providineg concise documentation for IDEs. Rather than altering the file in any other way, return exactly the verbatim '
        'original file with only docstring that help IDEs understand the purpose of the code added. Only add docstring where they '
        'are genuinely useful, rather than adding them just because you can. If there are no docblock additions that are genuinely '
        'helpful, return the original file contents verbatim. Use the provided project context to assist having a full understanding:')
    MAIN_PROMPT_ULTIMATUM: OStr = (
        'Limit your response to the verbatim contents of {the-file}, including all existing code and comments, as well as any new docstring. '
        'Always write docstring in the Google style, notating params/returns in a way IDEs understand. Add nothing else, and remove nothing.')

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the updated file contents for writing."

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = f'{STOR_PATH}/context/nousrss_architecture.txt'
    CONTEXT_SUMMARY_PROMPT: OStr = None

    # Output
    OUTPUT_PATH: str = '~/local-git/nousrss'
    SKIP_EXISTING_OUTPUT_FILES: bool = False
    RELATIVE_OUTPUT_PATHS = True

    GIT_REPO_PATH = '~/local-git/nousrss'
    GPT_GIT_COMMITS = True
