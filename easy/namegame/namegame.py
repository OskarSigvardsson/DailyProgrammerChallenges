lyrics = \
"""{name}, {name} bo {bname} Bonana fanna fo {fname}
Fee fy mo {mname}
{name}!"""

def rhyme(name):
    first, rest = name[0], name[1:]
    
    if first.upper() in "AEIOU":
        rest = first.lower() + rest

    if first.upper() in "BFM":
        bname = "Bo-" + rest
        fname = "Fo-" + rest
        mname = "Mo-" + rest
    else:
        bname = "B" + rest
        fname = "F" + rest
        mname = "M" + rest

    return lyrics.format(name=name, bname=bname, fname=fname, mname=mname)

if __name__ == "__main__":
    name = "Nick!"

    print(rhyme(name[:-1]))
