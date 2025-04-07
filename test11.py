from fastapi import FastAPI

app=FastAPI()


@app.get("/")
def data():
    return {"name":"pratyaksh","info":"qwerpokihgfc vbnjytgfcvb"}