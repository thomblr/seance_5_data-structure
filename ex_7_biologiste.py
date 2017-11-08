def is_sequence_valid(sequence):
    """
    Returns whether or not an DNA sequence is valid
    :param sequence: the DNA sequence (str)
    :return: whether the sequence is valid (bool)
    """

    acid = ['A', 'T', 'G', 'C']

    for letter in sequence:
        if letter not in acid:
            return False

    return True


def get_distinct_values(sequence, subsequence):
    """
    Returns the number of distinct subsequence in sequence
    :param sequence: the suequence of DNA (str)
    :param subsequence: the subsequence of the DNA (str)
    :return: number of distinct subsequence in sequence (int)
    """
    # TODO
