from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import Optional
from pydantic import BaseModel

app = FastAPI()
class Hello(BaseModel):
    name :str
    format : str


@app.get("/helloj/{name}/{format}")
async def helloj_get(name: str = "abc", format: str = "json", request: Request = None):
   
    query_params = dict(request.query_params)
    fname = query_params.get("name", name)
    fformat = query_params.get("format", format)
    
    return {
        
        "name": fname,
        "format": fformat
    }


@app.post("/helloj")
async def helloj_post(request: Hello):
    

    fname = request.name
    fformat = request.format

    return {"name": fname, "format": fformat}

