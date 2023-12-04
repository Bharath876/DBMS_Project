import streamlit as st
import mysql.connector
import subprocess

# Define a SessionState class to persist the login state
class SessionState:
    def __init__(self):
        self.is_logged_in = False

# Initialize SessionState globally
session_state = SessionState()

# Function to check user credentials
def authenticate(username, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gautam@10",
            database="WildlifeConservationDB"
        )

        cursor = connection.cursor()
        query = f"SELECT * FROM Users WHERE username = '{username}' AND pswd = '{password}'"
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

# Streamlit UI for login
def login():
    st.title("Wildlife Conservation DBMS - Login")

    # Create a database connection for login
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="gautam@10",
        database="WildlifeConservationDB"
    )

    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    if st.button("Login"):
        user_data = authenticate(username, password)
        if user_data:
            st.experimental_set_query_params(login_status='success')
            session_state.is_logged_in = True
        else:
            st.error("Invalid username or password. Please try again.")

    # Close the database connection for login when Streamlit app is closed
    connection.close()

# Main app page
def main_app():
    st.title("Wildlife Conservation DBMS - Login Page")
    st.write("Welcome to the login app page!")

# Streamlit app
def main():
    st.set_page_config(page_title="Login App", page_icon="🔒")

    # Login
    login()

    # Redirect after login
    if session_state.is_logged_in:
        st.markdown("[Go to Admin Page](main.py)")
        subprocess.run(["python", "main.py"])

if __name__ == "__main__":
    main()
