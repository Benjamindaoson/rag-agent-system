# Local Runtime

> 项目路径：`D:\01_project\flagship-projects\harness-agent-platform\rag-agent-system`
> LLM：DeepSeek（读取系统环境变量 `DEEPSEEK_API_KEY`）
> Embedding：fastembed / BAAI/bge-small-zh-v1.5（本地 ONNX，首次运行自动下载 ~50MB）

## 1. 启动基础服务（PostgreSQL + Redis + Milvus）

```powershell
cd D:\01_project\flagship-projects\harness-agent-platform\rag-agent-system
docker compose up -d
```

## 2. 启动后端

```powershell
cd D:\01_project\flagship-projects\harness-agent-platform\rag-agent-system\backend
.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

健康检查：`http://127.0.0.1:8000/health`（返回 postgres/redis/milvus 全 OK）

## 3. 启动前端

```powershell
cd D:\01_project\flagship-projects\harness-agent-platform\rag-agent-system\front\rag_front
npm run dev -- --host 127.0.0.1 --port 5173
```

打开：`http://127.0.0.1:5173/`

## 重置本地数据（慎用）

```powershell
docker compose down -v
```
