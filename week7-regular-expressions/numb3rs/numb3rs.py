import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    digit = r"(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)"
    return bool(re.search(rf"^({digit}\.){{3}}{digit}$", ip))


if __name__ == "__main__":
    main()
