from enum import Enum


class ContactStatus(Enum):
	"""Enumerator used to mark a communication try"""

	NO_COMMUNICATION = 0
	COMMUNICATION_ESTABLISHED = 100

	ACCEPTED = 200
	REJECTED = 300
