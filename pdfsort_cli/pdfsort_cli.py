import click
import time
import PyPDF2
import os
#
# @click.group(invoke_without_command=False)
# @click.pass_context
# def cli(ctx):
#     print "hello"
#     pass

@click.command()
def cli():
    """Example script."""
    click.echo('Hello World!')

if __name__ == '__main__':
    cli()
