
import pytest
import statistics
from statistics_formulae import calculate_median_without_statistics_module
import numpy as np

def test_calculate_arithmetic_mean_without_statistics_module():
    # Calculates the arithmetic mean (平均値) from the elements in mean_target_values.
    mean_target_values = [1000, 500, 700, 1200, 800]
    mean_target_sum = sum(mean_target_values)
    target_mean = mean_target_sum / len(mean_target_values)
    assert target_mean == 840

def test_calculate_arithmetic_mean_with_statistics_module():
    # Calculates the arithmetic mean (平均値) from the elements in mean_target_values.
    mean_target_values = [1000, 500, 700, 1200, 800]
    target_mean = statistics.mean(mean_target_values)
    assert target_mean == 840

def test_calculate_median_without_statistics_module():
    # Calculates the median (中央値) from the elements in median_target_values.
    median_target_values = [0, 1, 2, 3, 6, 7, 7, 8, 10, 12]
    median_target_values_sorted = sorted(median_target_values)
    if len(median_target_values) % 2 == 0: # In case the list has even numbers of elements.
        median_target_candidates = [median_target_values_sorted[(int(len(median_target_values_sorted)/2) - 1)], median_target_values_sorted[int(len(median_target_values_sorted)/2)]] # Sorts the median_target_values and find 2 candidates for the median.
        target_median = sum(median_target_candidates) / len(median_target_candidates)
    else: # In case the list has odd numbers of elements.
        median_target_candidates = [median_target_values_sorted[int(len(median_target_values_sorted)/2)]] # Sorts the median_target_values and find 1 candidate for the median.
        target_median = median_target_candidates[0]
    assert target_median == 6.5

def test_calculate_median_with_statistics_module():
    # Calculates the median (中央値) from the elements in median_target_values.
    median_target_values = [0, 1, 2, 3, 6, 7, 7, 8, 10, 12]
    target_median = statistics.median(median_target_values)
    assert target_median == 6.5

def test_calculate_mode_without_statistics_module():
    # Calculates the mode (最頻値) from the elements in mode_target_values.
    mode_target_values = [300, 100, 200, 100, 400, 150, 100, 200, 200, 150, 200, 50, 300]
    no_duplicates_list = list(set(mode_target_values)) # Makes a list of values without duplicates.
    duplicates_dict = {}
    for target_number in no_duplicates_list:
        # Assigns each number in no_duplicates_list to the dictionary key and the numbers of its duplicates to the dictionary value.
        duplicates_dict[target_number] = mode_target_values.count(target_number)
    mode = max(duplicates_dict, key=duplicates_dict.get) # Finds the max number among the values in the duplicates_dict dictionary.
    assert mode == 200
"""
ところでモードが複数の場合をカバーしてない気がする〜
"""

def test_calculate_mode_with_statistics_module():
    # Calculates the mode (最頻値) from the elements in mode_target_values.
    mode_target_values = [300, 100, 200, 100, 400, 150, 100, 200, 200, 150, 200, 50, 300]
    target_mode = statistics.mode(mode_target_values)
    assert target_mode == 200

@pytest.mark.parametrize(
    "quartiles_target_values, quartiles_1_expected, quartiles_2_expected, quartiles_3_expected, interquartile_range_expected",
    [([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2], 3.0, 3.75, 4.2, 1.2),
     ([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2, 3.8], 3.0, 3.8, 4.2, 1.2),
     ([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2, 3.8, 4.6], 3.2, 3.9, 4.4, 1.2)]
)
def test_calculate_quartiles_without_statistics_module(quartiles_target_values, quartiles_1_expected, quartiles_2_expected, quartiles_3_expected, interquartile_range_expected):
    # Calculates the quartiles（四分位数） from the elements in quartiles_target_values.
    quartiles_target_values_sorted = sorted(quartiles_target_values) # Creates a sorted list.
    quartiles_2 = calculate_median_without_statistics_module(quartiles_target_values) # Calculates the median of the quartiles_target_values_sorted list.
