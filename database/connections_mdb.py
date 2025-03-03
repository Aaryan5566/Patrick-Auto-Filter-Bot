import json
import pymongo
from info import PRIMARY_DB_URI, PRIMARY_DB_NAME, SECONDARY_DB_URI, SECONDARY_DB_NAME

# Function to get active database from config.json
def get_active_db():
    with open("config.json", "r") as f:
        config = json.load(f)
        return config["active_db"]

# Select the active database
active_db_name = get_active_db()
if active_db_name == "PrimaryDB":
    myclient = pymongo.MongoClient(PRIMARY_DB_URI)
    mydb = myclient[PRIMARY_DB_NAME]
else:
    myclient = pymongo.MongoClient(SECONDARY_DB_URI)
    mydb = myclient[SECONDARY_DB_NAME]

mycol = mydb['CONNECTION']  # Collection to store user-group connections

# Add a new connection between a user and a group
async def add_connection(group_id, user_id):
    query = mycol.find_one({"_id": user_id}, {"_id": 0, "active_group": 0})
    if query is not None:
        group_ids = [x["group_id"] for x in query["group_details"]]
        if group_id in group_ids:
            return False

    group_details = {"group_id": group_id}

    data = {
        '_id': user_id,
        'group_details': [group_details],
        'active_group': group_id,
    }

    if mycol.count_documents({"_id": user_id}) == 0:
        try:
            mycol.insert_one(data)
            return True
        except:
            print('Some error occurred!')
    else:
        try:
            mycol.update_one(
                {'_id': user_id},
                {
                    "$push": {"group_details": group_details},
                    "$set": {"active_group": group_id}
                }
            )
            return True
        except:
            print('Some error occurred!')

# Get the active connection for a user
async def active_connection(user_id):
    query = mycol.find_one({"_id": user_id}, {"_id": 0, "group_details": 0})
    if not query:
        return None
    return int(query['active_group']) if query['active_group'] is not None else None

# Get all groups connected to a user
async def all_connections(user_id):
    query = mycol.find_one({"_id": user_id}, {"_id": 0, "active_group": 0})
    return [x["group_id"] for x in query["group_details"]] if query else None

# Check if a user is active in a specific group
async def if_active(user_id, group_id):
    query = mycol.find_one({"_id": user_id}, {"_id": 0, "group_details": 0})
    return query is not None and query['active_group'] == group_id

# Make a specific group active for a user
async def make_active(user_id, group_id):
    update = mycol.update_one({'_id': user_id}, {"$set": {"active_group": group_id}})
    return update.modified_count != 0

# Make a user inactive
async def make_inactive(user_id):
    update = mycol.update_one({'_id': user_id}, {"$set": {"active_group": None}})
    return update.modified_count != 0

# Delete a connection between a user and a group
async def delete_connection(user_id, group_id):
    try:
        update = mycol.update_one(
            {"_id": user_id},
            {"$pull": {"group_details": {"group_id": group_id}}}
        )
        if update.modified_count == 0:
            return False

        query = mycol.find_one({"_id": user_id}, {"_id": 0})
        if len(query["group_details"]) >= 1:
            if query['active_group'] == group_id:
                prvs_group_id = query["group_details"][-1]["group_id"]
                mycol.update_one(
                    {'_id': user_id},
                    {"$set": {"active_group": prvs_group_id}}
                )
        else:
            mycol.update_one(
                {'_id': user_id},
                {"$set": {"active_group": None}}
            )
        return True
    except Exception as e:
        print(f'Some error occurred! {e}')
        return False
