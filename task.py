def read_population_data(file_path):
    """
    Зчитує дані про населення з файлу та повертає словник,
    де ключ - це назва країни, а значення - список кортежів (рік, населення).
    """
    population_data = {}
    with open(file_path, 'r') as file:
        for line in file:
            country, year, population = line.strip().split(', ')
            if country not in population_data:
                population_data[country] = []
            population_data[country].append((int(year), int(population)))
    return population_data

def calculate_population_change(population_data):
    """
    Обчислює зміну населення за роками для кожної країни та повертає словник,
    де ключ - це назва країни, а значення - список кортежів (рік, зміна населення).
    """
    population_change = {}
    for country, data in population_data.items():
        population_change[country] = []
        for i in range(1, len(data)):
            year, population = data[i]
            prev_year, prev_population = data[i - 1]
            change = population - prev_population
            population_change[country].append((year, change))
    return population_change