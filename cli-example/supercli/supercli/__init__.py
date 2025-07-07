import click

@click.command()
@click.option('--name', '-n', help="The name of the person to say hello to!", required=True)
def supercli(name):
    print("Hello, "+name)