
import pytest
import statistics

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
        median_target_candidates = [median_target_values_sorted[int((len(median_target_values_sorted)/2) + 1)]] # Sorts the median_target_values and find 1 candidate for the median.
        target_median = median_target_candidates[0]
    assert target_median == 6.5
