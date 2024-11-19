# Первым делом напишем конструктор __init__, в котором n - кол-во параметров в формуле релевантности
# chisla_ai - n чисел a_i, используемых для вычисления релевантности
# d - количество объектов для ранжирования
# chisla_fi - это числовые признаки, записанные в d строках, в каждой по n чисел

class Relevantnost:
    def __init__(self, n, chisla_ai, d, chisla_fi):
        self.n = n
        self.chisla_ai = chisla_ai
        self.d = d
        self.chisla_fi = chisla_fi
        self.relevant_pokazatel = self.relevant()          # Вычисляем релевантность для каждого объекта

    def relevant(self):                                    # Вычисляем релевантность для каждого объекта
        return [sum(self.chisla_ai[j] * self.chisla_fi[i][j] for j in range(self.n)) for i in range(self.d)]   # Записали формулу релевантности (сумма a_i*f_i,j)

    def obnovlenie(self, index, chislo_fi_index, znach):    # Обновляем признак объекта и пересчитываем релевантность
        self.chisla_fi[index][chislo_fi_index] = znach      # Обновляем значение признака
        self.relevant_pokazatel[index] = sum(self.chisla_ai[j] * self.chisla_fi[index][j] for j in range(self.n))    # Пересчитываем релевантность

    def get_index(self, k):                                 # Получаем индексы k самых релевантных объектов
        sorted_index = sorted(range(self.d), key=lambda i: self.relevant_pokazatel[i], reverse=True)
        return [index + 1 for index in sorted_index[:k]]  # +1 для 1-индексации

##### Пример работы данного класса #####

vhod_dannye = """
2
1 100
10
1 2
2 1
3 1
4 1
5 1
6 1
7 1
8 1
9 1
10 1
4
1 2
1 10
2 4 1 1000
1 10
"""
dannye = vhod_dannye.strip().splitlines()                # Удаляем в начале и в конце пробелы и делим строки на список строк, чтобы удобнее было работать дальше
                                                         # Переводим наши строки в числа
n = int(dannye[0])
chisla_ai = list(map(int, dannye[1].split()))            # Берем вторую строку, разделяем по пробелам, у каждую часть переводим в число
d = int(dannye[2])

chisla_fi = []
for i in range(3, 3 + d):
  chisla_fi.append(list(map(int, dannye[i].split())))   # Берем третью строку, разделяем по пробелам, у каждую часть переводим в число и так до 3+d строки

q = int(dannye[3 + d]) # Со строки 3+d сичтываем число q-количество запросов

r_system = Relevantnost(n, chisla_ai, d, chisla_fi)   # Создаем объект нашего класса

results = []
for i in range(4 + d, 4 + d + q):                     # в этом цикле выполняем q запросов, всего два типа запросов
  zapros = list(map(int, dannye[i].split()))

  if zapros[0] == 1:  # Запрос на получение k самых релевантных объектов
    k = zapros[1]
    top_k = r_system.get_index(k)
    results.append(" ".join(map(str, top_k)))

  elif zapros[0] == 2:  # Запрос на изменение значения признака объекта
    _, obj_index, chislo_fi_index, znach = zapros
    r_system.obnovlenie(obj_index - 1, chislo_fi_index - 1, znach)

print("\n".join(results))