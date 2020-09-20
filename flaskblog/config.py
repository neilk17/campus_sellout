import os


class Config:
    SECRET_KEY = '624ab6d55816ceac69613548d9f4dcc9'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'campus.sellout@gmail.com'
    MAIL_PASSWORD = """8{@.dLzb[>]GL~=3'.hF'}KA_LfBqjVQBWd's8J!KJ3~k:*SpnxK/YW:-)vx"""

n = Config
