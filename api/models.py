class User:
    def __init__(self, **kwargs):
        self.user_id = kwargs["user_id"]
        self.first_name = kwargs["first_name"]
        self.last_name = kwargs["last_name"]
        self.other_names = kwargs["other_names"]
        self.email = kwargs["email"]
        self.phone_number = kwargs["phone_number"]
        self.password = (kwargs["password"])
        self.user_name = kwargs["user_name"]
        self.registered = datetime.date.today()
        self.admin = kwargs["admin"]
        user_id += 1

    def user_details(self):
        return {
            "userId": self.user_id,
            "firstname": self.first_name,
            "lastname": self.last_name,
            "othernames": self.other_names,
            "email": self.email,
            "phoneNumber": self.phone_number,
            "password": self.password,
            "userName": self.user_name,
            "registered": self.registered,
            "Admin": self.admin
        }


class RedFlagRecord:
    def __init__(self, **kwargs):

        self.red_flag_id = kwargs["red_flag_id"],
        self.createdOn = kwargs["createdOn"],
        self.createdBy = kwargs["createdBy"],
        self.incident_type = kwargs["incident_type"],
        self.location = kwargs["location"],
        self.status = kwargs["draft"],
        self.images = kwargs["images"],
        self.videos = kwargs["videos"],
        self.comment = kwargs["comment"]

    def redflag_details(self):
        return {
            "redflagId": self.red_flag_id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "incidentType": self.incident_type,
            "location": self.location,
            "status": self.status,
            "images": self.images,
            "videos": self.videos,
            "comment": self.comment
        }
