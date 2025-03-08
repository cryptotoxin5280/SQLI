# SQL Injection (SQLi) Attack Demo

## 🛠 Step 1: Install Colima
Colima is a lightweight container runtime for macOS.

1. Open a terminal and install Colima via Homebrew:
```sh
brew install colima
```
2. Start Colima
```sh
colima start
```
## 🛠 Step 2: Install docker-compose
Docker Compose is required to manage multiple containers.

1. Install Docker Compose via Homebrew:
   ```sh
   brew install docker-compose
   ```
2. Verify installation:
   ```sh
   docker-compose version
   ```
## 🛠 Step 3: Install Thunder Client (VSCode API Test Tool)
1. Open **VSCode**.
2. Go to **Extensions** (`Cmd+Shift+X` on macOS, `Ctrl+Shift+X` on Windows/Linux).
3. Search for **Thunder Client** and click **Install**.
4. Once installed, open Thunder Client from the sidebar.

## 🚀 Step 4: Run the Containers
Ensure you have docker-compose installed and follow these steps:
1. Navigate to the project directory:
    ```sh
    cd path/to/your/project
    ```
2. Start the containers:
    ```sh
    docker-compose up -d --build
    ```
This will start both the **MySQL** database and **FastAPI** backend.

3. Verify the containers are running:
    ```sh
    docker ps
    ```
## 🔥 Step 5: Test the SQL Injection Attack with Thunder Client

1. Open **Thunder Client** in VSCode.
2. Click **New Request**.
3. Select `POST` as the request method.
4. Enter the API endpoint:
   ```
   http://localhost:8000/login
   ```
5. Click on the **Query** tab and enter the following payload:
   ```json
   {
      "username": "admin",
      "password": "password' OR '1'='1"
   }
   ```
6. Click **Send**.
7. If the API is vulnerable, you should receive a response indicating successful authentication, even if the password is incorrect.
---
## 🛡️ How to Fix the Vulnerability
To prevent SQL Injection, modify the login function to use **parameterized queries**:

```python
@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if user:
        return {"message": "Login Successful!", "user": user[1]}
    else:
        return {"message": "Invalid Credentials!"}
```
---
## 📌 Additional Notes
- Stop the containers when done:
  ```sh
  docker-compose down
  ```
- Restart Colima if needed:
  ```sh
  colima restart
  ```
Happy Hacking! 🚀