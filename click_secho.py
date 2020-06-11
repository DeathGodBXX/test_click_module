import click


@click.command()
@click.option('--name', default='Nancy', help='the name to greet')
def hello(name):
    click.secho('Hello %s!' % name, fg='green',bg='black',underline=True,bold=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')


if __name__ == '__main__':
    hello()
