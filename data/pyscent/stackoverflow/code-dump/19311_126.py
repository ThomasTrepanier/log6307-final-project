import click

@click.group()
def cli():
    pass

@cli.command()
def a():
   print("I am a")

@cli.command()
def b():
   print("Je suis b")

if __name__ == '__main__':
    cli()
