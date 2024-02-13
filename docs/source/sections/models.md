# Models

## Base models

We have 2 main entities in this project. The first one is the company.
We define a company as an organization with people that we can offer some product
of their interest.

We can define a company as follow:

```python
class Company:
    id: str
    name: str
    category: str

    status: ContactStatus
```

The second entity is the employee. The employee belongs to a company and is the medium
we are going to make contact with the company. Note that we can have many employees to make contact
with a company, the more employees, the more the chances to concrete a first contact.

We define a employee as follow:

```python
from datetime import date
from typing import Optional

class Employee:
    id: str
    first_name: str
    last_name: str
    company_id: str

    status: ContactStatus
    first_contact: Optional[date] = None
    last_contact: Optional[date] = None
```

```{note}
In order to mark a company as contacted, at least one of its employee must've been contacted
```

## Contact status

We already mention `ContactStatus`. What is it?

We have to trace how we or communication with an employee have been. If we haven't contact it yet then there is no contact, if the send the first email, then we mark it as a first message, and so on...
