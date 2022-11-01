from datetime import datetime as dt
from time import time

def calc_logger(data, user_expression):
    time = dt.now().strftime('%H:%M')
    with open('log.csv', 'a') as file:
        file.write('{}; {} Result = {}\n'
                    .format(time, user_expression, data))

