from mynmap import parse_port_range


def test_single_port():
    assert parse_port_range("80") == [80]


def test_port_range():
    assert parse_port_range("20-22") == [20, 21, 22]


def test_comma_list():
    assert parse_port_range("22,80,443") == [22, 80, 443]


def test_range_of_one():
    assert parse_port_range("443-443") == [443]
