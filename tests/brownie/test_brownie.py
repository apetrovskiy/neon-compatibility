import pytest
from src.helpers.common.config import HTTP_URL
from src.helpers.common.constants import CD_BACK, NETWORK_NAME
from src.helpers.shell.processes import run_command_line

CD_BROWNIE = "cd brownie; pwd;"


@pytest.fixture(autouse=True)
def setup_and_teardown():
    aaa = f"{CD_BROWNIE} brownie networks add Development {NETWORK_NAME} host={HTTP_URL} {CD_BACK}"
    print(aaa)
    run_result = run_command_line(
        f"{CD_BROWNIE} brownie networks add Development {NETWORK_NAME} host={HTTP_URL} {CD_BACK}"
    )
    print(run_result)
    yield
    bbb = f"{CD_BROWNIE} brownie networks delete {NETWORK_NAME} {CD_BACK}"
    print(bbb)
    run_result = run_command_line(
        f"{CD_BROWNIE} brownie networks delete {NETWORK_NAME} {CD_BACK}")
    print(run_result)


@pytest.mark.skip(reason="now yet done")
def test_one():
    aaa = f"{CD_BROWNIE} brownie networks add Development {NETWORK_NAME} host={HTTP_URL} {CD_BACK}"
    print(aaa)