#    quartiles_2_index = quartiles_target_values_sorted.index(quartiles_2) # Verifies the index of the median of the quartiles_target_values_sorted list.
    quartiles_target_values_sorted_before_quartiles_2 = []
    quartiles_target_values_sorted_after_quartiles_2 = []
    if len(quartiles_target_values) % 2 == 0: # In case the list has even numbers of elements.
        for index_before in range(0, int(len(quartiles_target_values_sorted)/2)):
            # Creates a new list of the values until the quartiles_2.
            quartiles_target_values_sorted_before_quartiles_2.append(quartiles_target_values_sorted[index_before])
        for index_after in range(int(len(quartiles_target_values_sorted)/2), len(quartiles_target_values_sorted)):
            # Creates a new list of the values from the quartiles_2.
            quartiles_target_values_sorted_after_quartiles_2.append(quartiles_target_values_sorted[index_after])
        quartiles_1 = calculate_median_without_statistics_module(quartiles_target_values_sorted_before_quartiles_2)
        quartiles_3 = calculate_median_without_statistics_module(quartiles_target_values_sorted_after_quartiles_2)
    else: # In case the list has odd numbers of elements.
        quartiles_2_index = quartiles_target_values_sorted.index(quartiles_2)  # Verifies the index of the median of the quartiles_target_values_sorted list.
        for index_before in range(0, quartiles_2_index):
            # Creates a new list of the values before the quartiles_2.
            quartiles_target_values_sorted_before_quartiles_2.append(quartiles_target_values_sorted[index_before])
        for index_after in range(quartiles_2_index + 1, len(quartiles_target_values_sorted)):
            # Creates a new list of the values after the quartiles_2.
            quartiles_target_values_sorted_after_quartiles_2.append(quartiles_target_values_sorted[index_after])
        quartiles_1 = calculate_median_without_statistics_module(quartiles_target_values_sorted_before_quartiles_2)
        quartiles_3 = calculate_median_without_statistics_module(quartiles_target_values_sorted_after_quartiles_2)
    interquartile_range = quartiles_3 - quartiles_1
    assert quartiles_1 == quartiles_1_expected
    assert quartiles_2 == quartiles_2_expected
    assert quartiles_3 == quartiles_3_expected
    assert interquartile_range == pytest.approx(interquartile_range_expected)

# ON HOLD
# @pytest.mark.parametrize(
#     "quartiles_target_values_with, quartiles_1_expected_with, quartiles_2_expected_with, quartiles_3_expected_with, interquartile_range_expected_with",
#     [([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2], 3.0, 3.75, 4.2, 1.2),
#      ([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2, 3.8], 3.0, 3.8, 4.2, 1.2),
#      ([3.0, 4.0, 5.5, 3.5, 4.2, 3.4, 2.8, 4.2, 4.7, 2.2, 3.8, 4.6], 3.2, 3.9, 4.4, 1.2)]
# )
# def test_calculate_quartiles_with_statistics_module(quartiles_target_values_with, quartiles_1_expected_with, quartiles_2_expected_with, quartiles_3_expected_with, interquartile_range_expected_with):
#     quartiles_1, quartiles_2, quartiles_3 = statistics.quantiles(quartiles_target_values_with, n=4) # Errors with wrong results
#     # quartiles_1 = np.percentile(quartiles_target_values_with, 25)
#     # quartiles_2 = np.percentile(quartiles_target_values_with, 50)
#     # quartiles_3 = np.percentile(quartiles_target_values_with, 75)
#     interquartile_range = quartiles_3 - quartiles_1
#     assert quartiles_1 == pytest.approx(quartiles_1_expected_with)
#     assert quartiles_2 == pytest.approx(quartiles_2_expected_with)
#     assert quartiles_3 == pytest.approx(quartiles_3_expected_with)
#     assert interquartile_range == interquartile_range_expected_with

@pytest.mark.parametrize(
    "population_variance_target_values_with, population_variance_expected_with",
    [
        ([40, 35, 30, 25, 30], 26),
        ([50, 30, 60, 25, 65], 254)
    ]
)
def test_calculate_population_variance_with_statistics_module(population_variance_target_values_with, population_variance_expected_with):
    population_variance_result = statistics.pvariance(population_variance_target_values_with)
    assert population_variance_result == population_variance_expected_with

@pytest.mark.parametrize(
    "population_variance_target_values, population_variance_expected",
    [
        ([40, 35, 30, 25, 30], 26),
        ([50, 30, 60, 25, 65], 254)
    ]
)
def test_calculate_population_variance_without_statistics_module(population_variance_target_values_with, population_variance_expected_with):
    pass

"""
calculate mean -> use my mean def
subtract mean from each value
square each subtracted value
sum up the squared values
divide the sum by the number of samples
"""