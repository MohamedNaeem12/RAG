from fastapi import FastAPI, APIRouter
import os
base_router = APIRouter(
    prefix="/api/v1", #before all routers 
    tags =["api_v1"]  #to name category or using of routers
)

@base_router.get("/")
async def welcome():
    app_name = os.getenv("APP_NAME")
    app_version = os.getenv("APP_VERSION") 
    return {
     
        "app_name": app_name,
        "app_version": app_version
        }