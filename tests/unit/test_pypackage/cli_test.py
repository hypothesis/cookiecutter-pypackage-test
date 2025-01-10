from importlib.metadata import version

import pytest

from test_pypackage.cli import cli


def test_it():
    cli([])


def test_help():
    with pytest.raises(SystemExit) as exc_info:
        cli(["--help"])

    assert not exc_info.value.code


def test_version(capsys):
    with pytest.raises(SystemExit) as exc_info:
        cli(["--version"])

    assert capsys.readouterr().out.strip() == version("test-pypackage")
    assert not exc_info.value.code
