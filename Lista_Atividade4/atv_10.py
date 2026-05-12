numericos = [41,25,63,1,8,16]
total = 0

for i in numericos:
    total+=i

media = total/len(numericos)
print(media)

for pos,i in enumerate(numericos):
    if i > media:
        print(i,pos)