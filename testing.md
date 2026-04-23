## Endpoint: GET /employees

Purpose:
- Returns all employees stored in the database

Expected successful behavior:
- Status code 200
- Response body is a JSON list
- Each item contains:
  - employee_id
  - full_name
  - email
  - created_at

--------------------------------------------------

### Manual Testing — Swagger and cURL

#### Case 1 - Happy path

Expected:
- status code 200
- returns a list
- each item contains employee_id, full_name, email, created_at

Observed:
- status code 200 OK
- response is a JSON list
- all expected fields are present

Result:
PASS

--------------------------------------------------

#### Case 2 - Output field validation

Expected:
- employee_id is int
- full_name is string
- email is string
- created_at is string

Observed:
- all checked employees matched expected field types

Result:
PASS

--------------------------------------------------

#### Case 3 - Empty database

Expected:
- status code 200
- response body is []

Observed:
- endpoint returned 200 OK
- response body was an empty list
- no error occurred

Result:
PASS

--------------------------------------------------

#### Case 4 - Ordering

Expected:
- employees are returned in ascending employee_id order

Observed:
- employees were returned in ascending order
- order remained stable across repeated requests

Result:
PASS

--------------------------------------------------

#### Case 5 - Request via curl

Expected:
- same behavior as Swagger
- status 200
- response body in JSON format
- headers indicate application/json

Observed:
- curl returned HTTP/1.1 200 OK
- Content-Type: application/json
- JSON body matched Swagger response
- response order remained consistent (ORDER BY employee_id)

Result:
PASS

--------------------------------------------------

#### Case 6 - Repeated requests stability

Expected:
- repeated requests return the same structure and consistent order

Observed:
- endpoint returned 200 OK on repeated requests
- JSON structure remained stable
- ordering remained consistent

Result:
PASS

--------------------------------------------------

#### Case 7 - Collection contract consistency

Expected:
- endpoint always returns a JSON list
- one record does not change the response type

Observed:
- endpoint returned a list with multiple records
- endpoint returned a list with one record
- endpoint returned [] when database was empty

Result:
PASS

--------------------------------------------------

#### Case 8 - Valid but less typical data

Expected:
- endpoint returns valid JSON even with less typical employee data

Observed:
- response format remained correct
- fields were returned completely
- no serialization issues were detected

Result:
PASS

--------------------------------------------------

### General notes:
- FastAPI serializes the response to JSON
- response_model validates and structures output
- empty data is not an error for this endpoint

--------------------------------------------------

### Manual Testing — Postman

#### Case 1 - Happy path

Expected:
- status code 200
- response body is a JSON list
- each item contains employee_id, full_name, email, and created_at

Observed:
- the request was sent from Postman to GET /employees
- the application returned 200 OK
- the response body was a JSON list
- all returned employee objects matched the expected structure

Result:
PASS

--------------------------------------------------

### Automated Testing — Pytest

#### Case 1 - Returns employee collection

Expected:
- status code 200
- response body is a JSON list
- each employee contains employee_id, full_name, email, and created_at

Observed:
- pytest request returned 200 OK
- response body was a JSON list
- returned employee objects matched the expected response structure

Result:
PASS 

--------------------------------------------------

## Endpoint: GET /employees/{employee_id}

### Manual Testing — Swagger and cURL

#### Case 1 - Happy path

Expected:
- status code 200
- returns a single employee object
- employee_id matches the requested ID
- response contains employee_id, full_name, email, created_at

Observed:
- status code 200 OK
- endpoint returned a single JSON object
- returned employee_id matched the requested ID
- all expected fields were present

Result:
PASS

--------------------------------------------------

#### Case 2 - Non-existent employee

Expected:
- status code 404
- clear error message
- no empty object or null response

Observed:
- endpoint returned HTTP/1.1 404 Not Found
- response body was {"detail":"employee not found"}
- behavior matched the intended design

Result:
PASS

--------------------------------------------------

#### Case 3 - Invalid path parameter type

Expected:
- status code 422
- validation error generated before business logic

Observed:
- endpoint returned HTTP/1.1 422 Unprocessable Entity
- response body showed integer parsing validation error
- invalid path parameter was rejected before normal endpoint flow

Result:
PASS

--------------------------------------------------

