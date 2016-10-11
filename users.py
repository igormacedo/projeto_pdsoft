from flask_login import UserMixin

class User(UserMixin):

    def __init__(self, login, password, picture):
        self.id = login
        self.password = password
        self.picture = picture

    def __repr__(self):
        return "%s/%s" % (self.login, self.password)
