kaas = ""


vraag1 = input("Is de kaas geel?\n")
if vraag1 == "ja":
    vraag2 = input("Zitten er gaten in?\n")
    if vraag2 == "ja":
        vraag3 = input("Is de kaas belachelijk duur?\n")
        if vraag3 == "ja":
            kaas = "emmenthaler"
        elif vraag3 == "nee":
            kaas = "leerdammer"
    elif vraag2 == "nee":
        vraag3 = input("is de kaas zo hard als steen\n?")
        if vraag3 == "ja":
            kaas = "pamigiano Reggiano"
        elif vraag3 == "nee":
            kaas = "Goudse kaas"
elif vraag1 == "nee":
    vraag2 = input("heeft de kaas een blauwe schimmel?\n")
    if vraag2 == "ja":
        vraag3 = input("heeft de kaas een korst?\n")
        if vraag3 == "ja":
            kaas = "Camembert"
        elif vraag3 == "nee":
            kaas = "Mozzerella"
    elif vraag2 == "nee":
        vraag3 = input("heeft de kaas een korst?\n")
        if vraag3 == "ja":
            kaas = "Blue de rochbaron"
        elif vraag3 == "nee":
            kaas = "foume dámbert"






print (kaas)