name = input("What's your name? ")
'''Doc String'''
match name:
    case "Harry" | "Ron" | "Hermione":
        print("From gryfindor")
    case _:
        print("Not found")