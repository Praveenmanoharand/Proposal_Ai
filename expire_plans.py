from pymongo import MongoClient  # Resolve IDE import error
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = "mongodb://localhost:27017/proposeai_db"
DB_NAME = "proposeai_db"

def expire_plans():
    """Background task to expire subscriptions that have passed their expiry date."""
    print(f"[{datetime.now()}] Starting plan expiration check...")
    
    try:
        client = MongoClient(MONGO_URI)
        db = client[DB_NAME]
        users_collection = db['users']
        
        now = datetime.utcnow()
        now_iso = now.isoformat() + "Z"
        
        # Find active paid plans that have expired
        query = {
            "plan": {"$ne": "free"},
            "subscription.status": "active",
            "subscription.expiry_date": {"$lt": now_iso}
        }
        
        expired_users = list(users_collection.find(query))
        
        if not expired_users:
            print("No expired plans found.")
            return

        print(f"Found {len(expired_users)} expired plans. Reverting to free...")
        
        for user in expired_users:
            email = user.get('email', 'Unknown')
            users_collection.update_one(
                {"_id": user["_id"]},
                {
                    "$set": {
                        "plan": "free",
                        "subscription.status": "expired",
                        "subscription.last_updated": now_iso
                    }
                }
            )
            print(f" Reverted user: {email}")

        print("Expiration check complete.")
        
    except Exception as e:
        print(f"Error during expiration check: {e}")

if __name__ == "__main__":
    expire_plans()
