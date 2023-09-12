step1:
Import all the required modules and libraries in the code such as uvicorn, fastapi, sqlalchemy etc for the operation of APIs

step2:
Uvicorn is the Application server that is required to run the application and accepts the reqeusts coming through the browser

step3:
Create the FastAPI app and instatiate it by
app = FastAPI()

step4:
Establish the connection with the Database (SQLite DB)

step4:
create a base class that contains all the attributes(address attributes) required in the application for creation, updation and deletion activity.

step5:
API is written to create the new address attributes and to be put up in the DB
#Eg:
#Create an address
@app.post("/addresses/", response_model=AddressRetrieve)
The above snippet is the decorator function used to define the endpoint that is accessible through the browser, when the endpoint is hit the underlying data in the DB is rendered to the browser as a response and vice versa

step6:
This entire activity can be monitored via th inbuilt swagger docs available by the FASTAPI 
It can be accessed through 127.0.0.1:8081/docs
By hitting the above link, we get the performance of API

 
