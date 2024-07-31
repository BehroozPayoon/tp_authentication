## Setup and Run

1. Clone the repository
2. Make sure you have Docker and Docker Compose installed
3. Run `docker build -t tp_authentication:latest` to create image
4. Run `docker-compose up -d`
5. The Authentication Service will be available at http://localhost:8000

## API Endpoints

### Authentication Service

- POST /api/register/: Register a new user
- POST /api/login/: Login and receive an authentication token
- POST /api/authentication/: Validate token and return authenticated user data
