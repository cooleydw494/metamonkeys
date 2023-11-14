# CodeMonkeys

A framework for automating GPT-powered tasks, from simple to complex. Sphinx docs [here](https://cooleydw494.github.io/codemonkeys).

## 🌐 Overview

CodeMonkeys gives devs control over their automated GPT logic. The current focus is working on codebases but it is lovingly designed to enable automations of all kinds. This framework aims to use AI effectively, while being reliable, predictable, and tailored to your needs. There is a strong focus on only involving AI at crucial areas of strength, and using good old-fashioned code for everything else.

### 🚧 Alpha Status

There will soon be a stable Alpha release focused on establishing the framework's architecture/concepts to a point of relative stability, and providing a flexible, immediately useful default Automation that is instructional in how it utilizes the framework.

### 📅 Medium-term Goals
Some concerns have been set aside as I prepare for a stable Alpha release.

The next major focuses are:
- Test Coverage
- More testing on Windows/Linux (Should Work ™️)
- Streamlined fine-tuning support
- More open-ended design
  - framework-level support for non-CLI usage
  - GUI for framework (like Vue CLI UI)
- Expand pre-packaged Automations, Monkeys, Builders
  - focus on function calling support / Funcs
- Improve git workflow, contribution docs/standards
- Improve CLI output, custom Theming, accessibility

## 🎯 One-shot Prompts

CodeMonkeys is designed to utilize one-shot prompts at an atomic level, which an emphasis on breaking down AI-powered tasks into small, manageable pieces. The name comes from the idea that if you break down coding concerns into atomic tasks that even a monkey could do, you can get predictable results that are genuinely useful. This paradigm works well for simple use-cases like translating text, documenting code, writing TODOs, adding type-hints, etc.

Beyond the simpler use cases that inherently benefit from one-shot prompts, the framework helps you to configure more complex one-shot prompts by providing context files, dynamic prompt content, and open-ended custom logic.

Eventually CodeMonkeys will support other modes of prompting, but I strongly believe that boiling down tasks into one-shot prompts that have the necessary context for the goal at hand is currently the most powerful and predictable way to utilize the OpenAI API for coding tasks, especially paired with function calling that can go a long way toward coercing the right output.

# Get Started

## 🚀 Installation

First, install the framework with pip:

```bash
pip install codemonkeys
```

Then, use the `monk-new` command to create a new project:

_Note: CodeMonkeys treats your project as a package, so [project_name] must be in snake_case._

```bash
monk-new [project_name]
```

`cd` into your project and run `monk` or `monk help` to test your installation.

## 📁 Structure

CodeMonkeys' project structure aims to allow you to build/configure/run your automations in a simple, powerful way.
You're encouraged to get creative with your Automation/Command/Barrel `run()` methods, custom config properties, and
utilize any additional modules/classes/dirs you create. However, the base project scaffolding is assumed by the Monk CLI
and built-in config management. Don't fight these paradigms unless you're prepared to replace them.

| Dirs/Modules       | Summary                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------|
| `/commands`        | Command instances, runnable via `monk <command>`. Also handles bash/bat scripts.             |
| `/automations`     | Automation instances, runnable via `monk -a <automation>`.                                   |
| `/barrels`         | Custom or extended Barrel classes used to orchestrate multiple Automation/Monkeys.           |
| `/monkeys`         | Custom or extended Monkey classes used to precisely configure Automation behavior.           |
| `/builders`        | Custom or extended Builder classes for re-usable automation logic.                           |
| `/funcs`           | Custom or extended Func classes for GPT function-calling.                                    |
| `codemonkeys.defs` | A core module that dynamically exposes important PATHs for your project (ex: COMMANDS_PATH). |


# Configuration

## 🐒 Monkeys
Monkeys are your tool for specifying the exact behavior of your Automations. Your prompts, models, temperature, paths, and behavior specifications live here. The class-based approach unlocks advantages like inheritance, custom logic, and lifecycle hooks, but at heart the Monkey class maintains the simplicity of a config file.

You can specify a Monkey when running an Automation using the `--monkey=<name>` CLI arg.

```python
from monkeys.monkey import Monkey
from monkeys.docblock_monkey import DocblockMonkey

# Load a specific Monkey directly
m = DocblockMonkey()

# Load any Monkey dynamically using your base Monkey class
m = Monkey.load(<name>)

# access properties easily
main_prompt = m.MAIN_PROMPT
```

## 📝 Env
The Env class is an interface for accessing properties defined in your `.env`. On every run of the `monk` CLI, type-hinted properties that help avoid mistakes and make your IDE smarter are regenerated. You may customize or ignore your `config/env.py`, but it is used by core framework code, so _don't remove it or edit the generation tags_.

```python
from config.env import Env
env = Env.get()

# access properties easily
openai_api_key = env.OPENAI_API_KEY
```

# Monk CLI 🐵

CodeMonkeys' CLI tool is integral to usage of the framework. The `monk` command can be run anywhere in a CodeMonkeys
project, and will always run in the context of the project root.

## Usage

The Monk CLI primarily is used to run Automations, Barrels, and framework Commands. It also makes your own `commands`
directory readily usable.

`monk` uses recursive name-matching logic to locate runnable entities. This requires unique filenames for each runnable
entity type (Commands, Automations, Barrels).

- 🔷 Entity Type flags target Automations and Barrels.
- 🔷 Action flags perform alternate operations on targetable entities.

## Monk CLI

| Command                | Description            | Note                  |
|------------------------|------------------------|-----------------------|
| `monk help`            | Run this help script   |                       |
| `monk list`            | List existing entities | `-b/a/m`, `--all`     |
| `monk -v`              | Print version          | `--version`           |
| `monk <command>`       | Run a command          | default action/entity |
| `monk -a <automation>` | Run an automation      | `--automation`        |
| `monk -b <barrel>`     | Run a barrel           | `--barrel`            |
| `monk -e <entity>`     | Open in vim            | `--edit`              |
| `monk -h <entity>`     | Help for an entity     | `--help`              |

✅ That's it! For more, run `monk -h <entity>` or read the docs.

# 📜 Commands

CodeMonkeys is heavily CLI-oriented, and Commands are a core concept. There are basic framework Commands, like `monk list --all`, which will list all the _entities_ you have in your project, and you can easily create open-ended custom Commands.

## ⌨️ CliRunnable
The `Command` class, as well as the other _entities_, are a subclass of `CliRunnable`.

The `CliRunnable` class is a base class that provides a common interface "cli-runnable" _entities_. It includes a required `run()` method which is called when the _entity_ is run from the CLI.

Beyond that, `CliRunnable` handles CLI arguments. CLI args parsed by `argparse` are passed into the constructor, and class variables are used to configure how the args are handled.

These class variables can be overridden in subclasses (such as a custom `Command`):

```python
named_arg_keys: list = []
unnamed_arg_keys: list = []
required_arg_keys: list = []
```

#### named_arg_keys
`named_arg_keys` is a list of the named arg names that are expected to be passed to the CLI command. You must define a named arg for it to be handled correctly. Named arg keys must be passed with a leading `--` (ex: `--all`), but should be defined without the `--`. If a named arg is passed without a value, it will be set to `True`.

#### unnamed_arg_keys
`unnamed_arg_keys` is a list of the unnamed arg names that are expected to be passed to the CLI command. You must define an unnamed arg for it to be handled correctly.

#### required_arg_keys
`required_arg_keys` is a list of the args that are required to be passed to the CLI command. Required args must also be defined in either `named_args` or `unnamed_args`. Any required args that are not passed will result in an error.

In addition to this, you must define the args as variables on the subclass. For example, if you have a `named_arg_keys` of `['foo']`, you must define a `foo` variable on the subclass. If you typehint the variable, the CLI arg will be cast to that type.

## Example Command

The following is the Example Command that is used for generating new user Commands by running `monk make command <name>`.

```python
from codemonkeys.entities.command import Command
from codemonkeys.types import OStr, OBool, OInt


class ExampleCommand(Command):
    
    required_arg_keys = ['named_arg_one']
    
    # Specify named args
    named_arg_keys = ['named_arg_one', 'named_arg_two']

    # Specify unnamed args (in passing order)
    unnamed_arg_keys = ['unnamed_arg_one']

    # Define and set defaults for all args (incl required)
    # Setting type-hints will provide validation in CliRunnable base class.
    named_arg_one: OStr = None
    named_arg_two: OBool = True
    unnamed_arg_one: str = 'default_value'
    unnamed_arg_two: OInt = None

    def run(self) -> None:
        """
        Execute your Command logic here, utilizing args as needed.
        """
        print(f"named_arg_one: {self.named_arg_one}")
```

# Automations

## Run an Automation 

Automations are CliRunnable with the `-a` *action flag*. In the following example, the Default automation in `automation/default.py`  is invoked (and the Docblocks Monkey from `monkeys/docblocks.py` is invoked).
    
```bash
monk -a default --monkey=docblocks
```

## The Default Automation

The default automation, `automations/default.py`, is a generic but complete template for running automations on files in your `WORK_PATH`. Out-of-the-box, it allows you to run GPT-powered mass file operations simply by configuring Monkeys. The default Automation is also an instructive example of using the framework, as it includes configurable implementations of all stock Monkey properties.

## Creating a New Automation

To generate a scaffolded Automation, use the `monk make` framework command:

```bash
monk make automation my_automation
```

This will generate the class `MyAutomation(Automation)` in `automations/my_automation.py`, which can be run with `monk -a my_automation`.


# Barrels

Barrels in CodeMonkeys are a way to orchestrate multiple Automations/Monkeys into a single CliRunnable. 

## Run a Barrel

Barrels are CliRunnable with the `-b` *action flag*. In the following example, the ScaffoldPlus barrel in `barrels/scaffold_plus.py`  is invoked.
    
```bash
monk -b scaffold_plus
```

## Creating a New Barrel

To generate a scaffolded Barrel, use the `monk make` framework command:

```bash
monk make barrel my_barrel
```

This will generate the class `MyBarrel(Barrel)` in `barrels/my_barrel.py`, which can be run with `monk -b my_barrel`. 

# Monkeys Advanced

A deep dive into the more advanced aspects of Monkeys.

## 🍹 Mixins

Mixins are a way to extend the functionality of a Monkey without having to create a new class. They are a great way to share functionality between Monkeys, and to keep your code DRY.

For example, you could use a Mixin to add a set of Monkey Prop values that always apply for a particular WORK_PATH / project.

```python
class MyProjectWorkspace:

    # File Iteration
    WORK_PATH: str = "~/my_project"
    INCLUDE_EXTS: tuple = ('.py', '.js')
    FILEPATH_MATCH_EXCLUDE: tuple = ('.git', '__')
    FILTER_MAX_TOKENS: int = 8000

    # Output
    OUTPUT_PATH: str = "~/my_project"
    SKIP_EXISTING_OUTPUT_FILES: bool = False

    # Git
    GPT_GIT_COMMITS: bool = False
    GIT_REPO_PATH: str = "~/my_project"
```

Then, you can use this Mixin in any Monkey that needs to use these props:

```python
from monkeys.monkey import Monkey
from mixins.MyProjectWorkspace import MyProjectWorkspace

class IdeDocumentation(Monkey):

    mixins = (
        MyProjectWorkspace,
    )

    # Overrides the Mixin's INCLUDE_EXTS
    INCLUDE_EXTS: tuple = ('.py',)
```

### Mixin Property Precedence

First things first:

**Mixins override parent class properties, but class properties defined in the instantiated Monkey override Mixins.**

When a Monkey uses multiple Mixins, the properties of the last Mixin in the `mixins` tuple will take precedence over the properties of the previous Mixins.

For example, if the first Mixin in the tuple sets `INCLUDE_EXTS = ('.py',)` and a second Mixin defined in the tuple that sets `INCLUDE_EXTS = ('.js')`, then the final value of `INCLUDE_EXTS` will be `('.js',)`.

Mixins defined in the instantiated Monkey will overwrite the inherited `mixins` class property. When you override the `mixins` class property, you should include any and all Mixins you want to apply.

# Funcs

## Function Calling

Function calling is a GPT feature that allows you to call a function from within your prompt. This is useful because it means you can write a prompt and have the `GptClient` execute a function in response.

## The Func Class

Funcs are a CodeMonkeys feature that allows you to define simple subclasses that obfuscate a bit of the boilerplate involved in function calling. They also allow you to define an `_execute()` method that will be called when the function is executed.

## Func Strategies

There are different ways you can strategically utilize Funcs in your Automations (or even Commands). The most common ways I've used them are:

### Simple Execution

This is the most common use case. You define a Func that calls a function in your Automation, and then you call that Func from your prompt. This is useful for when you want to execute a function in your Automation that doesn't require any arguments.

### Coercing GPT Output

This is a more creative and very useful strategy I've used quite a bit. Instead of using Funcs to perform programmatic tasks, you can simple use them to imply a more specific attitude toward your prompt. For instance, the FinalizeOutput Func (included in the codemonkeys package).

Rather than try to accomplish something specific, this Func simply forces GPT to think about its response in more concrete terms. I've tried a million times to engineer prompts that prevent GPT from returning additional context or fluff, but its hit or miss. With FinalizeOutput, I've found the success rate to be extremely high.

```python
from codemonkeys.entities.func import Func


class FinalizeOutput(Func):

    """
    This Func is intended to be used in the default automation to finalize output for file writing.
    It is a very vague function that coerces GPT into intuiting the desired output and omitting extraneous text.
    As long as prompts include language that allow GPT to intuit the use-case properly, it can be used in other ways.
    """

    name: str = 'finalize_output'

    _description: str = 'This function is a handler for finalized output for various uses.'

    _parameters: dict = {
        "type": "object",
        "properties": {
            "output": {
                "type": "string",
                "description": "Finalized output requiring no further processing to be used as intended.",
            },
        },
        "required": ["output"],
    }

    @classmethod
    def _execute(cls, output: str) -> str:
        return output
```

### Response Transformation

This is a more advanced strategy that I've used to great effect. It involves using a Func to transform the response from GPT into something more useful, or more in line with your expected formatting.

This can mean writing Python code to transform the output in any way, and/or using the function description/parameters to coerce GPT into producing more specifically formatted output to begin with.