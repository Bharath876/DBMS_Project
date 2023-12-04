import streamlit as st
import base64

# Function to encode an image to base64
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Replace "path/to/your/image.jpg" with the actual path to your image file
img_path = "C:\sem 5\DBMS\Project/img.jpg"
img = get_img_as_base64(img_path)

# Define custom CSS for background image
page_bg_img = f"""
<style>
    .stApp {{
        background-image: url("data:image/png;base64,{img}");
        background-size: cover;
    }}
</style>
"""

# Set page configuration
st.set_page_config(page_title="Wildlife Conservation DBMS", page_icon="🌿")

# Apply the custom CSS to the app
st.markdown(page_bg_img, unsafe_allow_html=True)

# Rest of your script
st.title("Wildlife Conservation DBMS")
st.write("Our Wildlife Conservation Database Management System is a comprehensive platform dedicated to the conservation and preservation of wildlife. This innovative system allows users to efficiently manage and organize data related to animal species, individual animals, conservation organizations, projects, staff members, and donations.")
