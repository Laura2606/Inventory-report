from inventory_report.product import Product


def test_product_report() -> None:
    id = "450"
    product_name = "Product 1"
    company_name = "Company Name"
    manufacturing_date = "2022-01-01"
    expiration_date = "2023-01-01"
    serial_number = "ABC123"
    storage_instructions = "Store in a cool, dry place."

    product = Product(
        id=id,
        product_name=product_name,
        company_name=company_name,
        manufacturing_date=manufacturing_date,
        expiration_date=expiration_date,
        serial_number=serial_number,
        storage_instructions=storage_instructions,
    )

    expected_reported_phrase = (
        f"The product {id} - {product_name} "
        f"with serial number {serial_number} "
        f"manufactured on {manufacturing_date} "
        f"by the company {company_name} "
        f"valid until {expiration_date} "
        f"must be stored according to the following instructions: "
        f"{storage_instructions}."
    )
    assert str(product) == expected_reported_phrase
