from inventory_report.product import Product
import pytest


@pytest.fixture
def sample_product():
    id = "450"
    product_name = "Product 1"
    company_name = "Company Name"
    manufacturing_date = "2022-01-01"
    expiration_date = "2023-01-01"
    serial_number = "ABC123"
    storage_instructions = "Store in a cool, dry place."

    return Product(
        id,
        product_name,
        company_name,
        manufacturing_date,
        expiration_date,
        serial_number,
        storage_instructions,
    )


def test_create_product(sample_product) -> None:
    product = sample_product

    assert product.id == "450"
    assert product.product_name == "Product 1"
    assert product.company_name == "Company Name"
    assert product.manufacturing_date == "2022-01-01"
    assert product.expiration_date == "2023-01-01"
    assert product.serial_number == "ABC123"
    assert product.storage_instructions == "Store in a cool, dry place."

    # id = "450"
    # product_name = "Product 1"
    # company_name = "Company Name"
    # manufacturing_date = "2022-01-01"
    # expiration_date = "2023-01-01"
    # serial_number = "ABC123"
    # storage_instructions = "Store in a cool, dry place."

    # product = Product(
    #     id,
    #     product_name,
    #     company_name,
    #     manufacturing_date,
    #     expiration_date,
    #     serial_number,
    #     storage_instructions,
    # )

    # assert product.id == id
    # assert product.product_name == product_name
    # assert product.company_name == company_name
    # assert product.manufacturing_date == manufacturing_date
    # assert product.expiration_date == expiration_date
    # assert product.serial_number == serial_number
    # assert product.storage_instructions == storage_instructions
