print("benvenuto prima di procedere dammi qualche informazione su di te")
anno_di_nascita = int(input("Qual'è il tuo anno di nascita?"))

sposato = (input("sei sposato? si/no:"))

if sposato == "no":
    
    sposato1 = "non sei sposato"
else:
    sposato1 = "sei sposato"

ceni = (input("ceni?"))

if ceni == "si":
    ceni1 = "questa sera cenerai"
    
else:
    ceni1 = "questa sera non cenerai"
    

print("sei del",anno_di_nascita, sposato1, "e" ,ceni1,)