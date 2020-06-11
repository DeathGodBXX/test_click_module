import click


def print_version(ctx, param, value):
    click.echo(ctx)
    # <click.core.Context object at 0x00000193767C60F0>，里面有resilient_parsing参数，如果True,Click将解析而不进行任何交互或回调调用。
    click.echo(param)  # <Option version>
    click.echo(value)  # 判断是否输入了--version
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 1.0')
    ctx.exit()


@click.command()
@click.option('--version', callback=print_version,  is_flag=True, expose_value=False, is_eager=True)
@click.option('--name', default='Ethan', help='name')
def hello(name):
    click.echo('Hello %s!' % name)


if __name__ == '__main__':
    hello()
