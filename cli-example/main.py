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
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("file", type=click.Path(exists=False), required=0)
@click.option(
     "-n",
     "--name",
     prompt="Enter the name of the todo",
     help="Provide the name of the todo")
@click.option(
     "-desc",
     "--description",
     prompt="Enter the description of the todo file",
     help="Enter the description of the todo item" 
)
def add_todo(name, description, priority, todofile):
      filename = todofile if todofile is not None else "mytodos.txt"
      with open(filename, "a+") as f:
            f.write(f"{name}:{description} [Priority: {PRIORITIES[priority]}")


@click.command
@click.argument("idx",type=int, required=1)
def delete_todo(idx):
    with open("mytodos.txt", "r") as f:
          todo_list = f.read().splitlines()
          todo_list.pop(idx)
    
    with open("mytodos.txt", "w") as f:
        f.write("\n".join(todo_list))
        f.write('\n')