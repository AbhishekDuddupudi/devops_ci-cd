from app import run_app

def test_run_app():
    result = run_app()
    assert result == "App Running Successfully!"
