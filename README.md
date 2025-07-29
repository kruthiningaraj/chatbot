# Webinar Registration Chatbot 🤖

A **retrieval-based chatbot** built to automate **webinar registration, FAQs, feedback collection, and certificate generation**.  
This project uses **Python (NLTK, Keras)** for chatbot training, **Flask** for the web app, **MongoDB** for data storage, and **ReportLab** for PDF certificate generation.

---

## 🚀 Features
- Retrieval-based **chatbot** trained using Recurrent Neural Networks (RNN)
- Automates webinar tasks: **registration, FAQs, feedback, and certificate generation**
- **Flask Web UI** for interaction
- **MongoDB integration** for storing registration and feedback data
- **PDF certificate generation** with ReportLab
- Clean, modular **Python codebase**, production-ready

---

## 📂 Project Structure
```
chatbot-webinar-registration/
│
├── data/                  # Intents dataset (chatbot training data)
│   └── intents.json
│
├── models/                # Trained chatbot model (generated after training)
│
├── src/                   # Core chatbot modules
│   ├── preprocess.py
│   ├── train_chatbot.py
│   ├── chatbot_response.py
│   ├── certificate_generator.py
│   ├── database.py
│   └── feedback_collector.py
│
├── app/                   # Flask web app
│   ├── templates/         # HTML templates
│   │   └── index.html
│   ├── static/            # CSS & JS files
│   └── app.py
│
├── notebooks/             # EDA & experimentation notebooks
│   └── chatbot_eda.ipynb
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## 📊 Dataset
The chatbot is trained on a **custom intents dataset** (`intents.json`) containing tags, patterns (user inputs), and responses.

Example:
```json
{
  "tag": "register_webinar",
  "patterns": ["Register me for the webinar", "I want to join the webinar"],
  "responses": ["Sure! Please provide your name and email."]
}
```

You can modify `intents.json` to add more intents.

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/chatbot-webinar-registration.git
cd chatbot-webinar-registration
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Train Chatbot Model
Run the training script to generate `chatbot_model.h5` inside the `models/` folder:
```bash
python src/train_chatbot.py
```

---

## 🌐 Run Flask App
Start the chatbot web app:
```bash
python app/app.py
```
Now visit **`http://127.0.0.1:5000/`** in your browser.

---

## 🧪 Usage
- **Chat with the bot** for registration and FAQs
- **Submit feedback** after webinar
- **Download PDF certificates**

---

## 📦 Tech Stack
- **Python 3.x**
- **NLTK** (text preprocessing)
- **Keras (TensorFlow backend)** (RNN chatbot model)
- **Flask** (web app backend)
- **MongoDB** (data storage)
- **ReportLab** (PDF generation)

---

## 🤝 Contributing
Feel free to fork this repo and submit PRs for improvements.

---

## 📜 License
MIT License © 2025
