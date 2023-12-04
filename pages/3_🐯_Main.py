import streamlit as st
import mysql.connector
from mysql.connector import Error

# Define a SessionState class to persist the connection state
class SessionState:
    def __init__(self):
        self.conn = None
        self.data_inserted = False
        self.data_deleted = False

# Function to connect to the database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gautam@10",
            database="WildlifeConservationDB"
        )
        return conn
    except mysql.connector.Error as e:
        st.error(f"Error connecting to the database: {e}")
    return None

def insert_data(conn):
    # Creating a cursor object
    cursor = conn.cursor()

    # Get user input for the table selection
    selected_table = st.selectbox("Select Table to Insert Data Into", ["animal_species", "individual_animals", "conservation_organizations", "conservation_projects", "staff_members", "donations"])

    if selected_table == "animal_species":
        species_name = st.text_input("Enter Species Name:")
        scientific_name = st.text_input("Enter Scientific Name:")
        category = st.text_input("Enter Category:")
        conservation_status = st.text_input("Enter Conservation Status:")


        if st.button("Insert Animal Species"):
            animal_species_query = """
            INSERT INTO animal_species
            (species_name, scientific_name, category, conservation_status)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(animal_species_query, (species_name, scientific_name, category, conservation_status))
            conn.commit()
            st.success("Animal Species data inserted successfully.")

    elif selected_table == "individual_animals":
        # Insert data into the individual_animals table
        species_id = st.text_input("Enter Species ID:")
        name = st.text_input("Enter Animal Name:")
        gender = st.selectbox("Select Gender:", ["Male", "Female", "Unknown"])
        birth_date = st.text_input("Enter Birthdate (YYYY-MM-DD):")
        arrival_date = st.text_input("Enter Arrival Date (YYYY-MM-DD):")


        if st.button("Insert Individual Animal"):
            individual_animals_query = """
            INSERT INTO individual_animals
            (species_id, name, gender, birth_date, arrival_date)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(individual_animals_query, (species_id, name, gender,birth_date, arrival_date))
            conn.commit()
            st.success("Individual Animal data inserted successfully.")

    elif selected_table == "conservation_organizations":
        # Insert data into the conservation_organizations table
        org_name = st.text_input("Enter Organization Name:")
        contact_person = st.text_input("Enter Contact Person:")
        contact_email = st.text_input("Enter Contact Email:")
        contact_phone = st.text_input("Enter Contact Phone:")

        if st.button("Insert Conservation Organization"):
            conservation_org_query = """
            INSERT INTO conservation_organizations
            (org_name, contact_person, contact_email, contact_phone)
            VALUES (%s, %s, %s, %s)
            """

            cursor.execute(conservation_org_query, (org_name, contact_person, contact_email, contact_phone))
            conn.commit()
            st.success("Conservation Organization data inserted successfully.")

    elif selected_table == "conservation_projects":
        # Insert data into the conservation_projects table
        ProjectID = st.text_input("Enter Project ID:")
        project_name = st.text_input("Enter Project Name:")
        start_date = st.text_input("Enter Start Date (YYYY-MM-DD):")
        end_date = st.text_input("Enter End Date (YYYY-MM-DD):")
        budget = st.text_input("Enter Project Budget:")
        org_id = st.text_input("Enter Organization ID:")

        if st.button("Insert Conservation Project"):
            conservation_proj_query = """
                INSERT INTO conservation_projects
                (ProjectID,project_name, start_date, end_date, budget, org_id)
                VALUES (%s, %s, %s, %s, %s, %s)
                """

            cursor.execute(conservation_proj_query, (ProjectID, project_name, start_date, end_date, budget, org_id))
            conn.commit()
            st.success("Conservation Project data inserted successfully.")

    elif selected_table == "staff_members":
        # Insert data into the staff_members table
        vet_id = st.text_input("Enter Vet id:")
        vet_name = st.text_input("Enter Vet Name:")
        specialization = st.text_input("Enter Specialization:")
        contact_email = st.text_input("Enter Contact Email:")
        contact_phone = st.text_input("Enter Contact Phone:")

        if st.button("Insert Staff Member"):
            staff_members_query = """
                INSERT INTO staff_members
                (vet_id,vet_name,specialization,contact_email,contact_phone)
                VALUES (%s, %s, %s, %s, %s)
                """

            cursor.execute(staff_members_query, (vet_id, vet_name, specialization, contact_email, contact_phone))
            conn.commit()
            st.success("Staff Member data inserted successfully.")

    elif selected_table == "donations":
        # Insert data into the donations table
        donation_id = st.text_input("Enter Donation id:")
        donor_name = st.text_input("Enter Donor Name:")
        amount = st.text_input("Enter Donation Amount:")
        donation_date = st.text_input("Enter Donation Date (YYYY-MM-DD):")
        proj_id = st.text_input("Enter Project ID (referencing Conservation Projects):")

        if st.button("Insert Donation"):
            donations_query = """
                INSERT INTO donations
                (DonationID, DonorName, Amount, DonationDate)
                VALUES (%s, %s, %s, %s)
                """

            cursor.execute(donations_query, (donation_id,donor_name, amount, donation_date))
            conn.commit()
            st.success("Donation data inserted successfully.")


    # Commit the transaction
    conn.commit()

    cursor.close()


