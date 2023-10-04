import random

dictionary = {}
listNumbers = list(range(1, 46))

def lotterydrawing(size, numberToDrawn):
    for x in range(numberToDrawn):
        drawnNumber = random.randint(0, len(listNumbers)-1-x)
        a, b = drawnNumber, len(listNumbers)-1-x
        listNumbers[b], listNumbers[a] = listNumbers[a], listNumbers[b]
    print("gezogene Zahlen:" + str(listNumbers[len(listNumbers) - numberToDrawn:]))

def lottostatistics(size, numberTests):
    numberToDrawn = 6
    for x in range(1, size + 1):
        dictionary[f'{x}'] = 0
    for i in range(numberTests):
        lotterydrawing(size, numberToDrawn)
        for number in listNumbers[len(listNumbers) - numberToDrawn:]:
            dictionary[f'{number}'] += 1

lottostatistics(45, 1000)
print(dictionary)