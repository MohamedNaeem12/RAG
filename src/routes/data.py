from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from helpers.config import get_settings, Settings
from controllers import DataController, ProjectController
from fastapi.responses import JSONResponse
from models import ResponseStatus
import os 
import aiofiles
data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"],
)

@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                      app_setting: Settings = Depends(get_settings)):
        
    
    # validate the file properties
    data_controller = DataController()

    is_valid, result_signal = data_controller.validate_file_type(file=file)

    if not is_valid:
        return JSONResponse(
            status_code= status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
                }  
        )
        
    project_dir_path = ProjectController().get_project_path(project_id=project_id)   
    
    file_path = os.path.join(
        project_dir_path, 
        file.filename
        )
    async with aiofiles.open(file_path, 'wb') as f:
        while chunk := await file.read(app_setting.FILE_DEFAULT_CHUNK_SIZE):
            await f.write(chunk)
    return JSONResponse(
        content={
            "signal": ResponseStatus.FILE_UPLOADED_SUCCESS.value
        }
    )