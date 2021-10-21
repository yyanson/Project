from sys import argv


def salary(virb, stav, prem):
    return (int(virb) * int(stav)) + int(prem)


print(salary(argv[1], argv[2], argv[3]))

"""
PS C:\PyProjects\first> python less4_1.py 100 20 500
2500
"""
