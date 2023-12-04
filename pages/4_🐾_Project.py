import streamlit as st
import mysql.connector

# Function to call the stored procedure and retrieve project details
def get_project_details(project_id):
    connection = None  # Initialize connection to None
    cursor = None  # Initialize cursor to None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gautam@10",
            database="WildlifeConservationDB"
        )

        cursor = connection.cursor(dictionary=True)

        # Call the stored procedure
        cursor.callproc('GetProjectDetails', (project_id,))

        # Fetch the result
        result = next(cursor.stored_results())

        # Display the result
        project_details = result.fetchone()
        return project_details

    except mysql.connector.Error as err:
        st.error(f"Error connecting to the database: {err}")
        return None

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

# Streamlit UI
def main():
    st.title("Wildlife Conservation Project Details")


    project_id = st.text_input("Enter Project_ID to get details:")
    project_details = get_project_details(project_id)

    if project_details:
        st.subheader("Project Details:")
        st.write(f"Project ID: {project_details['project_id']}")
        st.write(f"Project Name: {project_details['project_name']}")
        st.write(f"Start Date: {project_details['start_date']}")
        st.write(f"End Date: {project_details['end_date']}")
        st.write(f"Budget: {project_details['budget']}")
        st.write(f"Organization Name: {project_details['organization_name']}")
        st.write(f"Staff Members: {project_details['staff_members']}")
    else:
        st.error("Failed to retrieve project details.")

if __name__ == "__main__":
    main()
