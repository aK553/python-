text = "Love all trust a few do wrong to none"
for m  in range (0,len(text)):
    count = m %2
    if count == 0:
        print(text[m])
