import couchdb3

db = couchdb3.Database(
    "asset",
    url="http://localhost:15984",
    user="admin",
    password="password",
)

print("db check:", db.check())

res = db.find(
    {"siteid": {"$exists": True}},
    fields=["siteid"],
    limit=100000,
)

print(res)