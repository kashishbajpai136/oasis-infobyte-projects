💬 Python Socket Chat Application
📌 Project Overview

This is a simple multi-client chat application built using Python and socket programming. It allows multiple users (clients) to connect to a server and exchange messages in real-time through the terminal.

🚀 Features
📡 Client-server architecture
👥 Multiple clients can connect simultaneously
💬 Real-time messaging
🔁 Continuous send & receive using threading
🖥️ Terminal-based interface (simple and lightweight)
🛠️ Technologies Used
Python
Socket Programming
Threading
📂 Project Structure
chatbot/
│── server.py   # Handles multiple client connections
│── client.py   # Connects to server and sends/receives messages
▶️ How to Run
1️⃣ Start the Server
python server.py
2️⃣ Run Clients (in separate terminals)
python client.py

👉 Open multiple terminals to simulate multiple users.

⚙️ How It Works
The server listens for incoming client connections.
Each client connects to the server using IP address and port.
The server handles multiple clients using threads.
Messages sent by one client are received by others in real-time.
🎯 Future Improvements
Add GUI using Tkinter or PyQt
Add usernames for clients
Implement private messaging
Add message timestamps
Improve UI/UX
📖 Learning Outcomes
Understanding of socket programming
Working with client-server architecture
Handling multiple clients using threading
Basics of real-time communication systems
