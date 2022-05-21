from docx_generator import *
from randomizer import *

# TODO
# Expand to create multiple packets
# Make work TU/B/TU/B format
# Split RM and PSS evenly between halves
# Change category labels (ie no more "Social Sci Thought" or "Myth Beliefs")

lit = list(["American Literature", "European Literature", "World Literature", "British Literature"])
hist = list(["American History", "European History", "World History", "Other History"])
sci = list(["Biology Science", "Chemistry Science", "Physics Science", "Other Science"])
fa = list(["Auditory Fine Arts", "Visual Fine Arts", "Other Fine Arts", "Other"])
rmpss = list(["Religion Beliefs", "Myth Beliefs", "Philosophy Thought", "Social Sci Thought"])

tu_b_pairs = True
adjacent_categories = True
adjacent_b_tu = True
same_quarter_repeats = True

while tu_b_pairs or adjacent_categories or adjacent_b_tu or same_quarter_repeats:
    print('shuffling...')
    shuffled_lit_tu = shuffle_lit_tu(lit)
    shuffled_hist_tu = shuffle_hist_tu(hist)
    shuffled_sci_tu = shuffle_sci_tu(sci)
    shuffled_fa_tu = shuffle_fa_tu(fa)
    shuffled_rmpss_tu = shuffle_rmpss_tu(rmpss)

    shuffled_lit_b = shuffle_lit_b(lit)
    shuffled_hist_b = shuffle_hist_b(hist)
    shuffled_sci_b = shuffle_sci_b(sci)
    shuffled_fa_b = shuffle_fa_b(fa)
    shuffled_rmpss_b = shuffle_rmpss_b(rmpss)

    final_order_tu = fill_quarters_tu(shuffled_lit_tu, shuffled_hist_tu, shuffled_sci_tu, shuffled_fa_tu, shuffled_rmpss_tu)

    final_order_b = fill_quarters_b(shuffled_lit_b, shuffled_hist_b, shuffled_sci_b, shuffled_fa_b, shuffled_rmpss_b)

    print('checking...')
    tu_b_pairs = check_pairs(final_order_tu, final_order_b)
    adjacent_categories = check_adjacent_categories(final_order_tu, final_order_b)
    adjacent_b_tu = check_adjacent_b_tu(final_order_tu, final_order_b)
    same_quarter_repeats = check_same_quarter_repeats(final_order_tu, final_order_b)

    #tu_b_pairs = False
    #adjacent_categories = False
    #adjacent_b_tu = False
    #same_quarter_repeats = False

create_docx(final_order_tu, final_order_b)