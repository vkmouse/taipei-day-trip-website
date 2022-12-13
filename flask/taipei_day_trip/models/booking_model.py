from datetime import datetime
from taipei_day_trip.models.types import Booking
from taipei_day_trip.models.types import List

class BookingModel:
    def add(self, memberId: int, attractionId: int, starttime: datetime, endtime: datetime, price: int) -> bool:
        return NotImplemented
    def get_by_memberId(self, memberId: int) -> List[Booking]:
        return NotImplemented
    def remove_by_id(self, id: int):
        return NotImplemented