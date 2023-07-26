# facade/service_facade.py

from api.services.user_group_service import UserGroupService


class ServiceFacade:
    def __init__(self):
        self.usergroupsvc = UserGroupService()

    def create_record(self, dto_object):
        return self.usergroupsvc.create_group(dto_object)

    def update_record(self, dto_object):
        return self.usergroupsvc.update_group(dto_object)
