
import streamlit as st
import base64

@st.cache_data
def get_base64(file_path):
    with open(file_path, 'rb') as file:
        file_data = file.read()
    return base64.b64encode(file_data).decode()


@st.cache_data
def set_background(image_file: str) -> None:
    """Set the background of the Streamlit app to the specified image file.

    Args:
        image_file (str): The file path of the image to use as the background.
    """

    with open(image_file, "rb") as file:
        image_data = base64.b64encode(file.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background: url(data:image/png;base64,{image_data});
        background-repeat: no-repeat;
        background-position: right 50% bottom 55%;
        background-size: cover;
        background-attachment: scroll;
    }}
    </style>
    """

    st.markdown(css, unsafe_allow_html=True)


# st.markdown(
#     f"""
#      <style>
#      .stApp {{
#          background: url(data:image/png;base64,{base64.b64encode(open("./assets/st_bg_img.png", "rb").read()).decode()});
#          background-repeat: no-repeat;
#          background-position: right 50% bottom 95%;
#          background-size: contain;
#          background-attachment: scroll;
#      }}
#      </style>
#      """,
#     unsafe_allow_html=True,
# )