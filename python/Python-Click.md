## Common options
- [StackOverflow Click options](https://stackoverflow.com/questions/52144383/how-to-add-common-options-to-sub-commands-which-can-go-after-the-name-of-the-s)
```python
import click
from functools import wraps

@click.group()
def cli():
    pass

def common_options(f):
    @wraps(f)
    @click.option('--option1', '-op1', help='Option 1 help text', type=click.FLOAT)
    @click.option('--option2', '-op2', help='Option 2 help text', type=click.FLOAT)
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs)

    return wrapper

@cli.group(invoke_without_command=True)
@common_options
@click.pass_context
def parent(ctx, option1, option2):
    ctx.ensure_object(dict)
    if ctx.invoked_subcommand is None:
         click.secho('Parent group is invoked. Perform specific tasks to do!', fg='bright_green')

@parent.command()
@click.option('--sub_option1', '-sop1', help='Sub option 1 help text', type=click.FLOAT)
@common_options
def sub_command1(option1, option2, sub_option1):
    click.secho('Perform sub command 1 operations', fg='bright_green')

@parent.command()
@click.option('--sub_option2', '-sop2', help='Sub option 2 help text', type=click.FLOAT)
@common_options
def sub_command2(option1, option2, sub_option2):
    click.secho('Perform sub command 2 operations', fg='bright_green')

if __name__ == "__main__":
    cli()

```