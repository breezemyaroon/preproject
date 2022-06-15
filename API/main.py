from fastapi import FastAPI
import uvicorn

from action import Action

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/my_name")
def my_name():
    data = "AROON WANTHONG"
    return data

@app.get("/input_name")
def input_name(name):
    data = name
    return data

@app.get("/input_name_Lastname")
def input_name_Lastname(fristname,lastname):
    data = fristname + " " + lastname
    return data

@app.get("/velocity")
def velocity(S:float,T:float):
    vel = "velcolcity {:.2f}".format(S/T)
    return vel

@app.get("/paralel-sereis_Cricuit")
def paralel(R1:float, R2:float, R3:float):
    resistence = "Paralel {:.2f}".format(((1/R1)+(1/R2)+(1/R3))**-1),"Sereis {:.2f}".format((R1)+(R2)+(R3))
    return resistence

@app.get("/update_status_hard_ware")
def update_status_hw(ID, status):
    data = Action.update_set_ware(ID, status)
    return data

@app.get("/select_ware")
def select_ware(ID):
    data= Action.select_ware(ID)
    return data

@app.get("/ADD_Hard_Ware")
def ADD_Hard_Ware(name, HW_name):
    data= Action.ADD_Hard_Ware(name, HW_name)
    return data

# @app.get("/delete_from_were")
# def delete_from_were(ID):
#     data = Action.delete_from_were(ID)
    return data

if __name__ == "__main__":
    uvicorn.run("main:app", host="192.168.43.48", port=8000, reload=True)