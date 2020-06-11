import click


def print_hello(context,parma,value):
    if not value or context.resilient_parsing:
        return
    click.echo('hello,everyone')
    context.exit()
# context是click.core.Context对象，内部有resilient_parsing参数，默认是False。if True,Click将解析而不进行任何交互或回调调用。
# param为<option --version>，命令行参数
# value 判断命令行是否输入了--version。若输入，为True。

@click.command()
@click.option('--version', callback=print_hello, is_flag=True, expose_value=False, is_eager=True)  # 这三个bool是一体的。
@click.option('--name', default='Helen', help='name')
def hello(name):
    click.echo('hello,%s' % name)

# is_flag 标识命令行参数--version
# is_eager=True 表明该命令行选项优先级高于其他选项；
# expose_value=False 表示如果没有输入该命令行选项，会执行既定的命令行流程；
# callback 指定了输入该命令行选项时，要跳转执行的函数；
if __name__ == '__main__':
    hello()
