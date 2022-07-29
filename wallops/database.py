from time import time
import aiosqlite

class Database(object):
    def __init__(self, db_location: str):
        self._db_location = db_location

    async def add_wallop(self,
            content: str,
            sender: str,
            server: str):

        async with aiosqlite.connect(self._db_location) as db:
            await db.execute("""
                INSERT INTO wallops
                (content, sender, server, ts)
                VALUES (?, ?, ?, ?)
            """, [content, sender, server, int(time())])
            await db.commit()
