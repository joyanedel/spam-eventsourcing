from eventsourcing.domain import Aggregate, event


class Employee(Aggregate):
	first_name: str
	last_name: str
	company_id: str

	@event("EMPLOYEE_REGISTERED")
	def __init__(self, first_name: str, last_name: str, company_id: str) -> None:
		super().__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.company_id = company_id
