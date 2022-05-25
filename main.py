from docx_generator import *
from randomizer import *
from tkinter import *
from tkinter import messagebox
import sys

# TODO
# Add a way to determine a distribution in the interface
# Create a better method for splitting RM and PSS evenly between halves

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

desired_packets = 0
paired_questions = 0

def create_window():
    root = Tk()
    yes = IntVar()
    no = IntVar()
    global desired_packets, paired_questions

    l1 = Label(root, text="Number of packets to generate")
    l1.pack()
    s1 = Scale(root, from_=1, to=20, orient=HORIZONTAL)
    s1.pack()
    l2 = Label(root, text="Paired tossups and bonuses")
    l2.pack()
    c1 = Checkbutton(root, text="Yes", variable=yes)
    c1.pack()
    c2 = Checkbutton(root, text="No", variable=no)
    c2.pack()
    b1 = Button(root, text="Submit", command=root.quit)
    b1.pack()
    root.mainloop()

    if yes.get() == 1 and no.get() == 0:
        paired_questions = 1
    elif yes.get() == 0 and no.get() == 1:
        paired_questions = 0
    else:
        messagebox.showerror('Invalid Choice', 'Please choose either paired or unpaired questions')
        sys.exit()

    desired_packets = s1.get()


create_window()

print(desired_packets, paired_questions)

adjacent_categories = True
spaced_rmpss = True

for x in range(int(desired_packets)):
    while adjacent_categories or spaced_rmpss:
        print('shuffling...')
        tossups, bonuses = shuffle(lit, hist, sci, fa, rmpss)
        final_order_tu, final_order_b = generateOrder(tossups, bonuses)

        print('checking...')
        adjacent_categories = check_adjacent_categories(final_order_tu, final_order_b, categories)
        spaced_rmpss = check_spaced_rmpss(final_order_tu, final_order_b, categories)

        # adjacent_categories = False
        # spaced_rmpss = False

    docName = 'Packet ' + str(x + 1) + '.docx'
    create_docx(final_order_tu, final_order_b, docName, paired_questions)
    adjacent_categories = True
    spaced_rmpss = True
    tossups, bonuses = shuffle(lit, hist, sci, fa, rmpss)
    final_order_tu, final_order_b = generateOrder(tossups, bonuses)
