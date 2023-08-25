def test_create(client):
    response = client.post(
        "api/entity",
        json={
            "name": "Flask",
            "theme": "dark",
        },
    )

    assert response.status_code == 200
    assert response.json == {"key": "{'name': 'Flask', 'theme': 'dark'}"}


def test_read(client):
    response = client.get(
        "api/entity/12",
    )

    assert response.status_code == 200
    assert response.json == {"key": 12}


def test_read_all(client):
    response = client.get(
        "api/entity",
    )

    assert response.status_code == 200
    assert response.json == {"key": "value"}
