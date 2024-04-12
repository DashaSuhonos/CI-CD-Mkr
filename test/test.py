import pytest
from task import read_population_data, calculate_population_change

@pytest.fixture
def sample_population_data():
    """
    Фікстура для надання зразкових даних про населення для тестів.
    """
    population_data = {
        'Ukraine': [(2000, 48000000), (2005, 47500000), (2010, 46000000), (2015, 44000000), (2020, 42000000)],
        'United States': [(2000, 280000000), (2005, 295000000), (2010, 310000000), (2015, 325000000), (2020, 335000000)],
        'China': [(2000, 1280000000), (2005, 1320000000), (2010, 1360000000), (2015, 1380000000), (2020, 1400000000)]
    }
    return population_data

@pytest.mark.parametrize("country, expected", [
    ('Ukraine', [(2005, -500000), (2010, -1500000), (2015, -2000000), (2020, -2000000)]),
    ('United States', [(2005, 15000000), (2010, 15000000), (2015, 15000000), (2020, 10000000)]),
    ('China', [(2005, 40000000), (2010, 40000000), (2015, 20000000), (2020, 20000000)])
])
def test_calculate_population_change(sample_population_data, country, expected):
    """
    Тест для перевірки функції calculate_population_change.
    """
    result = calculate_population_change({country: sample_population_data[country]})
    assert result[country] == expected

@pytest.mark.parametrize("file_content, expected", [
    ("Ukraine, 2000, 48000000\nUkraine, 2005, 47500000\nUkraine, 2010, 46000000\nUkraine, 2015, 44000000\nUkraine, 2020, 42000000\n", {'Ukraine': [(2000, 48000000), (2005, 47500000), (2010, 46000000), (2015, 44000000), (2020, 42000000)]}),
    ("United States, 2000, 280000000\nUnited States, 2005, 295000000\nUnited States, 2010, 310000000\nUnited States, 2015, 325000000\nUnited States, 2020, 335000000\n", {'United States': [(2000, 280000000), (2005, 295000000), (2010, 310000000), (2015, 325000000), (2020, 335000000)]}),
    ("China, 2000, 1280000000\nChina, 2005, 1320000000\nChina, 2010, 1360000000\nChina, 2015, 1380000000\nChina, 2020, 1400000000\n", {'China': [(2000, 1280000000), (2005, 1320000000), (2010, 1360000000), (2015, 1380000000), (2020, 1400000000)]})
])
def test_read_population_data(tmp_path, file_content, expected):
    """
    Тест для перевірки функції read_population_data.
    """
    file_path = tmp_path / "population_data.txt"
    file_path.write_text(file_content)
    result = read_population_data(file_path)
    assert result == expected
