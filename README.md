# 🌾 AgroMatch 

**AgroMatch** is a web-based platform built to empower farmers with personalized, climate-resilient crop recommendations. Designed for the **HCK3_17SDG Hackathon**, it blends data-driven logic with a clean, accessible interface to support sustainable agriculture in Kenya and beyond.

---

## 🎯 Hackathon Goal

- **SDG Focus:**  
  - SDG 15- Life on Land  
    

- **Challenge:**  
  Help farmers make smarter planting decisions using local data

- **Solution:**  
  A crop recommendation engine that adapts to soil, climate, and region — delivered through a user-friendly web app

---

## 🚀 Features

- 🧠 **Smart Crop Matching** — Based on soil type, region, and climate  
- 👤 **User Authentication** — Secure login, signup, and dashboard  
- 📄 **Dynamic Input Forms** — For farm data and preferences  
- 🎨 **Tailwind + DaisyUI Styling** — Clean, responsive, and mobile-friendly  
- 🧭 **Public Landing Page** — `about.html` with simplified navigation  
- 🔐 **Protected Dashboard** — `index.html` for logged-in users  
- 🖼️ **Visual-Ready Layout** — Designed for SVGs, 3D illustrations, and storytelling  

---

## 🛠 Tech Stack

| Layer         | Tools Used              |
|--------------|--------------------------|
| Backend       | Django, Python           |
| Frontend      | HTML, Tailwind CSS, DaisyUI |
| Auth & Routing| Django Auth, URLconf     |
| Deployment    | *(Add your method: e.g., Heroku, Render)* |

---

## 📦 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Flora72/HCK3_17SDG.git
cd HCK3_17SDG

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
Visit the app at: http://127.0.0.1:8000 
```

🌍 Impact
AgroMatch supports smallholder farmers by:

- Reducing crop failure risk

- Encouraging climate-smart agriculture

- Making technology accessible through intuitive design



📜 License
MIT License — built and maintained by Florence Ndinda
