## Why

The application cannot start on a clean local Windows host because its required PostgreSQL, Redis, and Milvus services are neither bundled nor configured for local execution. A reproducible runtime stack is required to verify the existing RAG workflow instead of treating external dependencies as implicit prerequisites.

## What Changes

- Add a local Docker Compose stack for PostgreSQL, Redis, and Milvus standalone with its required etcd and MinIO services.
- Add a documented local backend configuration that targets those services without replacing external API credentials.
- Add repeatable startup and health-verification instructions for the backend and Vue client.

## Capabilities

### New Capabilities

- `local-runtime-stack`: A developer can provision and verify all stateful services required by the existing FastAPI application on one machine.

### Modified Capabilities

- None.

## Impact

- Adds Docker Compose infrastructure and local-runtime documentation.
- Updates local backend connection settings only; the public API and RAG business flow remain unchanged.
- Requires Docker Desktop, Python 3.10+, Node.js, and a valid DashScope API key for LLM and embedding calls.
