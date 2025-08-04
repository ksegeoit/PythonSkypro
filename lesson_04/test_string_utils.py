import pytest
from string_utils import StringUtils


@pytest.fixture
def utils():
    return StringUtils()


def test_capitalize(utils):
    assert utils.capitalize("skypro") == "Skypro"
    assert utils.capitalize("hello world") == "Hello world"
    assert utils.capitalize("123") == "123"
    assert utils.capitalize("тест") == "Тест"
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    with pytest.raises(TypeError):
        utils.capitalize(None)


def test_trim(utils):
    assert utils.trim("   skypro") == "skypro"
    assert utils.trim("04 апреля 2023") == "04 апреля 2023"
    assert utils.trim("") == ""
    assert utils.trim(" ") == ""
    with pytest.raises(TypeError):
        utils.trim(None)


def test_contains(utils):
    assert utils.contains("SkyPro", "S") is True
    assert utils.contains("123", "2") is True
    assert utils.contains("04 апреля 2023", " ") is True
    assert utils.contains("", "a") is False
    assert utils.contains(" ", "x") is False
    assert utils.contains("abc", "") is True
    with pytest.raises(TypeError):
        utils.contains(None, "a")


def test_delete_symbol(utils):
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert utils.delete_symbol("Тест", "е") == "Тст"
    assert utils.delete_symbol("12345", "34") == "125"
    assert utils.delete_symbol("", "a") == ""
    assert utils.delete_symbol(" ", " ") == ""
    with pytest.raises(TypeError):
        utils.delete_symbol(None, "a")


def test_starts_with(utils):
    assert utils.starts_with("SkyPro", "S") is True
    assert utils.starts_with(" Тест", " ") is True
    assert utils.starts_with("123", "1") is True
    assert utils.starts_with("", "S") is False
    assert utils.starts_with(" ", "x") is False
    with pytest.raises(TypeError):
        utils.starts_with(None, "S")


def test_end_with(utils):
    assert utils.end_with("SkyPro", "o") is True
    assert utils.end_with("Тест ", " ") is True
    assert utils.end_with("123", "3") is True
    assert utils.end_with("", "o") is False
    assert utils.end_with(" ", "x") is False
    with pytest.raises(TypeError):
        utils.end_with(None, "o")


def test_is_empty(utils):
    assert utils.is_empty("") is True
    assert utils.is_empty(" ") is True
    assert utils.is_empty("       ") is True
    assert utils.is_empty("SkyPro") is False
    assert utils.is_empty("  test  ") is False
    with pytest.raises(TypeError):
        utils.is_empty(None)


def test_list_to_string(utils):
    assert utils.list_to_string(["a", "b", "c"]) == "a, b, c"
    assert utils.list_to_string(["Sky", "Pro"], "-") == "Sky-Pro"
    assert utils.list_to_string(["1", "2", "3"], ":") == "1:2:3"
    assert utils.list_to_string(
        ["04", "апреля", "2023"], " "
    ) == "04 апреля 2023"
    assert utils.list_to_string([]) == ""
    with pytest.raises(TypeError):
        utils.list_to_string(None, ",")
