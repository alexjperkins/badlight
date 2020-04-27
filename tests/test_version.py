from badlight.app import _API_ROOT, _VERSION


def test_version(client):
    endpoint = 'version'
    response = client.get(endpoint)

    assert response.status_code == 200
    assert _VERSION == response.get_json()['version']
