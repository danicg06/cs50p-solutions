import re


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r"(^|\W)um(\W|$)(.+)?"
    count = 0
    while True:
        matches = re.search(regex, s, re.IGNORECASE)

        if not matches:
            break

        count += 1

        if not matches.group(3):
            break

        s = f"{matches.group(3)}"
        matches = re.search(regex, s, re.IGNORECASE)

    return count


if __name__ == "__main__":
    main()
