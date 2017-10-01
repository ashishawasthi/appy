
import pytest

@pytest.fixture
def app():
    import main
    main.app.testing = True
    return main.app.test_client()


def test_landing(app):
    r = app.get('/')
    assert r.status_code == 200
    assert 'Create a Project' in r.data.decode('utf-8')


def test_create_project(app):
    r = app.post('/created-project', data={
        'name': 'P1'})
    assert r.status_code == 200
    assert 'P1' in r.data.decode('utf-8')
