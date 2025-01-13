import json
from datetime import datetime
from faker import Faker
import random

# Step 1: Simulate API data with schema variations
fake = Faker()
def generate_fake_record(api_source):
    record = {
        "transaction_id": fake.uuid4(),
        "amount": round(random.uniform(10.0, 1000.0), 2),
        "currency": random.choice(["USD", "EUR", "EGP"]),
        "timestamp": fake.date_time_this_year().isoformat(),
        "region": random.choice(["North America", "Europe", "Middle East"]),
    }
    # Simulate schema differences
    if api_source == "API_1":
        record["user_id"] = fake.uuid4()
    elif api_source == "API_2":
        record["customer_id"] = fake.uuid4()
        record["amount"] = str(record["amount"])  # as a string
    return record

# Generate sample data
api_sources = ["API_1", "API_2"]
raw_data = [generate_fake_record(random.choice(api_sources)) for _ in range(5)]
print("Raw Data:", json.dumps(raw_data, indent=2))

# Step 2: Transform data
def transform_record(record):
    # Normalize schema
    standardized_record = {
        "transaction_id": record.get("transaction_id"),
        "amount": float(record["amount"]) if isinstance(record["amount"], str) else record["amount"],
        "currency": record.get("currency", "USD"),
        "timestamp": datetime.fromisoformat(record["timestamp"]).strftime("%Y-%m-%d %H:%M:%S"),
        "region": record.get("region", "Unknown"),
        "user_id": record.get("user_id") or record.get("customer_id")
    }
    # Handle missing values
    if not standardized_record["user_id"]:
        standardized_record["user_id"] = "Unknown"
    return standardized_record

# Process data
transformed_data = [transform_record(record) for record in raw_data]
print("\nTransformed Data:", json.dumps(transformed_data, indent=2))
