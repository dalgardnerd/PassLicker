"""Generates and pushes a passphrase to pwpush.com, returns a link that expires"""
from cgitb import text
from tkinter import *
import pw
import json
from settings import load_defaults, write_defaults, handle_defaults

root = Tk()
root.title("PassLicker")
root.resizable(False, False)
root.configure(background='#08243b')
root.iconbitmap("passlicker.ico")


LABEL_WIDTH = 15
LABEL_PADX = 2
LABEL_PADY = 10


def gen_and_push_click():
    print(include_digits_var.get())
    passphrase = pw.get_passphrase(
        (int(num_chars_box.get())), int(total_words_box.get()), (word_separator_box.get()), include_digits_var.get())
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


def save_settings_click():
    num_chars = num_chars_box.get()
    total_words = total_words_box.get()
    word_separator = word_separator_box.get()
    include_digits = "True" if (include_digits_var.get() == 1) else "False"
    expire_days = expire_days_box.get()
    expire_views = expire_views_box.get()
    write_defaults(num_chars, total_words, word_separator,
                   include_digits, expire_days, expire_views)
    text_box.configure(state='normal')
    text_box.insert(1.0, "Settings saved to defaults.json")
    text_box.insert(1.0, '\n\n')
    text_box.configure(state='disabled')


settings = handle_defaults()


# WIDGETS

text_box = Text(root, height=20, width=80, padx=15, pady=15)
text_box.tag_configure("center", justify="center")
text_box.tag_add("center", 1.0, "end")
text_box.configure(state='disabled')


l0 = Label(root, height=1, bg='#08243b')
l0.grid(column=0, row=0)

l10 = Label(root, height=1, bg='#08243b')
l10.grid(column=0, row=6)

num_chars_label = Label(root, text="Characters per word:",
                        width=LABEL_WIDTH,
                        bg='#08243b',
                        fg='white',
                        border=2,
                        anchor='e',
                        padx=LABEL_PADX,
                        pady=LABEL_PADY)

total_words_label = Label(root, text="Total words:",
                          width=LABEL_WIDTH,
                          bg='#08243b',
                          fg='white',
                          border=2,
                          anchor='e',
                          padx=LABEL_PADX,
                          pady=LABEL_PADY)
word_separator_label = Label(root, text="Word Separator:",
                             width=LABEL_WIDTH,
                             bg='#08243b',
                             fg='white',
                             border=2,
                             anchor='e',
                             padx=LABEL_PADX,
                             pady=LABEL_PADY)
include_digits_label = Label(root, text="Include Digits?",
                             width=LABEL_WIDTH,
                             bg='#08243b',
                             fg='white',
                             border=2,
                             anchor='e',
                             padx=LABEL_PADX,
                             pady=LABEL_PADY)
expire_days_label = Label(root, text="Expiration Days:",
                          bg='#08243b',
                          fg='white',
                          border=2,
                          anchor='e',
                          padx=LABEL_PADX,
                          pady=LABEL_PADY)
expire_views_label = Label(root, text="Expiration Views:",
                           bg='#08243b',
                           fg='white',
                           border=2,
                           anchor='e',
                           padx=LABEL_PADX,
                           pady=LABEL_PADY)
passphrase_settings_label = Label(root, text="Passphrase Settings:",
                                  width=LABEL_WIDTH,
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

num_chars_var = IntVar()
num_chars_var.set(settings['num_chars'])
num_chars_box = Spinbox(
    root,
    from_=3,
    to=17,
    textvariable=num_chars_var,
    width=2,
    border=2,
    wrap=True)
total_words_var = IntVar()
total_words_var.set(settings['total_words'])
total_words_box = Spinbox(
    root,
    from_=2,
    to=7,
    textvariable=total_words_var,
    width=2,
    border=2,
    wrap=True)
expire_days_var = IntVar()
expire_days_var.set(settings['expire_days'])
expire_days_box = Spinbox(
    root,
    from_=settings['expire_days'],
    to=60,
    textvariable=expire_days_var,
    width=2,
    border=2,
    wrap=True)

expire_views_var = IntVar()
expire_views_var.set(settings['expire_views'])
expire_views_box = Spinbox(
    root,
    from_=1,
    to=50,
    textvariable=expire_views_var,
    width=2,
    border=2,
    wrap=True)

word_separator_var = StringVar()
word_separator_var.set(settings['word_separator'])
word_separator_box = Entry(
    root, width=3, textvariable=word_separator_var, fg='black', borderwidth=0)


specify_passphrase_box = Entry(root, width=25,
                               fg='black', borderwidth=0)

include_digits_var = IntVar()
if settings['include_digits'] == "True":
    include_digits_var.set(1)
else:
    include_digits_var.set(0)
include_digits_box = Checkbutton(
    root, variable=include_digits_var, bg='#08243b')


gen_and_push = Button(root, text="Generate and Push\nRandom Passphrase", padx=5, pady=5, bg='white', fg="#17568a", font="Helvetica",
                      command=gen_and_push_click)
push_only = Button(root, text="Push Specified\nPassphrase", padx=5, pady=5, bg='white', fg="#17568a", font="Helvetica",
                   command=push_only_click)
save_settings = Button(root, text="Save Current Settings", padx=5, pady=5, bg='white', fg="#17568a", font="Helvetica",
                       command=save_settings_click)


# GRID

specify_passphrase_label.grid(column=4, row=1,  columnspan=1,
                              rowspan=1)
specify_passphrase_box.grid(column=4, row=2,  columnspan=1,
                            rowspan=1)
push_only.grid(column=4, row=3,  columnspan=1,
               rowspan=2, padx=5, pady=5)
gen_and_push.grid(column=4, row=5,  columnspan=1,
                  rowspan=2, padx=5, pady=5)
save_settings.grid(column=2, row=5,  columnspan=2,
                   rowspan=2, padx=5, pady=5)


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
