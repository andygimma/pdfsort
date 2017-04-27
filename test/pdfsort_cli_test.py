import click
from click.testing import CliRunner
from pdfsort_cli.pdfsort_cli import cli

def test_greet():
    runner = CliRunner()
    result = runner.invoke(cli)
    assert result.output == 'Hello World!\n'

if __name__ == '__main__':
    test_greet()
