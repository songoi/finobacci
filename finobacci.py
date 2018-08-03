def finobacciGen(number):
    if number ==1:
        sequence=[0,1,1]
        return sequence
    elif number==2:
        sequence= [0,1,1,2]
        return sequence
    elif number>2:
        sequence= [0,1,1,2]
        x=sequence[-1]
        while x<number:
            y=sequence[-1]+sequence[-2]
            sequence.append(y)
            x+=1
        return (sequence)

print (finobacciGen(4))
