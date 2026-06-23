from playwright.sync_api import sync_playwright
from conftest import page




def test_api_flow(playwright):  
    #  api_request = playwright.request.new_context(base_url="https://gorest.co.in/")
# access the server of the API
  api_request = playwright.request.new_context(base_url="https://gorest.co.in/",
                                               extra_http_headers = {"Authorization": "Bearer e7c10ef3f48257c0c331a36b50462fe391d403c1e1302ad75aada59defaa2c36"})

  # post api request 
  response = api_request.post(url ="/public/v2/users", 
                              data={ 
                                "name" : "Shivkumar ",
                                "email" : "shivkumar@example.com",
                                "gender" : "Male",
                                "status" : "Active"})
  json_data = response.json()
  assert response.status == 201
  user_id = json_data["id"]
  print("created user id is :", user_id)

  # get the data of the recent created user 
  get_response = api_request.get(url = f"/public/v2/users/{user_id}")
  assert get_response.status == 200 
  print("get the data of the created user", get_response.json())

  # Update complete user 
  update_response = api_request.put(url = f"/public/v2/users/{user_id}",
                                    data ={
                                      "name" : "Yadav suraj",
                                      "email" : "shivkumar@example.com",
                                      "gender": "Male",
                                      "status" : "active"
                                    })
  assert update_response.status == 200
  print("User updated successfully by using Put Request ", update_response.json())

# get all the users Data or Api request data 
  get_all_user_response = api_request.get(url = "/public/v2/users")
 
  assert get_all_user_response.status == 200 
  json_data1 = get_all_user_response.json()
  user_name = json_data1[0]["name"] 
  print("there is an created user ", json_data1)

# Update specific user field 

  update_specific_response = api_request.patch(url = f"/public/v2/users/{user_id}",
                                            data = {
                                              "name" : "Raja Raghu singh"
                                            })
  assert update_specific_response.status == 200 
  print("user update successfully by using Patch Request ", update_specific_response.json()) 
  print("get all user data from get api", get_all_user_response.json() )







  