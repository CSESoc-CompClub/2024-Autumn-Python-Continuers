# Dictionaries
"""
A student named Jack is using a dictionary to make a list of all the countries he wants to visit in the future,
starting with their capital cities.
"""
capitals = {"USA":"Washington D.C.", "France":"Paris", "China": "Mexico"}

"""1. Jack found a mistake in his dictionary. Can you fix it?"""
# TODO: IMPLEMENT THIS
capitals['China'] = 'Beijing'

print('1. Updated dictionary:', capitals)  # DO NOT MODIFY THIS LINE

# =========================================================================================================================#
"""2. Jack suddenly wants to visit Japan and Spain as well. Can you help him add the relevant entries to his dictionary?"""
# TODO: IMPLEMENT THIS
capitals['Japan'] = 'Tokyo'
capitals['Spain'] = 'Madrid'

print('2. Updated dictionary:', capitals)  # DO NOT MODIFY THIS LINE

# =========================================================================================================================#
"""3. Jack doesn't want to go to France anymore. Can you update his dictionary to reflect this?"""
# TODO: IMPLEMENT THIS
capitals.pop('France')

print('3. Updated dictionary:', capitals)  # DO NOT MODIFY THIS LINE

# =========================================================================================================================#
"""4. Edit this for loop so it prints out all the countries and capitals Jack is visiting, and how many cities he visits in total."""
def countries_and_capitals():
  sum = 0
  for key in capitals:
    print('The capital of ' + key + ' is ' + capitals[key])
    sum += 1
  print('In the end, Jack visited', sum, 'capital cities.')

countries_and_capitals()
