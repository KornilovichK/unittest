#!/bin/bash

echo "=== ЭТАП 1: Запуск слабых тестов (шумные и медленные) ==="
echo "Команда: python -m unittest discover -b --locals -v tests.test_user_profile_initial"
python -m unittest discover -b --locals -v tests.test_user_profile_initial

echo -e "\n=== ЭТАП 2: Улучшенные тесты (говорящий failure) ==="
echo "Теперь failure показывает точную причину:"
python -m unittest tests.test_user_profile_improved -v

echo -e "\n=== ЭТАП 3: Исправляем баг в production коде ==="
echo "Нужно заменить .upper() на .lower() в app/user_profile.py"
read -p "Нажмите Enter после исправления бага..."

echo -e "\n=== ЭТАП 4: Запуск исправленных тестов ==="
python -m unittest tests.test_user_profile_improved -v

echo -e "\n=== ЭТАП 5: Тесты контрактов (warnings и logs) ==="
python -m unittest tests.test_user_profile_contracts -v

echo -e "\n=== ЭТАП 6: Измерение скорости МЕДЛЕННЫХ тестов ==="
echo "Запуск с --durations=0 -v:"
python -m unittest tests.test_user_profile_initial.TestWaitUntilReadySlow --durations=0 -v

echo -e "\n=== ЭТАП 7: Быстрые тесты (после оптимизации) ==="
python -m unittest tests.test_user_profile_fast -v

echo -e "\n=== ЭТАП 8: Финальный замер скорости ==="
echo "Все тесты вместе с быстрыми версиями:"
python -m unittest tests.test_user_profile_improved tests.test_user_profile_contracts tests.test_user_profile_fast --durations=0 -v