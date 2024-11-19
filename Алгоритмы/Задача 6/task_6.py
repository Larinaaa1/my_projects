from collections import defaultdict         # defaultdict — словарь, который при вызове отсутствующего ключа записывает значение по умолчанию, я использую defaultdict(int) - значит по умолчанию будет 0
from datetime import datetime, timedelta    # datetime используется для создания объектов даты и времени, а timedelta — для работы с промежутками времени (длительностью даты)

def gosti_max(gosti):
  count = defaultdict(int)                  # Создаем счетчик, который будет хранить количество гостей для каждой даты. Если дата (ключ) отсутствует в словаре, то автоматически значение 0
  for zaezd, otezd in gosti:                # Проходимся по кортежу и преобразовываем даты из строк в объекты datetime
    a = datetime.strptime(zaezd,"%Y-%m-%d")
    b = datetime.strptime(otezd, "%Y-%m-%d")
    count[a] += 1
    count[b + timedelta(days=1)] -= 1       # Берем день отъезда и следующий день, в след день после отъезда они не считаются присутствующими
  now_gosti = 0
  max_gosti = 0
  max_date = None
  # print(count)
  for date in sorted(count.keys()):
    now_gosti += count[date]               # Добавляем количество приехавших / отнимаем уехавших гостей
    if now_gosti > max_gosti:
      max_gosti = now_gosti
      max_date = date
  return max_date.strftime("%Y-%m-%d"), max_gosti       # Прелбразуем дату в строку


##### Пример использования #####
g = [("2024-09-15","2024-09-15"), ("2024-09-14","2024-09-21"),("2024-09-11","2024-09-29"), ("2024-09-10","2024-09-13")]
result_date, result_count = gosti_max(g)
print(f"Наиболее загруженный день: {result_date}, количество гостей в этот день: {result_count}")


