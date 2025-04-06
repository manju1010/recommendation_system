from database.schema import get_user_behavior

class CustomerAgent:
    def __init__(self):
        pass

    def get_profile(self, user_id):
        return {
            "user_id": user_id,
            "age": 25,
            "gender": "F",
            "history": get_user_behavior(user_id)
        }
