from fastapi_app.app_v1 import basic_app
import uvicorn 


if __name__ == "__main__":
    uvicorn.run("fastapi_app.app_v1:basic_app",host="127.0.0.1",port=8000, reload=True)