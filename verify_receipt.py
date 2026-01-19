import json, hashlib

def verify(payload):
    hash_value = payload.pop("hash")
    recalculated = hashlib.sha256(
        json.dumps(payload, sort_keys=True).encode()
    ).hexdigest()
    return hash_value == recalculated