### General notes:
- This endpoint returns a single employee resource, not a list
- 404 means the employee_id was valid but no employee was found
- 422 means the path parameter did not match the expected integer type
- FastAPI validates the path parameter before normal endpoint logic
- response_model validates and structures the successful output

--------------------------------------------------

### Automated Testing — Pytest

#### Case 1 - Non-existent employee (404)

Expected:
- status code 404
- response body {"detail":"employee not found"}

Observed:
- the request reached the endpoint with a valid integer ID
- no employee was found for that ID
- the application returned 404 Not Found
- the error response followed the expected structure {"detail":"employee not found"}

Result:
PASS

--------------------------------------------------

#### Case 2 - Invalid path parameter type (422)

Expected:
- status code 422
- validation error generated by FastAPI
- invalid input rejected before normal endpoint flow completes

Observed:
- FastAPI validation rejected the invalid path parameter
- the request did not pass input validation
- the framework returned 422 Unprocessable Entity
- type enforcement was handled automatically

Result:
PASS

--------------------------------------------------

### Manual Testing — Postman

#### Case 1 - Happy path

Expected:
- status code 200
- returns a single employee object

Observed:
- status code 200 OK
- endpoint returned a JSON object with expected fields

Result:
PASS

--------------------------------------------------

#### Case 2 - Non-existent employee

Expected:
- status code 404
- clear error message

Observed:
- endpoint returned 404 Not Found
- response body: {"detail":"employee not found"}

Result:
PASS

--------------------------------------------------

#### Case 3 - Invalid path parameter

Expected:
- status code 422
- validation error before business logic

Observed:
- endpoint returned 422 Unprocessable Entity
- FastAPI validation rejected the invalid ID

Result:
PASS

--------------------------------------------------

## Endpoint: POST /employees

### Manual Testing — Swagger and cURL

### Case 1 - Happy path

Expected:
- status code 201
- employee is created successfully
- response body is {"message":"employee created"}

Observed:
- curl.exe returned HTTP/1.1 201 Created
- response headers included content-type: application/json
- response body was {"message":"employee created"}
- service log showed employee_create called
- request completed successfully

Result:
PASS

--------------------------------------------------

### Case 2 - Duplicate email

Expected:
- status code 400
- duplicate email should be rejected
- response body is {"detail":"email already exists"}

Observed:
- curl.exe returned HTTP/1.1 400 Bad Request
- response headers included content-type: application/json
- response body was {"detail":"email already exists"}
- behavior matched the intended business rule

Result:
PASS

--------------------------------------------------

### Case 3 - Invalid email format

Expected:
- status code 422
- request body should fail schema validation
- response body should contain a validation error

Observed:
- curl.exe returned HTTP/1.1 422 Unprocessable Entity
- response headers included content-type: application/json
- response body contained a validation error for the email field
- request was rejected before business logic execution

Result:
PASS

--------------------------------------------------

### Case 4 - missing required field

Expected:
- status code 422
- request body should fail schema validation
- response body should indicate that a required field is missing

Observed:
- curl.exe returned HTTP/1.1 422 Unprocessable Entity
- response headers included content-type: application/json
- response body contained a validation error indicating that the email field was missing
- request was rejected before business logic execution

Result:
PASS

--------------------------------------------------

These tests were executed manually in Postman using saved requests inside the collection `Company API V1 - Testing`.

--------------------------------------------------

### Manual Testing — Postman

#### Case 1 - Happy path

Expected:
- status code 201
- successful creation message

Observed:
- status code 201 Created
- response body: {"message":"employee created"}

Result:
PASS

--------------------------------------------------

#### Case 2 - Duplicate email

Expected:
- status code 400
- clear error message
- employee should not be created again

Observed:
- status code 400 Bad Request
- response body: {"detail":"email already exists"}

Result:
PASS

--------------------------------------------------

#### Case 3 - Invalid email format

Expected:
- status code 422
- validation error before business logic

Observed:
- status code 422 Unprocessable Entity
- FastAPI/Pydantic rejected the invalid email format

Result:
PASS

--------------------------------------------------

#### Case 4 - Missing required field

Expected:
- status code 422
- missing required field error

Observed:
- status code 422 Unprocessable Entity
- validation error indicated that `email` was required

