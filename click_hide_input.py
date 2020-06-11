import click


@click.command()
@click.option('--password', prompt='please enter the password', hide_input=True, confirmation_promt=True)
def input_passwd(password):
    click.echo('password=%s' % password)


if __name__ == '__main__':
    input_passwd()
