from pydantic import BaseSettings

class Settings(BaseSettings):
    PORT : int
    SSL : bool
    class Config:
        env_file = '.env'

config = Settings()

print(type(config.SSL),  config.SSL)
print(type(config.PORT),  config.PORT)
# <class 'bool'> False
# <class 'int'> 5000
