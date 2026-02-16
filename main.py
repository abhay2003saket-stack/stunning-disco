from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

class Prompt(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI App Running 🚀"}

@app.post("/chat")
def chat(prompt: Prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt.text}]
    )
    return {"response": response.choices[0].message.content}
