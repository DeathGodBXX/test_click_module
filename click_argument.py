import click

# 固定参数
@click.command()
@click.argument('coordinates',nargs=-1,type=float)
@click.argument('radius')
# 不支持写help帮助说明，help='coordinate',也不能指定参数个数，比如nargs=2，但是可以指定不定量参数，例如：nargs=-1，这种好处在于输入多维下的坐标，而不指定维数
def show(coordinates,radius):
    click.echo('coordinates: %s,radius %s'%(coordinates,radius))

if __name__ == '__main__':
    show()