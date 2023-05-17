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

## Swagger API Documentation

The project includes Swagger for API documentation. After starting the containers, you can access the Swagger UI at [http://localhost:8000/swagger/](http://localhost:8000/swagger/).

## License

This project is licensed under the [MIT License](LICENSE).