import streamlit as st
from utils.firebase_config import ref

st.title("Firebase CRUD App with Streamlit")

# --- CREATE DATA ---
st.header("Add New User")
name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=150, step=1)
city = st.text_input("City")
if st.button("Add User"):
    if name and city:
        ref.child('users').push({'name': name, 'age': age, 'city': city})
        st.success(f"User {name} added successfully!")
    else:
        st.error("Please enter name and city.")

# --- READ DATA ---
st.header("All Users")
users = ref.child('users').get()
if users:
    for key, value in users.items():
        st.write(f"ID: {key} | Name: {value['name']} | Age: {value['age']} | City: {value['city']}")
else:
    st.info("No users found.")

# --- UPDATE DATA ---
st.header("Update First User's City")
new_city = st.text_input("New City for First User")
if st.button("Update First User"):
    if users and new_city:
        first_key = list(users.keys())[0]
        ref.child('users').child(first_key).update({'city': new_city})
        st.success("User city updated successfully!")
    else:
        st.error("No users to update or enter a new city.")

# --- DELETE DATA ---
st.header("Delete First User")
if st.button("Delete First User"):
    if users:
        first_key = list(users.keys())[0]
        ref.child('users').child(first_key).delete()
        st.warning("User deleted successfully!")
    else:
        st.error("No users to delete.")
