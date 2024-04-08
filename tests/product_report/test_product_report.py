from inventory_report import Product


def test_product_report(sample_product) -> None:
    product = sample_product

    expected_reported_phrase = (
        "The product Product 1, with serial number ABC123, "
        "manufactured on 2022-01-01 by the company Company Name, "
        "valid until 2023-01-01, "
        "must be stored according to the following instructions: "
        "Store in a cool, dry place."
    )

    assert str(product) == expected_reported_phrase
