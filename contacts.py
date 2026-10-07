contacts = []

def add_contact(name, phone):
    contacts.append({
        "name": name,
        "phone": phone
    })

def show_contacts():
    for contact in contacts:
        print(contact["name"], "-", contact["phone"])

add_contact("Alice", "081234567")
add_contact("Bob", "089876543")

show_contacts()
