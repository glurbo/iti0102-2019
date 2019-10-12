"""The Pies Eating Competition."""
import csv


def get_competitors_list(filename: str) -> list:
    """
    Get the names of all registered competitors.

    :param filename: is the path to the file with the names of competitors.
    :return: a list containing the names of competitors.
    """
    with open(f"{filename}") as csv_file:
        csv_reader = csv.reader(csv_file)
        comp_list = list(csv_reader)
        competitors_list = [i[0] for i in comp_list]
    return competitors_list


def get_results_dict(filename: str) -> dict:
    """
    Get the results and store them in the dictionary.

    Results are following the format 'Firstname Lastname - result'.
    You have to return a dict, where the names of the competitors
    are keys and the results are values.

    :param filename: is the path to the file with the results.
    :return: a dict containing names as keys and results as values.
    """
    results = {}
    with open(f"{filename}") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='-')
        for row in csv_reader:
            key, value = row
            results[key[:-1]] = int(value)
        return results


def filter_results(path_to_competitors: str, path_to_results: str) -> dict:
    """
    Filter out all illegal competitors.

    Illegal competitor is the one, whose name is not in the registered competitors list.
    You have to return a results dict, which doesn't contain the results of illegal competitors.
    Use methods defined above.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :return: a dict with correct results.
    """
    comp = get_competitors_list(path_to_competitors)
    res = get_results_dict(path_to_results)
    filtered_dict = {}
    filtered_dict.update(res)
    for k, v in res.items():
        if k not in comp:
            del filtered_dict[k]
    return filtered_dict


def sort_results(path_to_competitors: str, path_to_results: str) -> list:
    """
    Sort the filtered results dictionary.

    In order to find the winner you have to sort the results.
    Results have to be sorted based on the cakes eaten by the competitors.
    The sorted results must be in a descending order.
    This means that the more cakes the competitor has eaten the better place they get.
    If there are multiple competitors with the same result the better place goes to the
    competitor, whose place in the registered competitors list is higher.

    For example, if Mati and Kati both have 5 pies eaten and Kati is on a higher place
    than Mati in the registered competitors list, then the better place must go to Kati
    (i.e. Kati gets 4th place and Mati gets 5th).

    It is recommended to use filter_results method here.

    The result has to be a list of tuples (name, result) where result is int (number of cakes eaten).

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :return: a sorted results list of tuples (name, number of cakes eaten).
    """
    filtered_dict = filter_results(path_to_competitors, path_to_results)
    sorted_result = sorted(filtered_dict.items(), key=lambda x: (-x[1], path_to_competitors.find(x[0])))
    print(sorted_result)
    return list(sorted_result)


def find_average_score(results: dict) -> int:
    """
    Find the average score.

    :param results: is a dictionary with the results.
    :return: average score rounded down.
    """
    scores = results.values()
    average_score = sum(scores) / len(scores)
    return int(average_score)


def write_results_csv(path_to_competitors: str, path_to_results: str, file_to_write: str) -> None:
    """
    Write the filtered and sorted results to csv file.

    The csv file must contain three columns:
    1. Place;
    2. Name;
    3. Result.

    :param path_to_competitors: is the path to the file with the names of competitors.
    :param path_to_results: is the path to the file with the results.
    :param file_to_write: is the name of the csv file.
    :return: None
    """
    place_list = []
    place = 1
    correct_results = sort_results(path_to_competitors, path_to_results)
    while place <= len(correct_results):
        place_list.append(place)
        place += 1
    final_result = zip(place_list, correct_results)
    with open(f"{file_to_write}", "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerow(["Place", "Name", "Result"])
        for row in final_result:
            writer.writerow([row[0], row[1][0], row[1][1]])


# Some examples based on the given files:
if __name__ == '__main__':
    competitors = get_competitors_list('competitors_list.txt')
    results_dict = get_results_dict('results.txt')
    filtered_results = filter_results('competitors_list.txt', 'results.txt')
    sorted_results = sort_results('competitors_list.txt', 'results.txt')

    print('Check the lengths:')
    print(len(competitors))  # -> 66
    print(len(results_dict))  # -> 93
    print(len(filtered_results))  # -> 66
    print(len(sorted_results))  # -> 66

    print('Check results for certain competitors:')
    print(results_dict['Marina Eley'])  # -> 35
    print(results_dict['Takako Vena'])  # -> 7
    print(results_dict['So Koziel'])  # -> 5
    print(results_dict['Macy Tenenbaum'] == 22)  # -> True
    print(results_dict['Edwina Alaniz'] == 48)  # -> False

    print('Check presence of the illegal competitors:')
    print('Tiffanie Mcdaniel' not in filtered_results)  # -> True
    print('Ela Gallow' not in filtered_results)  # -> True
    print('Sam Cheney' not in filtered_results)  # -> True
    print('Jayme Malachi' not in filtered_results)  # -> True
    print('Sabine Danos' not in filtered_results)  # -> True

    print('Check the order of the sorted results (must be descending):')
    values = [result[1] for result in sorted_results]
    print(all(values[i] >= values[i + 1] for i in range(65)))  # -> True

    print('Check places for certain competitors:')
    keys = [result[0] for result in sorted_results]
    print(keys.index('Ewa Grothe') + 1)  # -> 5
    print(keys.index('Cedrick Span') + 1)  # -> 20
    print(keys.index('Morris Ragusa') + 1)  # -> 37
    print(keys.index('Jaak Aaviksoo') + 1)  # -> 23
    print(keys.index('Ago Luberg') + 1)  # -> 66

    print('Check the average value:')
    print(find_average_score(results_dict))  # -> 19
    print(find_average_score(filtered_results))  # -> 19

    print('Write the results to CSV file:')
    write_results_csv('competitors_list.txt', 'results.txt', 'correct_results.csv')
