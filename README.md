# AI-Code-Reviewer

An intelligent **AI-powered Code Reviewer** built using **Streamlit** and **Groq API** that analyzes your code and provides detailed feedback like a senior software engineer.

---

## 🚀 Features

* 🔍 Detects **bugs** in your code
* ✨ Suggests **code improvements**
* 🔐 Identifies **security issues**
* 📊 Gives a **code quality score (out of 10)**
* ⚡ Fast and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API (LLM)**
* **Pylint** (for static code analysis)

---

## 📂 Project Structure

```
AI-Code-Reviewer/
│── app.py              # Streamlit UI
│── reviewer.py         # AI review logic
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

---

## ⚙️ Installation

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Replace your Groq API key in `reviewer.py`:

```python
client = Groq(api_key="your_api_key_here")
```

⚠️ **Important:** Never upload your real API key to GitHub. Use `.env` file instead.

---

## ▶️ Run the App

```bash
python -m streamlit run app.py 
```

---

## 💡 How It Works

1. User pastes code into the input box
2. The app sends code to the AI model
3. AI analyzes and returns:

   * Bugs 🐞
   * Improvements 🚀
   * Security issues 🔐
   * Score 📊

---

## 📸 Screenshot

*(Add your app screenshot here)*

---

## 🔮 Future Improvements

* 🌐 GitHub repo integration
* 📁 Upload files instead of paste
* 📊 Advanced scoring system
* 🧠 Multiple AI model support

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork this repo and submit a pull request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Souvik Manna**

---

  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.3:8501

⭐ If you like this project, give it a star on GitHub!
