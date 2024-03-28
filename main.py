from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins and methods, and set the allow credentials flag
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




'''
Data
'''
home_page_data =[ 
        {
            "profileId":1,
            "pageName":"Home",
            "websiteName":"My Portfolio",
            "message":"Welcome to my Knowledge world! Let's start knowledge sharing.",
            "mobileNumber":7820923701,
            "email":"prasadsawant11121999@gmail.com",
            "password":"Prasad@123",
            "candidateFirstName":"Prasad",
            "candidateMiddleName":"Ratnakant",
            "candidateLastName":"Sawant",
            "address":"169, Salgaon, Kudal",
            "district":"Sindhudurg",
            "state":"Maharashtra",
            "country":"India",
            "pinCode":416520,
            "education":[
                {
                    "course":"Secondary School Examination",
                    "streem":"",
                    "startYear":2015,
                    "endYear":2016,
                    "academy":"S.M.M.V. Salogaon",
                    "academyAddress":"Salgoan, Sindhudurg, MH,India",
                    "percent":93.80,
                    "CGPA":0
                },
                {
                    "course":"Higher Secondary Examination",
                    "streem":"Science",
                    "startYear":2017,
                    "endYear":2018,
                    "academy":"Kudal Highschool Jr.College,Kudal",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":76.92,
                    "CGPA":0
                },
                {
                    "course":"Bachelor Of Science (B.Sc)",
                    "streem":"Mathematics",
                    "startYear":2018,
                    "endYear":2021,
                    "academy":"S.R.M. College Kudal, Mumbai University",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":0,
                    "CGPA":9.71
                },
                {
                    "course":"Master Of Science (M.Sc)",
                    "streem":"Mathematics",
                    "startYear":2021,
                    "endYear":2023,
                    "academy":"S.R.M. College Kudal, Mumbai University",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":0,
                    "CGPA":6.21
                }
            ]
        },
        {
            "profileId":2,
            "pageName":"Home",
            "websiteName":"My Portfolio",
            "message":"Welcome to my Knowledge world! Let's start knowledge sharing.",
            "mobileNumber":7820923701,
            "candidateFirstName":"Divya",
            "candidateMiddleName":"Kashiram",
            "candidateLastName":"Wairkar",
            "email":"divyawairkar2010@gmail.com",
            "password":"Divya@123",
            "address":"1245, Varad, Malvan",
            "district":"Sindhudurg",
            "state":"Maharashtra",
            "country":"India",
            "pinCode":416512,
            "education":[
                {
                    "course":"Secondary School Examination",
                    "streem":"",
                    "startYear":2015,
                    "endYear":2016,
                    "academy":"Varad Highschool, Malvan Katta",
                    "academyAddress":"Varad, Malvan Katta, Sindhudurg, MH,India",
                    "percent":94.80,
                    "CGPA":0
                },
                {
                    "course":"Higher Secondary Examination",
                    "streem":"Science",
                    "startYear":2017,
                    "endYear":2018,
                    "academy":"Kudal Highschool Jr.College,Kudal",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":86.90,
                    "CGPA":0
                },
                {
                    "course":"Bachelor Of Science (B.Sc)",
                    "streem":"Mathematics",
                    "startYear":2018,
                    "endYear":2021,
                    "academy":"S.R.M. College Kudal, Mumbai University",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":0,
                    "CGPA":9.71
                },
                {
                    "course":"Master Of Science (M.Sc)",
                    "streem":"Mathematics",
                    "startYear":2021,
                    "endYear":2023,
                    "academy":"S.R.M. College Kudal, Mumbai University",
                    "academyAddress":"Kudal, Sindhudurg, MH, India",
                    "percent":0,
                    "CGPA":6.21
                }
            ]
        }
    ]

@app.get("/")
async def read_root():    
    return "Welcome to site"

@app.get("/resumeData/{profileId}")
async def resumeData(profileId:int):  
    data = [d for d in home_page_data if d.get('profileId')== profileId]
    return data

@app.get("/login/")
async def login(email:str,password:str):  
    data = [d for d in home_page_data if d.get('email')== email and d.get('password')==password]
    if (len(data))>0:
        return {"isAuthenticated":True,"email":email}
    else:
        return {"isAuthenticated":False,"email": ""}
