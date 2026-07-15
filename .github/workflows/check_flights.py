import os
import requests

TARGET_PRICE = 180

ORIGIN = "PHX"
DESTINATION = "SEA"


print("Checking flights...")

# Placeholder for flight API connection
# This will connect to your flight data provider

price = 999

if price <= TARGET_PRICE:
    print(
        f"""
        ALERT!

        PHX to SEA is ${price}

        Under your target of ${TARGET_PRICE}
        """
    )

else:
    print(
        f"No deal yet. Current price: ${price}"
    )
