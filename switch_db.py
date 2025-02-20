import json

def switch_database():
    with open("config.json", "r") as f:
        config = json.load(f)

    new_db = "SecondaryDB" if config["active_db"] == "PrimaryDB" else "PrimaryDB"
    config["active_db"] = new_db

    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)

    print(f"✅ Database switched to {new_db}")

switch_database()
