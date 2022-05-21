from docx_generator import *
from randomizer import *

# TODO
# Expand to create multiple packets
# Make work TU/B/TU/B format
# Split RM and PSS evenly between halves

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

while adjacent_categories:
    print('shuffling...')
    tossups, bonuses = shuffle(lit, hist, sci, fa, rmpss)
    final_order_tu, final_order_b = generateOrder(tossups, bonuses)

    print('checking...')
    adjacent_categories = check_adjacent_categories(final_order_tu, final_order_b, categories)

    #adjacent_categories = False

docName = 'Packet 3.docx'
create_docx(final_order_tu, final_order_b, docName)