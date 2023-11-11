class XPosterWorkspace:

    # File Iteration
    WORK_PATH: str = "~/local-git/x_poster"
    FILEPATH_MATCH_EXCLUDE: tuple = ('help', '__')
    FILEPATH_MATCH_INCLUDE: tuple = ()  # empty === all
    INCLUDE_EXTS: tuple = ()  # empty === all

    # Output
    OUTPUT_PATH: str = "~/local-git/x_poster"
    SKIP_EXISTING_OUTPUT_FILES: bool = True
    RELATIVE_OUTPUT_PATHS = True

    # Git
    GIT_REPO_PATH = '~/local-git/x_poster'
    GPT_GIT_COMMITS = False
