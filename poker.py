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
    values = [(card % NumberCards) for card in hand]        #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 2:                        #Prüfen, ob eine Zahl genau 2mal vorkommt
            test.append(value)
            paar = 1
    #print('Paar:'+f'{paar}')
    return paar


def zweiPaare(hand, NumberCards):
    test = []
    zweiPaare = 0
    values = [card % NumberCards for card in hand]       #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 2:                     #Prüfen, ob eine Zahl genau 2mal vorkommt
            test.append(value)
        if(len(test) == 4):                              #wenn 4 Zahlen(also 2 mal doppelte) hinzugefügt wurden ist es ein zweiPaar
            zweiPaare = 1
    #print('ZweiPaare:'+f'{zweiPaare}')
    return zweiPaare

def drillinge(hand, NumberCards):
    drillinge = 0
    values = [card % NumberCards for card in hand]        #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 3:                      #Prüfen, ob eine Zahl genau 3mal vorkommt
            drillinge = 1
    #print('Drillinge:'+f'{drillinge}')
    return drillinge

def vierlinge(hand, NumberCards):
    vierlinge = 0
    values = [card % NumberCards for card in hand]        #Die Zahlen ausgeben
    for value in values:
        if values.count(value) == 4:                      #Prüfen, ob eine Zahl genau 4mal vorkommt
            return True
    return vierlinge

def flush(hand, NumberCards):
    suits = [card // NumberCards for card in hand]
    for value in suits:
        if suits.count(value) == 5:                       #schauen ob alle 5 karten dieselbe Farbe haben
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
    values = [card % NumberCards for card in hand]
    values.sort()
    if(0 in values and 9 in values and 10 in values and 11 in values and 12 in values):
        return True
    for i in range(1, 5):
        if((values[i]-values[i-1]) != 1):
            return False
    return True

def straightFlush(hand, NumberCards):
    values = [card % NumberCards for card in hand]
    values.sort()
    if(flush(hand, NumberCards)):
        for i in range(1, 5):
            if ((values[i] - values[i - 1]) != 1):
                return False
        return True
    return False