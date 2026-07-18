
from app.models.user import User
from app.models.enums import UserRole
from app.models.category import Category
from app.core.security import hash_password


def create_admin(db_session):

    admin = User(
        username="admin",
        email="admin@test.com",
        hashed_password=hash_password("12345678"),
        role=UserRole.ADMIN
    )

    db_session.add(admin)
    db_session.commit()
    db_session.refresh(admin)

    return admin



def get_admin_token(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "admin@test.com",
            "password": "12345678"
        }
    )

    return response.json()["access_token"]



def create_category(db_session):

    category = Category(
        name="Electronics"
    )

    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)

    return category



def test_get_products(client):

    response = client.get(
        "/products"
    )

    assert response.status_code == 200

    data = response.json()

    assert "items" in data



def test_create_product_without_admin(client):

    client.post(
        "/auth/register",
        json={
            "username": "normaluser",
            "email": "normal@test.com",
            "password": "12345678"
        }
    )


    login = client.post(
        "/auth/login",
        data={
            "username": "normal@test.com",
            "password": "12345678"
        }
    )


    token = login.json()["access_token"]


    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": "1000",
            "stock": 10,
            "category_id": 1
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 403



def test_create_product_as_admin(
    client,
    db_session
):

    create_admin(db_session)

    category = create_category(
        db_session
    )


    token = get_admin_token(
        client
    )


    response = client.post(
        "/products",
        json={
            "name": "Laptop",
            "price": "1000",
            "stock": 10,
            "category_id": category.id
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["name"] == "Laptop"



def test_get_product(
    client,
    db_session
):

    create_admin(db_session)

    category = create_category(
        db_session
    )


    token = get_admin_token(
        client
    )


    create_response = client.post(
        "/products",
        json={
            "name": "Phone",
            "price": "500",
            "stock": 5,
            "category_id": category.id
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    product_id = create_response.json()["id"]


    response = client.get(
        f"/products/{product_id}"
    )


    assert response.status_code == 200

    assert response.json()["name"] == "Phone"



def test_update_product_as_admin(
    client,
    db_session
):

    create_admin(db_session)

    category = create_category(
        db_session
    )


    token = get_admin_token(
        client
    )


    create = client.post(
        "/products",
        json={
            "name": "Old Laptop",
            "price": "1000",
            "stock": 5,
            "category_id": category.id
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    product_id = create.json()["id"]


    response = client.put(
        f"/products/{product_id}",
        json={
            "name": "New Laptop",
            "price": "1500"
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["name"] == "New Laptop"



def test_delete_product_as_admin(
    client,
    db_session
):

    create_admin(db_session)

    category = create_category(
        db_session
    )


    token = get_admin_token(
        client
    )


    create = client.post(
        "/products",
        json={
            "name": "Delete Laptop",
            "price": "900",
            "stock": 3,
            "category_id": category.id
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    product_id = create.json()["id"]


    response = client.delete(
        f"/products/{product_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["message"] == "Deleted successfully"