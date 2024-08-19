import asyncio
import re
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend_models import Counter, Runner, Tenant

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://frontend:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def strip_api_prefix(request: Request, call_next):
    path = request.url.path
    if path.startswith("/api/"):
        newpath = re.sub("/api/", "/", path)
        request.scope["path"] = newpath
    response = await call_next(request)
    return response


@app.get("/")
async def root():
    return {"message": "Hi there!"}


@app.get("/somedata/")
async def data():
    return {"x": [1,2,3], "y": [3,4,5]}


@app.post("/clear_tenants")
async def clear_tenants():
    Tenant.users = {}

@app.post("/start_counter/{tenant_id}")
async def counter(tenant_id):
    Tenant.users[tenant_id] = Runner()
    asyncio.create_task(Tenant.users[tenant_id].run_main())
    return True

@app.get("/get_count/{tenant_id}")
async def get_count(tenant_id):
    return {tenant_id: Tenant.users[tenant_id].counter.get_count()}

@app.post("/increment_count/{tenant_id}")
async def increment_count(tenant_id):
    Tenant.users[tenant_id].counter.increment()
    return True


@app.post("/reset_count/{tenant_id}")
async def reset_count(tenant_id):
    Tenant.users[tenant_id].counter.reset()
    return True
