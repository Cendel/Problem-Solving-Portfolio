# Question: https://www.codingame.com/ide/puzzle/retro-typewriter-art

# Completed!

t = ['1sp', '1/', '1bS', '1_', '1/', '1bS', 'nl', '1(', '1sp', '1o', '1.', '1o', '1sp', '1)', 'nl', '1sp', '1>', '1sp',
     '1^', '1sp', '1<', 'nl', '2sp', '3|']

abbreviations = {"sp": " ", "bS": "\\", "sQ": "'", "nl": "\n"}

result = ""

for i in t:
    symbol = ""
    times = 1
    if any(abb for abb in abbreviations.keys() if i.endswith(abb)):
        symbol = [abbreviations[abb]
                  for abb in abbreviations.keys() if i.endswith(abb)][0]
        times = int(i[0:-2]) if len(i) > 2 else 1
    else:
        symbol = i[-1]
        times = int(i[0:-1])
    result = result + f"{symbol * times}"
print(result)
