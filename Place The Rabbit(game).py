print("Welcome to place the rabbit...")
grass = [ 
    ['🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿'],
    ['🌿', '🌿', '🌿']
]
print(f"\n{grass[0]}\n{grass[1]}\n{grass[2]}")

print("\nWhere should the rabbit go? 🐇")
place = input("Please choose a row and a column: ")

row = int((place[0])) - 1
col = int((place[1])) - 1

grass[row][col] = "🐇"

print(f"\n{grass[0]}\n{grass[1]}\n{grass[2]}")

