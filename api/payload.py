import uuid
def create_user_payload():

    unique_id = str(uuid.uuid4())[:6]

    return {
        "name": "Sachin Yadav",
        "email": f"sachin{unique_id}@gmail.com",
        "gender": "male",
        "status": "active"
    }


def update_user_payload():

    unique_id = str(uuid.uuid4())[:6]

    return {
        "name": f"Updated Sachin{unique_id}",
        "email": f"updated{unique_id}@gmail.com",
        "gender": "male",
        "status": "active"
    }


def patch_payload():
    unique_id = str(uuid.uuid4())[:6]

    return {
        "name": f"User{unique_id}"
    }
