# 🏥 FastAPI CRUD – Patient Management System

This is a fully functional REST API built with **FastAPI** that allows you to manage patient records stored in a JSON file. It supports all major HTTP methods including `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `OPTIONS`, `HEAD`, `TRACE`, and `CONNECT`.

---

## 📁 Folder: `fastapi-crud/`

### 🩺 Features

- Add, view, update, delete, and sort patient records
- Computes **BMI** and **health verdict** (e.g., *Normal*, *Overweight*, etc.)
- Pydantic models for input validation
- Custom HTTP method handlers: `OPTIONS`, `HEAD`, `TRACE`, `CONNECT`
- JSON-based data storage (via `patients.json`)
- Modular and scalable design

---

## 🚀 How to Run

### 1. Install dependencies

```bash
pip install fastapi uvicorn
```

### 2. Start the API server

```bash
uvicorn fast_api:app --reload
```

> Make sure you're inside the `fastapi-crud/` folder.

---

## 🧪 API Endpoints

| Method | Endpoint              | Description                          |
|--------|------------------------|--------------------------------------|
| GET    | `/`                    | Home route                           |
| GET    | `/about`               | About the API                        |
| GET    | `/view`                | View all patient records             |
| GET    | `/patients/{id}`       | View a specific patient              |
| GET    | `/sort`                | Sort patients by BMI, height, etc.   |
| POST   | `/create`              | Add a new patient                    |
| PUT    | `/edit?patient_id=...` | Edit a patient’s details             |
| PATCH  | `/patients/{id}`       | Partially update patient info        |
| DELETE | `/delete/{id}`         | Delete a patient                     |
| HEAD   | `/patients/{id}`       | Check if a patient exists (headers) |
| OPTIONS| `/patients`            | Get allowed HTTP methods             |
| CONNECT| `/connect`             | Simulated CONNECT request            |
| TRACE  | `/trace`               | Echo request body (for debugging)    |

---

## 📊 JSON Data Format

```json
"P001": {
  "name": "Ananya Verma",
  "city": "Guwahati",
  "age": 28,
  "gender": "female",
  "height": 1.65,
  "weight": 90.0,
  "bmi": 33.06,
  "verdict": "Obese"
}
```

---

## 🛠 Technologies Used

- [FastAPI](https://fastapi.tiangolo.com/)
- Pydantic
- Python 3.10+
- JSON (as database)

---

## 🧩 Future Enhancements

- Replace JSON with SQLite or PostgreSQL
- Add authentication/authorization
- Frontend integration (React/Streamlit)

---

## 👨‍💻 Author

 Md Farhan Naushad  
📧 farhannaushad08@gmail.com
📦 GitHub: [@farhannaushad08](https://github.com/farhannaushad08)

---

## 📝 License

This project is open-source and free to use under the MIT License.
