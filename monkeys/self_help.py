from dataclasses import dataclass

from mixins.codemonkeys_workspace import CodemonkeysWorkspace
from monkeys.monkey import OStr, Monkey


@dataclass
class SelfHelp(Monkey):

    mixins = (
        CodemonkeysWorkspace,
    )

    # File Iteration
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys/commands"
    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys/help/commands"
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', '__', 'defs.py')

    # Main Prompts
    MAIN_PROMPT: str = \
        ('Write a python script that prints an appealing summary of {the-file} and its usage via `monk {the-file}`, '
         'in the style of documentation for a CLI command. Rather than writing a script using similar functionality '
         'as {the-file}, use the provided monk command context and print_t function to generate a script that prints '
         'a help summary for {the-file}. When referring to {the-file} as a command, do not include the extension.')

    MAIN_PROMPT_ULTIMATUM: OStr = \
        'Return only the contents of a script that prints a helpful summary and usage explanation of {the-file}.'

    OUTPUT_PROMPT: OStr = \
        ("Make your output similar to the following, but with as much detail and creativity as necessary to explain "
         "the command: ```{cop:~/local-git/metamonkeys/stor/context/self-help-context-file.py}```.")

    # Context / Summary
    CONTEXT_FILE_PATH: OStr = None
    CONTEXT_SUMMARY_PROMPT: OStr = None

    SKIP_EXISTING_OUTPUT_FILES: bool = True
