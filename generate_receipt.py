import qrcode, json, hashlib
from datetime import datetime

def generate_receipt(reference, amount):
    payload = {
        "reference": reference,
        "amount": amount,
        "timestamp": datetime.utcnow().isoformat(),
        "status": "CONFIRMED"
    }

    payload["hash"] = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode()
    ).hexdigest()

    qr = qrcode.make(json.dumps(payload))
    filename = f"{reference}.png"
    qr.save(filename)

    return filename, payload
