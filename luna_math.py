import random

def intDigit(x):
    c = int(len(str(x)))
    d = []
    for i in range(0, c):
        num = int( x % (10**(i+1)) / (10**i) )
        d.append(num)
    return d

# Generate an equation randomly
def equGenerator(a_interval, b_interval, c_interval, operator):
    while True:
        a = random.randint(a_interval[0], a_interval[1])
        b = random.randint(b_interval[0], b_interval[1])
        if(operator=='+'):
            oper = 1
        if(operator=='-'):
            oper = -1
        if(operator=='r'):
            oper_list = [-1, 1]
            oper = random.choice(oper_list)
        c = a+oper*b
        if c>=c_interval[0] and c<=c_interval[1]:
            return a, b, oper

def addPage(f):
    print(r'\begin{tabular}{lll}', file=f)
    eq_list = []
    for i in range(0, 51):
        a, b, oper = equGenerator([1, 50], [1, 50], [0, 50], '-')
        if(oper==1):
            eq = str(a)+" + "+str(b)+" = \_\_\_~~"
            eq_list.append(eq)
        else:
            eq = str(a)+" - "+str(b)+" = \_\_\_~~"
            eq_list.append(eq)

        if( len(eq_list) == 3 ):
            print(r'\vspace{0.3cm}', file=f)
            print(eq_list[0], " & ", eq_list[1], " & " , eq_list[2], "\\\\", file=f)
            eq_list.clear()
    print(r'\end{tabular}', file=f)
    return

def main():
    f = open('./workfile.tex', 'w')
    print(r'\documentclass[12pt,letterpaper]{article}', file=f)
    print(r'\usepackage{geometry}', file=f)
    print(r'\geometry{left=2cm,right=2cm,top=2cm,bottom=2cm}', file=f)
    print(r'\begin{document}', file=f)
    print(r'\huge', file=f)
    print(r'\begin{center}', file=f)

    for i in range(0, 50):
        addPage(f)

    print(r'\end{center}', file=f)
    print(r'\end{document}', file=f)
    f.close()
    return

if __name__ == "__main__":
    main()
