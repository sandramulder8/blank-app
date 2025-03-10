
import streamlit as st

def quiz():
    st.title("Which Diet is Right for You?")
    
    score = {"structured": 0, "flexible": 0, "fast": 0, "steady": 0, "low_carb": 0, "balanced": 0, "affordable": 0, "easy": 0, "specific": 0, "alcohol": 0, "only_meat": 0, "only_veggies": 0, "less_veggies": 0}
    
    q1 = st.radio("Do you prefer structured meal plans or flexibility?", 
                  ("Structured", "Flexible"))
    if q1 == "Structured":
        score["structured"] += 1
    else:
        score["flexible"] += 1
    
    q2 = st.radio("How fast do you want to lose weight?", 
                  ("Fast results (1-2 kg per week / 2+ pounds per week)", "Steady long-term weight loss (0.5-1 kg per week / 1-2 pounds per week)"))
    if q2 == "Fast results (1-2 kg per week / 2+ pounds per week)":
        score["fast"] += 1
    else:
        score["steady"] += 1
    
    q3 = st.radio("Do you struggle with carb cravings?", 
                  ("Yes, I need a low-carb approach", "No, I prefer balanced meals"))
    if q3 == "Yes, I need a low-carb approach":
        score["low_carb"] += 1
    else:
        score["balanced"] += 1
    
    q4 = st.radio("Do you want a cheaper affordable diet or does it not matter?", 
                  ("Affordable", "Does not matter"))
    if q4 == "Affordable":
        score["affordable"] += 1
    
    q5 = st.radio("Do you want an easy-to-follow diet or does it matter?", 
                  ("Easy-to-follow", "Does not matter"))
    if q5 == "Easy-to-follow":
        score["easy"] += 1
    
    q6 = st.multiselect("Do you want to include specific foods and drinks like some meat, only meat, only veggies, less veggies, Halaal-food, alcohol, sugar, and carbohydrates?", 
                         ["Meat", "Only Meat", "Only Veggies", "Less Veggies", "Halaal Friendly", "Alcohol", "Sugar", "Carbohydrates"])
    
    if "Only Meat" in q6 and len(q6) > 1:
        st.error("If you select 'Only Meat', you may only select 'Halaal Friendly' and 'Alcohol'. Please adjust your selections.")
        return
    
    if "Alcohol" in q6:
        score["alcohol"] += 1
    if "Only Meat" in q6:
        score["only_meat"] += 1
    if "Only Veggies" in q6:
        score["only_veggies"] += 1
    if "Less Veggies" in q6:
        score["less_veggies"] += 1
    if len(q6) > 0:
        score["specific"] += 1
    
    if st.button("Get My Recommended Diet!"):
        max_score = max(score, key=score.get)
        diet_links = {
            "structured": "[Learn more about Keto, Atkins, DASH, or Whole30](https://yourwebsite.com/structured-diets)",
            "flexible": "[Learn more about Mediterranean, Flexitarian, Low-Carb, or Pescatarian](https://yourwebsite.com/flexible-diets)",
            "fast": "[Learn more about Keto, Military, HMR, Dukan, or Intermittent Fasting](https://yourwebsite.com/fast-weight-loss)",
            "steady": "[Learn more about Mediterranean, DASH, Volumetrics, Nordic, or Flexitarian](https://yourwebsite.com/steady-weight-loss)",
            "low_carb": "[Learn more about Keto, Atkins, Low-Carb, Dukan, or South Beach](https://yourwebsite.com/low-carb-diets)",
            "balanced": "[Learn more about Mediterranean, DASH, MIND, High-Fiber, or Pescatarian](https://yourwebsite.com/balanced-diets)",
            "affordable": "[Learn more about Flexitarian, High-Fiber, or Low-Carb Diets](https://yourwebsite.com/affordable-diets)",
            "easy": "[Learn more about Mediterranean, DASH, or Pescatarian](https://yourwebsite.com/easy-diets)",
            "specific": "[Learn more about Vegan, Paleo, or Whole30](https://yourwebsite.com/specific-diets)",
            "alcohol": "[Learn more about Mediterranean, Sirtfood, Flexitarian, or DASH Diet](https://yourwebsite.com/alcohol-friendly-diets)",
            "only_meat": "[Learn more about Carnivore or Keto Diet](https://yourwebsite.com/only-meat-diets)",
            "only_veggies": "[Learn more about Vegan, Vegetarian, Mediterranean, or Sirtfood Diet](https://yourwebsite.com/only-veggies-diets)",
            "less_veggies": "[Learn more about Paleo, Keto, or Carnivore Diet](https://yourwebsite.com/less-veggies-diets)"
        }
        
        if max_score in diet_links:
            st.success(f"{diet_links[max_score]}")

if __name__ == "__main__":
    quiz()
