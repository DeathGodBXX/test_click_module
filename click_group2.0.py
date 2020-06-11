import click
# 这种高级用法，就是函数组用法
# python3 test.py
@click.command()
@click.option('--name', help='The person to greet.')
def hello(name):
    click.secho('Hello %s!' % name, fg='red', underline=True)
    click.secho('Hello %s!' % name, fg='yellow', bg='black')


@click.group()
def obiwan():
    pass


if __name__ == '__main__':
    try:
        # python3 test.py hello --help
        # python3 test.py hello --name=4
        obiwan.add_command(hello)
    except Exception as e:
        print(e)