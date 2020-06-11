import click

@click.group()
def apiwin():
    pass

@click.command()
@click.option('--name',help='The person to greet')
def hello(name):
    click.secho('Hello,%s!'%name,fg='red',underline=True)
    click.secho('Hello,%s!'%name,fg='yellow',bg='white')


if __name__ == '__main__':
    try:
        apiwin.add_command(hello)
    except Exception as e:
        print(e)






