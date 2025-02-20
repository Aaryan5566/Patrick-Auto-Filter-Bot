import json
import pymongo
from info import PRIMARY_DB_URI, PRIMARY_DB_NAME, SECONDARY_DB_URI, SECONDARY_DB_NAME
from pyrogram import enums
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

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

# Function to add a global filter
async def add_gfilter(gfilters, text, reply_text, btn, file, alert):
    mycol = mydb[str(gfilters)]
    data = {
        'text': str(text),
        'reply': str(reply_text),
        'btn': str(btn),
        'file': str(file),
        'alert': str(alert)
    }
    try:
        mycol.update_one({'text': str(text)}, {"$set": data}, upsert=True)
    except:
        logger.exception('Some error occurred!', exc_info=True)

# Function to find a global filter
async def find_gfilter(gfilters, name):
    mycol = mydb[str(gfilters)]
    query = mycol.find({"text": name})

    try:
        for file in query:
            reply_text = file['reply']
            btn = file['btn']
            fileid = file['file']
            try:
                alert = file['alert']
            except:
                alert = None
        return reply_text, btn, alert, fileid
    except:
        return None, None, None, None

# Function to get all global filters
async def get_gfilters(gfilters):
    mycol = mydb[str(gfilters)]
    texts = []
    query = mycol.find()
    try:
        for file in query:
            text = file['text']
            texts.append(text)
    except:
        pass
    return texts

# Function to delete a specific global filter
async def delete_gfilter(message, text, gfilters):
    mycol = mydb[str(gfilters)]
    myquery = {'text': text}
    query = mycol.count_documents(myquery)

    if query == 1:
        mycol.delete_one(myquery)
        await message.reply_text(
            f"'`{text}`' deleted. I'll not respond to that gfilter anymore.",
            quote=True,
            parse_mode=enums.ParseMode.MARKDOWN
        )
    else:
        await message.reply_text("Couldn't find that gfilter!", quote=True)

# Function to delete all global filters
async def del_allg(message, gfilters):
    if str(gfilters) not in mydb.list_collection_names():
        await message.edit_text("Nothing to remove!")
        return

    mycol = mydb[str(gfilters)]
    try:
        mycol.drop()
        await message.edit_text(f"All gfilters have been removed!")
    except:
        await message.edit_text("Couldn't remove all gfilters!")
        return

# Function to count global filters
async def count_gfilters(gfilters):
    mycol = mydb[str(gfilters)]
    count = mycol.count_documents({})
    return False if count == 0 else count

# Function to get global filter stats
async def gfilter_stats():
    collections = mydb.list_collection_names()

    if "CONNECTION" in collections:
        collections.remove("CONNECTION")

    totalcount = 0
    for collection in collections:
        mycol = mydb[collection]
        count = mycol.count_documents({})
        totalcount += count

    totalcollections = len(collections)

    return totalcollections, totalcount
