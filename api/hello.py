# api/bot.py
import json
from http.server import BaseHTTPRequestHandler

def handler(request):
    # JSON payload from Telegram
    data = request.json()

    # Example: print to logs
    print("Received Telegram update:", data)

    # Respond with OK
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Webhook received!"})
    }
