
def calculate_median_without_statistics_module(median_target_values):
    # Calculates the median (中央値) from the elements in median_target_values.
    median_target_values_sorted = sorted(median_target_values)
    if len(median_target_values) % 2 == 0: # In case the list has even numbers of elements.
        median_target_candidates = [median_target_values_sorted[(int(len(median_target_values_sorted)/2) - 1)], median_target_values_sorted[int(len(median_target_values_sorted)/2)]] # Sorts the median_target_values and find 2 candidates for the median.
        target_median = sum(median_target_candidates) / len(median_target_candidates)
    else: # In case the list has odd numbers of elements.
        median_target_candidates = [median_target_values_sorted[int((len(median_target_values_sorted)/2) + 1)]] # Sorts the median_target_values and find 1 candidate for the median.
        target_median = median_target_candidates[0]