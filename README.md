# Serasa Test Project

This is a Django project for the Serasa test.

## Setup

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
```


## Running the Tests

To run the tests, use the following command:
```bash
docker-compose exec web python manage.py test 
```


## Code Quality and Security

To ensure code quality and enhance security, the following tools are integrated into the project:

### isort

[isort](https://pycqa.github.io/isort/) is a Python utility that sorts imports alphabetically and automatically separates them into sections.

To run isort and automatically format your imports, use the following command:

```bash
isort .
```


### flake8

flake8 is a code linter that checks Python code for style and programming errors.

To run flake8 and check your code, use the following command:
```bash
flake8
```

### safety

safety is a command-line tool that checks your Python dependencies for known security vulnerabilities.

To run safety and check for vulnerabilities, use the following command:
```bash
safety check
```

## Swagger API Documentation

The project includes Swagger for API documentation. After starting the containers, you can access the Swagger UI at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## License

This project is licensed under the [MIT License](LICENSE).