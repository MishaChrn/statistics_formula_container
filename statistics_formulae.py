
import numpy as np

def calculate_median_without_statistics_module(median_target_values):
    # Calculates the median (中央値) from the elements in median_target_values.
    median_target_values_sorted = sorted(median_target_values)
    if len(median_target_values) % 2 == 0: # In case the list has even numbers of elements.
        median_target_candidates = [median_target_values_sorted[(int(len(median_target_values_sorted)/2) - 1)], median_target_values_sorted[int(len(median_target_values_sorted)/2)]] # Sorts the median_target_values and find 2 candidates for the median.
        target_median = sum(median_target_candidates) / len(median_target_candidates)
    else: # In case the list has odd numbers of elements.
        median_target_candidates = [median_target_values_sorted[int(len(median_target_values_sorted)/2)]] # Sorts the median_target_values and find 1 candidate for the median.
        target_median = median_target_candidates[0]
    return target_median

def calculate_arithmetic_mean_without_statistics_module(mean_target_values):
    # Calculates the arithmetic mean (平均値) from the elements in mean_target_values.
    mean_target_sum = sum(mean_target_values)
    target_mean = mean_target_sum / len(mean_target_values)
    return target_mean

def calculate_population_variance_without_statistics_module(population_variance_target_values):
    population_variance_target_value_mean = calculate_arithmetic_mean_without_statistics_module(population_variance_target_values)
    subtracted_population_variance_values = [population_variance_target_value - population_variance_target_value_mean for population_variance_target_value in population_variance_target_values]
    squared_subtracted_population_variance_values = np.square(subtracted_population_variance_values)
    sum_of_squared_population_variance_values = sum(squared_subtracted_population_variance_values)
    population_variance = sum_of_squared_population_variance_values / len(population_variance_target_values)
    return population_variance

def calculate_population_standard_deviation_without_statistics_module(population_standard_deviation_target_values):
    population_variance = calculate_population_variance_without_statistics_module(population_standard_deviation_target_values)
    population_standard_deviation_result = abs(population_variance ** 0.5)
    return population_standard_deviation_result

