## Context

The FastAPI lifecycle creates the relational schema and therefore requires PostgreSQL before it can serve requests. The repository has no local orchestration for PostgreSQL, Redis, or Milvus, while the existing `.env` points at unreachable placeholder hosts. The Vue client already proxies API calls to `127.0.0.1:8000`.

## Goals / Non-Goals

**Goals:**

- Provision PostgreSQL, Redis, and Milvus 2.5 locally with one Compose command.
- Make the existing backend start against those dependencies without changing its public API or RAG behavior.
- Provide deterministic readiness checks and a local startup path for the Vue client.

**Non-Goals:**

- Replace PostgreSQL, Redis, Milvus, DashScope, or the existing data model.
- Add production secrets, Kubernetes, authentication, or a new deployment target.
- Claim that AI ingestion or chat works without a valid DashScope credential.

## Decisions

- Use Docker Compose rather than host-native service installation. This keeps the three stateful services isolated, reproducible, and removable on Windows.
- Use PostgreSQL 16 and Redis 7 with fixed development-only credentials. The backend already consumes standard DSNs, so no application code change is required.
- Use the official Milvus standalone image with required etcd and MinIO companions. This preserves the existing `pymilvus`/LangChain-Milvus integration instead of substituting a different vector store.
- Append explicit local runtime overrides to `backend/.env`. Pydantic dotenv parsing uses the final assignment and existing external credentials remain untouched. The local values are development credentials only.
- Validate in layers: Compose service health, FastAPI `/health`, frontend proxy `/health`, then an actual text-ingestion request if the DashScope API key is accepted.

## Risks / Trade-offs

- [Docker Desktop is stopped or unavailable] → Start it explicitly and wait for the engine before running Compose.
- [Milvus image startup is slower than PostgreSQL/Redis] → Use health checks and poll readiness rather than fixed short sleeps.
- [DashScope key is absent or invalid] → Keep infrastructure and health verification successful; report AI requests as a credential blocker rather than adding a mock provider.
- [Local volumes retain prior data] → Use named Compose volumes and document `docker compose down -v` as the explicit reset operation.
- [Development credentials are not suitable for production] → Scope them to the local Compose file and never promote them as a deployment configuration.

## Migration Plan

1. Start Docker Desktop and run `docker compose up -d`.
2. Apply local connection overrides, start FastAPI, and verify `/health` reports all services healthy.
3. Start Vue and verify its proxy reaches the backend.
4. Roll back infrastructure with `docker compose down`; remove data only with `docker compose down -v`.

## Open Questions

- Whether the existing DashScope credential is valid can only be established by a real embedding or chat request.
