def calculate_registration(name, category, participants):

    if category == "Student":
        fee = 200

    elif category == "Faculty":
        fee = 500

    elif category == "Industry":
        fee = 1000

    else:
        return "Invalid registration category"

    total_amount = fee * participants
    registration = {
        "name": name,
        "category": category,
        "participants": participants,
        "fee": fee,
        "total_amount": total_amount
    }

    return registration
# Predefined participant details
result = calculate_registration(
    "Apeksha",
    "Student",
    3
)
print("===== TECHNICAL EVENT REGISTRATION =====")
print("Participant Name:", result["name"])
print("Registration Category:", result["category"])
print("Number of Participants:", result["participants"])
print("Fee per Participant: Rs.", result["fee"])
print("Total Registration Amount: Rs.", result["total_amount"])
