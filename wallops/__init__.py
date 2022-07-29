from irctokens import build, Line
from ircrobots import Bot as BaseBot
from ircrobots import Server as BaseServer

from ircstates.numerics import *

from .config   import Config
from .database import Database

class Server(BaseServer):
    def __init__(self,
            bot:      BaseBot,
            name:     str,
            config:   Config):

        super().__init__(bot, name)
        self._config   = config
        self._database = Database(config.database)
        self._server_name = "(unknown)" # for wallop logging purposes, grab it at RPL_WELCOME

    def set_throttle(self, rate: int, time: float):
        # turn off throttling
        pass

    async def _log(self, message: str):
        await self.send(build("PRIVMSG", [self._config.channel, message]))

    async def line_read(self, line: Line):
        if line.command == RPL_WELCOME:
            await self.send(build("MODE", [self.nickname, "+gw"]))
            self._server_name = line.source

        elif line.command == "WALLOPS":
            await self._log(f"got wallop from \x02{line.source}\x02 - it says: {line.params[0]}")
            await self._database.add_wallop(line.params[0], line.source, self._server_name)

    def line_preread(self, line: Line):
        print(f"< {line.format()}")
    def line_presend(self, line: Line):
        print(f"> {line.format()}")

class Bot(BaseBot):
    def __init__(self, config: Config):
        super().__init__()
        self._config = config

    def create_server(self, name: str):
        return Server(self, name, self._config)
