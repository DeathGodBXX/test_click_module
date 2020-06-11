import click


@click.command()
@click.option('--center', nargs=2, type=float, help='the center of the circle')
@click.option('--radius', default=1, type=float, help='the radius of the circle')
def circle(center, radius):
    click.echo('center=%s,radius=%s' % (center, radius))


if __name__ == '__main__':
    circle()
