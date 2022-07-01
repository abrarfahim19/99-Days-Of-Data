def main():
    student = get_students()
    print(f"{student['name']}")


def get_students():
    name = input("name?")
    house = input("house?")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main()
