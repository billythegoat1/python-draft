import click


@click.command()
@click.option("--name", prompt="Enter your name", help="The name of the user")
def hello(name):
    click.echo(f"Hello {name}!")


PRIORITIES = {
    "o": "Optional",
    "l": "Low",
    "h": "High",
    "m": "Medium",
    "c": "crucial"
}
@click.command
@click.argument("priority", type=click.Choice())
def add_todo(name, description, priority, todofile):
if __name__ == "__main__":
    hello()