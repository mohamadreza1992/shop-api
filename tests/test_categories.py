from app.models.user import User
from app.models.enums import UserRole
from app.core.security import hash_password


def test_get_categories(client):

    response = client.get(
        "/categories"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)



def test_create_category_without_admin(client):

    # register normal user
    client.post(
        "/auth/register",
        json={
            "username": "normaluser",
            "email": "normal@test.com",
            "password": "12345678"
        }
    )


    # login normal user
    login_response = client.post(
        "/auth/login",
        data={
            "username": "normal@test.com",
            "password": "12345678"
        }
    )


    token = login_response.json()["access_token"]


    # try create category
    response = client.post(
        "/categories",
        json={
            "name": "Electronics"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 403



def test_create_category_as_admin(client, db_session):

    # create admin directly in test database
    admin = User(
        username="admin",
        email="admin@test.com",
        hashed_password=hash_password("12345678"),
        role=UserRole.ADMIN
    )


    db_session.add(admin)
    db_session.commit()


    # login admin
    login_response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "12345678"
        }
    )


    assert login_response.status_code == 200


    token = login_response.json()["access_token"]


    # create category
    response = client.post(
        "/categories",
        json={
            "name": "Electronics"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200


    data = response.json()

    assert data["name"] == "Electronics"