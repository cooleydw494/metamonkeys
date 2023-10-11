import os

from codemonkeys.defs import content_sep, nl, nl2
from codemonkeys.funcs.write_files import WriteFiles
from codemonkeys.utils.gpt.gpt_client import GPTClient
from pandas.io.common import file_exists

from codemonkeys.builders.committer import Committer
from codemonkeys.entities.automation import Automation
from codemonkeys.utils.file_ops import get_file_contents
from codemonkeys.utils.monk.theme_functions import print_t

from codemonkeys.funcs.extract_list import ExtractList
from monkeys.scaffold import Scaffold as ScaffoldMonkey


class Scaffold(Automation):

    def run(self) -> None:
        m: ScaffoldMonkey = self._monkey

        # Fetch the context (should be a file detailing a codebase)
        context = get_file_contents(m.CONTEXT_FILE_PATH)

        extract_prompt = f"{m.FILE_EXTRACTION_PROMPT}:{nl}{content_sep}{nl}{context}{nl}{content_sep}"
        print_t(f"Filepath extraction prompt:{nl}{extract_prompt}{nl}", "quiet")

        # Use ExtractList Func to get a list of absolute filepaths that the context file references
        file_paths: list = (GPTClient(m.FILE_EXTRACTION_MODEL, m.FILE_EXTRACTION_TEMP, m.FILE_EXTRACTION_MAX_TOKENS)
                            .generate(extract_prompt, [ExtractList()], 'extract_list'))

        if len(file_paths) == 0:
            print_t("No filepaths were extracted. Exiting.", 'error')
            return

        print_t(f"Extracted {len(file_paths)} filepaths: {file_paths}", 'info')

        # If enabled, build a Committer for GPT Git Commits
        committer = None
        if m.GPT_GIT_COMMITS:
            committer = (Committer(repo_path=m.OUTPUT_PATH)
                         .model('gpt-3.5-turbo', 0.7, 2000))

        # Iterate through filepaths and generate scaffolded files
        while True:

            files_remaining = len(file_paths)
            print_t(f"Filepaths remaining: {files_remaining}", 'info')

            if files_remaining == 0:
                print_t("All Filepaths Handled.", 'done')
                break
            file_path = file_paths.pop()
            file_path = os.path.expanduser(file_path)

            if m.SKIP_EXISTING_OUTPUT_FILES and file_exists(file_path):
                print_t(f"Skipping file, output exists at: {file_path}", 'quiet')
                continue

            print(f"Processing filepath: {file_path}")
            old_content = get_file_contents(file_path) if file_exists(file_path) else ''

            scaffold_prompt = (f"{m.MAIN_PROMPT}:{content_sep}{nl}{context}{content_sep}{nl2}The current file to "
                               f"implement/write is {file_path} (use this to determine absolute paths / root path).")
            print_t(f"Scaffolding prompt:{nl}{scaffold_prompt}{nl}", "quiet")

            written_file_paths = (GPTClient(m.MAIN_MODEL, m.MAIN_TEMP, m.MAIN_MAX_TOKENS)
                                  .generate(scaffold_prompt, [WriteFiles()], 'write_files'))

            if len(written_file_paths) == 0:
                print_t(f" No written filepaths were returned, seeming to indicate a file was not written. Skipping "
                        f"file: {file_path}", 'warning')
                continue

            if file_path not in written_file_paths:
                print_t(f" The current file to implement/write was not written: {file_path}.", 'warning')

            if file_path not in written_file_paths or len(written_file_paths) > 1:
                print_t(f"Multiple files were written: {written_file_paths}", 'info')
                continue

            new_content = get_file_contents(file_path) if file_exists(file_path) else ''

            # Commit changes if a Committer was configured
            if committer is not None:
                if file_path not in written_file_paths:
                    committer.message('Updated via CodeMonkeys with unexpected written files.')
                elif new_content != '':
                    committer.message_from_context(old_content, new_content).commit()
