import math
fact = math.factorial


def likelihood(vct, drw, dft, fstd_vct, fstd_drw, fstd_dft):
    return (fact(sum([vct, drw, dft])) / (fact(vct) * fact(drw) * fact(dft))) \
        * (fstd_vct**vct) * (fstd_drw**drw) * (fstd_dft**dft)


def update(dataset, p_fstd, data):
    p_d_fstd = [likelihood(*dataset, *data[i]) for i in range(3)]
    p_d = sum([p_d_fstd[i] * p_fstd[i] for i in range(3)])
    return [(p_d_fstd[i] * p_fstd[i]) / p_d for i in range(3)]


def main(datasets, p_fstd, data):
    print('|--------------------------|')
    print('| P(COR) | P(SID) | P(CEN) |')
    print('|--------------------------|')

    for dataset in datasets:
        p_fstd = update(dataset, p_fstd, data)
        print("| {0[0]:0.4f} | {0[1]:0.4f} | {0[2]:0.4f} |".format(p_fstd))

    print('|--------------------------|')


if __name__ == '__main__':
    data = [
        # [victory, draw, defeat]
        [0.59, 0.12, 0.27],  # COR
        [0.55, 0.12, 0.32],  # SID
        [0.66, 0.11, 0.21],  # CEN
    ]
    datasets = [
        [5, 1, 4],  # 1st
        [6, 2, 2],  # 2nd
        [9, 0, 1],  # ...
        [7, 2, 1],
        [6, 1, 3],
        [6, 2, 2],
        [7, 0, 3],
        [8, 1, 1],
        [7, 0, 3],
        [9, 0, 1],
    ]
    p_fstd = [1/3, 1/3, 1/3]  # assumption

    main(datasets, p_fstd, data)
