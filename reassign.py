from pymongo import MongoClient
from bson.objectid import ObjectId

def reassign_proposals():
    client = MongoClient("mongodb://localhost:27017/proposeai_db")
    db = client['proposeai_db']
    
    # Target user (Praveen)
    # I saw this ID in my previous grep/find
    target_user_id = "69b970b0723af80b6af7672"
    
    # Let's find any user that is NOT anonymous just in case
    # But usually the first one created is the one.
    
    print(f"Assigning all 'anonymous' proposals to {target_user_id}...")
    
    result = db.proposals.update_many(
        {"user_id": "anonymous"},
        {"$set": {"user_id": target_user_id}}
    )
    
    print(f"Reassigned {result.modified_count} proposals.")

if __name__ == "__main__":
    reassign_proposals()
