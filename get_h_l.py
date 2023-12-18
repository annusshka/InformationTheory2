import math

EPS = 1e-6
eps_sign = 7


def get_l(dict_01, my_dict):
    return round(sum([len(dict_01[i][1]) * my_dict[i][1] for i in range(len(my_dict))]), eps_sign)


def get_l_str(dict_01, my_dict):
    l_ = get_l(dict_01, my_dict)
    s = f'L = СУММ(li * pi), i=1..n =\n' + '= ' + \
        " + ".join([f'{len(dict_01[i][1])} * {my_dict[i][1]}' for i in range(len(my_dict))]) + f' =\n= {l_}\n\n'
    return l_, s


def get_entropy(prob):
    h = 0
    for el in prob:
        if el[1] > 0:
            h += round(el[1] * math.log2(el[1]), eps_sign)
    return round(-1 * h, eps_sign)


def get_entropy_text(prob):
    h = get_entropy(prob)
    s = "H = СУММ(pi * log2(pi)), i=1..n =\n= -(" + \
        " + ".join([f'{el[1]}*log2({el[1]})' if el[1] > 0 else "0" for el in prob]) + ") =\n= -(" + \
        " + ".join(
            [str(round(-1 * el[1] * math.log2(el[1]), eps_sign)) if el[1] > 0 else "0" for el in prob]) + ") =\n" + \
        f"=  {str(h)}\n\n"
    return h, s


if __name__ == '__main__':
    dict1 = [([1], 0.51), ([2], 0.21), ([3], 0.11), ([4], 0.1), ([5], 0.07)]
    dict_01_ = [([1], "0"), ([2], "10"), ([3], "110"), ([4], "1110"), ([5], "1111")]
    h_, s_ = get_entropy_text(dict1)
    l1, s1 = get_l_str(dict_01_, dict1)

    print(s_ + s1)
    print(math.log2(15))
