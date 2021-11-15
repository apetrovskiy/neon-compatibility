import allure
import pytest
import os
from src.helpers.common.config import CD_BACK
from src.helpers.common.constants import NETWORK_NAME, RunCommand, Subfolder
from src.helpers.common.error_message import TruffleError, TruffleBasedError
from src.helpers.shell.file_system import clean_up_folder
from src.helpers.shell.processes import preset_variables, run_command_line

BUILT_CONTRACTS_PATH = "/Metacoin/build/contracts"
FEATURE = "Truffle"


@pytest.fixture(autouse=True)
def prepare_truffle_config():
    preset_variables()
    print(os.path.abspath(os.getcwd()) + BUILT_CONTRACTS_PATH)
    clean_up_folder(os.path.abspath(os.getcwd()) + BUILT_CONTRACTS_PATH)
    yield


@allure.feature(FEATURE)
def test_truffle_migration():
    # truffle migrate --network neonlabs
    actual_result = run_command_line(
        f"{Subfolder.CD_METACOIN} {RunCommand.TRUFFLE} " +
        f"migrate --network {NETWORK_NAME} {CD_BACK}")
    assert TruffleBasedError.ERROR_NO_ATTRIBUTE_ETH_ACCOUNTS \
        not in actual_result
    assert TruffleError.ERROR_COULD_NOT_CONNECT not in actual_result
    assert TruffleError.ERROR_NOT_AUTHORIZED not in actual_result
    assert TruffleError.ERROR_TIMEOUT not in actual_result
    assert TruffleError.ERROR_CANNOT_READ_PROPERTIES not in actual_result
    assert TruffleError.ERROR_DEPLOYMENT_FAILED not in actual_result
    assert TruffleError.ERROR_BLOCK_NOT_AVAILABLE not in actual_result
    assert TruffleError.ERROR_SOCKET_TIMEOUT not in actual_result
    print(actual_result)


@allure.feature(FEATURE)
def test_truffle_contract():
    # truffle neonlabs ./test/TestMetaCoin.sol
    actual_result = run_command_line(
        f"{Subfolder.CD_METACOIN} {RunCommand.TRUFFLE} --network \
            {NETWORK_NAME} test ./test/TestMetaCoin.sol {CD_BACK}")
    assert TruffleError.ERROR_CONTRACTS_NOT_DEPLOYED not in actual_result
    assert TruffleError.ERROR_NO_CONTRACTS_DEPLOYED not in actual_result
    print(actual_result)


@allure.feature(FEATURE)
def test_truffle_test():
    # truffle neonlabs ./test/metacoin.js
    actual_result = run_command_line(
        f"{Subfolder.CD_METACOIN} {RunCommand.TRUFFLE} --network " +
        f"{NETWORK_NAME} test ./test/metacoin.js {CD_BACK}")
    assert TruffleError.ERROR_CONTRACTS_NOT_DEPLOYED not in actual_result
    assert TruffleError.ERROR_NO_CONTRACTS_DEPLOYED not in actual_result
    print(actual_result)


@allure.feature(FEATURE)
def test_issue_364_self_destruct_contract():
    truffle_result = run_command_line(
        f"cd issues/364; {RunCommand.TRUFFLE} "
        f"--network {NETWORK_NAME} migrate -f 3 --to 3"
    )
    assert "instruction changed the balance of a read-only account" \
           not in truffle_result
    print(truffle_result)
