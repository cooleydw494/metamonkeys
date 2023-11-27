from dataclasses import dataclass

from mixins.codemonkeys_workspace import CodemonkeysWorkspace
from monkeys.monkey import OStr, Monkey


@dataclass
class TestWriter(Monkey):

    mixins = (
        CodemonkeysWorkspace
    )

    # Main Prompts
    MAIN_PROMPT: str = \
        ('Your role is to read the contents of python files, examine the provided testing notes, conftest.py file, '
         'and project summary, and write a full set of tests (pytest) based on {the-file}. Try to adhere to the '
         'testing notes: \n\n {cop:~/local-git/metamonkeys/stor/context/testing-notes.md}\n\nas well as the existing '
         'conftest.py: \n\n {cop:~/local-git/metamonkeys/conftest.py}\n\n')

    MAIN_PROMPT_ULTIMATUM: OStr = \
        ('Limit your response to the verbatim contents of {the-file}, including all existing code and comments, '
         'as well as any docstring alterations to comply with the reST style. Add nothing else, and remove nothing.')

    OUTPUT_PROMPT: OStr = "Output should be nothing more than the test file contents."

    OUTPUT_FILENAME_PREPEND = 'test_'

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = '~/local-git/metamonkeys/stor/context/codemonkeys-docs.md'
    CONTEXT_SUMMARY_PROMPT: OStr = \
        ('Summarize the CodeMonkeys Docs so that an AI reading the summary understands the greater context of the '
         'project. Rather than be overly specific, try to give info that connects the dots for an AI viewing a '
         'specific file.')
