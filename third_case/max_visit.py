
def max_visit(data_for_calculation):
    """по результатам замеров найти максимальное число посетителей за день"""
    kassa1 = data_for_calculation[0]
    kassa2 = data_for_calculation[1]
    kassa3 = data_for_calculation[2]
    kassa4 = data_for_calculation[3]
    kassa5 = data_for_calculation[4]
    result = []
    for i in range(0, len(data_for_calculation)):
        sum_in_30_minut = kassa1[i] + kassa2[i] + kassa3[i] + kassa4[i] + kassa5[i]
        result.append(sum_in_30_minut)
    max_num = max(result)
    max_time = result.index(max_num)
    return max_time


if __name__ == "__main__":
    f = open('data.txt', 'r')
    data_for_calculation = [list(map(int, line.split())) for line in f]
    f.close()
    print("-------------------------------------------------------------------------")
    print("Всё время замеров разбито на 16 интервалов по 30 минут.")
    print("0 - первые 30 минут, 2 - вторые 30 минут и .... 15 - последние 30 минут")
    print("-------------------------------------------------------------------------")
    print("Наибольшее число посетителей было в {} отрезок времени".format(max_visit(data_for_calculation)))