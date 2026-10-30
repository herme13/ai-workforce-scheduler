from dataclasses import dataclass

@dataclass
class Booking:
    customer: str
    date: str
    time: str
    students: int
    status: str
    