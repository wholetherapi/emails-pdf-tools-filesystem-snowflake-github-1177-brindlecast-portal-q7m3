from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.invoices import router as invoices_router
from routes.remittances import router as remittances_router

app = FastAPI(title="Supplier Portal API", version="2.6.3")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://portal.brindlecasttooling.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(invoices_router, prefix="/api/supplier")
app.include_router(remittances_router, prefix="/api/supplier")


@app.get("/healthz")
def healthz():
    return {"status": "ok"}
