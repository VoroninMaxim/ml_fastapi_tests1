from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() == {"message": "World"}

def test_predict_sentiment():
    positive_sentences = ["I love machine learning!", "Machine learning is great!"]
    negative_sentences = ["I hate machine learning!", "Machine learning is terrible!"]

    for sentence in positive_sentences:
        response = client.post("/predict/", json={"text": sentence})
        assert response.status_code == 200
        assert response.json()['label'] == 'POSITIVE'

    for sentence in negative_sentences:
        response = client.post("/predict/", json={"text": sentence})
        assert response.status_code == 200
        assert response.json()['label'] == 'NEGATIVE'