from Poker import poker as p

def pokerstatistics(NumberCardsDrawn, NumberCards, numberTests):
    dictionary = {"Royal Flush":0,"Straight Flush":0,"Vierling":0,"Full House":0,"Flush":0,"Straight":0,"Drilling":0,"Zwei Paare":0,"Ein Paar":0,"Höchste Karte":0}
    warsch = {"Royal Flush": 0, "Straight Flush": 0, "Vierling": 0, "Full House": 0, "Flush": 0, "Straight": 0, "Drilling": 0, "Zwei Paare": 0, "Ein Paar": 0, "Höchste Karte": 0}
    for a in range(1,numberTests+1):
        hand = p.cards(NumberCardsDrawn, NumberCards)
        if p.royalFlush(hand, NumberCards):
            dictionary['Royal Flush'] += 1
            continue
        elif p.straightFlush(hand, NumberCards):
            dictionary['Straight Flush'] += 1
            continue
        elif p.vierlinge(hand, NumberCards):
            dictionary['Vierling'] += 1
            continue
        elif p.fullHouse(hand,NumberCards):
            dictionary['Full House'] += 1
            continue
        elif p.flush(hand, NumberCards):
            dictionary['Flush'] += 1
            continue
        elif p.straight(hand, NumberCards):
            dictionary['Straight'] += 1
            continue
        elif p.drillinge(hand, NumberCards):
            dictionary['Drilling'] += 1
            continue
        elif p.zweiPaare(hand, NumberCards):
            dictionary['Zwei Paare'] += 1
            continue
        elif p.paar(hand, NumberCards):
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
    return warsch