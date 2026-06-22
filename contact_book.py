from tkinter import *

root = Tk()

root.geometry("1000x500")
root.title("Contact Book")


# ---------- FUNCTIONS ----------

def add_contact():

    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        result_box.delete("1.0", END)
        result_box.insert(END, "Name and Phone are required!")
        return

    if not phone.isdigit():
        result_box.delete("1.0", END)
        result_box.insert(END, "Phone number must contain digits only!")
        return

    if len(phone) != 10:
        result_box.delete("1.0", END)
        result_box.insert(END, "Phone number must be 10 digits!")
        return

    with open("contact_book.txt", "a") as file:
        file.write(name + "," + phone + "," + email + "," + address + "\n")

    result_box.delete("1.0", END)
    result_box.insert(END, "Contact added successfully!")

    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

def view_contact():

    try:
        with open("contact_book.txt", "r") as file:
            data = file.read()

        result_box.delete("1.0", END)
        result_box.insert(END, data)

    except FileNotFoundError:
        result_box.delete("1.0", END)
        result_box.insert(END, "No contacts found!")


def search_contact():

    search_name = name_entry.get()

    try:
        with open("contact_book.txt", "r") as file:
            lines = file.readlines()

        found = False

        for line in lines:

            name, phone, email, address = line.strip().split(",")

            if name.lower() == search_name.lower():

                result_box.delete("1.0", END)
                result_box.insert(
                    END,
                    f"Name: {name}\nPhone: {phone}\nEmail: {email}\nAddress: {address}"
                )

                found = True
                break

        if not found:
            result_box.delete("1.0", END)
            result_box.insert(END, "Contact not found!")

    except FileNotFoundError:
        result_box.delete("1.0", END)
        result_box.insert(END, "No contacts found!")


def update_contact():

    search_name = name_entry.get()

    try:
        with open("contact_book.txt", "r") as file:
            lines = file.readlines()

        found = False

        with open("contact_book.txt", "w") as file:

            for line in lines:

                name, phone, email, address = line.strip().split(",")

                if name.lower() == search_name.lower():

                    new_name = name_entry.get()
                    new_phone = phone_entry.get()
                    new_email = email_entry.get()
                    new_address = address_entry.get()

                    file.write(
                        new_name + "," +
                        new_phone + "," +
                        new_email + "," +
                        new_address + "\n"
                    )

                    found = True

                else:
                    file.write(line)

        result_box.delete("1.0", END)

        if found:
            result_box.insert(END, "Contact updated successfully!")
        else:
            result_box.insert(END, "Contact not found!")

    except FileNotFoundError:
        result_box.delete("1.0", END)
        result_box.insert(END, "No contacts found!")


def delete_contact():

    delete_name = name_entry.get()

    try:
        with open("contact_book.txt", "r") as file:
            lines = file.readlines()

        found = False

        with open("contact_book.txt", "w") as file:

            for line in lines:

                name, phone, email, address = line.strip().split(",")

                if name.lower() == delete_name.lower():
                    found = True
                    continue

                file.write(line)

        result_box.delete("1.0", END)

        if found:
            result_box.insert(END, "Contact deleted successfully!")
        else:
            result_box.insert(END, "Contact not found!")

    except FileNotFoundError:
        result_box.delete("1.0", END)
        result_box.insert(END, "No contacts found!")


def exit_app():
    root.destroy()


# ---------- LABELS ----------

name_label = Label(root, text="Name")
name_label.pack()

name_entry = Entry(root, width=40)
name_entry.pack()

phone_label = Label(root, text="Phone")
phone_label.pack()

phone_entry = Entry(root, width=40)
phone_entry.pack()

email_label = Label(root, text="Email")
email_label.pack()

email_entry = Entry(root, width=40)
email_entry.pack()

address_label = Label(root, text="Address")
address_label.pack()

address_entry = Entry(root, width=40)
address_entry.pack()


# ---------- BUTTONS ----------

add = Button(root, text="Add Contact", command=add_contact)
add.pack(pady=5)

view = Button(root, text="View Contacts", command=view_contact)
view.pack(pady=5)

search = Button(root, text="Search Contact", command=search_contact)
search.pack(pady=5)

update = Button(root, text="Update Contact", command=update_contact)
update.pack(pady=5)

delete = Button(root, text="Delete Contact", command=delete_contact)
delete.pack(pady=5)

exit_button = Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)


# ---------- OUTPUT BOX ----------

result_box = Text(root, height=10, width=60)
result_box.pack(pady=10)


root.mainloop()