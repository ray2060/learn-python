import sys


DICT_MAN = {
    2:[16.3, 17.7, 18.6],
    3:[15.7, 17.0, 17.9],
    4:[15.3, 16.7, 17.6],
    5:[15.2, 16.7, 17.6],
    6:[15.3, 17.0, 18.1],
    7:[15.6, 17.5, 18.8],
    8:[16.0, 18.1, 19.7],
    9:[16.4, 18.9, 20.7],
    10:[17.0, 19.6, 21.7],
    11:[17.5, 20.5, 22.7],
    12:[18.1, 21.2, 23.6],
    }
DICT_WOMAN = {
    2:[15.9, 17.3, 18.3],
    3:[15.4, 16.8, 17.7],
    4:[15.3, 16.5, 17.5],
    5:[15.2, 16.5, 17.5],
    6:[15.0, 16.5, 17.6],
    7:[15.0, 16.7, 17.9],
    8:[15.2, 17.1, 18.5],
    9:[15.6, 17.7, 19.2],
    10:[16.1, 18.4, 20.1],
    11:[16.7, 19.3, 21.2],
    12:[17.4, 20.2, 22.3],
    }


def assess(ls, BMI):
    if BMI <= ls[0]:
        return 'lanky'
    elif BMI <= ls[1]:
        return 'normal'
    elif BMI <= ls[2]:
        return 'overweight'
    else:
        return 'fat'

def get_input_value():
    global height
    height = float(input('height(m)(>0):'))
    global weight
    weight = float(input('weight(kg)(>0):'))
    global age
    age = int(input('age(2-60)(integer):'))
    global sex
    sex = input('sex(m or f):')


try:
    get_input_value()
except ValueError:
    sys.exit('The input values do not meet the requirements!')
if height <= 0 or weight <= 0 or age < 2 or age > 60 or (sex != 'm' and sex != 'f') or age % 1 != 0:
    sys.exit('The input values do not meet the requirements!')
BMI = weight / height ** 2
if age >= 13 and age <= 60:
    print(assess([18.7, 21.9, 24.4], BMI))
if sex == 'm':
    print(assess(DICT_MAN[age], BMI))
if sex == 'f':
    print(assess(DICT_WOMAN[age], BMI))
print('BMI:%.5f' % (BMI))
