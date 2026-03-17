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

print(format_welcome(team_name))
display_members(members)
print("Liczba członków zespołu:", count_members(members))

print("Projekt uruchomił się poprawnie")