from fastapi import FastAPI
from utils.data_collector import collect_all_data

app = FastAPI()

@app.post("/gill/competitor-reaction")
async def react_to_competitor():
    # Step 1: Collect data
    data = collect_all_data()

    # Step 2: Process data (e.g., send to GPT for reasoning)
    # (We'll implement this in the next phase)

    return {"collected_data": data}
