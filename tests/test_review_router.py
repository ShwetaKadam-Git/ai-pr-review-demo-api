def test_create_review_returns_findings(client):
    payload = {
        "policy": "default",
        "files": [{"filename": "x.py", "patch": "+    except:\n+        pass"}],
    }
    resp = client.post("/review", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["policy"] == "default"
    assert len(data["findings"]) >= 1


def test_list_reviews_after_create(client):
    payload = {"policy": "default", "files": [{"filename": "y.py", "patch": "+print('x')"}]}
    client.post("/review", json=payload)
    resp = client.get("/reviews")
    assert resp.status_code == 200
    assert isinstance(resp.json(), list)