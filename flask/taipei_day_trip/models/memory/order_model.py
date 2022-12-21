from datetime import datetime
from functools import reduce
from taipei_day_trip.models.types import List
from taipei_day_trip.models.types import Order
from taipei_day_trip.models.order_model import OrderModel
from taipei_day_trip.models.memory.booking_model import MemoryBookingModel

class MemoryOrderModel(OrderModel):
    def __init__(self, bookings: MemoryBookingModel):
        self.__db: List[Order] = []
        self.__bookings = bookings
        self.__id: int = 0

    def add(self,
            member_id: int,
            price: int,
            booking_ids: List[int],
            payment_status: int,
            contact_name: str,
            contact_email: str,
            contact_phone: str) -> int | None:
        length = len(booking_ids)
        if length == 0:
            return None
        bookings = self.__bookings.get_by_ids_and_member_id(booking_ids, member_id)
        if len(bookings) != length:
            return None

        id = self.__next_id
        self.__db.append(
            Order(id, member_id, price, bookings, payment_status,
                  contact_name, contact_email, contact_phone, datetime.now()))
        return id

    def get_by_id(self, id: int, member_id: int) -> Order | None:
        output = list(filter(lambda i: (i.id == id and i.member_id == member_id), self.__db))
        if len(output) == 0:
            return None
        return output[0]

    @property
    def __next_id(self):
        self.__id += 1
        return self.__id
