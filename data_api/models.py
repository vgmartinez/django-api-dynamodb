from dynamodb_mapper.model import DynamoDBModel
from dynamodb_mapper.model import ConnectionBorg

class DoomMap(DynamoDBModel):
    __table__ = u"doom_map"
    __hash_key__ = u"episode"
    __range_key__ = u"map"
    __schema__ = {
        u"episode": int,
        u"map": int,
        u"name": str,
        u"cheats": set,
    }
    __defaults__ = {
        u"cheats": set([u"Konami"]),
    }

connBorg = ConnectionBorg()
conn=connBorg._get_connection()

if not conn.list_tables().__contains__(DoomMap.__table__):
    connBorg.create_table(DoomMap, 10, 10, wait_for_active=True)