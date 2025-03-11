import streamlit as st

def quiz():
    st.title("Which Diet is Right for You?")
    
    score = {"Keto": 0, "Mediterranean": 0, "Intermittent Fasting": 0, "WW": 0, "DASH": 0, "Low-Carb": 0, "Atkins": 0, "Volumetrics": 0,
    "Fast800": 0, "TLC": 0, "Mayo Clinic": 0, "Flexitarian": 0, "Sirtfood": 0, "South Beach": 0, "HMR": 0, "Dukan": 0, "PSMF": 0, "ADF": 0, "Military": 0, "CICO": 0}

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
                  ("Fast results (1-2 kg per week / 2+ pounds per week)", "Steady long-term weight loss (0.5-1 kg per week / 1-2 pounds per week)", "I need rapid weight loss for medical reasons", "I want to focus on muscle retention while losing weight"))
    if q2 == "Fast results (1-2 kg per week / 2+ pounds per week)":
        score["Keto"] += 1
        score["Military"] += 1
        score["Fast800"] += 1
    elif q2 == "I need rapid weight loss for medical reasons":
        score["HMR"] += 1
        score["PSMF"] += 1
        score["ADF"] += 1
    elif q2 == "I want to focus on muscle retention while losing weight":
        score["Dukan"] += 1
        score["PSMF"] += 1
        score["Military"] += 1
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

    q5 = st.radio("Do social activities force you to take some alcoholic beverages at times?", 
                  ("Yes", "No"))
    if q5 == "Yes":
        score["Mediterranean"] += 1
        score["Sirtfood"] += 1

    q6 = st.radio("Do you get sugar cravings?", 
                  ("Yes, I struggle to go without sugar", "No, I manage to go without sugar", "Yes and no, if I manage to get over my sugar addiction"))
    if q6 == "Yes, I struggle to go without sugar":
        score["CICO"] += 1
    elif q6 == "Yes and no, if I manage to get over my sugar addiction":
        score["Mediterranean"] += 1
        score["DASH"] += 1
    
    q7 = st.radio("Would you like to follow a diet that focuses more on when you eat rather than what you eat?", 
                  ("Yes", "No"))
    if q7 == "Yes":
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
        }
        
        with st.expander("📌 **Your Recommended Diet(s):** Click to view details!"):
            for diet in recommended_diets:
                if diet in diet_links:
                    st.markdown(f"🔗 {diet}: {diet_links[diet]}")

if __name__ == "__main__":
    quiz()

