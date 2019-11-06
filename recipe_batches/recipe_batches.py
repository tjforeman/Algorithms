#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = []


  for k,v in recipe.items():
    print(f'{k}:{v}') 

    if len(recipe) > len(ingredients):
      return 0

    if k in ingredients:
      if recipe[k] <= ingredients[k]:

        max_batches.append(ingredients[k] // recipe[k])
        print(max_batches)
        print(ingredients[k])
        print(recipe[k])

        return min(max_batches)

      else:
        return 0

  return max_batches




if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = {'milk': 2, 'sugar': 40, 'butter': 20 }
  ingredients = {'milk': 5, 'sugar': 120, 'butter': 500 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))

  # milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }), 2)