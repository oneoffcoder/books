from dataclasses import dataclass


@dataclass
class ServerConfig:
    host: str = 'localhost'
    port: int = 8000
    debug: bool = False


config = ServerConfig(debug=True)
print(config)
