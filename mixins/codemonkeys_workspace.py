class CodemonkeysWorkspace:

    # File Iteration
    WORK_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'help', '__', 'committer', 'output_resolver', 'summarizer')
    FILEPATH_MATCH_INCLUDE: tuple = ()  # empty === all
    INCLUDE_EXTS: tuple = ('.py',)

    # Output
    OUTPUT_PATH: str = "~/local-git/codemonkeys/codemonkeys"
    SKIP_EXISTING_OUTPUT_FILES: bool = False
    RELATIVE_OUTPUT_PATHS = True

    # Git
    GIT_REPO_PATH = '~/local-git/codemonkeys/codemonkeys'
    GPT_GIT_COMMITS = False
