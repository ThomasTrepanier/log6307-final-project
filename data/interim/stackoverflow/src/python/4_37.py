import pytest
from fastapi.testclient import TestClient
from app.main import app
import multiprocessing
from uvicorn import Config, Server


class UvicornServer(multiprocessing.Process):

    def __init__(self, config: Config):
        super().__init__()
        self.server = Server(config=config)
        self.config = config

    def stop(self):
        self.terminate()

    def run(self, *args, **kwargs):
        self.server.run()




@pytest.fixture(scope="session")
def server():
    config = Config("app.main:app", host="127.0.0.1", port=5000, log_level="debug")
    instance = UvicornServer(config=config)
    instance.start()
    yield instance
    instance.stop()

@pytest.fixture(scope="module")
def mock_app(server):
    client = TestClient(app)
    yield client
