
"""table = []
message = message.replace(" ", "_")
for _ in range(key):
    row = []
    for _ in range(len(message)):
        row.append(".")
    table.append(row)
row = 0
down_move = True
for i in range(len(message)):

    table[row][i] = message[i]
    if row == 0:
        row += 1
        down_move = True
    elif row == key - 1:
        row -= 1
        down_move = False
    elif down_move:
        row += 1
    elif not down_move:
        row -= 1
result = ""
for row in table:
    print("".join(row))
for i in range(1, len(message)):
    result += """