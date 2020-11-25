af = 0
bf = 0
cf = 0
df = 0
ef = 0
ff = 0
gf = 0
hf = 0
ife = 0
jf = 0
kf = 0
lf = 0
mf = 0
nf = 0
of = 0
pf = 0
qf = 0
rf = 0
sf = 0
tf = 0
uf = 0
vf = 0
wf = 0
xf = 0
yf = 0
zf = 0
lc = 0
with open("freqlist.txt") as f:
    for line in f:
        line = line.lower()
        for char in range(0, len(line)):
            if line[char] == "a":
                af+=1
            if line[char] == "b":
                bf+=1
            if line[char] == "c":
                cf+=1
            if line[char] == "d":
                df+=1
            if line[char] == "e":
                ef+=1
            if line[char] == "f":
                ff+=1
            if line[char] == "g":
                gf+=1
            if line[char] == "h":
                hf+=1
            if line[char] == "i":
                ife+=1
            if line[char] == "j":
                jf+=1
            if line[char] == "k":
                kf+=1
            if line[char] == "l":
                lf+=1
            if line[char] == "m":
                mf+=1
            if line[char] == "n":
                nf+=1
            if line[char] == "o":
                of+=1
            if line[char] == "p":
                pf+=1
            if line[char] == "q":
                qf+=1
            if line[char] == "r":
                rf+=1
            if line[char] == "s":
                sf+=1
            if line[char] == "t":
                tf+=1
            if line[char] == "u":
                uf+=1
            if line[char] == "v":
                vf+=1
            if line[char] == "w":
                wf+=1
            if line[char] == "x":
                xf+=1
            if line[char] == "y":
                yf+=1
            if line[char] == "z":
                zf+=1
        lc+=1
        print(lc)

print("A:", af)
print("B:", bf)
print("C:", cf)
print("D:", df)
print("E:", ef)
print("F:", ff)
print("G:", gf)
print("H:", hf)
print("I:", ife)
print("J:", jf)
print("K:", kf)
print("L:", lf)
print("M:", mf)
print("N:", nf)
print("O:", of)
print("P:", pf)
print("Q:", qf)
print("R:", rf)
print("S:", sf)
print("T:", tf)
print("U:", uf)
print("V:", vf)
print("W:", wf)
print("X:", xf)
print("Y:", yf)
print("Z:", zf)
print("\nSorted:")
print(sorted([af, bf, cf, df, ef, ff, gf, hf, ife, jf, kf, lf, nf, mf, of, pf, qf, rf, tf, uf, vf, wf, xf, yf, zf], reverse=True))
