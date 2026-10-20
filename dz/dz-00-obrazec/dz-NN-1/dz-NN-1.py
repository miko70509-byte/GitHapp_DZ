distance = 500
fuel_price = 45.5
fuel_efficiency = 12
cost_home = 2500

fuel_cost = (distance / fuel_efficiency) * fuel_price
total_cost = fuel_cost + cost_home

print("Стоимость путешествия:")
print(f"Расходы на топливо: {fuel_cost:.2f} руб.")
print(f"Расходы на проживание: {cost_home:.2f} руб.")
print(f"Общая стоимость: {total_cost:.2f} руб.")
