def count_members(members):
    return len(members)

def format_welcome(team_name):
    return f"Witaj w projekcie zespołu: {team_name}"

def display_members(members):
    print("Członkowie zespołu:")
    for member in members:
        print("-", member)

team_name = "Grupa 4"
members = ["Jakub Karaśkiewicz", "Jakub Karolewski"]

print("-----------------TEST1-----------------")

if count_members(members) == 2:
    print("W grupie jest dwóch członków")
else:
    print("Liczba członków w grupie jest różna od 2")

print("\n-----------------TEST2-----------------")

if count_members(members) != 0:
    print("W grupie są członkowie")
else:
    print("W grupie nie ma członków")