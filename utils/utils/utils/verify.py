import json
import hashlib

def verify_receipt(receipt):
    data_copy = receipt.copy()
    received_hash = data_copy.pop("hash")
    data_copy.pop("qr_path", None)

    recalculated = hashlib.sha256(
        json.dumps(data_copy, sort_keys=True).encode()
    ).hexdigest()

    if recalculated == received_hash:
        return True, "RECEIPT VERIFIED — SYSTEM CONFIRMED"
    return False, "RECEIPT INVALID — DATA TAMPERED"
