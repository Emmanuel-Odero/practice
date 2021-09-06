from netmiko import ConnectHandler

#take the router inputs details
print("Inpute router details\n")
dt = input("device_type :")
ip_add = input("router-IP :")
usname = input("username :")
pword = input("password :")

#connect to router and print the version number
device = ConnectHandler(device_type="", ip="", username="", password="")
output = device.send_command("show version")
print(output)
device.disconnect()