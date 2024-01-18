def main():
    age = get_age()
    print(f"Hello world from {age}")

def get_age():
    while True:
        try:
            return int(input("What's your age? "))
        except ValueError:
            pass
            

main()