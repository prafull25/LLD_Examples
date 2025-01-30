from Group.models import Group
from User.models import User
from typing import List


class GroupController:

    def __init__(self):
        self.group_list : List[Group] = []

    def create_new_group(self,group_name:Group,created_by: User):
        group = Group()
        group.add_member(created_by)
        group.set_group_name(group_name)
        self.group_list.append(group)

    def get_group_by_group_id(self, group_id):
        for group in self.group_list:
            if group.get_group_id() == group_id:
                return group
        return None