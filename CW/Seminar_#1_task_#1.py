# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.


n = int(input('Введите сколько за день машина проезжает км.: '))
total_km = int(input('Введите сколько машина должна проехать км.: '))
result = (n - 1 + total_km) // n
print(f'Машина проедет {total_km} км. за {result} дня(-ей) ')