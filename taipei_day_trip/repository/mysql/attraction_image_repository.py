from taipei_day_trip.core import List
from taipei_day_trip.repository.mysql.repository import MySQLRepository

class MySQLAttractionImageRepository(MySQLRepository):
    def __init__(self, cnxpool, attraction_table_name: str, debug: bool):
        self.attraction_table_name = attraction_table_name
        MySQLRepository.__init__(self, cnxpool, debug)

    @MySQLRepository.with_connection
    def add(self, attraction_id: int, urls: List[str], cnx, cursor):
        if len(urls) > 0:
            query = 'INSERT INTO {} (attraction_id, url) VALUES (%s, %s)'.format(self.tablename)
            data = list(map(lambda url: (attraction_id, url,), urls))
            cursor.executemany(query, data)
            cnx.commit()

    @property
    def tablename(self) -> str:
        if self.debug:
            return 'test_attraction_image'
        return 'attraction_image'

    @property
    def create_table_statement(self) -> str:
        return (
            'CREATE TABLE {attraction_image} ('
            '    attraction_id   bigint        NOT NULL,'
            '    url             varchar(255)  NOT NULL,'
            '    PRIMARY KEY (attraction_id, url),'
            '    FOREIGN KEY (attraction_id) REFERENCES {attraction} (id)'
            ');'
        ).format(attraction_image=self.tablename,
                 attraction=self.attraction_table_name)
