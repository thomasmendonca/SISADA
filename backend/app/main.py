import uvicorn
from sqlalchemy import text
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_session


app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get('/db-check')
async def db_check(session: AsyncSession = Depends(get_session),):
    result = await session.execute(text("SELECT 1"))
    return {"database": result.scalar_one()}

if __name__ == "__main__":
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=3002,
    )
