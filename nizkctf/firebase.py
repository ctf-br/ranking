import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


if (os.environ.get('SERVICE_ACCOUNT')):
    # Fetch the service account key JSON file contents
    cred = credentials.Certificate(os.environ.get('SERVICE_ACCOUNT'))

    default_app = firebase_admin.initialize_app(cred, {
        'databaseURL' : os.environ.get('DATABASE_URL')
    })


def saveToFirebase(path, payload):
    if (os.environ.get('SERVICE_ACCOUNT')):
        ref = db.reference(path)
        ref.set(payload)
