from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def get_email():
    return "22f2001382@ds.study.iitm.ac.in"