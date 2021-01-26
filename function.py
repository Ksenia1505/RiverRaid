def is_line_intersection(line_plane, line_ship):
    """Проверка пересечения линий"""
    plane_x1, plane_y1, plane_x2, plane_y2 = line_plane[0][0], line_plane[0][1], line_plane[1][0], line_plane[1][1]
    ship_x1, ship_y1, ship_x2, ship_y2 = line_ship[0][0], line_ship[0][1], line_ship[1][0], line_ship[1][1]
    delta = 1
    # если есть пересечение по горизонтальной стороне
    if abs(plane_y1 - ship_y1) <= delta and abs(plane_y2 - ship_y2) <= delta:
        if min(plane_x1, plane_x2) <= max(ship_x1, ship_x2):
            if max(plane_x1, plane_x2) >= min(ship_x1, ship_x2):
                return True
        elif min(ship_x1, ship_x2) <= max(plane_x1, plane_x2):
            if max(ship_x1, ship_x2) >= min(plane_x1, plane_x2):
                return True
        return False
    # если есть пересечение по вертикальной стороне
    elif abs(plane_x1 - ship_x1) <= delta and abs(plane_x2 - ship_x2) <= delta:
        if min(plane_y1, plane_y2) <= max(ship_y1, ship_y2):
            if max(plane_y1, plane_y2) >= min(ship_y1, ship_y2):
                return True
        elif min(ship_y1, ship_y2) <= max(plane_y1, plane_y2):
            if max(ship_y1, ship_y2) >= min(plane_y1, plane_y2):
                return True
        return False
    else:
        d = (ship_y2 - ship_y1) * (plane_x2 - plane_x1) - (ship_x2 - ship_x1) * (plane_y2 - plane_y1)
        if d:
            uA = ((ship_x2 - ship_x1) * (plane_y1 - ship_y1) - (ship_y2 - ship_y1) * (plane_x1 - ship_x1)) / d
            uB = ((plane_x2 - plane_x1) * (plane_y1 - ship_y1) - (plane_y2 - plane_y1) * (plane_x1 - ship_x1)) / d
        else:
            return False
        if not (0 <= uA <= 1 and 0 <= uB <= 1):
            return False
        return True


def calculatePoints(object):
    """Вычисление вершин"""
    object.point_1 = [object.x, object.y]
    object.point_2 = [object.x, object.y + object.h]
    object.point_3 = [object.x + object.w, object.y + object.h]
    object.point_4 = [object.x + object.w, object.y]


def is_plane_collided_with_ship(plane, ship):
    """Проверка на столкновения корабля и самолета"""
    calculatePoints(ship)
    calculatePoints(plane)

    lines_plane = [[plane.point_1, plane.point_2],
                   [plane.point_2, plane.point_3],
                   [plane.point_3, plane.point_4],
                   [plane.point_4, plane.point_1]]

    lines_ship = [[ship.point_1, ship.point_2],
                  [ship.point_2, ship.point_3],
                  [ship.point_3, ship.point_4],
                  [ship.point_4, ship.point_1]]

    for line_plane in lines_plane:
        for line_ship in lines_ship:
            if is_line_intersection(line_plane, line_ship):
                return True
    return False


def is_shell_collided_with_ship(shell, ship):
    """Проверка на столкновения снаряда и корабля"""
    calculatePoints(ship)

    if abs(shell.y - ship.point_2[1]) <= shell.radius and \
            ship.point_2[0] <= shell.x <= ship.point_3[0]:
        return True
    return False
