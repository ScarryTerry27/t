import matplotlib.pyplot as plt
import pandas as pd

# Сброс ограничений на количество выводимых рядов
pd.set_option('display.max_rows', None)

agents = pd.read_csv('travel_agents.csv', delimiter=';')
travels = pd.read_csv('travels.csv', delimiter=';')
sales = pd.read_csv('sale_of_tour_packages.csv', delimiter=';')

agents.head()
travels.head()
sales.tail()
# Соединим все полученные данные в один DataFrame
tmp = pd.merge(sales, agents)
all_tours = pd.merge(tmp, travels)
all_tours.head()

# получаем уникальные значения (города)
df = pd.DataFrame(all_tours)

# Get the unique values of 'B' column
df['Город'].unique()

# список названий региональных центров
region_centers = ['Москва', 'Ярославль', 'Сыктывкар', 'Иваново', 'Архангельск',
                  'Кострома', 'Псков', 'Тверь', 'Вологда', 'Петрозаводск', 'Мурманск']

# Группируем по дате
task1 = all_tours.groupby('Город')
# Находим для каждой группы общее количество путевок
task1_max = task1.aggregate({'Количество проданных путёвок': 'sum'})

task1_1 = all_tours[all_tours['Город'].isin(region_centers)]  # отбор городов, которые являются региональными центрами
task_req = task1_1.groupby('Город')  # группировка по городу
task_sum = task_req.aggregate({'Количество проданных путёвок': 'sum'})  # нахождение количества проданных путевок

# Отберем строки, в которых ресь идет о туроператоре "Горизонт"
gorizont = all_tours[all_tours['Название'] == 'Горизонт']

# Сгруппируем эти строки по полю "Город" и найдем сумму по каждой группе
task2 = gorizont.groupby('Город')['Количество проданных путёвок'].sum()

# Строим круговую диаграмму по этим данным
pie, ax = plt.subplots(figsize=[10, 6])
labels = task2.keys()
plt.pie(x=task2, autopct="%.1f%%", labels=labels, pctdistance=0.8)
plt.title("Туроператор Горизонт. Путевки", fontsize=14)
plt.show()

dream = all_tours[all_tours['Название'] == 'Мечта']
# Сгруппируем эти строки по дням и найдем сумму по каждой группе
task3 = dream.groupby('Дата')['Количество проданных путёвок'].sum()

task3.plot.bar()
plt.show()

