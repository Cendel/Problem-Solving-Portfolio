# Question: https://www.codingame.com/ide/puzzle/you-are-the-father-maury-povich-style

# Completed!

mother = "Mother Louise:       &R %N ;; GE p2 *j 7U 5b 3y BY 6S gC NN 9R mJ TC d/ G< xv 3J w+ 3i Zw 4< C$ -F X% wB I2 Mi <B rU !# -; p6"
child = 'Child Samantha:      MR %I ;h E6 Gp *f a7 75 :y eB 6= mC zN 9# md Cm Rd <3 xo ;3 hw X3 wK <J L$ -" %L Bd I# i$ vB Br #u C- +p'


f_lst = [
    'Lawrence:            ZM BI h; c6 VG fi ax 7b :n (e (= mQ Nz !# id m! &R 3U ov K; hk UX =K Jr Lx "% L7 Ed 7# G$ >! pU N1 Zv "\'',
    'Zachariah:           hM ID hp 6, G" fj Ga 7k C: eb Y= 0m z* &# d7 Im Rk o3 (o h; hP XK lK J1 \'L t" L, dv #Y :$ v> B= Bu Ci +t',
    "Calvin:              ;l v. ;m %j P! 6! z< vW A. kq N6 D? Vu (> au mB ,N 1% mK uP R3 y7 <a NI IJ CR VF /O Yw IQ =x O- Kn +I p,",
    "Angus:               oM I2 8h v6 G* fS a? P7 N: Le E= =m !9 7< ', x6 C( Bj Up W% &- Q0 uP +T ,Z 3h x6 XY Bf :. l3 b: xn Mi Y8",
    "Elliot:              3M I# h3 6t YG fV ae h7 :& 'e == mk Nz #\" 5d #m /R 3t (o 5; Ch XY aK >H iM fo >X '# 62 k- hO Py i. .% +U",
    "Frank:               '9 .5 1% -g ;' mC HY .: cX Q, c* FD 2w nB YJ ;- mZ <; 0, C; B9 #C xn :5 Bx &D c/ %- IU !T Kc ,a u- -r 9#",
]


def parser(elem):
    elem = elem.split(":", 1)
    elem[1] = elem[1].lstrip().split(" ")
    return elem


mother = parser(mother)
child = parser(child)
f_lst = [parser(lst) for lst in f_lst]


for i in f_lst:
    count = 0
    for j in range(len(i[1])):
        if i[1][j][0] in child[1][j] or i[1][j][1] in child[1][j]:
            count += 1
    if count == len(i[1]):
        print(f"{i[0]}, you are the father!")

# a more concise alternative for the above for loop:
for i in f_lst:
    if all(any(val in child[1][j] for val in i[1][j]) for j in range(len(i[1]))):
        print(f"{i[0]}, you are the father!")
