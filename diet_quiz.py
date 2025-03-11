import streamlit as st

def quiz():
    st.title("Which Diet is Right for You?")

    score = {
        "Keto": 0, "Mediterranean": 0, "Intermittent Fasting": 0, "WW": 0, "DASH": 0,
        "Low-Carb": 0, "Atkins": 0, "Volumetrics": 0, "Fast800": 0, "TLC": 0,
        "Mayo Clinic": 0, "Flexitarian": 0, "Sirtfood": 0, "South Beach": 0,
        "HMR": 0, "Dukan": 0, "PSMF": 0, "ADF": 0, "Military": 0, "CICO": 0
    }

    q1 = st.radio("1. Do you prefer structured meal plans or flexibility?", 
                  ("Structured", "Flexible"))
    if q1 == "Structured":
        score["Keto"] += 1
        score["WW"] += 1
        score["Fast800"] += 1
        score["Intermittent Fasting"] += 1
    else:
        score["Mediterranean"] += 1
        score["Flexitarian"] += 1

    q2 = st.radio("2. How fast do you want to lose weight?", 
                  ("Fast results (1-2 kg per week / 2+ pounds per week)", 
                   "Steady long-term weight loss (0.5-1 kg per week / 1-2 pounds per week)"))
    if q2 == "Fast results (1-2 kg per week / 2+ pounds per week)":
        score["Keto"] += 1
        score["Military"] += 1
        score["Fast800"] += 1
        score["Intermittent Fasting"] += 1
    else:
        score["Mediterranean"] += 1
        score["DASH"] += 1

    q3 = st.radio("3. Do you struggle with carb cravings?", 
                  ("Yes, I need a low-carb approach", "No, I prefer balanced meals"))
    if q3 == "Yes, I need a low-carb approach":
        score["Keto"] += 1
        score["Atkins"] += 1
        score["Low-Carb"] += 1
        score["Intermittent Fasting"] += 1
    else:
        score["Mediterranean"] += 1
        score["Volumetrics"] += 1

    q4 = st.radio("4. Do you want a cheaper diet or does it not matter?", 
                  ("Cheaper", "Does not matter"))
    if q4 == "Cheaper":
        score["CICO"] += 1
        score["WW"] += 1
        score["Intermittent Fasting"] += 1
else:
    score["Keto"] += 1
    score["Atkins"] += 1
    score["Dukan"] += 1

    q5 = st.radio("5. Do you want an easy-to-follow diet or does it matter?", 
                  ("Easy-to-follow", "Does not matter"))
    if q5 == "Easy-to-follow":
        score["Mediterranean"] += 1
        score["WW"] += 1
        score["Intermittent Fasting"] += 1

    q6 = st.radio("6. Do you get sugar cravings?", 
                  ("Yes, I struggle to go without sugar", 
                   "No, I manage to go without sugar", 
                   "Yes and no, if I manage to get over my sugar addiction"))
    if q6 == "Yes, I struggle to go without sugar":
        score["CICO"] += 1
        score["Mediterranean"] += 1
        score["Sirtfood"] += 1
        score["Flexitarian"] += 1
        score["WW"] += 1
        score["Volumetrics"] += 1
        score["Intermittent Fasting"] += 1
                
    elif q6 == "Yes and no, if I manage to get over my sugar addiction":
        score["Mediterranean"] += 1
        score["DASH"] += 1
        score["Intermittent Fasting"] += 1
        score["Atkins"] += 1
        score["Dukan"] += 1

    q7 = st.multiselect("7. Do you want to include specific foods and drinks like some meat, some fish, lots of veggies, less veggies, Halaal-food, alcohol, sugar, and carbohydrates?", 
                         ["Meat", "Only Fish", "Lots Of Veggies", "Less Veggies", "Halaal Friendly", 
                          "Alcohol", "Sugar", "Carbohydrates"])

    if "Only Fish" in q7 and len(q7) > 1:
        st.error("If you select 'Only Fish', you may only select 'Halaal Friendly', 'Alcohol', 'Sugar', 'Carbohydrates', and 'Less Veggies'. Please adjust your selections.")
        return

    if "Alcohol" in q7:
        score["Mediterranean"] += 1
        score["Sirtfood"] += 1
        score["WW"] += 1
        score["DASH"] += 1
        score["Flexitarian"] += 1
        score["CICO"] += 1
        score["Intermittent Fasting"] += 1
    if "Only Fish" in q7:
        score["DASH"] += 1
        score["Mediterranean"] += 1
        score["Volumetrics"] += 1
        score["Flexitarian"] += 1
        score["Intermittent Fasting"] += 1
    if "Lots Of Veggies" in q7:
        score["Flexitarian"] += 1
        score["Vegetarian"] += 1
        score["Intermittent Fasting"] += 1
    if "Less Veggies" in q7:
        score["Paleo"] += 1
        score["Keto"] += 1
        score["Atkins"] += 1
        score["South Beach"] += 1
        score["Dukan"] += 1
        score["PSMF"] += 1
        score["Military"] += 1
        score["Intermittent Fasting"] += 1
    if "Sugar" in q7:
        score["CICO"] += 1
        score["Mediterranean"] += 1
        score["Sirtfood"] += 1
        score["Flexitarian"] += 1
        score["WW"] += 1
        score["Volumetrics"] += 1
        score["Intermittent Fasting"] += 1
    if "Carbohydrates" in q7:
        score["Mediterranean"] += 1
        score["DASH"] += 1
        score["CICO"] += 1
        score["Mayo Clinic"] += 1
        score["Sirtfood"] += 1
        score["Flexitarian"] += 1
        score["WW"] += 1
        score["Volumetrics"] += 1
        score["South Beach"] += 1
        score["Intermittent Fasting"] += 1

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
            "TLC": "[Learn more about TLC](https://yourwebsite.com/TLC)",
            "Mayo Clinic": "[Learn more about Mayo Clinic](https://yourwebsite.com/Mayo Clinic)",
            "South Beach": "[Learn more about South Beach](https://yourwebsite.com/South Beach)",
            "HMR": "[Learn more about HMR](https://yourwebsite.com/HMR)",
            "Dukan": "[Learn more about Dukan](https://yourwebsite.com/Dukan)",
            "PSMF": "[Learn more about PSMF](https://yourwebsite.com/PSMF)",
            "ADF": "[Learn more about ADF](https://yourwebsite.com/ADF)", 
            "Military": "[Learn more about Military](https://yourwebsite.com/Military)",
            "CICO": "[Learn more about CICO](https://yourwebsite.com/CICO)"
    }
               
        results = "\n".join([diet_links[diet] for diet in recommended_diets if diet in diet_links])
        st.success(f"Based on your answers, you might consider these diets: \n{results}")

if __name__ == "__main__":
    quiz()
