# 🧿 TEC — The Encrypted Chatroom

TEC (short for **The Encrypted Chatroom**) is a private, anonymous chat tool you can run with your friends — perfect for school, side projects, or anytime you want to send secret messages that no one else can read.

> 🔐 Messages are encrypted, encoded, and obfuscated — only your group can decode them.

---

## 📦 Requirements

- Python 3.x
- Node.js (for running the backend server)
- A [Pastebin](https://pastebin.com) account (for the save feature)

---

## 🚀 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/tec.git
cd tec
```

### 2. Start the server

Navigate into the `server` directory (you’ll need to create it if not already there), and run a basic Node.js server that accepts POST/GET requests.

Example `server.js` (inside `/server`):

```js
const fs = require('fs');
const express = require('express');
const app = express();
const port = 3000;

let messages = [];

app.use(express.text());

app.get('/', (req, res) => {
  res.send(messages.join('\n'));
});

app.post('/', (req, res) => {
  messages.push(req.body.trim());
  res.sendStatus(200);
});

app.post('/clear', (req, res) => {
  messages = [];
  res.send('Cleared');
});

app.listen(port, () => {
  console.log(`TEC server running at http://localhost:${port}`);
});
```

Then start it:

```bash
node server.js
```

> ✅ Tip: Deploy this to Replit, Glitch, Render, or Railway for free hosting.

---

### 3. Configure the script

Open the main Python file and do **two things**:

- **Update the server URL**:
  Replace:
  ```python
  url = "https://yournodeserver.com/"
  ```
  With your actual server URL, for example:
  ```python
  url = "http://localhost:3000/"
  ```

- **Add your Pastebin API key**:
  Replace:
  ```python
  api_dev_key = 'INSERT_PASTEBIN_KEY_HERE'
  ```
  With your [Pastebin API dev key](https://pastebin.com/doc_api).

---

## 💬 How to Use

1. Run the Python script:

```bash
python3 tec.py
```

2. When asked:
```
What numbers would you like to multiply?
```
Type: `no` — this skips the calculator and launches the encrypted chatroom.

3. Choose:
- `c0v3r`: join the encrypted chat
- `s@v3r`: upload code/files to Pastebin

4. Start chatting anonymously! Messages are encrypted, encoded, and stored only on your Node.js server.

---

## 🎒 Why This Exists

Because sometimes, you just want to talk with your friends at school or online — without teachers, admins, or companies reading over your shoulder.

> TEC lets you speak freely. It’s like passing notes, but smarter.

---

## ⚠️ Disclaimer

This is a hobby project and not a substitute for real secure messaging tools. Don’t use TEC for anything illegal or sensitive. Use it to learn, experiment, and build cool stuff.

---

## 🧠 Made by f1shticks
