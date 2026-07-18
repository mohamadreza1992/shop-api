
from app.models.user import User
from app.models.enums import UserRole
from app.models.category import Category
from app.models.product import Product
from app.core.security import hash_password


def create_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "cartuser",
            "email": "cart@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200


def login(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "cart@test.com",
            "password": "12345678"
        }
    )

    return response.json()["access_token"]



def create_product(db_session):

    category = Category(
        name="Test Category"
    )

    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)


    product = Product(
        name="Laptop",
        price=1000,
        stock=10,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    return product



def test_add_item_to_cart(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    response = client.post(
        "/cart/items",
        json={
            "product_id": product.id,
            "quantity": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["product_id"] == product.id
    assert data["quantity"] == 2



def test_get_cart(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    client.post(
        "/cart/items",
        json={
            "product_id": product.id,
            "quantity": 3
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    response = client.get(
        "/cart",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert len(data["items"]) == 1
    assert data["items"][0]["quantity"] == 3



def test_update_cart_item(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add = client.post(
        "/cart/items",
        json={
            "product_id": product.id,
            "quantity": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    item_id = add.json()["id"]


    response = client.patch(
        f"/cart/items/{item_id}",
        json={
            "quantity":5
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["quantity"] == 5



def test_delete_cart_item(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add = client.post(
        "/cart/items",
        json={
            "product_id": product.id,
            "quantity":1
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    item_id = add.json()["id"]


    response = client.delete(
        f"/cart/items/{item_id}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["message"] == "Item removed successfully"