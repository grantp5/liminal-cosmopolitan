import random

def shuffle_lit_tu(lit):
    return random.sample(lit, 4)
def shuffle_hist_tu(hist):
    return random.sample(hist, 4)
def shuffle_sci_tu(sci):
    return random.sample(sci, 4)
def shuffle_fa_tu(fa):
    return random.sample(fa, 4)
def shuffle_rmpss_tu(rmpss):
    return random.sample(rmpss, 4)

def shuffle_lit_b(lit):
    return random.sample(lit, 4)
def shuffle_hist_b(hist):
    return random.sample(hist, 4)
def shuffle_sci_b(sci):
    return random.sample(sci, 4)
def shuffle_fa_b(fa):
    return random.sample(fa, 4)
def shuffle_rmpss_b(rmpss):
    return random.sample(rmpss, 4)

def fill_quarters_tu(shuffled_lit_tu, shuffled_hist_tu, shuffled_sci_tu, shuffled_fa_tu, shuffled_rmpss_tu):
    first_quarter_tu = list([shuffled_lit_tu[0], shuffled_hist_tu[0], shuffled_sci_tu[0], shuffled_fa_tu[0], shuffled_rmpss_tu[0]])
    second_quarter_tu = list([shuffled_lit_tu[1], shuffled_hist_tu[1], shuffled_sci_tu[1], shuffled_fa_tu[1], shuffled_rmpss_tu[1]])
    third_quarter_tu = list([shuffled_lit_tu[2], shuffled_hist_tu[2], shuffled_sci_tu[2], shuffled_fa_tu[2], shuffled_rmpss_tu[2]])
    fourth_quarter_tu = list([shuffled_lit_tu[3], shuffled_hist_tu[3], shuffled_sci_tu[3], shuffled_fa_tu[3], shuffled_rmpss_tu[3]])
    return random.sample(first_quarter_tu, 5) + random.sample(second_quarter_tu, 5) + random.sample(third_quarter_tu, 5) + random.sample(fourth_quarter_tu, 5)
def fill_quarters_b(shuffled_lit_b, shuffled_hist_b, shuffled_sci_b, shuffled_fa_b, shuffled_rmpss_b):
    first_quarter_b = list([shuffled_lit_b[0], shuffled_hist_b[0], shuffled_sci_b[0], shuffled_fa_b[0], shuffled_rmpss_b[0]])
    second_quarter_b = list([shuffled_lit_b[1], shuffled_hist_b[1], shuffled_sci_b[1], shuffled_fa_b[1], shuffled_rmpss_b[1]])
    third_quarter_b = list([shuffled_lit_b[2], shuffled_hist_b[2], shuffled_sci_b[2], shuffled_fa_b[2], shuffled_rmpss_b[2]])
    fourth_quarter_b = list([shuffled_lit_b[3], shuffled_hist_b[3], shuffled_sci_b[3], shuffled_fa_b[3], shuffled_rmpss_b[3]])
    return random.sample(first_quarter_b, 5) + random.sample(second_quarter_b, 5) + random.sample(third_quarter_b, 5) + random.sample(fourth_quarter_b, 5)

def check_pairs(final_order_tu, final_order_b):
    condition = 0
    for x in range(len(final_order_tu)):
        if "Literature" in final_order_tu[x] and "Literature" in final_order_b[x]:
            condition += 1
        elif "History" in final_order_tu[x] and "History" in final_order_b[x]:
            condition += 1
        elif "Science" in final_order_tu[x] and "Science" in final_order_b[x]:
            condition += 1
        elif "Fine Arts" in final_order_tu[x] and "Fine Arts" in final_order_b[x]:
            condition += 1
        elif "Beliefs" in final_order_tu[x] and "Beliefs" in final_order_b[x]:
            condition += 1
        elif "Thought" in final_order_tu[x] and "Thought" in final_order_b[x]:
            condition += 1
    if condition == 0:
        return False
    else:
        return True

def check_adjacent_categories(final_order_tu, final_order_b):
    condition = 0
    for x in range(len(final_order_tu)-1):
        if "Literature" in final_order_tu[x] and "Literature" in final_order_tu[x+1]:
            condition += 1
        elif "History" in final_order_tu[x] and "History" in final_order_tu[x+1]:
            condition += 1
        elif "Science" in final_order_tu[x] and "Science" in final_order_tu[x+1]:
            condition += 1
        elif "Fine Arts" in final_order_tu[x] and "Fine Arts" in final_order_tu[x+1]:
            condition += 1
        elif "Beliefs" in final_order_tu[x] and "Beliefs" in final_order_tu[x+1]:
            condition += 1
        elif "Thought" in final_order_tu[x] and "Thought" in final_order_tu[x+1]:
            condition += 1
        elif "Literature" in final_order_b[x] and "Literature" in final_order_b[x+1]:
            condition += 1
        elif "History" in final_order_b[x] and "History" in final_order_b[x+1]:
            condition += 1
        elif "Science" in final_order_b[x] and "Science" in final_order_b[x+1]:
            condition += 1
        elif "Fine Arts" in final_order_b[x] and "Fine Arts" in final_order_b[x+1]:
            condition += 1
        elif "Beliefs" in final_order_b[x] and "Beliefs" in final_order_b[x+1]:
            condition += 1
        elif "Thought" in final_order_b[x] and "Thought" in final_order_b[x+1]:
            condition += 1
    if condition == 0:
        return False
    else:
        return True

def check_adjacent_b_tu(final_order_tu, final_order_b):
    condition = 0
    for x in range(len(final_order_tu)-1):
        if "Literature" in final_order_b[x] and "Literature" in final_order_tu[x+1]:
            condition += 1
        elif "History" in final_order_b[x] and "History" in final_order_tu[x+1]:
            condition += 1
        elif "Science" in final_order_b[x] and "Science" in final_order_tu[x+1]:
            condition += 1
        elif "Fine Arts" in final_order_b[x] and "Fine Arts" in final_order_tu[x+1]:
            condition += 1
        elif "Beliefs" in final_order_b[x] and "Beliefs" in final_order_tu[x+1]:
            condition += 1
        elif "Thought" in final_order_b[x] and "Thought" in final_order_tu[x+1]:
            condition += 1
    if condition == 0:
        return False
    else:
        return True

def check_same_quarter_repeats(final_order_tu, final_order_b):
    condition = 0
    for x in range(len(final_order_tu)-15):
        tu = final_order_tu[x]
        b_position = final_order_b.index(tu)
        if b_position <= 4:
            condition += 1
    for x in range(len(final_order_tu)-15):
        tu = final_order_tu[x+5]
        b_position = final_order_b.index(tu)
        if b_position >= 5 and b_position <=9:
            condition += 1
    for x in range(len(final_order_tu)-15):
        tu = final_order_tu[x+10]
        b_position = final_order_b.index(tu)
        if b_position >= 10 and b_position <= 14:
            condition += 1
    for x in range(len(final_order_tu)-15):
        tu = final_order_tu[x+15]
        b_position = final_order_b.index(tu)
        if b_position >= 15:
            condition += 1
    if condition == 0:
        return False
    else:
        return True
