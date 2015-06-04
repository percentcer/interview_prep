__author__ = 'percentcer'
# Chapter 1
# Arrays and Strings

# 1.8
def is_substr(s1, s2):
    return s1 in s2

def is_rotated(s1, s2):
    if len(s1) != len(s2):
        return False

    return is_substr(s1, s2*2)

# 1.7
def row_blanker(inmat):
    mat = inmat[:]

    blank_rows = {}
    blank_cols = {}

    M = len(mat)

    if M < 1:
        return inmat

    N = len(mat[0])

    for r in range(M):
        for c in range(N):
            if mat[r][c] == 0:
                blank_rows[r] = True
                blank_cols[c] = True

    for r in range(M):
        for c in range(N):
            if blank_rows.get(r) or blank_cols.get(c):
                mat[r][c] = 0

    return mat

# 1.6
def rotate_ip(pic):
    from math import ceil
    def swap(s, t):
        tmp = pic[s[0]][s[1]]
        pic[s[0]][s[1]] = pic[t[0]][t[1]]
        pic[t[0]][t[1]] = tmp

    if len(pic) and len(pic) != len(pic[0]):
        raise ValueError(
            "pic is defined as an NxN matrix, received {}x{}".format(
                len(pic), len(pic[0])
            ))

    num_shells = ceil(len(pic)/2)
    for shell in range(num_shells):
        for pos in range(len(pic) - shell*2 - 1):
            nw = (shell, shell+pos)
            ne = (shell+pos, -(shell+1))
            se = (-(shell+1), -(shell+1+pos))
            sw = (-(shell+1+pos), shell)
            swap(nw, se)
            swap(se, ne)
            swap(nw, sw)

def rotate(pic):
    if len(pic) and len(pic[0]) != len(pic):
        raise ValueError("pic is defined as an NxN matrix, received {}x{}".format(
        len(pic), len(pic[0])
        ))
    elif len(pic) == 0:
        return []

    ret = []
    for c in range(len(pic)):
        new_row = []
        for r in reversed(pic):
            new_row.append(r[c])
        ret.append(new_row)
    return ret

# 1.5
def space_replace0(s):
    return s.replace(' ', '%20')

def space_replace1(s):
    ret = s.split()
    return '%20'.join(ret)

def space_replace2(s):
    chars = []
    for x in s:
        if x == ' ':
            chars.append('%20')
        else:
            chars.append(x)
    return ''.join(chars)

# 1.4
def anagrams(lhs, rhs):
    from collections import defaultdict

    if len(lhs) != len(rhs):
        return False

    comp = defaultdict(int)

    for x in lhs:
        comp[x] += 1
    for x in rhs:
        comp[x] -= 1
    for i in comp.values():
        if i != 0:
            return False
    else:
        return True


# 1.2
def reverse_cstr(in_cstr):
    string_comps = in_cstr.split('\0')
    if not len(string_comps) > 1:
        raise ValueError("expected a c-style (null terminated) string")
    base = list(string_comps[0])
    for x in range(len(base)//2):
        ri  = -(x+1)
        tmp = base[x]
        base[x] = base[ri]
        base[ri] = tmp
    return ''.join(base + ['\0'])

# 1.1
def unique (in_str):
    si = sorted(in_str)
    prev = None
    for c in si:
        if c == prev:
            return False
        prev = c
    else:
        return True
