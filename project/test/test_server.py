import socket
import subprocess
import os

def test_env_password():
    assert os.environ['INPUT_PASSWORD'] == 'admin'

def test_connection():
    subprocess.Popen(["python", ".project/src/server.py"])

    client = socket.socket()
    client.connect(('localhost', 6565))

    message = "Massage123!"
    client.send(message.encode())
    data = client.recv(1024)
    
    assert data.decode() == message
