from fastapi import FastAPI

app= FastAPI()
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
            ],
            "place":"Mumbai goregaon gat kr.8 ....SEBC...SRFP"
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
            #"place":"Mumbai goregaon gat kr.8 ....SEBC...SRFP"
        }
    ]

@app.get("/")
async def read_root():    
    return "Welcome to site"

@app.get("/resumeData/{profileId}")
async def resumeData(profileId:int):  
    data = [d for d in home_page_data if d.get('profileId')== profileId]
    return data