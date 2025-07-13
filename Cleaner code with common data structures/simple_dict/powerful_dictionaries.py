# create a dictionary:
d = dict()
d = {}
d = dict(bill=2, zoe=7, michael=4)
d = {"bill": 2, "zoe": 7, "michael": 4}

# access the value by key
name = "zoe"
print(f"Wins by {name} are {d[name]}")
# prints: Wins by zoe are 7

# Safer access:
wins = d.get("name")
if wins:
    print(f"There are {wins} wins")
else:
    print("No games played")
