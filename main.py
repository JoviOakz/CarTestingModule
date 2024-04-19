from firebase_admin import credentials
from firebase_admin import db
import firebase_admin
import time
import obd

connection = obd.Async(fast=False)

cred = credentials.Certificate("./certificate.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://cartestingmodule-default-rtdb.firebaseio.com/"
})

def firebase_push(data_name):
    def callback(data): 
        ref = db.reference(f"/{data_name}/{time.time()}")
        ref.set(data)
    return callback


connection.watch(obd.commands.RPM, firebase_push("rpm"))
connection.watch(obd.commands.SPEED, firebase_push("speed"))

connection.close()