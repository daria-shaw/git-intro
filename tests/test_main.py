from git_intro.main import hello_world_msg


def test_hello_world_msg_returns_expected_message() -> None:
    assert hello_world_msg() == "hello world"
