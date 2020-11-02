import Table
import Operation


def dot(*args):
    result = args[0]
    for i in range(1, len(args)):
        result = T[result][args[i]]
    return result


def setdot(*args):
    args = list(args)
    for i in range(len(args)):
        if type(args[i]) != set:
            args[i] = {args[i]}
    result = args[0]
    for i in range(1, len(args)):
        temp = []
        for x in result:
            for y in args[i]:
                temp.append(dot(x, y))
        result = set(temp)
    return result


def check_axa():
    for a in S:
        if a not in setdot(a, S, a):
            print(False)
            return False
    print(True)
    return True


def check_xaya():
    for a in S:
        if a not in setdot(S, a, S, a):
            print(False)
            return False
    print(True)
    return True


def check_axay():
    for a in S:
        if a not in setdot(a, S, a, S):
            print(False)
            return False
    print(True)
    return True


def check_ax():
    for a in S:
        if a not in setdot(a, S):
            print(False)
            return False
    print(True)
    return True


def check_xa():
    for a in S:
        if a not in setdot(S, a):
            print(False)
            return False
    print(True)
    return True


def check_xay():
    for a in S:
        if a not in setdot(S, a, S):
            print(False)
            return False
    print(True)
    return True


def check_xayaz():
    for a in S:
        if a not in setdot(S, a, S, a, S):
            print(False)
            return False
    print(True)
    return True


def check_xaay():
    for a in S:
        if a not in setdot(S, a, a, S):
            print(False)
            return False
    print(True)
    return True


def check_axaaya():
    for a in S:
        if a not in setdot(a, S, a, a, S, a):
            print(False)
            return False
    print(True)
    return True


def check_aaxaa():
    for a in S:
        if a not in setdot(a, a, S, a, a):
            print(False)
            return False
    print(True)
    return True

if __name__ == '__main__':
    S = Table.S4
    for T in Table.table4:
        check_xa()


