from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient
import os


class Database():
    
    def __init__(self) -> None:
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.ats_database = self.client["ats"]
        self.ats_collection = self.ats_database["ats-payment"]
        
        
    def add_proof(self, name, email, amount, upi_id, transaction_id):
        
        check = self.ats_collection.find_one({"email": email})
        print(check)
        if check is not None and check["_id"]:
            if check["verify"] == True:
                return {
                    "error": f'Already donated {check["name"]} ! Thanks for donating',
                    "unique_code": None
                }
            if check["verify"] == False:
                return {
                    "error": f'Already donated {check["name"]} ! It is not confirm yet',
                    "unique_code": None
                }
        
        if name and email and amount and upi_id:
            unique_code = self.ats_collection.insert_one({"name": name, "email": email, "amount": amount, "upi_id": upi_id, "transaction_id": transaction_id,"verify": False})
            
            return {
                "error": None,
                "unique_code": unique_code.inserted_id
            }
        else:
            return {
                "error": "Fill all the details",
                "uinqueCode": None
            }

