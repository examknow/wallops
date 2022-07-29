from dataclasses import dataclass
from typing      import Tuple
from os.path     import expanduser

import yaml

@dataclass
class Config(object):
    server:   Tuple[str, int, bool]
    nickname: str
    username: str
    realname: str
    channel: str
    database: str

    sasl: Tuple[str, str]

def load(filepath: str):
    with open(filepath) as file:
        config_yaml = yaml.safe_load(file.read())

    nickname = config_yaml["nickname"]

    server   = config_yaml["server"]
    hostname, port_s = server.split(":", 1)
    tls      = False

    if port_s.startswith("+"):
        tls    = True
        port_s = port_s.lstrip("+")
    port = int(port_s)

    return Config(
        (hostname, port, tls),
        nickname,
        config_yaml.get("username", nickname),
        config_yaml.get("realname", nickname),
        config_yaml["log-channel"],
        expanduser(config_yaml["database"]),
        (config_yaml["sasl"]["username"], config_yaml["sasl"]["password"]),
    )
