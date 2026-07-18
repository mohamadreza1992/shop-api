from app.models.category import Category
from app.models.product import Product


def create_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "orderuser",
            "email": "order@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200


def login(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "order@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200

    return response.json()["access_token"]



def create_product(db_session):

    category = Category(
        name="Order Category"
    )

    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)


    product = Product(
        name="Phone",
        price=500,
        stock=10,
        category_id=category.id
    )

    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    return product



def add_product_to_cart(
    client,
    token,
    product_id,
    quantity
):

    response = client.post(
        "/cart/items",
        json={
            "product_id": product_id,
            "quantity": quantity
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 200



def test_create_order(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add_product_to_cart(
        client,
        token,
        product.id,
        2
    )


    response = client.post(
        "/orders",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "pending"



def test_order_reduce_stock(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add_product_to_cart(
        client,
        token,
        product.id,
        3
    )


    client.post(
        "/orders",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    db_session.refresh(product)

    assert product.stock == 7



def test_cart_empty_after_order(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add_product_to_cart(
        client,
        token,
        product.id,
        1
    )


    response = client.post(
        "/orders",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200


    cart = client.get(
        "/cart",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert cart.status_code == 200

    assert cart.json()["items"] == []



def test_order_not_enough_stock(
    client,
    db_session
):

    create_user(client)

    token = login(client)

    product = create_product(
        db_session
    )


    add_product_to_cart(
        client,
        token,
        product.id,
        20
    )


    response = client.post(
        "/orders",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 400