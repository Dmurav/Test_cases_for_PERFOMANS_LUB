
def where_dot(coordinates, dot):

    a, b, c, d = coordinates
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]
    dx, dy = d[0], d[1]
    x, y = dot[0], dot[1]

    if x == coordinates[0][0] and y == coordinates[0][1] \
            or x == coordinates[1][0] and y == coordinates[1][1] \
            or x == coordinates[2][0] and y == coordinates[2][1] \
            or x == coordinates[3][0] and y == coordinates[3][1]:
        print('точка - вершина четырехугольника')
    elif (y - ay) * (bx - ax) == (x - ax) * (by - ay) or \
            (y - by) * (cx - bx) == (x - bx) * (cy - by) or \
            (y - cy) * (dx - cx) == (x - cx) * (dy - cy) or \
            (y - dy) * (cx - dx) == (x - dx) * (ay - dy):
        print('точка лежит на сторонах четырехугольника')
    elif (x - ax) * (x - bx) <= 0 and (y - ay) * (y - by) <= 0 \
            or (x - bx) * (x - cx) <= 0 and(y - by) * (y - cy) <= 0 \
            or (x - cx) * (x - dx) <= 0 and (y - cy) * (y - dy) <= 0 \
            or (x - dx) * (x - ax) <= 0 and (y - dy) * (y - ay) <= 0:
        print('точка внутри четырехугольника')
    else:
        print('точка снаружи четырехугольника')


if __name__ == '__main__':
    f = open('data.txt', 'r')
    data_for_calculation = [list(map(float, line.split())) for line in f]
    f.close()
    dot = list(map(float, input("Введите два числа через пробел (x y): ").split()))
    where_dot(data_for_calculation, dot)