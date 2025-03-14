from config import mongo

def get_user_collection():
    return mongo.db.users

def get_room_collection():
    return mongo.db.rooms

def get_tenant_collection():
    return mongo.db.tenants

def get_invoice_collection():
    return mongo.db.invoices

