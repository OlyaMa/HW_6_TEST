import requests

def geo_logs_func(geo_logs):

    index = 0
    x =[]
    for visits in geo_logs:
        for country in visits.values():
            if country[1] == 'Россия':
              x.append(geo_logs[index])
            index +=1
    geo_logs = x
    return geo_logs


def geo_id_func(ids):

    z = set()
    for users in ids:
      set_user = set(ids[users])
      z = set_user | z
    return z


def stats_func(stats):

    max_value = 0
    chanal = ''
    for key, value in stats.items():
      if value > max_value:
        max_value = value
        chanal = key
    return chanal


# Создание папки на Яндекс-диске
token="" # Необходимо указать токен
def create_folder(path):
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(f'{URL}?path={path}', headers=headers)
    return response




