import random

def find_preferences():
   questions = {
       "strong": "Do ye like yer drinks strong?",
       "salty": "Do ye like it with a salty tang?",
       "bitter": "Are ye a lubber who likes it bitter?",
       "sweet": "Would ye like a bit of sweetness with yer poison?",
       "fruity": "Are ye one for a fruity finish?"
}
   preferences = {}
   for question in questions:
      ans = raw_input(questions[question])
      if ans == 'yes' or ans == 'y':
          preferences[question] = True
      else:
          preferences[question] = False
   return preferences

def make_drinks(preferences):

  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
  drink_ingredients = []
  for x in preferences:
      if (preferences[x]) == True:
          drink_ingredients.append(random.choice(ingredients[x]))
  return drink_ingredients

def main():
  preferences = find_preferences()
  drink = make_drinks(preferences)

  for ingredient in drink:
      print "A {}".format(ingredient)
if __name__ == '__main__':
  main()  

