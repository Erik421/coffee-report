from reports.median_coffee import MedianCoffeeReport


def test_median_coffee_even_count():
    rows = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "300"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert result == [["A", 200.0]]


def test_median_coffee_odd_count():
    rows = [
        {"student": "B", "coffee_spent": "200"},
        {"student": "B", "coffee_spent": "400"},
        {"student": "B", "coffee_spent": "600"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert result == [["B", 400.0]]


def test_sorting_desc():
    rows = [
        {"student": "A", "coffee_spent": "100"},
        {"student": "A", "coffee_spent": "300"},
        {"student": "B", "coffee_spent": "500"},
        {"student": "B", "coffee_spent": "700"},
    ]

    report = MedianCoffeeReport()
    result = report.build(rows)

    assert result == [
        ["B", 600.0],
        ["A", 200.0],
    ]