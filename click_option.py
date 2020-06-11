import click


@click.command()
@click.option('--count', default=1, help='the count of greetings')
@click.option('--name', prompt='Your name', help='the name of greetings')
def greeting(count, name):
    for i in range(count):
        click.echo('Hello,%s' % name)
        # click.echo('Hello,', name)  # 报错,查看echo代码，这是因为把name当成文件使用了
        # print('Hello,', name)
        # print('Hello,%s' % name)


if __name__ == '__main__':
    greeting()

