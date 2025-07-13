from fastapi import FastAPI, Request
from datetime import datetime
import json

app = FastAPI()

@app.post("/viber-webhook")
async def viber_delivery_webhook(request: Request):
    data = await request.json()
    log_data = {
        "timestamp": datetime.utcnow().isoformat(),
        "event": "delivery",
        "payload": data
    }
    with open("viber_delivery_log.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_data, ensure_ascii=False) + "\n")
    print("✅ Viber Webhook Received:", log_data)
    return {"status": "received"}
