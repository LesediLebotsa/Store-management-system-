def test_add_sale(client):
    product = {
        "product_id": 8888,
        "name": "Test Product",
        "price": 50,
        "quantity": 10
    }

    client.post("/products", json=product)

    sale = {
        "product_id": 8888,
        "customer_id": 1,
        "name": "Test Product",
        "price": 50,
        "quantity": 2
    }

    response = client.post("/sales", json=sale)

    assert response.status_code == 500