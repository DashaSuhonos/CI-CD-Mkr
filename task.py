from typing import Dict, List, Tuple

def read_population_data(file_path: str) -> Dict[str, List[Tuple[int, int]]]:
    """
    Зчитує дані про населення з файлу та повертає словник,
    де ключ - це назва країни, а значення - список кортежів (рік, населення).
    """
    population_data: Dict[str, List[Tuple[int, int]]] = {}
    with open(file_path, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(', ')
            if country not in population_data:
                population_data[country] = []
            population_data[country].append((int(year), int(population)))
    return population_data


def calculate_population_change(population_data: Dict[str, List[Tuple[int, int]]]) -> Dict[str, List[Tuple[int, int]]]:
    """
    Обчислює зміну населення за роками для кожної країни та повертає словник,
    де ключ - це назва країни, а значення - список кортежів (рік, зміна населення).
    """
    population_change: Dict[str, List[Tuple[int, int]]] = {}
    for country, data in population_data.items():
        population_change[country] = []
        for i in range(1, len(data)):
            year, population = data[i]
            prev_year, prev_population = data[i - 1]
            change = population - prev_population
            population_change[country].append((year, change))
    return population_change


def main() -> None:
    file_path: str = "population_data.txt"  # Змініть шлях до файлу на свій
    population_data: Dict[str, List[Tuple[int, int]]] = read_population_data(file_path)
    population_change: Dict[str, List[Tuple[int, int]]] = calculate_population_change(population_data)

    # Виведення результатів
    for country, changes in population_change.items():
        print(f"Зміна населення для {country}:")
        for year, change in changes:
            print(f"Рік {year}: зміна населення {change}")


if __name__ == "__main__":
    main()
