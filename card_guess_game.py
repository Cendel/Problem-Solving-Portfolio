# Question: https://www.codingame.com/ide/puzzle/card-counting-when-easily-distracted

# Completed!

import sys


def calculate_percentage(stream, threshold):
    char_list = ["A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "T", "J", "Q", "K"]

    def get_value(symbol):
        if symbol in ["J", "Q", "K", "T"]:
            return 10
        elif symbol == "A":
            return 1
        else:
            return int(symbol)

    lst = [i for i in stream if all(c in char_list for c in i)]
    deck = "".join([i * (4 - lst.count(i)) for i in char_list])
    lower = sum(1 for i in deck if get_value(i) < threshold)

    percentage = round(lower / len(deck) * 100, 2)
    return f"{percentage}%"


if __name__ == "__main__":
    try:
        stream = input("Enter characters separated by dots: ").split(".")
        threshold = int(input("Enter the threshold: "))
        result = calculate_percentage(stream, threshold)
        print("Percentage below threshold:", result)
    except ValueError:
        print("Invalid input. Please enter a valid threshold.")
    except Exception as e:
        print("An error occurred:", str(e))
