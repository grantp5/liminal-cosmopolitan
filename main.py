from docx_generator import *
from randomizer import *

# TODO
# Create interface for selecting number of packets, distribution, etc
# Make work TU/B/TU/B format (integrate into interface)
# Split RM and PSS evenly between halves (create a better method for it)

categories = {"American Literature": "Literature",
              "European Literature": "Literature",
              "World Literature": "Literature",
              "British Literature": "Literature",
              "Biology": "Science",
              "Chemistry": "Science",
              "Physics": "Science",
              "Other Science": "Science",
              "American History": "History",
              "European History": "History",
              "World History": "History",
              "Other History": "History",
              "Auditory Fine Arts": "Arts",
              "Visual Fine Arts": "Arts",
              "Other Fine Arts": "Arts",
              "Religion": "Beliefs",
              "Mythology": "Beliefs",
              "Philosophy": "Thought",
              "Social Science": "Thought",
              "Other": "Other"}

lit = ["American Literature", "European Literature", "World Literature", "British Literature"]
hist = ["American History", "European History", "World History", "Other History"]
sci = ["Biology", "Chemistry", "Physics", "Other Science"]
fa = ["Auditory Fine Arts", "Visual Fine Arts", "Other Fine Arts", "Other"]
rmpss = ["Religion", "Mythology", "Philosophy", "Social Science"]

adjacent_categories = True
spaced_rmpss = True

desired_packets = input("How many packets?: ")

for x in range(int(desired_packets)):
    while adjacent_categories or spaced_rmpss:
        print('shuffling...')
        tossups, bonuses = shuffle(lit, hist, sci, fa, rmpss)
        final_order_tu, final_order_b = generateOrder(tossups, bonuses)

        print('checking...')
        adjacent_categories = check_adjacent_categories(final_order_tu, final_order_b, categories)
        spaced_rmpss = check_spaced_rmpss(final_order_tu, final_order_b, categories)

        #adjacent_categories = False
        #spaced_rmpss = False

    docName = 'Packet ' + str(x+1) + '.docx'
    create_docx(final_order_tu, final_order_b, docName)
    tossups, bonuses = shuffle(lit, hist, sci, fa, rmpss)
    final_order_tu, final_order_b = generateOrder(tossups, bonuses)
