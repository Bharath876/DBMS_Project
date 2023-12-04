import streamlit as st
import mysql.connector

# Function to execute the MySQL update operation and return the appointment details
def update_staff_for_endangered_animals():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="gautam@10",
            database="WildlifeConservationDB"
        )

        # Create a MySQL cursor
        cursor = connection.cursor()

        # MySQL update query
        update_query = """
        UPDATE Individual_Animals ia
        JOIN Animal_Species asp ON ia.species_id = asp.species_id
        JOIN Staff_Members sm ON ia.vet_id = sm.vet_id

        SET ia.vet_id = sm.vet_id

        WHERE ia.weight < asp.weight
            AND asp.conservation_status = 'Endangered'
            AND ia.vet_id IS NULL
        ORDER BY RAND() LIMIT 1
        """

        # Execute the update query
        cursor.execute(update_query)

        # Commit changes
        connection.commit()

        # Fetch the updated appointment details
        cursor.execute("""
            SELECT ia.animal_id, ia.name AS animal_name, sm.vet_name, asp.species_name
            FROM Individual_Animals ia
            JOIN Staff_Members sm ON ia.vet_id = sm.vet_id
            JOIN Animal_Species asp ON ia.species_id = asp.species_id
            WHERE ia.vet_id IS NOT NULL
        """)

        appointment_details = cursor.fetchall()

        return appointment_details

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


# Streamlit UI
st.title("Wildlife Conservation Staff Assignment")
st.write("Click the button below to assign staff to endangered animals based on their weight and species criteria.")

# Button to trigger the update operation
if st.button("Assign Staff"):
    if appointment_details:
        st.success("Staff assigned successfully. Appointment details:")
        for appointment in appointment_details:
            st.info(
                f"Animal ID: {appointment['animal_id']}, "
                f"Animal Name: {appointment['animal_name']}, "
                f"Vet: {appointment['vet_name']},"
                f"Species: {appointment['species_name']}")
    else:
        st.warning("No appointments were made.")




