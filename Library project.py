library = []
wishlist = []

owned = input("Enter the name of a book you own: ")
library.append(owned)

owned_2 = input("Enter the name of another book you own or press 'Enter' to skip: ")
if owned_2:
    library.append(owned_2)

print(f"\nYour library: {library}\n")

wishes = input("Enter the name of a book you wish to have: ")
wishlist.append(wishes)

wishes_2 = input("Enter the name of another book you wish to have or press 'Enter' to skip: ")
if wishes_2:
    wishlist.append(wishes_2)

print(f"\nYour wishlist: {wishlist}\n")

have_acquired = input("Enter the name of a book from your wishlist you've acquired or press 'Enter' to skip: ")
if have_acquired in wishlist:
    wishlist.remove(have_acquired)
    library.append(have_acquired)

print(f"\nUpdated library: {library}")
print(f"Updated wishlist: {wishlist}\n")

donation = input("Enter the name of a book from your library you wish to donate or press 'Enter' to skip: ")
if donation in library:
    library.remove(donation)

print(f"\nFinal library after donations: {library}")
