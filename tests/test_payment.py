from app.models.category import Category
from app.models.product import Product



def create_user(client):

    response = client.post(
        "/auth/register",
        json={
            "username": "paymentuser",
            "email": "payment@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200



def login(client):

    response = client.post(
        "/auth/login",
        data={
            "username": "payment@test.com",
            "password": "12345678"
        }
    )

    assert response.status_code == 200

    return response.json()["access_token"]



def create_product(db_session):

    category = Category(
        name="Payment Category"
    )

    db_session.add(category)
    db_session.commit()
    db_session.refresh(category)


    product = Product(
        name="Keyboard",
        price=100,
        stock=10,
        category_id=category.id
    )


    db_session.add(product)
    db_session.commit()
    db_session.refresh(product)

    return product



def create_order(
    client,
    token,
    db_session
):

    product = create_product(
        db_session
    )


    client.post(
        "/cart/items",
        json={
            "product_id": product.id,
            "quantity": 2
        },
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    response = client.post(
        "/orders",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    return response.json()



def test_create_payment(
    client,
    db_session
):

    create_user(client)

    token = login(client)


    order = create_order(
        client,
        token,
        db_session
    )


    response = client.post(
        f"/payments/{order['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200


    data = response.json()

    assert data["order_id"] == order["id"]
    assert data["status"] == "pending"



def test_success_payment(
    client,
    db_session
):

    create_user(client)

    token = login(client)


    order = create_order(
        client,
        token,
        db_session
    )


    payment = client.post(
        f"/payments/{order['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    payment_id = payment.json()["id"]


    response = client.post(
        f"/payments/{payment_id}/success",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["status"] == "success"



def test_order_status_after_payment(
    client,
    db_session
):

    create_user(client)

    token = login(client)


    order = create_order(
        client,
        token,
        db_session
    )


    payment = client.post(
        f"/payments/{order['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    payment_id = payment.json()["id"]


    client.post(
        f"/payments/{payment_id}/success",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    response = client.get(
        f"/orders/{order['id']}",
        headers={
            "Authorization": f"Bearer {token}"
        }
    )


    assert response.status_code == 200

    assert response.json()["status"] == "paid"