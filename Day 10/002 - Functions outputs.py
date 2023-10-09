def capitalize(fname, lname):
    fname = fname.lower()
    lname = lname.lower()

    fullname = fname + " " + lname

    return fullname.title(), fname, lname

final = capitalize("aNGelA", "CailO")

print(type(final))