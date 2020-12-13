import pytest

from lib import license_operations


def test_verify_valid_license():
    """
    This test cases will check the user has valid license
    i.e. scenario 1
    1. Scenario - License `Found` status
    State & Type: CA - [DEMO] Registered Nurse
    License #: 2
    Provider Name: Jane Doe

    Verification: when user has only one valid license then
    result is a 'Found' state
    """
    license_state = 'CA'
    license_number = 2
    provider_name = 'Jane Doe'
    provider_ids = license_operations.get_provider_id_list(provider_name, license_state, license_number=license_number)
    assert len(provider_ids) == 1, "Failed user has multiple license"


def test_verify_multiple_matches_license():
    """
    This test cases will check the user has multiple licenses
    i.e. scenario 2
    2. Scenario - Multiple matches that results in NeedsReview
    State & Type: CA - [DEMO] Registered Nurse
    License #: 6
    Provider Name: Jane Doe

    Verification: when user has multiple licenses then
    result is a "NeedReview" state
    """
    license_state = 'CA'
    license_number = 6
    provider_name = 'Jane Doe'
    provider_ids = license_operations.get_provider_id_list(provider_name, license_state, license_number=license_number)
    assert len(provider_ids) > 1, "Failed user has only one license"


def test_verify_no_valid_license():
    """
    This test cases will check the user has no valid license
    i.e. scenario 3
    3. Scenario - License `NotFound` status
    State & Type: CA - [DEMO] Registered Nurse
    License #: 7
    Provider Name: Jane Doe

    Verification: when user has no valid license then
    result is a "NotFound" state
    """
    license_state = 'CA'
    license_number = 7
    provider_name = 'Jane Doe'
    provider_ids = license_operations.get_provider_id_list(provider_name, license_state, license_number=license_number)
    assert provider_ids is False, "Failed user has some license"
