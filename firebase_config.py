import streamlit as st
import firebase_admin
from firebase_admin import credentials, db
import json

# Load Firebase credentials from Streamlit secrets
firebase_creds = st.secrets["firebase"]
cred = credentials.Certificate(firebase_creds)

# Initialize Firebase
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://YOUR_PROJECT_ID.firebaseio.com/'
})

ref = db.reference('/')