def delete_data(conn):
    # Creating a cursor object
    cursor = conn.cursor()

    # Get user input for the table selection
    selected_table = st.selectbox("Select Table to Delete Data From", ["animal_species", "individual_animals", "conservation_organizations", "conservation_projects", "staff_members", "donations"])

    if selected_table == "animal_species":
        species_name = st.text_input("Enter Species Name to Delete:")
        if st.button("Delete Animal Species"):
            delete_query = "DELETE FROM animal_species WHERE species_name = %s"
            cursor.execute(delete_query, (species_name,))
            conn.commit()
            st.success(f"Animal Species data with species name {species_name} deleted successfully.")

    elif selected_table == "individual_animals":
        animal_id = st.text_input("Enter Animal ID to Delete:")
        if st.button("Delete Individual Animal"):
            delete_query = "DELETE FROM individual_animals WHERE animal_id = %s"
            cursor.execute(delete_query, (animal_id,))
            conn.commit()
            st.success(f"Individual Animal data with animal ID {animal_id} deleted successfully.")

    elif selected_table == "conservation_organizations":
        org_name = st.text_input("Enter Organization Name to Delete:")
        if st.button("Delete Conservation Organization"):
            delete_query = "DELETE FROM conservation_organizations WHERE org_name = %s"
            cursor.execute(delete_query, (org_name,))
            conn.commit()
            st.success(f"Conservation Organization data with organization name {org_name} deleted successfully.")

    elif selected_table == "conservation_projects":
        project_id = st.text_input("Enter Project ID to Delete:")
        if st.button("Delete Conservation Project"):
            delete_query = "DELETE FROM conservation_projects WHERE ProjectID = %s"
            cursor.execute(delete_query, (project_id,))
            conn.commit()
            st.success(f"Conservation Project data with project ID {project_id} deleted successfully.")

    elif selected_table == "staff_members":
        vet_id = st.text_input("Enter Vet ID to Delete:")
        if st.button("Delete Staff Member"):
            delete_query = "DELETE FROM staff_members WHERE vet_id = %s"
            cursor.execute(delete_query, (vet_id,))
            conn.commit()
            st.success(f"Staff Member data with vet ID {vet_id} deleted successfully.")

    elif selected_table == "donations":
        donation_id = st.text_input("Enter Donation ID to Delete:")
        if st.button("Delete Donation"):
            delete_query = "DELETE FROM donations WHERE DonationID = %s"
            cursor.execute(delete_query, (donation_id,))
            conn.commit()
            st.success(f"Donation data with donation ID {donation_id} deleted successfully.")

    # Commit the transaction
    conn.commit()

    cursor.close()



def view_entity(conn, entity_name):
    cursor = conn.cursor(dictionary=True)

    # Customize SQL query based on the selected entity
    if entity_name == "Animal Species":
        cursor.execute("SELECT * FROM Animal_Species")
        data = cursor.fetchall()
        st.write("Animal Species:")
        st.table(data)
    elif entity_name == "Individual Animals":
        cursor.execute("SELECT * FROM Individual_Animals")
        data = cursor.fetchall()
        st.write("Individual Animals:")
        st.table(data)
    elif entity_name == "Conservation Organizations":
        cursor.execute("SELECT * FROM ConservationOrganizations")
        data = cursor.fetchall()
        st.write("Conservation Organizations:")
        st.table(data)
    elif entity_name == "Conservation Projects":
        cursor.execute("SELECT * FROM ConservationProjects")
        data = cursor.fetchall()
        st.write("Conservation Projects:")
        st.table(data)
    elif entity_name == "Staff Members":
        cursor.execute("SELECT * FROM Staff_Members")
        data = cursor.fetchall()
        st.write("Staff Members:")
        st.table(data)
    elif entity_name == "Donations":
        cursor.execute("SELECT * FROM Donations")
        data = cursor.fetchall()
        st.write("Donations:")
        st.table(data)


    cursor.close()

def main():
    st.set_page_config(page_title="Wildlife Conservation DBMS", page_icon="🌿")
    st.title("Wildlife Conservation DBMS")

    # Initialize or retrieve session state
    session_state = SessionState()

    if not session_state.conn:
        # If connection is not established, connect to the database
        session_state.conn = connect_to_database()

    if session_state.conn:

        menu_options = ["Insert Data", "Delete Data", "View Entities"]
        choice = st.select_slider("Select an option", menu_options)

        if choice == "Insert Data":
            if not session_state.data_inserted:
                insert_data(session_state.conn)
                session_state.data_inserted = True
            else:
                st.info("Data has already been inserted.")
        elif choice == "Delete Data":
            if not session_state.data_deleted:
                delete_data(session_state.conn)
                session_state.data_deleted = True
            else:
                st.info("Data has already been deleted.")

        elif choice == "View Entities":
            entity_name = st.selectbox("Select an entity to view",["Animal Species", "Individual Animals", "Conservation Organizations","Conservation Projects","Staff Members","Donations"])
            view_entity(session_state.conn, entity_name)

    # Close the connection when the Streamlit app is closed
    if session_state.conn:
        session_state.conn.close()

if __name__ == "__main__":
    main()

