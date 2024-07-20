def parse_input(user_input):
    parts = user_input.strip().split()
    command = parts[0].lower()
    args = parts[1:]
    return command, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: You need to provide a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with number {phone}."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: You need to provide a name and a new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated to new number {phone}."
    else:
        return "Error: Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: You need to provide a name."
    name = args[0]
    if name in contacts:
        return f"{name}'s number is {contacts[name]}."
    else:
        return "Error: Contact not found."

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot! Type 'exit' or 'close' to exit.")
    
    while True:
        user_input = input("Enter a command: ")
        if user_input.lower() in ["exit", "close"]:
            print("Good bye!")
            break

        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
