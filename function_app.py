import azure.functions as func
import datetime
import json
import logging
from example_validation import validation_logic

app = func.FunctionApp()

@app.route(route="validate")
def validate_data_http(req: func.HttpRequest) -> func.HttpResponse:

  status_code = 200

  try:
    # Get the data from the request body (adjust based on your data format)
    data = req.get_json()
    
    # Call the validation logic from the imported module
    response = validation_logic.validate_salary_records(data);
  
  except ValueError as e:
    # Extract the JSON data from the exception
    response = e.args[0]  # Access the JSON object within the exception
    status_code = 400  # Bad Request

  except Exception as e:  # Catch any exceptions raised during validation
    response = {"message": str(e)}
    status_code = 500  # Internal Server Error

  return func.HttpResponse(
      body=json.dumps(response),
      status_code=status_code,
      mimetype="application/json"
  )