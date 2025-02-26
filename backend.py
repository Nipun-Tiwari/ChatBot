# backend.py
from fastapi import FastAPI
import pandas as pd

app = FastAPI()

# Load the Titanic dataset
df = pd.read_csv("titanic.csv")

@app.get("/query")
def query_data(question: str):
    # Process the question and generate a response
    if "percentage of passengers were male" in question.lower():
        male_percentage = (df['Sex'] == 'male').mean() * 100
        return {"response": f"{male_percentage:.2f}% of passengers were male."}
    
    elif "histogram of passenger ages" in question.lower():
        return {"response": "histogram", "data": df['Age'].dropna().tolist()}
    
    elif "average ticket fare" in question.lower():
        avg_fare = df['Fare'].mean()
        return {"response": f"The average ticket fare was ${avg_fare:.2f}."}
    
    elif "passengers embarked from each port" in question.lower():
        embark_counts = df['Embarked'].value_counts().to_dict()
        return {"response": f"Passengers embarked from: {embark_counts}."}
    
    else:
        return {"response": "Sorry, I couldn't understand your question."}