from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from typing import Annotated

import os

"""
main.py는 FastAPI 프로젝트의 전체적인 환경을 설정하는 파일
app객체를 통해 FastAPI의 설정을 할 수 있음
"""
app = FastAPI()


@app.get("/")
def hello_world():
    return {"message": "hi~~~! sky's world"}

@app.get("/hello")
def hello_world():
    return {"message": "Hello World"}

@app.post("/photo")
async def upload_photo(file: UploadFile): # UploadFile은 파일을 업로드할 때 사용하는 클래스
    UPLOAD_DIR = "./upload" # 이미지를 저장할 경로
    file_name = file.filename # 업로드한 파일의 이름
    contents = await file.read() # 업로드한 파일의 내용
    with open(os.path.join("./uploads", file_name), "wb") as f: # 업로드한 파일을 저장할 경로와 파일 이름을 설정
        return{"filename": file_name}




@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


# @app.get("/downloadfile/{file}")
# async def download_file(file):
#     targetFile = file
#     print(file)
#     print(f"File Download: {targetFile}")
#     # return FileResponse(targetFile, media_type="application/octet-stream", filename=file)
#     return FileResponse(targetFile, media_type="image/png", filename=file)


@app.get("/downloadfile/{file}")
async def download_file(file):
    # 파일 경로 설정
    file_path = os.path.join("uploads", file)
    print(file_path)

    if os.path.exists(file_path):
        # return FileResponse(file_path, media_type="application/octet-stream", filename=file)
        return FileResponse(file_path, media_type="image/png", filename=file)

    else:
        return "파일이 존재하지 않습니다."


# # 파일 다운로드 엔드포인트
# @app.get("/downloadfile/{file_name}")
# async def download_file(file_name: str):
#     # 파일이 저장된 디렉토리
#     directory = "uploads"  # 파일이 저장된 디렉토리를 설정하세요.
#
#     # 디렉토리 내의 모든 파일 검색
#     for root, dirs, files in os.walk(directory):
#         if file_name in files:
#             # 파일을 찾으면 해당 파일의 경로를 생성
#             file_path = os.path.join(root, file_name)
#             # 파일을 다운로드
#             return FileResponse(file_path, media_type="application/octet-stream", filename=file_name)
#
#     # 파일을 찾지 못한 경우 404 에러를 반환
#     raise HTTPException(status_code=404, detail="파일을 찾을 수 없습니다.")

