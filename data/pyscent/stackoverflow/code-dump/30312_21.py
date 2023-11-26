import unittest
from fastapi.testclient import TestClient
from engine.routes.base import app


class PostTest(unittest.TestCase):
    def setUp(self) -> None:
        self.client = TestClient(app)

    def test_home_page(self):
        response = self.client.get("/")
        assert response.status_code == 200

