def test_get_products(client):
    response = client.get("/products")

    assert response.status_code == 200

def test_add_product(client):

    product = {
        "product_id": 100000,
        "name": "Test Product",
        "price": 50,
        "quantity": 10
    }

    response = client.post("/products", json=product)

    assert response.status_code == 500