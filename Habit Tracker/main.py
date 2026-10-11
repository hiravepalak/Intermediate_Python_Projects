import requests
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

USER_ENDPOINT = "https://pixe.la/v1/users"


# SETTING UP USER ACCOUNT
# params = {"token": os.getenv("PIXELA_TOKEN"),
#           "username": os.getenv("PIXELA_USERNAME"),
#           "agreeTermsOfService": "yes",
#           "notMinor": "yes"}
#
# send_request = requests.post(USER_ENDPOINT, json=params)


# MAKING THE GRAPH
# GRAPH_ENDPOINT = f"{USER_ENDPOINT}/{os.getenv("PIXELA_USERNAME")}/graphs"
#
pixel_header = {"X-USER-TOKEN" : os.getenv("PIXELA_TOKEN") or ""}
#
# graph_config = {"id": "tech100projects",
#                 "name": "Building Tech Projects",
#                 "unit": "commit",
#                 "type": "int",
#                 "color": "ajisai",
#                 "timezone": "Asia/Kolkata",
#                 "description": "Any tech-related project, whether it be typing programs, building robots, hacking programs & any other sort of fun. Measured in contributions, each small task done counts!"}
#
# requests.post(GRAPH_ENDPOINT, json=graph_config, headers=pixel_header)


# ADDING A PIXEL
# POST_PIXEL_ENDPOINT = f"{USER_ENDPOINT}/{os.getenv("PIXELA_USERNAME") or ""}/graphs/tech100projects"
#
today = datetime.date.today()
time = today.strftime("%Y%m%d")
#
# pixel_config = {"date": time,
#                "quantity": "2"}
#
# requests.post(POST_PIXEL_ENDPOINT, json=pixel_config, headers=pixel_header)


# UPDATING PIXEL
EDIT_PIXEL_ENDPOINT= f"{USER_ENDPOINT}/{os.getenv("PIXELA_USERNAME") or ""}/graphs/tech100projects/{time}"
# update_pixel_config = {"quantity": "6"}
#
# requests.put(EDIT_PIXEL_ENDPOINT, json=update_pixel_config, headers=pixel_header)


# DELETE PIXEL
#print(requests.delete(EDIT_PIXEL_ENDPOINT, headers=pixel_header))

# DELETE ACCOUNT
# response = requests.delete(f"{USER_ENDPOINT}/{os.getenv("PIXELA_USERNAME") or ""}", headers=pixel_header)
#
# print("Status Code:", response.status_code)
# print("Response:", response.json())