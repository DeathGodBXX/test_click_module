import click


@click.command()
@click.password_option()
def input_passwd(password):
    click.echo('password=%s' % password)


if __name__ == '__main__':
    input_passwd()
