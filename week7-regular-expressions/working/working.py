import re

def main():
    print(convert(input("Hours: ")))

def format_24h(h, m, k):

    h = int(h)
    m = int(m)

    if h > 12 or h == 0 or m >= 60:
        raise ValueError("Invalid format or time")

    if k == "AM":
            h = 0 if h == 12 else h
    else:
        if h != 12:
            h += 12

    return f"{h:02}:{m:02}"

def convert(s):
    valid_hour = r"(\d{1,2})(?::(\d{2}))?"
    valid_meridiem = r"([AP]M)"
    hour = re.search(rf"^{valid_hour} {valid_meridiem} to {valid_hour} {valid_meridiem}$",s)

    if not hour:
        raise ValueError("Invalid format or time")

    h1, m1, k1, h2, m2, k2 = hour.groups()

    m1 = m1 if m1 else "00"
    m2 = m2 if m2 else "00"

    time1 = format_24h(h1, m1, k1)
    time2 = format_24h(h2, m2, k2)

    return f"{time1} to {time2}"


if __name__ == "__main__":
    main()
