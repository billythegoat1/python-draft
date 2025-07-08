import click

@click.command()
@click.option('--name', '-n', help="The name of the person to say hello to!", required=True, prompt="Your name, please ? ")
@click.argument('number')
def supercli(name, number):
    for _ in range((int(number))):
        print("A super important text for "+name+":\n\n\tYou have been a "
        "great person to talk with ...")