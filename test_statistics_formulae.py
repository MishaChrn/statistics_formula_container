
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

def test_calculate_median_with_statistics_module():
    # Calculates the median (中央値) from the elements in median_target_values.
    median_target_values = [0, 1, 2, 3, 6, 7, 7, 8, 10, 12]
    target_median = statistics.median(median_target_values)
    assert target_median == 6.5

def test_calculate_mode_without_statistics_module():
    # Calculates the mode (最頻値) from the elements in mode_target_values.
    mode_target_values = [300, 100, 200, 100, 400, 150, 100, 200, 200, 150, 200, 50, 300]
    iteration_indexes = [0]
    for target_index in range(len(mode_target_values)):
        if target_index == 0:
            continue
    """
    重複していない値を.cont()に渡して出現回数を数えさせたい。
    mode_target_values[0]のときは無条件でiteration_indexesにリストインデックスを.append()。
    mode_target_values[1]以降のとき、もし重複があればiteration_indexesにリストインデックスを.append()しない。
    
    モジュールを使うとこう：
    result = statistics.mode(mode_target_values)
    """

