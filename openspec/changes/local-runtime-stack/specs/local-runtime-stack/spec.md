## ADDED Requirements

### Requirement: Local stateful dependency provisioning
The repository SHALL provide one Docker Compose configuration that provisions PostgreSQL, Redis, and Milvus 2.5 with all Milvus-required supporting services for local development.

#### Scenario: Fresh local provisioning
- **WHEN** Docker Desktop is running and a developer executes `docker compose up -d`
- **THEN** PostgreSQL, Redis, and Milvus SHALL become reachable on ports 5432, 6379, and 19530 respectively.

### Requirement: Backend local startup compatibility
The repository SHALL provide local backend connection settings that allow the existing FastAPI application to create its schema and serve its health endpoint against the Compose services.

#### Scenario: Backend health check
- **WHEN** the Compose services are ready and the backend starts with its project virtual environment
- **THEN** `GET /health` SHALL return HTTP 200 with `postgres`, `redis`, and `milvus` marked healthy.

### Requirement: Frontend proxy verification
The local Vue development server SHALL retain its proxy path to the backend health endpoint.

#### Scenario: Browser health proxy
- **WHEN** the Vue server and a healthy backend are running
- **THEN** `GET http://127.0.0.1:5173/health` SHALL return the backend health response with HTTP 200.
