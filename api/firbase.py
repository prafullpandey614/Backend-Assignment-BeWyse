import firebase_admin
from firebase_admin import credentials


def init_fire():
    if not firebase_admin._apps:
        cred = credentials.Certificate('bewyse-dd11e-firebase-adminsdk-1od1b-d23f4d5655.json')
        firebase_admin.initialize_app(cred)
