import obd



connection = obd.Async(fast=False)

connection.watch(obd.commands.RPM, )
connection.watch(obd.commands.SPEED, )

connection.close()