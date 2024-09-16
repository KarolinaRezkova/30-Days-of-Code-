#!/bin/python3

from sys import stdin

# Enter your code here. Read input from STDIN. Print output to STDOUT


def load_phone_book(n: int) -> dict[str, str]:
    contact_book = {}
    for i in range(n):
        line = input()
        entry = line.split()
        assert len(entry) == 2, "Invalid phone entry: " + line

        name, phone_number = entry
        assert name.isalpha() and name.islower(), "Name should contain only lowercase English alphabetic letters."
        assert phone_number.isdigit() and len(phone_number) == 8, "Phone number should consist of 8 digits."

        contact_book[name] = phone_number

    return contact_book


def answer_queries(contact_book: dict[str, str]):
    for line in stdin:
        query = line.strip()
        if query in contact_book:
            print(query + "=" + contact_book[query])
        else:
            print("Not found")


if __name__ == '__main__':
    number_of_entries = int(input().strip())
    assert 1 <= number_of_entries <= 100_000, "There are too many entries, should be less than 100_000."

    phone_book = load_phone_book(number_of_entries)

    answer_queries(phone_book)
