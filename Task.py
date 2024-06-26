# Опис домашнього завдання​

# Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
# використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
# Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин,
# а загальні витрати дорівнюють сумі з'єднання всіх кабелів.

# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq

def connect_cabel(cabels):
    if cabels:
        heapq.heapify(cabels)
        while len(cabels) > 1:
            first = heapq.heappop(cabels)
            second = heapq.heappop(cabels)
            print(f"З'єднання кабелів {first} i {second}")
            heapq.heappush(cabels, first+second)
            print(f"Усі кабелі {cabels}")
        return cabels[0]

def main():
    cabels = [4, 10, 3, 5, 1]
    print(f"Загальні витрати дорівнюють: {connect_cabel(cabels)}")

if __name__ == "__main__":
    main()