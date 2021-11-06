"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    file = open(filename)
    species = {line.split('|')[1] for line in file}

    file.close()

    return species
  
# print(all_species("villagers.csv"))


def get_villagers_by_species(filename, species="All"):
    """Return a list of villagers' names by species.

    Arguments:
      - filename (str): the path to a data file
      - species (str): optional, the name of a species

    Return:
      - list: a list alphabetical
    """

    file = open(filename)

    if species != 'All':
      villagers = [line.split('|')[0] for line in file if line.split('|')[1] == species]
    else:
      villagers = [line.split('|')[0] for line in file]

    file.close()

    return sorted(villagers)

# print(get_villagers_by_species("villagers.csv", "Anteater"))


def all_names_by_hobby(filename):
    """Return a list that villagers' names, grouped by hobby.

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    # TODO: replace this with your code
    hobbies = ['Fitness' , 'Nature', 'Education', 'Music', 'Fashion', 'Play']
    result = [[] for hobby in hobbies]

    file = open(filename)

    for line in file:
      data = line.split('|')
      name = data[0]
      hobby = data[3]
      if hobby == 'Fitness':
        result[0].append(name)
      elif hobby == 'Nature':
        result[1].append(name)
      elif hobby == 'Education':
        result[2].append(name)
      elif hobby == 'Music':
        result[3].append(name)
      elif hobby == 'Fashion':
        result[4].append(name)
      elif hobby == 'Play':
        result[5].append(name)
    file.close()
    return [sorted(names) for names in result]

# print(all_names_by_hobby("villagers.csv"))

def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    file = open(filename)
    all_data = []

    #create a for loop
    for line in file:
      #create a tuple for each line in the file
      villager = tuple(line.strip().split('|'))
      #append the tuple to the all_data list
      all_data.append(villager)

    file.close()
    # TODO: replace this with your code

    return all_data
# print(all_data("villagers.csv"))

def find_motto(filename, name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's motto or None
    """
    file = open(filename)
    result = None

    for line in file:
      line = line.strip().split('|')
      villager = line[0]
      motto = line[4]
      if villager == name:
        result = motto

    file.close()

    return result

# print(find_motto("villagers.csv", "Audie"))


def find_likeminded_villagers(filename, name):
    """Return a set of villagers with the same personality as the given villager."""

    file = open(filename)
    personality = ""
    like_minded = set()
  # look up villager's personality
    for line in file:
      line = line.strip().split('|')
      villager = line[0]
      if villager == name:
        personality = line[2]
    
    file.close()
    file = open(filename)
  # for loop to build set of all villagers w/ same personality
    for line in file:
        line = line.strip().split('|')
        villager_p = line[2]
        if villager_p == personality:
          like_minded.add(line[0])
    file.close()

    return like_minded

print(find_likeminded_villagers('villagers.csv','Kyle'))