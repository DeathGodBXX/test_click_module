import click


@click.command()
@click.option('--gender', type=click.Choice(['man', 'woman']), help='the gender of the person')
def person(gender):
    click.echo('gender=%s' % gender)


if __name__ == '__main__':
    person()