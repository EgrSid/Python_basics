import numpy as np
import pandas as pd
import unittest
from tools_ML import detect_outliers, fillna, corr_features


def check_types(values: list, target_type: tuple | type) -> bool:
    """Проверка типов входных данных"""
    return all(isinstance(value, target_type) for value in values)


def create_random_df_with_outliers(num_cols, num_rows_without_outliers, num_outliers):
    """Создание df с выбросами и сохранение индексов выбросов"""
    assert check_types([num_cols, num_outliers, num_rows_without_outliers], int) and \
           num_rows_without_outliers >= num_outliers and all([num_cols, num_outliers, num_rows_without_outliers]) > 0, (
        'Incorrect parameter type or num_outliers. All parameters must be '
        'int and num_rows_without_outliers >= num_outliers')

    df = pd.DataFrame(np.random.rand(num_rows_without_outliers, num_cols))
    num_outliers = [num_outliers for _ in range(num_cols)]
    out = []  # индексы выбросов в датасете
    for i in range(num_cols):
        outlier_rows = np.random.choice(num_rows_without_outliers, num_outliers[i], replace=False)
        out.extend([outlier_rows])
        df.iloc[outlier_rows, i] = np.random.rand(num_outliers[i]) * 100 + np.mean(df.iloc[:, i])

    return df, out


class Outliers_test(unittest.TestCase):

    df, out = create_random_df_with_outliers(3, 100000, 10)

    def test_detect_outliers_sigma(self):
        self.assertEqual(detect_outliers(self.df).values.tolist(), self.out)

    def test_detect_outliers_tukey(self):
        self.assertEqual(detect_outliers(self.df, method='tukey').values.tolist(), self.out)


if __name__ == '__main__':
    unittest.main()
