nam = input("What's your name? ")

match nam:
    case "Harry" | "Ron" | "Hermione":
        print("From gryfindor")
    case _:
        print("Not found")
