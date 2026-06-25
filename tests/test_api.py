from api.user_api import UserAPI
from api.payload import (create_user_payload, update_user_payload, patch_payload )


def test_api_flow(playwright):
    user_api = UserAPI(playwright)

#POST API Request
    create_response = user_api.create_user(data = create_user_payload())
    assert create_response.status ==201
    user_id = create_response.json()["id"]
    print( "Create user ID  is ",user_id)

# GET API Request
    get_response = user_api.get_user(user_id)
    assert get_response.status == 200
    print("Get the data of the created user ", get_response.json())

# PUT API Request 
    update_response = user_api.update_user(user_id , data = update_user_payload() ) 
    assert update_response.status == 200
    print("User updated successfully by using Put Request ", update_response.json())

# PATCH API Request
    patch_data = patch_payload() 
    patch_response = user_api.patch_user(user_id , data = patch_data)

    assert patch_response.status == 200
    # validate name from response matches payload
    assert patch_response.json()["name"]== patch_data["name"]

#DELETE API Request 
    delete_response = user_api.delete_user(user_id)
    assert delete_response.status == 204