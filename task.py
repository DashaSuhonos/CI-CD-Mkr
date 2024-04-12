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

