from taipei_day_trip.models.attraction_model import AttractionModel
from taipei_day_trip.models.category_model import CategoryModel
from taipei_day_trip.models.mrt_model import MRTModel

class Database:
    def __init__(self):
        self.__categories = self._create_category_model()
        self.__mrts = self._create_mrt_model()
        self.__attractions = self._create_attraction_model()

    @property
    def attractions(self) -> AttractionModel:
        return self.__attractions

    @property
    def categories(self) -> CategoryModel:
        return self.__categories

    @property
    def mrts(self) -> MRTModel:
        return self.__mrts

    def _create_attraction_model(self) -> AttractionModel:
        return NotImplemented

    def _create_category_model(self) -> CategoryModel:
        return NotImplemented

    def _create_mrt_model(self) -> MRTModel:
        return NotImplemented

def copy_db(src: Database, dst: Database):
    copy_categories(src, dst)
    copy_mrt(src, dst)
    copy_attractions(src, dst)

def copy_attractions(src: Database, dst: Database):
    values = dst.attractions.get_all()
    for value in src.attractions.get_all():
        is_existed = len(list(filter(lambda x: x.name == value.name, values))) > 0
        if not is_existed:
            dst.attractions.add(name=value.name,
                                description=value.description,
                                address=value.address,
                                lat=value.lat,
                                lng=value.lng,
                                transport=value.transport,
                                images=value.images,
                                category=value.category,
                                mrt=value.mrt)

def copy_categories(src: Database, dst: Database):
    values = dst.categories.get_all()
    for value in src.categories.get_all():
        is_existed = len(list(filter(lambda x: x.name == value.name, values))) > 0
        if not is_existed:
            dst.categories.add(value.name)

def copy_mrt(src: Database, dst: Database):
    values = dst.mrts.get_all()
    for value in src.mrts.get_all():
        is_existed = len(list(filter(lambda x: x.name == value.name, values))) > 0
        if not is_existed:
            dst.mrts.add(value.name)
