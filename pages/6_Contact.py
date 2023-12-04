import streamlit as st


def contact_us():
    st.title("Contact Us")

    st.write("Have questions or suggestions? Reach out to us!")

    # Input fields for user information
    name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    message = st.text_area("Your Message:")

    # Submit button
    if st.button("Submit"):
        # You can add your logic here to handle the form submission
        st.success("Thank you for reaching out! We will get back to you soon.")

    st.write("\n\n---\n\n")
    st.write("Connect with us on social media:")

    # Links to social media
    st.markdown("[Twitter](https://twitter.com/YourTwitterHandle)")
    st.markdown("[Facebook](https://facebook.com/YourFacebookPage)")
    st.markdown("[Instagram](https://instagram.com/YourInstagramProfile)")


if __name__ == "__main__":
    contact_us()
