import random

def shuffle(lit, hist, sci, fa, rmpss):
    litT = random.sample(lit, 4)
    litB = generateDerangement(litT)

    histT = random.sample(hist, 4)
    histB = generateDerangement(histT)

    sciT = random.sample(sci, 4)
    sciB = generateDerangement(sciT)

    faT = random.sample(fa, 4)
    faB = generateDerangement(faT)

    rmpssT = random.sample(rmpss, 4)
    rmpssB = generateDerangement(rmpssT)

    tossups = {"lit": litT, "hist": histT, "sci": sciT, "fa": faT, "rmpss": rmpssT}
    bonuses = {"lit": litB, "hist": histB, "sci": sciB, "fa": faB, "rmpss": rmpssB}

    return tossups, bonuses

def generateDerangement(cats):
    derangements = ["1230", "2031", "3012", "1302", "2301", "3201", "1032", "2310", "3012"]
    d = [int(x) for x in random.choice(derangements)]
    return [cats[d[0]], cats[d[1]], cats[d[2]], cats[d[3]]]

def generateOrder(tossups, bonuses):
    q1t = [tossups["lit"][0], tossups["hist"][0], tossups["sci"][0], tossups["fa"][0], tossups["rmpss"][0]]
    q2t = [tossups["lit"][1], tossups["hist"][1], tossups["sci"][1], tossups["fa"][1], tossups["rmpss"][1]]
    q3t = [tossups["lit"][2], tossups["hist"][2], tossups["sci"][2], tossups["fa"][2], tossups["rmpss"][2]]
    q4t = [tossups["lit"][3], tossups["hist"][3], tossups["sci"][3], tossups["fa"][3], tossups["rmpss"][3]]

    q1b = [bonuses["lit"][0], bonuses["hist"][0], bonuses["sci"][0], bonuses["fa"][0], bonuses["rmpss"][0]]
    q2b = [bonuses["lit"][1], bonuses["hist"][1], bonuses["sci"][1], bonuses["fa"][1], bonuses["rmpss"][1]]
    q3b = [bonuses["lit"][2], bonuses["hist"][2], bonuses["sci"][2], bonuses["fa"][2], bonuses["rmpss"][2]]
    q4b = [bonuses["lit"][3], bonuses["hist"][3], bonuses["sci"][3], bonuses["fa"][3], bonuses["rmpss"][3]]

    tossupOrder = random.sample(q1t, 5) + random.sample(q2t, 5) + random.sample(q3t, 5) + random.sample(q4t, 5)
    bonusOrder = random.sample(q1b, 5) + random.sample(q2b, 5) + random.sample(q3b, 5) + random.sample(q4b, 5)

    return tossupOrder, bonusOrder

def check_adjacent_categories(final_order_tu, final_order_b, categories):
    for i in range(len(final_order_tu) - 1):
        if categories[final_order_tu[i]] == categories[final_order_tu[i+1]]:
            return True
        elif categories[final_order_b[i]] == categories[final_order_b[i+1]]:
            return True
        if categories[final_order_b[i]] == categories[final_order_tu[i+1]]:
            return True
        if categories[final_order_tu[i]] == categories[final_order_b[i]]:
            return True
    return False

def check_same_quarter_repeats(final_order_tu, final_order_b):
    for i in range(len(final_order_tu)-15):
        tu = final_order_tu[i]
        b_position = final_order_b.index(tu)
        if b_position <= 4:
            return True
    for i in range(len(final_order_tu)-15):
        tu = final_order_tu[i+5]
        b_position = final_order_b.index(tu)
        if b_position >= 5 and b_position <=9:
            return True
    for i in range(len(final_order_tu)-15):
        tu = final_order_tu[i+10]
        b_position = final_order_b.index(tu)
        if b_position >= 10 and b_position <= 14:
            return True
    for i in range(len(final_order_tu)-15):
        tu = final_order_tu[i+15]
        b_position = final_order_b.index(tu)
        if b_position >= 15:
            return True
    return False