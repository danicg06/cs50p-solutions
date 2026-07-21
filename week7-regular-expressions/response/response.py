from validator_collection import checkers

def main():
    print(is_email(input("What's your email address? ")))

def is_email(s):
    if checkers.is_email(s):
        return "Valid"
    else:
        return "Invalid"

if __name__ == "__main__":
    main()
