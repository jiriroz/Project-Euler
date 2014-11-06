#cislo zadavat do funkce jako string!

def numbers(n,listOfWords):
    oneToNine = {
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':''
    }
    twentyToNinety = {
    '2':'twenty',
    '3':'thirty',
    '4':'forty',
    '5':'fifty',
    '6':'sixty',
    '7':'seventy',
    '8':'eighty',
    '9':'ninety'
    }
    tenTo19 = {
    '10':'ten',
    '11':'eleven',
    '12':'twelve',
    '13':'thirteen',
    '14':'fourteen',
    '15':'fifteen',
    '16':'sixteen',
    '17':'seventeen',
    '18':'eighteen',
    '19':'nineteen'
    }

    if len(n) == 0:
        return listOfWords
    if n[0] == '0':
        n = n[1:]        
    if len(n) == 1:
        listOfWords.append(oneToNine[n])
    elif len(n) == 2:
        if n[0] == '1':
            listOfWords.append(tenTo19[n])
            return listOfWords
        listOfWords.append(twentyToNinety[n[0]])
    elif len(n) == 3:
        app = oneToNine[n[0]] + 'hundred'
        listOfWords.append(app)
        if n[1:3] == '00':
            return listOfWords
        else:
            listOfWords.append('and')
    elif len(n) == 4:
        listOfWords.append('onethousand')
        return listOfWords
    n = n[1:]
    return numbers(n,listOfWords)

bigList = []

for x in range(1,1001):
    bigList.append(''.join(numbers(str(x),[])))

bigList  = ''.join(bigList)

print (len(bigList))

input()