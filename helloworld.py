# APENAS UM EXEMPLO DE CÓDIGO PARA TESTAR O AMBIENTE DE DESENVOLVIMENTO
import os
from netmiko import ConnectHandler

#loads the environment variables from the .env file


#Retrieve the password from the environment variable. 
secret_password = os.environ.get("Costa_Lab_password")


router_cisco = {
    'device_type': 'cisco_ios',
    'host': '192.168.1.254',
    'username': 'admin',
    'password': secret_password,
}

print("Connecting to the router...")

# Establishing a connection to the router using ConnectHandler.
try:
    net_connect = ConnectHandler(**router_cisco)
    
    # 3. Enviar um comando e guardar a resposta
    output = net_connect.send_command("show vtp status")
    
    print("-" * 30)
    print("Interfaces state:")
    print(output)
    print("-" * 30)

    # Closing the connection.
    net_connect.disconnect()

except Exception as e:
    print(f"Error Connecting to Router: {e}")