from generate_receipt import generate_receipt
from verify_receipt import verify

file, data = generate_receipt("PHASE1-TEST", 50000)
result = verify(data)

print("Receipt Valid:", result)
