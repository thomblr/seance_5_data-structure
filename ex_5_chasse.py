def get_points(victims):
    """
    Returns the number of points you get with the victims
    :param victims: list of the victims (list)
    :return: the number of points (int)
    """

    targets = {
        'chicken': 1,
        'dog': 3,
        'cow': 5,
        'man': 10
    }

    points = 100

    for element in victims:
        if element in targets:
            points += targets[element]

    return points


def get_cost(victims):
    """
    Returns the cost of killing the victims
    :param victims: list of the victims (list)
    :return: the cost (int)
    """

    cost = 200
    if get_points(victims) > 100:
        cost += 200 * ((get_points(victims) // 100) - 1)

    return cost
