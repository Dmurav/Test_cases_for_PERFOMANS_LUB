
def where_dot(coordinates, dot):

    a, b, c, d = coordinates
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    cx, cy = c[0], c[1]
    dx, dy = d[0], d[1]
    x, y = dot[0], dot[1]

    vertex_cond = (x == coordinates[0][0] and y == coordinates[0][1]
                   or x == coordinates[1][0] and y == coordinates[1][1]
                   or x == coordinates[2][0] and y == coordinates[2][1]
                   or x == coordinates[3][0] and y == coordinates[3][1])
    if vertex_cond:
        print('точка - вершина четырехугольника')
        return

    side_cond = ((y - ay) * (bx - ax) == (x - ax) * (by - ay) or
                 (y - by) * (cx - bx) == (x - bx) * (cy - by) or
                 (y - cy) * (dx - cx) == (x - cx) * (dy - cy) or
                 (y - dy) * (cx - dx) == (x - dx) * (ay - dy))
    if side_cond:
        print('точка лежит на сторонах четырехугольника')
        return

    in_cond = (
        ((bx - ax) * (y - ay) < (by - ay) * (x - ax)) and
        ((cx - bx) * (y - by) < (cy - by) * (x - bx)) and
        ((dx - cx) * (y - cy) < (dy - cy) * (x - cx)) and
        ((ax - dx) * (y - dy) < (ay - dy) * (x - dx))
    )

    if in_cond:
        print('точка внутри четырехугольника')
        return

    print('точка снаружи четырехугольника')


if __name__ == '__main__':
    f = open('data.txt', 'r')
    data_for_calculation = [list(map(float, line.split())) for line in f]
    f.close()
    dot = list(map(float, input("Введите два числа через пробел (x y): ").split()))
    where_dot(data_for_calculation, dot)