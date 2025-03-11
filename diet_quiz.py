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
                  ("Structured", "Flexible", "Somewhat Structured"))
    if q1 == "Structured":
        score["keto"] += 1
        score["atkins"] += 1
        score["dukan"] += 1
        score["hmr"] += 1
        score["fast800"] += 1
    elif q1 == "Flexible":
        score["mediterranean"] += 1
        score["intermittent_fasting"] += 1
        score["flexitarian"] += 1
        score["sirtfood"] += 1
    else:
        score["ww"] += 1
        score["dash"] += 1
        score["cico"] += 1

    q2 = st.radio("How fast do you want to lose weight?", 
                  ("Fast results (1-2 kg per week)", "Steady weight loss (0.5-1 kg per week)", "Does not matter"))
    if q2 == "Fast results (1-2 kg per week)":
        score["fast800"] += 1
        score["keto"] += 1
        score["military"] += 1
        score["psmf"] += 1
        score["adf"] += 1
    elif q2 == "Steady weight loss (0.5-1 kg per week)":
        score["mediterranean"] += 1
        score["dash"] += 1
        score["volumetrics"] += 1
        score["ww"] += 1

    q3 = st.radio("Do you struggle with carb cravings?", 
                  ("Yes, I need a low-carb approach", "No, I prefer balanced meals"))
    if q3 == "Yes, I need a low-carb approach":
        score["keto"] += 1
        score["atkins"] += 1
        score["dukan"] += 1
        score["south_beach"] += 1
        score["psmf"] += 1
    else:
        score["mediterranean"] += 1
        score["dash"] += 1
        score["ww"] += 1

    q4 = st.radio("Do you want an affordable diet?", 
                  ("Yes", "No, cost does not matter"))
    if q4 == "Yes":
        score["cico"] += 1
        score["flexitarian"] += 1
        score["low_carb"] += 1
        score["volumetrics"] += 1

    q5 = st.radio("Do you prefer an easy-to-follow diet?", 
                  ("Yes", "No, I can handle complexity"))
    if q5 == "Yes":
        score["ww"] += 1
        score["dash"] += 1
        score["mediterranean"] += 1
    else:
        score["keto"] += 1
        score["psmf"] += 1
        score["dukan"] += 1

    q6 = st.multiselect("Do you want to include specific foods or restrictions?", 
                         ["Meat", "Only Meat", "Only Veggies", "Less Veggies", "Halaal Friendly", "Alcohol", "Sugar", "Carbohydrates"])
    
    if "Only Meat" in q6 and len(q6) > 1:
        st.error("If you select 'Only Meat', you may only select 'Halaal Friendly' and 'Alcohol'. Please adjust your selections.")
        return
    
    if "Alcohol" in q6:
        score["mediterranean"] += 1
        score["sirtfood"] += 1
        score["flexitarian"] += 1
    if "Only Meat" in q6:
        score["keto"] += 1
        score["carnivore"] = 1
    if "Only Veggies" in q6:
        score["vegan"] = 1
        score["vegetarian"] = 1
    if "Less Veggies" in q6:
        score["paleo"] += 1
        score["keto"] += 1

    if st.button("Get My Recommended Diet!"):
        max_score = max(score, key=score.get)
        diet_links = {
            "mediterranean": "[Learn more about the Mediterranean Diet](https://yourwebsite.com/mediterranean-diet)",
            "intermittent_fasting": "[Learn more about Intermittent Fasting](https://yourwebsite.com/intermittent-fasting)",
            "keto": "[Learn more about the Keto Diet](https://yourwebsite.com/keto-diet)",
            "ww": "[Learn more about Weight Watchers](https://yourwebsite.com/ww-diet)",
            "dash": "[Learn more about the DASH Diet](https://yourwebsite.com/dash-diet)",
            "low_carb": "[Learn more about Low-Carb Diet](https://yourwebsite.com/low-carb-diet)",
            "atkins": "[Learn more about the Atkins Diet](https://yourwebsite.com/atkins-diet)",
            "volumetrics": "[Learn more about the Volumetrics Diet](https://yourwebsite.com/volumetrics-diet)",
            "fast800": "[Learn more about the Fast800 Diet](https://yourwebsite.com/fast800-diet)",
            "tlc": "[Learn more about the TLC Diet](https://yourwebsite.com/tlc-diet)",
            "mayo": "[Learn more about the Mayo Clinic Diet](https://yourwebsite.com/mayo-clinic-diet)",
            "flexitarian": "[Learn more about the Flexitarian Diet](https://yourwebsite.com/flexitarian-diet)",
            "sirtfood": "[Learn more about the Sirtfood Diet](https://yourwebsite.com/sirtfood-diet)",
            "south_beach": "[Learn more about the South Beach Diet](https://yourwebsite.com/south-beach-diet)",
            "hmr": "[Learn more about the HMR Diet](https://yourwebsite.com/hmr-diet)",
            "dukan": "[Learn more about the Dukan Diet](https://yourwebsite.com/dukan-diet)",
            "psmf": "[Learn more about the Protein-Sparing Modified Fast](https://yourwebsite.com/psmf-diet)",
            "adf": "[Learn more about Alternate-Day Fasting](https://yourwebsite.com/adf-diet)",
            "military": "[Learn more about the Military Diet](https://yourwebsite.com/military-diet)",
            "cico": "[Learn more about the CICO Diet](https://yourwebsite.com/cico-diet)"
        }
        
        if max_score in diet_links:
            st.success(f"{diet_links[max_score]}")

if __name__ == "__main__":
    quiz()
