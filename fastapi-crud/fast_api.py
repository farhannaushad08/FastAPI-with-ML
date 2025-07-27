from fastapi import FastAPI, Path, HTTPException, Query,Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal,Optional
from starlette.responses import Response


import json
import os

# object for fastapi
app = FastAPI()


# pydantic base model of Patient used for post method
class Patient(BaseModel):
    id: Annotated[str, Field(..., description='ID of the patient', examples=['P001'])]
    name: Annotated[str, Field(..., description='Name of the patient')]
    city: Annotated[str, Field(..., description='City where the patient is living')]
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the patient')]
    gender: Annotated[Literal['male', 'female', 'others'], Field(..., description='Gender of the patient')]
    height: Annotated[float, Field(..., gt=0, description='Height of the patient in mtrs')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the patient in kgs')]

    # Computed field for BMI
    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    # Computed field for verdict based on BMI
    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'

# pydantic base model of Patient used for put method
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    city: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0)]
    gender: Annotated[Optional[Literal['male', 'female']], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0)]
    weight: Annotated[Optional[float], Field(default=None, gt=0)]

# function to load json file
def load_data():
    if not os.path.exists('patients.json'):
        return {}
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data


# function to save data
def save_data(data):
    with open('patients.json', 'w') as f:
        json.dump(data, f, indent=4)


# GET method for home route
@app.get("/")
def read_root():
    return {"message": "Hello, Patient Management System Api"}


# GET method for localhost http://127.0.0.1:8000/about
@app.get("/about")
def about():
    return "A fully functional API to manage your patient record"


# GET method to view patients data
@app.get('/view')
def view():
    data = load_data()
    return data


# Path params, here Path function enhances the readability
@app.get('/patients/{patient_id}')
def view_patient(patient_id: str = Path(..., description='Id of patient in db', example='P001')):
    # load all the patients
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    # we have to return status code as 404 because not in db so using HTTPException
    raise HTTPException(status_code=404, detail='Patient not found')


# Query params
@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description='Sort on the basis of height, weight or bmi'),
    order: str = Query('asc', description='Sort on asc or desc')
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f'Invalid field select from {valid_fields}')

    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail='Invalid order select from between asc and desc')

    data = load_data()

    # sort_order will be True for descending, False for ascending
    sort_order = True if order == 'desc' else False

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)

    return sorted_data


# POST method to create a new patient
@app.post('/create')
def create_patient(patient: Patient):
    # load existing data
    data = load_data()

    # check if the patient already exists
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient already exists')

    # new patient add to the database
    # patient.model_dump() converts pydantic object to dict
    data[patient.id] = patient.model_dump()

    # save into json file
    save_data(data)

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})

# PUT method to update/edit a patient
@app.put('/edit')
def update_patient(patient_id: str, patient_update: PatientUpdate):
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')

    # Merge existing data with updates
    existing_data = data[patient_id]
    updates = patient_update.model_dump(exclude_unset=True)
    updated_data = {**existing_data, **updates}

    # Recalculate computed fields using Pydantic model
    updated_data['id'] = patient_id
    validated_patient = Patient(**updated_data)

    # Save updated dict without 'id'
    data[patient_id] = validated_patient.model_dump(exclude={'id'})
    save_data(data)

    return JSONResponse(status_code=200, content={'message': 'Patient updated'})

# DELETE method to remove a patient 
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id: str):

    # load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail='Patient not found')
    
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={'message':'patient deleted'})

# PATCH: Partial update of patient data (e.g., just update weight)
@app.patch("/patients/{patient_id}")
def patch_patient(patient_id: str, fields: dict):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    data[patient_id].update(fields)

    if "height" in fields or "weight" in fields:
        patient = Patient(id=patient_id, **data[patient_id])
        data[patient_id] = patient.model_dump(exclude={"id"})

    save_data(data)
    return {"message": "Patient patched successfully"}


# HEAD: Returns metadata only, no body
@app.head("/patients/{patient_id}")
def head_patient(patient_id: str):
    data = load_data()
    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    return Response(headers={"X-Patient-Exists": "true"})
    


# OPTIONS: Returns allowed HTTP methods for patients resource
@app.options("/patients")
def options_patients():
    return JSONResponse(
        content=None,
        headers={
            "Allow": "GET, POST, PUT, DELETE, PATCH, HEAD, OPTIONS, CONNECT, TRACE"
        },
        status_code=204
    )


# CONNECT: Simulated handler (for learning only, not actual tunnel support)
@app.api_route("/connect", methods=["CONNECT"])
def connect_handler():
    return JSONResponse(content={"message": "CONNECT method received (simulated)"})


# TRACE: Echoes request body for debugging (not typically used)
@app.api_route("/trace", methods=["TRACE"])
async def trace_handler(request: Request):
    body = await request.body()
    return JSONResponse(content={"method": "TRACE", "body": body.decode("utf-8")})
