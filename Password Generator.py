import random

print("Password Generator -- A Project by Interstellar2424")

choices = ("random", "costum")

alpha = ("ajjsnx", "bhgvjhv", "chghg", "dhgcy", "egvgcyt", "fhgcty", "gghchg", "hyfj", "ihdksn", "jodmd", "khsic", "licnu", "mhusb", "nhds", "ogcbu","pgshi", "qmddjm", "rmemsk", "sjnsns", "tmemk", "uksmm", "vksm", "wisjw", "xojem", "yjsjw", "zisjw")

Alpha = ("AJSNS", "BIXS", "CBAH", "DMXJS", "EMQK", "FMZMXK", "GMSM", "HMSM", "IAKS", "JMSKW", "KMWJ", "LMSO", "MMWI", "NMWIS", "OMWMK", "PMXI", "QZJXJ", "RJYS", "SNB", "TNM", "UBH", "VBHJ", "WNBH", "XVH", "YPOH", "ZZFN")

spc = ("@", "#", "&", "*", "%", "_")

num = ("108", "287", "397", "4878", "5768", "698", "7089", "808", "9435", "1008")

mode = input("type (random) for randomly generated password. or type (costum) for for costumized password: ")

while mode not in choices:
    mode = input("type (random) for randomly generated password. or type costum for for costumized password")

if mode == "random":
    password1 = random.choice(alpha) + random.choice(Alpha) + random.choice(spc) + random.choice(num)
    
    print(password1)

elif mode == "costum":
    name = ("")
    Date_of_birth = ("")
    hobbies = ("")

    name = input("fullname (write one word follwed by ,): ")
    Date_of_birth = input("Date_of_birth(write one word followed by) (only the date): ")
    hobbies = input("hobbies (write whithout spaces): ")

    password2 = print(hobbies + random.choice(spc) + random.choice(spc) + name + random.choice(spc)+ random.choice(spc) + Date_of_birth + random.choice(spc) + random.choice(spc))

print("Thanks For Using!")

# end of code :)