def test_register_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "testuser",
            "email": "test@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "test@test.com"
    assert data["username"] == "testuser"


def test_register_duplicate_email(client):

    user_data = {
        "username": "testuser",
        "email": "test@test.com",
        "password": "12345678"
    }

    client.post(
        "/auth/register",
        json=user_data
    )

    response = client.post(
        "/auth/register",
        json={
            "username": "anotheruser",
            "email": "test@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 400

    assert response.json()["detail"] == "Email already exists"    


def test_login_success(client):

    client.post(
        "/auth/register",
        json={
            "username": "loginuser",
            "email": "login@test.com",
            "password": "12345678"
        }
    )


    response = client.post(
        "/auth/login",
        data={
            "username": "login@test.com",
            "password": "12345678"
        }
    )


    assert response.status_code == 200


    data = response.json()

    assert "access_token" in data
    assert data["token_type"] == "bearer"    


def test_get_current_user(client):

    client.post(
        "/auth/register",
        json={
            "username": "currentuser",
            "email": "current@test.com",
            "password": "12345678"
        }
    )

    login_response = client.post(
        "/auth/login",
        data={
            "username": "current@test.com",
            "password": "12345678"
        }
    )

    token = login_response.json()["access_token"]


    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["email"] == "current@test.com"
    assert data["username"] == "currentuser"    