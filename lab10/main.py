import numpy as np

# Метод  двоичного поиска по всем координатам
# Y=Sin(x1) + Cos(x2), -3 < x1 < 3, -3 < x2 < 3
# (1.57, 0)

def f(x,y):
    return (np.sin(x) + np.cos(y))

def find_m_pos(f, m, e):
    if f(m) > f(m + e*0.5) and f(m) > f(m - e*0.5):
        return 'max'
    elif f(m) > f(m - e*0.5) and f(m) < f(m + e*0.5):
        return 'climb'
    elif f(m) < f(m - e*0.5) and f(m) > f(m + e*0.5):
        return 'descend'
    else:
        return'min'

def binmax(f, left_bound, right_bound, e):
    l = left_bound
    r = right_bound
    while r - l > e:
        m = (l + r) / 2
        if find_m_pos(f, m, e) =='max':
            return m
        elif find_m_pos(f, m, e) in ('climb', 'min'):
            l = m
        elif find_m_pos(f, m, e) == 'descend':
            r = m
    return m


def main():
    x1_max = binmax(np.sin, -3, 3, 0.01)
    x2_max = binmax(np.cos, -3, 3, 0.01)
    print(x1_max, x2_max)

if __name__ == '__main__':
    main()
