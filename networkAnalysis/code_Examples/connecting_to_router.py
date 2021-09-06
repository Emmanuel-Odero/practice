from netmiko import ConnectHandler

device = ConnectHandler(device_type='HG8346M', ip='192.168.255.249',
username='cisco', password='cisco')
output = device.send_command("show version")
print (output)
device.disconnect()