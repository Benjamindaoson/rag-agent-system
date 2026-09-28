## 1. Local dependency infrastructure

- [x] 1.1 Create a Compose stack for PostgreSQL, Redis, etcd, MinIO, and Milvus 2.5.
- [x] 1.2 Add development-only backend connection overrides for the Compose services.
- [x] 1.3 Document the local start and explicit data-reset commands.

## 2. Runtime verification

- [ ] 2.1 Validate the Compose configuration and start Docker Desktop.
- [ ] 2.2 Start the stateful services and verify their readiness.
- [ ] 2.3 Start FastAPI and verify `/health` returns all dependencies healthy.
- [ ] 2.4 Verify the Vue proxy and a representative document ingestion/retrieval flow.
