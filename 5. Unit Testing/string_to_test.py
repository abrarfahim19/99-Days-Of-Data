import sys
# print(sys.argv[1])
def main():
    name = input("")
    print(hello(name))

def hello( to = "World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()