from taipei_day_trip.core import AttractionRepository
from taipei_day_trip.core import CategoryRepository
from taipei_day_trip.core import MRTRepository
from taipei_day_trip.core import UnitOfWork
from taipei_day_trip.repository.memory.attraction_repository import MemoryAttractionRepository
from taipei_day_trip.repository.memory.category_repository import MemoryCategoryRepository
from taipei_day_trip.repository.memory.mrt_repository import MemoryMRTRepository

class MemoryUnitOfWork(UnitOfWork):
    def _create_attraction_repository(self) -> AttractionRepository:
        return MemoryAttractionRepository(self.categories, self.mrts)

    def _create_category_repository(self) -> CategoryRepository:
        return MemoryCategoryRepository()

    def _create_mrt_repository(self) -> MRTRepository:
        return MemoryMRTRepository()
