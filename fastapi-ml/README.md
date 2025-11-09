# FastAPI ML – Insurance Premium Category Predictor

This project demonstrates a complete ML pipeline for predicting insurance premium categories based on user inputs like age, BMI, income, etc. It includes a FastAPI backend and a Streamlit frontend.

---

## Folder: `fastapi-ml/`

### Features

- Predicts insurance premium category (e.g., low, medium, high)
- FastAPI backend (`backend.py`) serves ML model via `/predict`
- Streamlit frontend (`frontend.py`) sends user input to the API
- Uses a trained model stored in `model.pkl`
- CSV data: `insurance.csv`
- Jupyter notebook for training: `fastapi_ml_model.ipynb`

---

## How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn pandas scikit-learn streamlit
```

### 2. Run FastAPI backend

```bash
uvicorn backend:app --reload
```

### 3. Run Streamlit frontend

```bash
streamlit run frontend.py
```

---

## Example API Input

```json
{
  "age": 35,
  "weight": 75,
  "height": 1.75,
  "income_lpa": 12.5,
  "smoker": false,
  "city": "Mumbai",
  "occupation": "private_job"
}
```

---

## API Output (Updated)

```json
{
  "response": {
    "predicted_category": "high",
    "confidence": 0.91,
    "class_probabilities": {
      "low": 0.01,
      "medium": 0.08,
      "high": 0.91
    }
  }
}
```

---

## Tech Stack

- Python 3.10+
- FastAPI
- Streamlit
- scikit-learn
- pandas
- Uvicorn

---

## Author

Md Farhan Naushad  
GitHub: [@farhannaushad08](https://github.com/farhannaushad08)

---

## License

MIT License. Free to use and modify.
