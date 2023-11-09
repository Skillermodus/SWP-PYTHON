import random

#liste bis 51 machen
#dann 5 mal ziehen mit schuffle
#52 werte modulo 13 dann hat man die farben, weil dann hat man jeweils 0,1,2,3
#die farbe ist deshalb egal weil man sich denkt

listNumbers = list(range(1, 53))


def cards(NumberCardsDrawn, NumberCards):
    cards = list(range(0, (NumberCards*4)))
    random.shuffle(cards)
    return cards[:NumberCardsDrawn]

def paar(hand, NumberCards):
    paar = 0
    test = []
    values = [(card % NumberCards) for card in hand]       #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 2:            #Prüfen, ob eine Zahl genau 2mal vorkommt
            test.append(value)
            paar = 1
    #print('Paar:'+f'{paar}')
    return paar


def zweiPaare(hand, NumberCards):
    test = []
    zweiPaare = 0
    values = [card % NumberCards for card in hand]       #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 2:            #Prüfen, ob eine Zahl genau 2mal vorkommt
            test.append(value)
        if(len(test) == 4):
            zweiPaare = 1
    #print('ZweiPaare:'+f'{zweiPaare}')
    return zweiPaare

def drillinge(hand, NumberCards):
    drillinge = 0
    values = [card % NumberCards for card in hand]        #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 3:             #Prüfen, ob eine Zahl genau 3mal vorkommt
            drillinge = 1
    #print('Drillinge:'+f'{drillinge}')
    return drillinge

def vierlinge(hand, NumberCards):
    vierlinge = 0
    values = [card % NumberCards for card in hand]       #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 4:            #Prüfen, ob eine Zahl genau 4mal vorkommt
            return True
    return vierlinge

def flush(hand, NumberCards):
    suits = [card // NumberCards for card in hand]
    for value in suits:
        if suits.count(value) == 5:
                return True
    return False

def royalFlush(hand, NumberCards):
    if flush(hand,NumberCards):
        values = [card % NumberCards for card in hand]
        values.sort()
        if(0 in values and 9 in values and 10 in values and 11 in values and 12 in values):
            return True
    return False

def fullHouse(hand, NumberCards):
    if paar(hand,NumberCards) and drillinge(hand,NumberCards):
        return True
    return False

def straight(hand, NumberCards):
    values = [card % 13 for card in hand]
    values.sort()
    if(0 in values and 9 in values and 10 in values and 11 in values and 12 in values):
        return True
    for i in range(1, 5):
        if((values[i]-values[i-1]) != 1):
            return False
    return True

def straightFlush(hand, NumberCards):
    values = [card % 13 for card in hand]
    values.sort()
    if(flush(hand, NumberCards)):
        for i in range(1, 5):
            if ((values[i] - values[i - 1]) != 1):
                return False
        return True
    return False

def pokerstatistics(NumberCardsDrawn, NumberCards, numberTests):
    dictionary = {"Royal Flush":0,"Straight Flush":0,"Vierling":0,"Full House":0,"Flush":0,"Straight":0,"Drilling":0,"Zwei Paare":0,"Ein Paar":0,"Höchste Karte":0}
    warsch = {"Royal Flush": 0, "Straight Flush": 0, "Vierling": 0, "Full House": 0, "Flush": 0, "Straight": 0, "Drilling": 0, "Zwei Paare": 0, "Ein Paar": 0, "Höchste Karte": 0}
    for a in range(1,numberTests+1):
        hand = cards(NumberCardsDrawn, NumberCards)
        if royalFlush(hand, NumberCards):
            dictionary['Royal Flush'] += 1
            continue
        elif straightFlush(hand, NumberCards):
            dictionary['Straight Flush'] += 1
            continue
        elif vierlinge(hand, NumberCards):
            dictionary['Vierling'] += 1
            continue
        elif fullHouse(hand,NumberCards):
            dictionary['Full House'] += 1
            continue
        elif flush(hand, NumberCards):
            dictionary['Flush'] += 1
            continue
        elif straight(hand, NumberCards):
            dictionary['Straight'] += 1
            continue
        elif drillinge(hand, NumberCards):
            dictionary['Drilling'] += 1
            continue
        elif zweiPaare(hand, NumberCards):
            dictionary['Zwei Paare'] += 1
            continue
        elif paar(hand, NumberCards):
            dictionary['Ein Paar'] += 1
            continue
        else:
            dictionary['Höchste Karte'] += 1
    warsch['Royal Flush'] = (dictionary['Royal Flush'] / numberTests )*100
    warsch['Straight Flush'] = (dictionary['Straight Flush'] / numberTests) * 100
    warsch['Vierling'] = (dictionary['Vierling'] / numberTests) * 100
    warsch['Full House'] = (dictionary['Full House'] / numberTests) * 100
    warsch['Flush'] = (dictionary['Flush'] / numberTests) * 100
    warsch['Straight'] = (dictionary['Straight'] / numberTests) * 100
    warsch['Drilling'] = (dictionary['Drilling'] / numberTests) * 100
    warsch['Zwei Paare'] = (dictionary['Zwei Paare'] / numberTests) * 100
    warsch['Ein Paar'] = (dictionary['Ein Paar'] / numberTests) * 100
    warsch['Höchste Karte'] = (dictionary['Höchste Karte'] / numberTests) * 100
    print(warsch)

if __name__ == '__main__':
    pokerstatistics(5, 13, 1000000)