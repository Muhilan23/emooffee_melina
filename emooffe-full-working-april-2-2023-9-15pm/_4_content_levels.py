'''
Title : Content levels  for Emooffee
Date Created :  April 2, 2023 | Last Updated : April 2, 2023
Python version 3.11.2 
'''


# ----- Imports 
import matplotlib.pyplot as plt

def content_levels(current_user_emotion):
    
    levels = {}
    emooffee_type = ''

    if (current_user_emotion == 'HAPPY') :
        emooffee_type = 'WHIPPED CREAM COFFEE'
        cup = 6
        levels ={ 
            'espresso' : 4/cup, 
            'whipped' : 2/cup
        }

    elif (current_user_emotion in ['SAD','STRESSED']):
        emooffee_type = 'ESPRESSO'
        cup = 3
        levels ={
            'espresso' : 2/cup,
            'water' : 1/cup
        }

    elif (current_user_emotion in ['FEAR', 'ANGRY']):
        emooffee_type = 'ICED / DEFAC LATTE'
        cup = 12
        levels ={
            'milk' : 6/cup,
            'espresso' : 2/cup ,
            'ice' : 4/cup
        }

    elif (current_user_emotion == 'NEUTRAL'):
        emooffee_type = 'CAPPUCINO / LATTE'
        cup = 7
        levels ={
            'espresso' : 1/cup,
            'steamed milk' : 2/cup,
            'foamed milk' : 2/cup,
            'chocolate powder' : 2/cup
        }

    elif (current_user_emotion == 'SURPRISE'):
        emooffee_type = 'MOCHA'
        cup = 7
        levels = {
            'espresso' : 1/cup,
            'chocolate syrup' : 2/cup,
            'steamed milk' : 2/cup,
            'whipped cream' : 2/cup
        }


    content_values = [i for i in levels.values()]
    content_keys = [j for j in levels.keys()]


    # ----- Final show
    plt.pie(content_values, labels = content_keys , startangle = 90, autopct = '%1.1f%%')
    plt.title(current_user_emotion+"\n"+emooffee_type)
    plt.savefig("C:/Users/navee/Documents/programs/python/emooffee/static/temp/user_levels.png")
    
    return current_user_emotion, emooffee_type, levels

'''
# Current user emotion 
current_user_emotion = 'FEAR'
content_levels(current_user_emotion)
'''