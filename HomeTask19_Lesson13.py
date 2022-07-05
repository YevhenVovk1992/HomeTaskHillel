import math


total_sale = -1
coffee = dict()
tea = dict()
top_15 = dict()
sales_month = dict()
sales_time = dict()


# function to populate dictionaries
def add_key(dictionary: dict, key_word, val=1) -> dict:
    if key_word in dictionary:
        dictionary[key_word] += val
    else:
        dictionary[key_word] = val
    return dictionary


# open file and start the analysis loop
data = open('Bakery.csv', 'r')
while True:
    line = data.readline().strip()
    if line == '':
        break

    # Skip the first line
    if total_sale == -1:
        total_sale = 0
        continue
    item = line.split(',')[1]
    day_type = line.split(',')[-1]
    date_time = line.split(',')[2]

    # Number of items sold
    add_key(top_15, item)

    # Analysis of sales of coffee and tea
    if item == 'Coffee':
        add_key(coffee, day_type)
    if item == 'Tea':
        add_key(tea, day_type)

    # Distribution of sales by months and hours
    add_key(sales_month, date_time[0:7])
    add_key(sales_time, date_time[11:13])
    total_sale += 1
data.close()

print('TOP 15 items: ')
for key, value in sorted(top_15.items(), key=lambda x: x[1], reverse=True)[0:15]:
    print(key,'-', value, end=', ')
print('\n')
print('Coffee weekday -', math.trunc((coffee['Weekday']/top_15['Coffee'])*100),
      'Tea weekday -', math.trunc((tea['Weekday']/top_15['Tea'])*100)
)
print('Coffee weekend -', math.trunc((coffee['Weekend']/top_15['Coffee'])*100),
      'Tea weekend -', math.trunc((tea['Weekend']/top_15['Tea'])*100)
)
print()
print('Распределение продаж по месяцам: ')
for key, value in sorted(sales_month.items(), key=lambda x: x[0]):
    print(key,'-',  round((value/total_sale)*100, 2))
print()
print('Распределение продаж по часам работы пекарни: ')
for key, value in sorted(sales_time.items(), key=lambda x: x[0]):
    print(key, '-', round((value/total_sale)*100, 2))

