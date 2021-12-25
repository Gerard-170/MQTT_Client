import paho.mqtt.client as mqtt
import sys

MIN_ARGS = 4

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(client, userdata, mid):
    print("Message Published: " + str(mid))

def main():

    if len(sys.argv) < MIN_ARGS:
        sys.exit("Datos insuficientes. Los datos deben ser al menos 4 \"python MQTT_com.py <server_addr> <username> <password> <Data>\"")
    # Get the server address
    Server = sys.argv[1]
    # Get the username
    Username = sys.argv[2]
    print(Username)
    # Get the password
    Password = sys.argv[3]
    print(Password)
    #Get Data
    Data = sys.argv[4]
    

    mqttc = mqtt.Client(client_id="PC", clean_session=True, userdata="UD", transport="tcp")
    mqttc.username_pw_set(username=Username,password=Password)
    mqttc.on_connect = on_connect
    try:
        mqttc.connect(Server, port=1883, keepalive=60, bind_address=Server)       #### usamos esta funcion porque no bloquea el promtp tenemos que llamar la funcion loop
    except Exception:
        print("No se pudo Conectar al server, por favor revise la conexion o la informacion proporcionada")
    ### Bind address indica la IP o la Interfaz de la PC desde la cual se conectara al server MQTT
    mqttc.on_publish = on_publish
    Message = Data
    mqttc.publish("paho/states", Message)


# Stand Alone execution
if __name__ == "__main__":
    main()