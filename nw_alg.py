def s(a, b):
    # we choose simple scoring missmatch and gap penalty is -1
    if a == b:
        return 1
    return -1


def needleman_wunsch(seq1, seq2):
    # sets up m*n zero matrix
    matrix = [[0] * (len(seq1) + 1) for i in range(len(seq2) + 1)]

    for i in range(len(seq1) + 1):
        matrix[0][i] = -i
    for i in range(len(seq2) + 1):
        matrix[i][0] = -i
    # fill the matrix according to the penalty scheme
    for i in range(1, len(seq2) + 1):
        for j in range(1, len(seq1) + 1):
            matrix[i][j] = max(
                matrix[i - 1][j - 1] + s(seq1[j - 1], seq2[i - 1]),
                matrix[i - 1][j] - 1,
                matrix[i][j - 1] - 1
            )
    # backtrace the matrix
    matched_sequence1 = ""
    matched_sequence2 = ""
    i, j = len(seq2), len(seq1)
    while i > 0 and j > 0:
        score_current = matrix[i][j]
        diagonal = matrix[i - 1][j - 1]
        up = matrix[i][j - 1]
        left = matrix[i - 1][j]
        # now we check how the current score was created
        if score_current == diagonal + s(seq1[j - 1], seq2[i - 1]):
            matched_sequence1 += seq1[j - 1]
            matched_sequence2 += seq2[i - 1]
            i -= 1
            j -= 1

        elif score_current == up - 1:
            matched_sequence1 += seq1[j - 1]
            matched_sequence2 += "-"
            j -= 1
        elif score_current == left - 1:
            matched_sequence1 += "-"
            matched_sequence2 += seq2[i - 1]
            i -= 1
    return (matched_sequence1[::-1], matched_sequence2[::-1])


if __name__ == '__main__':
    assert(needleman_wunsch("ATTACA", "ATGCT") == ('ATTACA', 'A-TGCT'))
    assert(
        needleman_wunsch(
            "CAGTCCTAGA",
            "CATGTCGTA") == (
            'CA-GTCCTAGA',
            'CATGTCGT--A'))