Result:
PASS

--------------------------------------------------

### Automated Testing — Pytest

--------------------------------------------------


#### Case 1 - Happy path (201)

Expected:
- status code 201
- response body {"message":"employee created"}

Observed:
- the request was sent with a valid full_name and a valid email
- the application returned 201 Created
- the response body matched the expected structure {"message":"employee created"}

Result:
PASS

--------------------------------------------------

#### Case 2 - Duplicate email (400)

Expected:
- status code 400
- response body {"detail":"email already exists"}

Observed:
- the first request created the employee successfully
- the second request reused the same email
- the application returned 400 Bad Request
- the error response matched the expected structure {"detail":"email already exists"}

Result:
PASS

--------------------------------------------------

#### Case 3 - Invalid email format (422)

Expected:
- status code 422
- validation error for the email field

Observed:
- the request was sent with an invalid email format
- the application returned 422 Unprocessable Entity
- the response body contained a validation error for the email field

Result:
PASS

--------------------------------------------------

#### Case 4 - Missing required field (422)

Expected:
- status code 422
- validation error indicating a missing required field

Observed:
- the request was sent without the email field
- the application returned 422 Unprocessable Entity
- the response body contained a validation error indicating that email was missing

Result:
PASS

--------------------------------------------------

### General notes:
- these tests were executed with FastAPI TestClient
- requests were sent internally to http://testserver, not to the running Uvicorn server
- because of that, pytest requests do not appear in the server terminal logs

--------------------------------------------------

## Endpoint: GET /tasks

### Manual Testing — Swagger and cURL

#### Case 1 - Happy path with existing employee and valid status

Expected:
- status code 200
- response body is a JSON list
- each returned task contains task_id, description, and status
- all returned tasks belong to the requested employee
- all returned tasks match the requested status

Observed:
- endpoint returned 200 OK
- response body was a JSON list
- returned tasks contained task_id, description, and status
- returned tasks matched employee_id = 1
- returned tasks matched status = pending
- output structure was consistent with the TaskOut response model

Result:
PASS

--------------------------------------------------

#### Case 2 - Employee with no assigned tasks

Expected:
- status code 200
- response body is an empty JSON list
- no error should occur when the employee has no tasks for the requested status

Observed:
- endpoint returned 200 OK
- response body was []
- behavior was correct for a collection endpoint with no matching records

Result:
PASS

--------------------------------------------------

#### Case 3 - Non-existent employee_id

Expected:
- status code 200
- response body is an empty JSON list
- no error should occur if no task matches the filters

Observed:
- endpoint returned 200 OK
- response body was []
- Swagger and cURL showed the same result
- service logs confirmed that the request was processed normally

Result:
PASS

--------------------------------------------------

#### Case 4 - Invalid employee_id type without status

Expected:
- status code 422
- validation errors should be returned for invalid query parameters
- missing required query fields should also be reported

Observed:
- endpoint returned 422 Unprocessable Entity
- response body included a validation error for employee_id because a string was sent instead of an integer
- response body also included a validation error indicating that status was required

Result:
PASS

--------------------------------------------------

#### Case 5 - Invalid employee_id type with valid status

Expected:
- status code 422
- validation error should be returned for employee_id

Observed:
- endpoint returned 422 Unprocessable Entity
- response body included a validation error for employee_id
- once status was provided correctly, the only remaining validation error was the invalid employee_id type

Result:
PASS

--------------------------------------------------

#### Case 6 - Invalid status value

Expected:
- status code 422
- validation error should indicate that the status value is not allowed

Observed:
- endpoint returned 422 Unprocessable Entity
- response body included an enum validation error
- FastAPI/Pydantic indicated that the expected value was "pending"

Result:
PASS

--------------------------------------------------

#### Case 7 - Response contract validation

Expected:
- response follows the TaskOut schema
- each item contains task_id, description, and status only

Observed:
- both Swagger and cURL returned task objects structured according to TaskOut
- returned fields matched the expected response contract: task_id, description, status
- no unexpected output structure was observed

Result:
PASS

--------------------------------------------------

#### Case 8 - Persistence after seeding data

Expected:
- inserted tasks remain stored in the database
- repeated requests return the same saved data after seeding

