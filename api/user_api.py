from api.api_client import APIClient

class UserAPI(APIClient):

    def create_user(self, data):
        return self.request_context.post(
            "/public/v2/users",
            data=data
        )

    def get_user(self, user_id):
        return self.request_context.get(
            f"/public/v2/users/{user_id}"
        )

    def update_user(self, user_id, data):
        return self.request_context.put(
            f"/public/v2/users/{user_id}",
            data=data
        )

    def patch_user(self, user_id, data):
        return self.request_context.patch(
            f"/public/v2/users/{user_id}",
            data=data
        )

    def delete_user(self, user_id):
        return self.request_context.delete(
            f"/public/v2/users/{user_id}"
        )
