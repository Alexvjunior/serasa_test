# Serasa Test Project

This is a Django project for the Serasa test.

## **Setup**

1. Clone the repository:
```bash
git clone https://github.com/Alexvjunior/serasa_test.git
```

2. Navigate to the project directory:
```bash
cd serasa_test
```

3. Build the Docker images:
```bash
docker-compose build
```

4. Start the containers:
```bash
docker-compose up -d
or
make run  
```


## **Running the Tests**

To run the tests, use the following command:
```bash
docker-compose exec web python manage.py test 
or
make test
```


## **Code Quality and Security**

To ensure code quality and enhance security, the following tools are integrated into the project:

### isort

[isort](https://pycqa.github.io/isort/) is a Python utility that sorts imports alphabetically and automatically separates them into sections.

To run isort and automatically format your imports, use the following command:

```bash
isort 
or
make format
```


### flake8

flake8 is a code linter that checks Python code for style and programming errors.

To run flake8 and check your code, use the following command:
```bash
flake8 apps
or 
make lint
```

### safety

safety is a command-line tool that checks your Python dependencies for known security vulnerabilities.

To run safety and check for vulnerabilities, use the following command:
```bash
safety check
or
make security
```


## **Swagger API Documentation**

The project includes Swagger for API documentation. After starting the containers, you can access the Swagger UI at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## **Available Makefile Commands**
The project includes a Makefile with several useful commands:

- make format: Format the code using isort and black.
- make lint: Run flake8 for linting the code.
- make test: Run pytest for running tests.
- make security: Perform a security check on the project dependencies using Safety.
- make run: Run the application using docker compose.
- make run-postgres: Run the postgres application using docker
- make run-redis: Run the redis application using docker
- make clean: Clean up the project by removing the virtual environment and cached files.


## **API Endpoints**
Listed below are all endpoints available in the API, along with the required payloads and expected responses.

### Endpoint 1: `/user/`
#### Descrição:
This endpoint allows you to create a new user.
#### Método HTTP:
`POST`

### Payload
```json
"name": "string",
"cpf": "string",
"email": "string",
"phone_number": "string"
```

### Resposta
```json
"id": 1,
"created": "string",
"modified": "string",
"name": "string",
"cpf": "string",
"email": "string",
"phone_number": "string"
```

### Endpoint 2: `/user/{id}`
#### Descrição:
Returns a specific user
#### Método HTTP:
`GET`

### Resposta
```json
"id": 1,
"created": "string",
"modified": "string",
"name": "string",
"cpf": "string",
"email": "string",
"phone_number": "string"
```

### Endpoint 3: `/user/?limit=&offset=&cpf=`
#### Descrição:
Returns a list of users. You can user cpf filter too.
#### Método HTTP:
`GET`

### Resposta
```json
"count": 1,
"next": "string",
"previous": "string",
"results":[
    {
        "id": 1,
        "created": "string",
        "modified": "string",
        "name": "string",
        "cpf": "string",
        "email": "string",
        "phone_number": "string"
    }
]
```

### Endpoint 4: `/user/{id}`
#### Descrição:
Delete user.
#### Método HTTP:
`DELETE`


### Endpoint 5: `/user/{id}`
#### Descrição:
Update user.
#### Método HTTP:
`PATCH`

### Payload
```json
"name": "string",
"cpf": "string",
"email": "string",
"phone_number": "string"
```

### Resposta
```json
"id": 1,
"created": "string",
"modified": "string",
"name": "string",
"cpf": "string",
"email": "string",
"phone_number": "string"
```

### Endpoint 6: `/token/`
#### Descrição:
Get Token system User.
#### Método HTTP:
`POST`

### Payload
```json
"username": "string",
"password": "string",
```

### Resposta
```json
"token": "string",
```


## **License**

This project is licensed under the [MIT License](LICENSE).