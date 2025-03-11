import streamlit as st

def quiz():
    st.title("Which Diet is Right for You?")
    
    score = {
        "mediterranean": 0, "intermittent_fasting": 0, "keto": 0, "ww": 0, "dash": 0, 
        "low_carb": 0, "atkins": 0, "volumetrics": 0, "fast800": 0, "tlc": 0, 
        "mayo": 0, "flexitarian": 0, "sirtfood": 0, "south_beach": 0, "hmr": 0, 
        "dukan": 0, "psmf": 0, "adf": 0, "military": 0, "cico": 0
    }

q1 = st.radio("Do you prefer structured meal plans or flexibility?", 
              ("Structured", "Flexible"))
if q1 == "Structured":
    score["Keto"] += 1
    score["WW"] += 1
    score["Fast800"] += 1
else:
    score["Mediterranean"] += 1
    score["Flexitarian"] += 1

q2 = st.radio("How fast do you want to lose weight?", 
              ("Fast results (1-2 kg per week / 2+ pounds per week)", "Steady long-term weight loss (0.5-1 kg per week / 1-2 pounds per week)"))
if q2 == "Fast results (1-2 kg per week / 2+ pounds per week)":
    score["Keto"] += 1
    score["Military"] += 1
    score["Fast800"] += 1
else:
    score["Mediterranean"] += 1
    score["DASH"] += 1

q3 = st.radio("Do you struggle with carb cravings?", 
              ("Yes, I need a low-carb approach", "No, I prefer balanced meals"))
if q3 == "Yes, I need a low-carb approach":
    score["Keto"] += 1
    score["Atkins"] += 1
    score["Low-Carb"] += 1
else:
    score["Mediterranean"] += 1
    score["Volumetrics"] += 1

q4 = st.radio("Do you want a cheaper affordable diet or does it not matter?", 
              ("Affordable", "Does not matter"))
if q4 == "Affordable":
    score["CICO"] += 1
    score["WW"] += 1

q5 = st.radio("Do you want an easy-to-follow diet or does it matter?", 
              ("Easy-to-follow", "Does not matter"))
if q5 == "Easy-to-follow":
    score["Mediterranean"] += 1
    score["WW"] += 1

q6 = st.radio("Do you get sugar cravings?", 
              ("Yes, I struggle to go without sugar", "No, I manage to go without sugar", "Yes and no, if I manage to get over my sugar addiction"))
if q6 == "Yes, I struggle to go without sugar":
    score["CICO"] += 1
elif q6 == "Yes and no, if I manage to get over my sugar addiction":
    score["Mediterranean"] += 1
    score["DASH"] += 1

q7 = st.multiselect("Do you want to include specific foods and drinks like some meat, only meat, only veggies, less veggies, Halaal-food, alcohol, sugar, and carbohydrates?", 
                     ["Meat", "Only Meat", "Only Veggies", "Less Veggies", "Halaal Friendly", "Alcohol", "Sugar", "Carbohydrates"])

if "Only Meat" in q7 and len(q7) > 1:
    st.error("If you select 'Only Meat', you may only select 'Halaal Friendly' and 'Alcohol'. Please adjust your selections.")
    return

if "Alcohol" in q7:
    score["Mediterranean"] += 1
    score["Sirtfood"] += 1
if "Only Meat" in q7:
    score["Keto"] += 1
    score["Carnivore"] += 1
if "Only Veggies" in q7:
    score["Flexitarian"] += 1
    score["Vegetarian"] += 1
if "Less Veggies" in q7:
    score["Paleo"] += 1
if "Sugar" in q7:
    score["CICO"] += 1
if "Carbohydrates" in q7:
    score["Mediterranean"] += 1
    score["DASH"] += 1

if st.button("Get My Recommended Diet!"):
    max_score = max(score.values())
    recommended_diets = [diet for diet, points in score.items() if points == max_score]
    diet_links = {
        "Keto": "[Learn more about Keto](https://yourwebsite.com/keto)",
        "Mediterranean": "[Learn more about Mediterranean](https://yourwebsite.com/mediterranean)",
        "Intermittent Fasting": "[Learn more about Intermittent Fasting](https://yourwebsite.com/if)",
        "WW": "[Learn more about WW](https://yourwebsite.com/ww)",
        "DASH": "[Learn more about DASH](https://yourwebsite.com/dash)",
        "Low-Carb": "[Learn more about Low-Carb](https://yourwebsite.com/low-carb)",
        "Atkins": "[Learn more about Atkins](https://yourwebsite.com/atkins)",
        "Volumetrics": "[Learn more about Volumetrics](https://yourwebsite.com/volumetrics)",
        "Fast800": "[Learn more about Fast800](https://yourwebsite.com/fast800)",
        "Flexitarian": "[Learn more about Flexitarian](https://yourwebsite.com/flexitarian)",
        "Sirtfood": "[Learn more about Sirtfood](https://yourwebsite.com/sirtfood)",
    }
    
    results = "\n".join([diet_links[diet] for diet in recommended_diets if diet in diet_links])
    st.success(f"Based on your answers, you might consider these diets: \n{results}")
```

if **name** == "**main**":
quiz()

