class ExampleWorkspace:

    # File Iteration
    WORK_PATH: str = "~/local-git/example"
    FILEPATH_MATCH_EXCLUDE: tuple = ('.config', '.md', '.git', 'help/', '__',
                                     'scripts/', 'imports/', 'commands/', 'config/', 'examples/', 'defaults/', 'funcs/',
                                     '/monkeys/')
    FILEPATH_MATCH_INCLUDE: tuple = ()  # empty === all
    INCLUDE_EXTS: tuple = ('.py',)

    # Output
    OUTPUT_PATH: str = "~/local-git/example"
    SKIP_EXISTING_OUTPUT_FILES: bool = False
    RELATIVE_OUTPUT_PATHS = True
