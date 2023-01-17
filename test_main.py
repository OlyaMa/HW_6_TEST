from unittest import TestCase
import pytest
from main import geo_logs_func, geo_id_func, stats_func

class TestGeoLogsFunc(TestCase):
    def test_list(self):
        geo_logs = [
            {'visit1': ['Москва', 'Россия']},
            {'visit2': ['Дели', 'Индия']},
            {'visit3': ['Владимир', 'Россия']},
            {'visit4': ['Лиссабон', 'Португалия']},
            {'visit5': ['Париж', 'Франция']},
            {'visit6': ['Лиссабон', 'Португалия']},
            {'visit7': ['Тула', 'Россия']},
            {'visit8': ['Тула', 'Россия']},
            {'visit9': ['Курск', 'Россия']},
            {'visit10': ['Архангельск', 'Россия']}
        ]
        res = geo_logs_func(geo_logs)
        self.assertEqual(res, [{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']}, {'visit7': ['Тула', 'Россия']}, {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']}, {'visit10': ['Архангельск', 'Россия']}])


class TestGeoIdFunc(TestCase):
    def test_ids(self):
        ids = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}
        res = geo_id_func(ids)
        self.assertEqual(res, {98, 35, 213, 54, 119, 15})

@pytest.mark.parametrize(
    'stats, result', [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
        ({'facebook': 70, 'yandex': 80, 'vk': 115, 'google': 100, 'email': 50}, 'vk'),
        ({'facebook': 100, 'yandex': 90, 'vk': 20}, 'facebook')
    ]
)
def test_stats_func(stats, result):
    res = stats_func(stats)
    assert res == result






