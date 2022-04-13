def unicos_em_comum(seq1, seq2):
    repete1 = []
    for i in range(len(seq1) - 1, -1, -1):
        if seq1[i] == seq1[i - 1]:
                seq1.pop(i)
                seq1.pop(i - 1)
    for i in range(len(seq2) - 1, -1, -1):
        if seq2[i] == seq2[i - 1]:
                seq2.pop(i)
                seq2.pop(i - 1)
    return seq1, seq2
