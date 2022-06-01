"""Generates and pushes a passphrase to pwpush.com, returns a link that expires"""
from tkinter import *
import pw

root = Tk()
root.title("PassLicker")
root.resizable(False, False)
root.configure(background='#08243b')
root.iconbitmap("passlicker.icns")

# global passphrase
# global link


def gen_and_push_click():
    print(include_digits_value.get())
    passphrase = pw.get_passphrase(
        (int(num_chars_box.get())), int(total_words_box.get()), (word_separator_box.get()), include_digits_value.get())
    link = pw.push_passphrase(passphrase, int(
        expire_days_box.get()), int(expire_views_box.get()))
    text_box.configure(state='normal')
    text_box.insert(1.0, link)
    text_box.insert(1.0, '\n')
    text_box.insert(1.0, passphrase)
    text_box.insert(1.0, '\n\n')
    text_box.configure(state='disabled')

def push_only_click():
    passphrase = specify_passphrase_box.get()
    link = pw.push_passphrase(passphrase, int(
        expire_days_box.get()), int(expire_views_box.get()))
    text_box.configure(state='normal')
    text_box.insert(1.0, link)
    text_box.insert(1.0, '\n')
    text_box.insert(1.0, passphrase)
    text_box.insert(1.0, '\n\n')
    text_box.configure(state='disabled')


# define text box
text_box = Text(root, height=20, width=80, padx=15, pady=15)
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
text_box.configure(state='disabled')

# tkinter variables


# WIDGETS

label_width = 15
label_padx = 2
label_pady = 10

l0 = Label(root, height=1, bg='#08243b')
l0.grid(column=0, row=0)

l10 = Label(root, height=1, bg='#08243b')
l10.grid(column=0, row=6)

num_chars_label = Label(root, text="Characters per word:",
                        width=label_width,
                        bg='#08243b',
                        fg='white',
                        border=2,
                        anchor='e',
                        padx=label_padx,
                        pady=label_pady)

total_words_label = Label(root, text="Total words:",
                          width=label_width,
                          bg='#08243b',
                          fg='white',
                          border=2,
                          anchor='e',
                          padx=label_padx,
                          pady=label_pady)
word_separator_label = Label(root, text="Word Separator:",
                             width=label_width,
                             bg='#08243b',
                             fg='white',
                             border=2,
                             anchor='e',
                             padx=label_padx,
                             pady=label_pady)
include_digits_label = Label(root, text="Include Digits?",
                             width=label_width,
                             bg='#08243b',
                             fg='white',
                             border=2,
                             anchor='e',
                             padx=label_padx,
                             pady=label_pady)
expire_days_label = Label(root, text="Expiration Days:",
                          bg='#08243b',
                          fg='white',
                          border=2,
                          anchor='e',
                          padx=label_padx,
                          pady=label_pady)
expire_views_label = Label(root, text="Expiration Views:",
                           bg='#08243b',
                           fg='white',
                           border=2,
                           anchor='e',
                           padx=label_padx,
                           pady=label_pady)
passphrase_settings_label = Label(root, text="Passphrase Settings:",
                                  width=label_width,
                                  bg='#1567ab',
                                  fg='white',
                                  border=2,
                                  anchor='e',
                                  padx=5,
                                  pady=5)

link_settings_label = Label(root, text="Link Settings:",
                            bg='#1567ab',
                            fg='white',
                            border=2,
                            anchor='e',
                            padx=5,
                            pady=5)
specify_passphrase_label = Label(root, text="Specify Passphrase:",
                            bg='#1567ab',
                            fg='white',
                            border=2,
                            anchor='e',
                            padx=5,
                            pady=5)


num_chars_box = Spinbox(
    root,
    from_=5,
    to=10,
    width=2,
    border=2,
    wrap=True)
total_words_box = Spinbox(
    root,
    from_=2,
    to=5,
    width=2,
    border=2,
    wrap=True)
expire_days_value = StringVar()
expire_days_value.set("14")
expire_days_box = Spinbox(
    root,
    from_=1,
    to=30,
    textvariable=expire_days_value,
    width=2,
    border=2,
    wrap=True)
expire_views_value = StringVar()
expire_views_value.set("10")
expire_views_box = Spinbox(
    root,
    from_=1,
    to=30,
    textvariable=expire_views_value,
    width=2,
    border=2,
    wrap=True)


word_separator_box = Entry(root, width=3,
                           fg='black', borderwidth=0)
word_separator_box.insert(0, '-')
specify_passphrase_box = Entry(root, width=15,
                           fg='black', borderwidth=0)

include_digits_value = IntVar()
include_digits_box = Checkbutton(
    root, variable=include_digits_value, bg='#08243b')
include_digits_box.select()
include_digits_box.include_digits_value = include_digits_value


gen_and_push = Button(root, text="Generate and Push\nRandom Passphrase", padx=5, pady=5, bg='white', fg="#17568a", font="Helvetica",
                       command=gen_and_push_click)
push_only = Button(root, text="Push Specified\nPassphrase", padx=5, pady=5, bg='white', fg="#17568a", font="Helvetica",
command=push_only_click)
# copy_pass_button = Button(root, text="Copy Passphrase", padx=0, pady=0,bg='white',fg="#17568a", font="Helvetica",
#                        command=copy_pass_click)
# copy_link_button = Button(root, text="Copy Link", padx=20, pady=0,bg='#17568a',fg="#17568a", font="Helvetica",
#                        command=pushit_click)

# GRID

specify_passphrase_label.grid(column=4, row=1,  columnspan=1,
                    rowspan=1)
specify_passphrase_box.grid(column=4, row=2,  columnspan=1,
                   rowspan=1)
push_only.grid(column=4, row=3,  columnspan=1,
                   rowspan=2, padx=5, pady=5)
gen_and_push.grid(column=4, row=5,  columnspan=1,
                   rowspan=2, padx=5, pady=5)



# copy_pass_button.grid(column=0, row=5,  columnspan=2,
#                    rowspan=1, padx=10, pady=10)
# copy_link_button.grid(column=3, row=5,  columnspan=3,
#                     rowspan=1, padx=10, pady=10)

passphrase_settings_label.grid(column=0, row=1, columnspan=2)
num_chars_box.grid(column=1, row=2)
total_words_box.grid(column=1, row=3)
word_separator_box.grid(column=1, row=4)
include_digits_box.grid(column=1, row=5)
expire_days_box.grid(column=3, row=2)
expire_views_box.grid(column=3, row=3)


num_chars_label.grid(column=0, row=2)
total_words_label.grid(column=0, row=3)
word_separator_label.grid(column=0, row=4)
include_digits_label.grid(column=0, row=5)

link_settings_label.grid(column=2, row=1, columnspan=2)
expire_days_label.grid(column=2, row=2)
expire_views_label.grid(column=2, row=3)


text_box.grid(column=0, row=10, columnspan=5)

root.mainloop()
