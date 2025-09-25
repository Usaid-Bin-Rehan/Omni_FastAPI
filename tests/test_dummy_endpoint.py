from test_client import test_client

def test_dummy_feature():
    response = test_client.get("/dummy")
    assert response.status_code == 200
    assert "expected_content" in response.text