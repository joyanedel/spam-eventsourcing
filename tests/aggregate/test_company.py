from datetime import datetime, timedelta
import pytest

from spam_eventsourcing.core.company.aggregate import Company
from spam_eventsourcing.core.enums import ContactStatus


@pytest.fixture(scope="function")
def company():
	yield Company(name="Mockup-Cola")


def test_company_created_correctly(company: Company):
	assert len(company.collect_events()) == 1


@pytest.mark.parametrize("days", [1, 7, 14, 28, 54])
def test_company_has_n_tries_of_communication(company: Company, days: int):
	for day_delta in range(days + 1):
		company.communication_tried(datetime(2021, 1, 1) + timedelta(days=day_delta))

	assert company.first_communication == datetime(2021, 1, 1)
	assert company.last_communication == datetime(2021, 1, 1) + timedelta(days=days)


def test_company_did_reply(company: Company):
	company.communication_tried(datetime(2021, 1, 1))
	company.replied(datetime(2021, 1, 3), ContactStatus.COMMUNICATION_ESTABLISHED)

	assert company.status == ContactStatus.COMMUNICATION_ESTABLISHED
	assert company.last_communication == datetime(2021, 1, 3)


def test_company_did_not_reply(company: Company):
	assert company.status == ContactStatus.NO_COMMUNICATION