Observed:
- after inserting seed tasks into company_test.db, Swagger continued to return the same tasks after refresh
- data remained available across repeated checks
- task records persisted correctly in the database

Result:
PASS

--------------------------------------------------

### General notes:

- GET /tasks behaves as a filtered collection endpoint
- if no records match the filters, the endpoint returns 200 OK with an empty list []
- a non-existent employee_id does not generate 404 because the query is executed against the tasks collection
- invalid query parameter types and invalid enum values are rejected by FastAPI/Pydantic with 422 Unprocessable Entity
- response output follows the TaskOut contract: task_id, description, status

- test data was inserted manually using a local seed script (seedtasks.py)
- tasks were added to employees in company_test.db before testing the endpoint
- status is stored as pending by default and queried with status=pending
- repeated requests confirmed persistence in the database and consistency across Swagger and cURL

--------------------------------------------------

### Manual Testing — Postman

#### Case 1 - Employee with tasks

Expected:
- status code 200
- response body is a non-empty JSON list
- each returned task contains task_id, description, and status
- all returned tasks match the requested employee_id and status

Observed:
- Postman returned 200 OK
- response body was a JSON list with task records
- returned task objects contained task_id, description, and status
- returned tasks matched employee_id = 1 and status = pending

Result:
PASS

--------------------------------------------------

#### Case 2 - Employee with no tasks

Expected:
- status code 200
- response body is an empty JSON list
- no error should occur when the employee has no tasks for the requested status

Observed:
- Postman returned 200 OK
- response body was []
- behavior matched the expected collection response with no records

Result:
PASS

--------------------------------------------------

#### Case 3 - Non-existent employee_id

Expected:
- status code 200
- response body is an empty JSON list
- no error should occur if no task matches the filters

Observed:
- Postman returned 200 OK
- response body was []
- no matching records were found for employee_id = 999 and status = pending

Result:
PASS

--------------------------------------------------

#### Case 4 - Invalid employee_id

Expected:
- status code 422
- validation error for employee_id query parameter

Observed:
- Postman returned 422 Unprocessable Entity
- response body included a validation error for employee_id
- invalid string input was rejected before normal endpoint logic

Result:
PASS

--------------------------------------------------

#### Case 5 - Invalid employee_id without status

Expected:
- status code 422
- validation errors should indicate both invalid employee_id and missing status

Observed:
- Postman returned 422 Unprocessable Entity
- response body included a validation error for employee_id
- response body also included a validation error indicating that status was required

Result:
PASS

--------------------------------------------------

#### Case 6 - Invalid status

Expected:
- status code 422
- validation error for status query parameter
- invalid enum value should be rejected

Observed:
- Postman returned 422 Unprocessable Entity
- response body included an enum validation error for status
- invalid value "done" was rejected because the expected value was "pending"

Result:
PASS

--------------------------------------------------

### Automated Testing — Pytest

#### Case 1 - Employee with tasks

Expected:

status code 200
response body is a list
the list contains at least one task for the given employee
each task includes task_id, description and status

Observed:

the request was sent with a valid employee_id and status
the application returned 200 OK
the endpoint returned a JSON list with tasks
the returned items followed the expected structure

Result:
PASS

--------------------------------------------------

#### Case 2 - Employee with no tasks

Expected:

status code 200
response body is an empty list []
the endpoint should not fail when no matching tasks are found

Observed:

the request was sent with a valid employee_id and status
the application returned 200 OK
the endpoint returned an empty JSON list []
the no-results case was handled correctly

Result:
PASS

--------------------------------------------------

#### Case 3 - Invalid employee_id (422)

Expected:

status code 422
validation error should occur before reaching business logic
the error should point to employee_id in the query parameters

Observed:

the request was sent with a string instead of an integer for employee_id
the application returned 422 Unprocessable Entity
the response body contained a validation error in detail
the error location matched ["query", "employee_id"]

Result:
PASS

--------------------------------------------------

#### Case 4 - Invalid status (422)

Expected:

status code 422
validation error should occur before reaching business logic
the error should point to status in the query parameters

Observed:

the request was sent with an invalid status value
the application returned 422 Unprocessable Entity
the response body contained a validation error in detail
the error location matched ["query", "status"]

Result:
PASS

--------------------------------------------------
