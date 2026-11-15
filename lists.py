fav_games = ["Rdr2", "Expedition33", "Roblox", "GTAV"]
fav_games.append("Muse Dash")
print(fav_games)

print("Most: ", fav_games[0])
print("Less: ", fav_games[-1])

#///////////////////

notes = [99, 43, 78, 83]
print(len(notes))  #adet
notes.sort()
print(notes)

print("Highest note: ", notes[-1])
print("Lowest note: ", notes[0])

#//////////////////

books = []
a = input("book: ")
books.append(a)
a = input("book: ")
books.append(a)
a = input("book: ")
books.append(a)

books.sort()

print(books)
