filename = "opendata.stat.txt"
pensions = []

try:
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            data = line.strip().split(',')

            if len(data) < 4:
                continue

            if (data[0] == "Средняя пенсия" and
                    data[1] == "Забайкальский край" and
                    data[2].startswith("2018")):

                try:
                    pensions.append(float(data[3]))
                except ValueError:
                    continue

except FileNotFoundError:
    print(f"Файл '{filename}' не найден.")
    exit()

if not pensions:
    print("Нет данных о пенсиях в Забайкальском крае за 2018 год.")
    exit()

average = sum(pensions) / len(pensions)
print(f"Средняя пенсия в Забайкальском крае в 2018 году: {average:.2f} руб.")

# Визуализация
try:
    import matplotlib.pyplot as plt

    plt.plot(range(1, len(pensions) + 1), pensions, marker='o')
    plt.title("Средняя пенсия в Забайкальском крае (2018)")
    plt.xlabel("Месяц")
    plt.ylabel("Рубли")
    plt.grid(True)
    plt.xticks(range(1, len(pensions) + 1))
    plt.show()

except ImportError:
    print("Для построения графика установите matplotlib: pip install matplotlib")