def ingredients():

   questions = {
       "strong": "Do ye like yer drinks strong?",
       "salty": "Do ye like it with a salty tang?",
       "bitter": "Are ye a lubber who likes it bitter?",
       "sweet": "Would ye like a bit of sweetness with yer poison?",
       "fruity": "Are ye one for a fruity finish?"
}

   prefs = {}
   for q in questions:
      ans = raw_input(questions[q])
      if ans == 'yes' or ans == 'y':
          prefs[q] = True
      else:
          prefs[q] = False
   return prefs



def mixologist(a):

  ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}
  drink = []
  for x in a:
      if (a[x]) == True:
          drink.append(random.choice(ingredients[x]))
  print(drink)
   
if __name__ == '__main__':
  import random
  flavors = ingredients()
  mixologist(flavors)

