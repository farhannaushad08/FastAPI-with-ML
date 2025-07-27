# 🚀 FastAPI-with-ML

This repository includes two FastAPI-based microprojects:

1. 🏥 *Patient Management System (CRUD API)*  
2. 🤖 *Insurance Premium Prediction with ML (API + Frontend)*

Both projects are modular and self-contained.

---

## 📁 Project Structure

```
FastAPI-with-ML/
├── fastapi-crud/          # CRUD API for managing patient records
│   ├── fast_api.py
│   ├── patients.json
│   └── README.md
│
├── fastapi-ml/            # ML model API + Streamlit frontend
│   ├── backend.py
│   ├── frontend.py
│   ├── model.pkl
│   ├── insurance.csv
│   ├── fastapi_ml_model.ipynb
│   └── README.md
│
└── README.md              # ← You are here
```

---

## 🏥 1. Patient Management API (fastapi-crud/)

A complete REST API for managing patients using FastAPI and JSON for storage.

*Features:*
- Full CRUD: Create, read, update, delete
- Computed BMI and health verdicts
- JSON data persistence
- Supports advanced HTTP methods: GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, CONNECT, TRACE

📄 [Read full details →](./fastapi-crud/README.md)

---

## 🤖 2. Insurance Premium ML App (fastapi-ml/)

An ML model to classify users into *insurance premium tiers*. Comes with both an API (backend.py) and a Streamlit frontend (frontend.py).

*Features:*
- FastAPI backend for prediction
- Streamlit frontend UI
- Uses model stored in model.pkl
- Input: age, height, weight, income, occupation, smoking, city
- Output: predicted category, confidence, and class probabilities

📄 [Read full details →](./fastapi-ml/README.md)

---

## 🔧 Getting Started

Install required packages:

bash
pip install -r requirements.txt


Or manually install:

bash
pip install fastapi uvicorn pandas scikit-learn streamlit


Then run each app from its folder.



---

## 📝 License

This project is open-source under the *MIT License*.
