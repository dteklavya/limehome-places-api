# REST API for results from HERE PLACES API

## Api Endpoints

- http://localhost/places?q=hotel&at=13.0563101,77.5951032

## Initialization

    Get the code:
    
        $ git clone https://github.com/dteklavya/limehome-places-api.git

        $ cd limehome-places-api

    
    Service can be started in development mode or can be deployed using docker.

    - Deploy using Docker
      - $ docker run --env-file .env -p 80:5000 kanakraj/limehome-nearby-api:v0
  
    - Development
      - IMPORTANT NOTE: API will return 400 "Invalid Usage" unless .env file in project directory is updated with proper API keys and codes. Please see the .env file and replace appropriate values before proceeding. The docker image will run just fine as it ships with required API keys and codes.
      - After cloning the git repository, cd to the prject folder:
        - $ python -m venv venv
        - $ source venv/bin/activate
        - $ pip install -r requirements.txt
      - Start the Flask development server
        - ./start.sh
        - The API will be accesible on port 5000 http://localhost:5000/

## Deployment

    Docker container can be deployed manually using commands listed above. Or container orchetration/clustering tools can be used to deploy and manage it.

    The solution has been implemented keeping following points in mind to ensure better scaling without significant changes to tooling or development practices:

        - Dependency: All dependencies are explicitly declared and isolated using virtual environment for Python.
        - Configuration: Information such as database credentials and other values are retrived from environment so that these can be changed without changing the code. The .env file in repository has been added knowingly but without any confidential values like API keys and IDs.
        - Seperate build and run processes.
        - Both error and access logs (of Gunicorn application server) are directed to STDOUT for centralized storage and retrieval.
        - The app exports HTTP as a service by binding to a port (using Gunicorn), and listening to requests coming in on that port.

## Testing

    Unit tests for the application are included in the code base and tests can be run from the codebase as::
  
        python -m unittest

## Documentation

    The Python code has been appropriately commented using Docstrings for Class, methods, functions etc. Docstrings can be used in conjunction with document generation tools to auto generate feature rich documentation for codebase.
