from datetime import datetime
from typing import Optional
from eventsourcing.domain import Aggregate, event

from spam_eventsourcing.core.enums import ContactStatus


class Company(Aggregate):
	name: str
	status: ContactStatus
	category: Optional[str] = None

	first_communication: Optional[datetime] = None
	last_communication: Optional[datetime] = None

	@event("REGISTERED")
	def __init__(self, name: str, category: Optional[str] = None) -> None:
		super().__init__()
		self.name = name
		self.category = category
		self.status = ContactStatus.NO_COMMUNICATION

	@event("COMMUNICATION_TRIED")
	def communication_tried(self, date: datetime):
		if self.first_communication is None:
			self.first_communication = date
		self.last_communication = date

	@event("REPLIED")
	def replied(self, date: datetime, status: ContactStatus):
		self.status = status
		self.last_communication = date
