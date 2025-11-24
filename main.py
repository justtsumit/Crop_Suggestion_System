#CROP SUGGESTION SYSTEM

def suggest_crop(soil_type,season,budget):
    import random
    crops = {
        'black': {'kharif':['cotton','jowar','bajra','groundnut','soyabean'],
                  'rabi':['wheat','mustard','gram','barley'],
                  'zaid':[ 'watermelon','muskmelon','vegetable']
        },
        'alluvial':{'kharif':['rice','maize','sugarcane','cotton'],
                    'rabi':['wheat','gram','barley','mustard'],
                    'zaid':['vegetables','foodercrops','watermelon']
        },
        'red':{'kharif':['rice','groundnut','milets','cotton'],
                    'rabi':['wheat','gram','mustard'],
                    'zaid':['vegetables','foodercrops','watermelon']
        },
    }
    affordable_crops = {
        'low':['maize','bajra','vegetable','foodercrop'],       
        'medium':['cotton','groundnut','watermelons','bajra'],
        'high': [ 'maize', 'wheat','soyabean','mustards','gram','jowar','rice']
    }
    possible_crops = crops.get(soil_type,{}).get(season,[])
    suggested_crops = [crop for crop in possible_crops if crop in affordable_crops.get(budget,[])]
    if not suggested_crops :
        return " SOrrY ! no suitable crop found for the given conditions "
    return random.choice(suggested_crops)
#example use
soil = input("Enter soil type (black / alluvial / red): ").lower()
season = input("Enter season (kharif / rabi / zaid): ").lower()
budget = input("Enter budget (low / medium / high): ").lower()

valid_soils = ['black', 'alluvial', 'red']
valid_seasons = ['kharif', 'rabi', 'zaid']
valid_budgets = ['low', 'medium', 'high'] 
if soil in valid_soils and season in valid_seasons and budget in valid_budgets:
    suggested_crop = suggest_crop(soil,season,budget)
    print(f"\nSuggested crop for soil type '{soil}' , season '{season}' , and budget '{budget}': {suggested_crop}")
else :
    print("\nYOU ENTER SOMETHINg WRONG PLEASE CHECK IT !")

