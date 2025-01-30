from typing import List, Optional, Dict
from User.models import User

class UserController:
    def __init__(self):
        self.user_map: Dict[str, User] = {}

    def add_user(self,user:User)->None:
        self.user_map[user.get_user_id()] = user

    def get_user_by_user_id(self,user_id:str)->Optional[User]:
        return self.user_map.get(user_id, None)
    
    def get_all_users(self)->List[User]:
        return list(self.user_map.values())