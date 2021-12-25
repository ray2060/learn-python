import csv


with open('C:\\_ray\\dev\\learn-python\\exercise\\csv\\xiaoming.csv', 
    'w', 
    newline = '', 
    encoding = 'utf-8'
    ) as f:
    fo = csv.writer(f)
    fo.writerow(['城市', '人口/万', 'GDP总额/亿元'])
    fo.writerows([
            ['A', '2424', '38155'],
            ['B', '2171', '35371'],
            ['C', '1302', '26927'],
            ['D', '1491', '23628'],
            ['E', '3372', '23605'],
            ['F', '1073', '19235']
        ])
