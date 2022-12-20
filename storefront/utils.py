import pymongo

from django.conf import settings
my_client = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&ssl=false&directConnection=true")

dbname = my_client['seller']

collection_name = dbname["storefront"]

medicine_1 = {
    "medicine_id": "RR000123456",
    "common_name" : "Paracetamol",
    "scientific_name" : "",
    "available" : "Y",
    "category": "fever"
}
medicine_2 = {
    "medicine_id": "RR000342522",
    "common_name" : "Metformin",
    "scientific_name" : "",
    "available" : "Y",
    "category" : "type 2 diabetes"
}
# Insert the documents
# collection_name.insert_many([medicine_1,medicine_2])
# Check the count


# # Read the documents
# med_details = collection_name.find({})
# # # Print on the terminal
# for r in med_details:
#     print(r["common_name"])
# # # Update one document
# update_data = collection_name.update_one({'medicine_id':'RR000123456'}, {'$set':{'common_name':'Paracetamol 500'}})

# # Delete one document
# delete_data = collection_name.delete_one({'medicine_id':'RR000123456'})


query={"medicine_id":{"$eq":'RR000342522'}}
print(collection_name.find_one(query))


query={"medicine_id":{"$eq":'RR000342522'}}

present_data=collection_name.find_one(query)
new_data={'$set':{"Name":'Ramesh'}}
collection_name.update_one(present_data,new_data)



