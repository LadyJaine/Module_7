team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
print("В команде Мастера кода участников: %s !"%team1_num)
print("В команде Волшебники данных участников: %s !"%team2_num)
print("Итого сегодня в командах участников: : %s и %s!" %(team1_num,team2_num))
print()
print('Команда Волшебники данных решила задач: {}!'.format(score2))
print('Команда Мастера кода решила задач: {}!'.format(score1))
print()
print("Волшебники данных решили задачи за {}!".format(team2_time))
print("Мастера кода решили задачи за {}!".format(team1_time))
print()
print(f'Команды решили {tasks_total} задач!')
print(f'Результат битвы: {challenge_result}')
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'
print(result)