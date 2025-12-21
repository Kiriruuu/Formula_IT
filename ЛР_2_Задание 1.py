money_capital = 20000  # Подушка безопасности
salary = 5000          # Ежемесячная зарплата
spend = 6000           # Траты за первый месяц
increase = 0.05        # Ежемесячный рост цен

months = 0
current_spend = spend

while True:
    # Бюджет текущего месяца
    budget = money_capital + salary

    # Проверяем, хватает ли денег
    if budget >= current_spend:
        months += 1

        # Обновляем подушку безопасности
        money_capital = budget - current_spend

        # Увеличиваем траты со следующего месяца
        current_spend = current_spend * (1 + increase)
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)
