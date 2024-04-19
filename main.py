import obd
import firebase_admin
import json
import serial
from firebase_admin import credentials
from firebase_admin import db
import time


cred = credentials.Certificate("./certificate.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://cartestingmodule-default-rtdb.firebaseio.com/"
})

ser = serial.Serial("/dev/ttyUSB0", 9600)
ref = db.reference("/collectedData")


while True:
    json_serial = json.loads(ser.readline())
    ref.push(json_serial)


connection = obd.Async(fast=False)

connection.watch(obd.commands.RPM, )
connection.watch(obd.commands.SPEED, )

connection.close()