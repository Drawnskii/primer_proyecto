from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, JSON, TIMESTAMP, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Any
import datetime

# Configura tu conexión a MySQL aquí
DATABASE_URL = "mysql+pymysql://root@localhost/weatherdb"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Modelo de tabla
class WeatherData(Base):
    __tablename__ = "weather_data"
    id = Column(Integer, primary_key=True, index=True)
    city_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    data = Column(JSON, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

Base.metadata.create_all(bind=engine)

# Modelo de entrada con validación
class WeatherPayload(BaseModel):
    data: dict[str, Any] = Field(...)

    @property
    def city_id(self) -> int:
        return self.data.get("id")

    @property
    def name(self) -> str:
        return self.data.get("name")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/api/weather")
def register_weather(payload: WeatherPayload):
    db = next(get_db())

    city_id = payload.city_id
    name = payload.name

    if not city_id or not name:
        raise HTTPException(status_code=400, detail="Missing 'id' or 'name' in JSON")

    try:
        record = WeatherData(
            city_id=city_id,
            name=name,
            data=payload.data
        )
        db.add(record)
        db.commit()
        db.refresh(record)
        return {
            "message": "Weather data saved",
            "id": record.id,
            "created_at": record.created_at.isoformat()
        }
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))
