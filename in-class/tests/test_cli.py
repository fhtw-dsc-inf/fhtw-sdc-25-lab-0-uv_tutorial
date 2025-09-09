from mini_uv_project.cli import main


def test_main_runs(capsys):
    assert main() == 0
    captured = capsys.readouterr()
    assert "Hello, world!" in captured.out
