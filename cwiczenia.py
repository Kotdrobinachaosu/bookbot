# products = {
#     "jabłko": 5,
#     "gruszka": 12,
#     "banan": 8,
#     "arbuz": 20,
#     "pomarańcza": 9
# }


# powyzej10 = {k: v for k,v in products.items() if v < 10}

# print(powyzej10)

# numbers = {
#     1: 2,
#     2: 3,
#     3: 4,
#     4: 5
# }

# kwadrat = {k: v**2 for k,v in numbers.items()}
# print(kwadrat)

# words = {
#     "kot": 1,
#     "pies": 2,
#     "ryba": 3
# }

# upper_letter = {k.upper(): v for k, v in words.items()}
# print(upper_letter)

scores = {
    "Ala": 45,
    "Bartek": 82,
    "Kasia": 67,
    "Tomek": 39,
    "Ola": 90
}

adjusted_scores = {
    name: int(score * 1.1) if score < 50 else int(score * 0.95) if score > 80 else score
    for name, score in scores.items()
}

print(adjusted_scores)
