import pytest

from config import config
from lib import auth_operations


def test_verify_auth_api_returns_tokenid_and_token_when_provide_valid_credentials():
    """
    This test case verifies auth api returns token Id and token
    when provide correct username and password
    """
    result = auth_operations.get_auth_token(config.USERNAME, config.PASSWORD, need_details=True)
    assert 'tokenId' in result.keys(), "Failed tokenId not present in response"
    assert 'token' in result.keys(), "Failed token not present in response"


def test_verify_auth_api_returns_correct_status_code_and_reason_when_not_provide_credentials():
    """
    This test case verifies auth api returns token Id and token
    when provide correct username and password
    """
    status_code, reason, error_msg = auth_operations.get_auth_token('', '', need_details=True)
    assert status_code == 400, "Failed wrong status code returned by auth API"
    assert reason == 'Bad Request', "Failed Failed wrong reason returned by auth api"


def test_verify_auth_api_returns_correct_error_msg_when_email_not_provided():
    """
    This test case verifies auth api returns correct error message
    when email not provided
    """
    status_code, reason, error_msg = auth_operations.get_auth_token('', config.PASSWORD, need_details=True)
    assert error_msg['errors']['Email'][0] == 'The Email field is required.', "Failed wrong error message returned"


def test_verify_auth_api_returns_correct_error_msg_when_password_not_provided():
    """
    This test case verifies auth api returns correct error message
    when password not provided
    """
    status_code, reason, error_msg = auth_operations.get_auth_token(config.USERNAME, '', need_details=True)
    assert error_msg['errors']['Password'][0] == 'The Password field is required.', "Failed wrong error message returned"


def test_verify_auth_api_returns_correct_status_code_when_provide_incorrect_username():
    """
    This test case verifies auth api returning correct error code and message
    when incorrect username provided
    """
    status_code, reason, error_msg = auth_operations.get_auth_token('incorrect-user', config.PASSWORD, need_details=True)
    assert status_code == 403, "Failed wrong status code returned by auth API"


def test_verify_auth_api_returns_correct_status_code_when_provide_incorrect_password():
    """
    This test case verifies auth api returning correct error code and message
    when incorrect username provided
    """
    status_code, reason, error_msg = auth_operations.get_auth_token(config.USERNAME, 'incorrect-password', need_details=True)
    assert status_code == 403, "Failed wrong status code returned by auth API"
