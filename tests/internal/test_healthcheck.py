from badlight.app import _API_ROOT


def test_healthcheck(client):
    endpoint = f'{_API_ROOT}/__internal__/healthcheck'
    response = client.get(endpoint)

    assert response.status_code == 200
    assert b'healthy' in response.data
