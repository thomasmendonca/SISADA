from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_deve_retornar_status_200_e_mensagem_funcionando():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"mensagem": "Funcionando"}
