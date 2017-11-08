def get_minimal_cuts(amount):
    """
    Returns the minimal cuts with amount of money
    :param amount: your amount of money (int)
    :return: the minimal number of cuts (int)
    """

    cuts = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    minimal_cuts = {}

    for cut in cuts:
        if amount >= cut:
            minimal_cuts[cut] = amount // cut
            amount -= minimal_cuts[cut] * cut

    return minimal_cuts


print(get_minimal_cuts(2017))
