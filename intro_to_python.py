games = ['Dark Souls', 'Death Stranding', 'Getting Over It']
# append items to a list
games.append('Far Cry 5')

# string interpolation
print(f'The Length of the games list is {len(games)}')
print('The length of the games list is {}'.format(games))

array_of_ones = [1] * 5

# creating a list with range
one_through_ten = list(range(10))
print(one_through_ten)

random_numbers = [2, 5, 9, 2, 1]
# sort a list
random_numbers.sort()

my_name = 'barent langwell'
# reverse order of string
my_name[::-1]

# dictionary
cat = {
  'name': 'waffles',
  'location': 'california',
  'age': 3
}

print(cat)

# access dictionary values with bracket notation
cat['name']
cat[0]
cat['location']
cat[1]
cat['age']
cat[2]


def print_games(game1, game2): 
    