from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()


class Product(BaseModel):
    nazwa: str
    opis: str


@app.post("/generuj")
def stworz_reklame(dane: Product):
    polecenie = f"Jesteś ekspertem marketingu. Napisz po polsku profesjonalną i kreatywną reklamę dla: {dane.nazwa}. Opis: {dane.opis}. Podziel tekst na nagłówek, treść i wezwanie do działania."

    wyniki = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3:latest",
            "prompt": polecenie,
            "stream": False
        }
    )

    odpowiedz_json = wyniki.json()
    tekst_reklamy = odpowiedz_json["response"]

    # TO JEST NAJWAŻNIEJSZA LINIA:
    return {"reklama": tekst_reklamy}