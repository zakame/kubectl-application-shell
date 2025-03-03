"""Testing .cli"""

import os

from typer.testing import CliRunner

from kubectl_application_shell.cli import app

runner = CliRunner()


def test_cli_bare():
    """Test the CLI with no arguments."""
    result = runner.invoke(app, [])
    assert result.exit_code == 2
    assert "Missing argument 'NAMESPACE'." in result.stdout


def test_cli_standard():
    """Test the CLI with standard simple invocation."""
    result = runner.invoke(app, ["kube-system", "coredns"])
    assert result.exit_code == 0
    assert "Starting" in result.stdout
    assert "coredns" in result.stdout
    assert "kube-system" in result.stdout
    assert "Please relax" in result.stdout
    assert "cluster version" in result.stdout


def test_cli_run(mocker):
    """Test the CLI with the --run flag."""
    mocker.patch("os.system")
    result = runner.invoke(app, ["kube-system", "coredns", "--run"])
    assert result.exit_code == 0
    assert "Starting" in result.stdout
    assert "coredns" in result.stdout
    assert "kube-system" in result.stdout
    assert "Please relax" in result.stdout
    assert "cluster version" in result.stdout
    assert "Running" in result.stdout
    os.system.assert_called_once()  # pylint: disable=no-member


def test_cli_run_with_image(mocker):
    """Test the CLI with the --run flag and image."""
    mocker.patch("os.system")
    result = runner.invoke(
        app,
        ["kube-system", "coredns", "--run", "--image", "busybox"],
    )
    assert result.exit_code == 0
    assert "Starting" in result.stdout
    assert "coredns" in result.stdout
    assert "kube-system" in result.stdout
    assert "Please relax" in result.stdout
    assert "cluster version" in result.stdout
    assert "Running" in result.stdout
    os.system.assert_called_once()  # pylint: disable=no-member


def test_cli_run_with_command_args(mocker):
    """Test the CLI with the --run flag and command/args."""
    mocker.patch("os.system")
    result = runner.invoke(
        app,
        [
            "kube-system",
            "coredns",
            "--run",
            "--image",
            "busybox",
            "--",
            "date",
            "'@2147483647",
        ],
    )
    assert result.exit_code == 0
    assert "Starting" in result.stdout
    assert "coredns" in result.stdout
    assert "kube-system" in result.stdout
    assert "Please relax" in result.stdout
    assert "cluster version" in result.stdout
    assert "Running" in result.stdout
    os.system.assert_called_once()  # pylint: disable=no-member
