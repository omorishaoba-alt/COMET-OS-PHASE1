import qrcode
import json
import hashlib
from datetime import datetime
import os

RECEIPT_DIR = "static/receipts"
os.makedirs(RECEIPT_DIR, exist_ok=True)

def generate_receipt(name, bvn, nin, amount):
    data = {
        "name": name,
        "bvn": bvn,
        "nin": nin,
        "amount": amount,
        "timestamp": datetime.utcnow().isoformat(),
        "system": "COMET OS – Phase I"
    }

    payload = json.dumps(data, sort_keys=True)
    receipt_hash = hashlib.sha256(payload.encode()).hexdigest()
    data["hash"] = receipt_hash

    qr = qrcode.make(json.dumps(data))
    filename = f"{name.replace(' ', '_')}_{receipt_hash[:8]}.png"
    filepath = os.path.join(RECEIPT_DIR, filename)
    qr.save(filepath)

    data["qr_path"] = filepath
    return data
