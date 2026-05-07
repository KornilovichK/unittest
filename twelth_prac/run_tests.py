#!/usr/bin/env python3
import unittest

if __name__ == '__main__':
    # Запускаем все тесты из tests/ директории
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)