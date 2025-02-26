import streamlit as st
import os
from ai.example import generate_code

if (
    not "selected_directory" in st.session_state
    or not st.session_state["selected_directory"]
):
    st.title("🤖 Multi-Agent AI System for Software Development")
    st.header("📂 Select a Project Directory")

    folder_path = st.text_input("Enter the path to your project folder:")

    if st.button("Select Folder"):
        if os.path.isdir(folder_path):
            if (
                os.path.commonpath([folder_path, st.session_state.app_dir])
                == st.session_state.app_dir
            ):
                if not os.listdir(folder_path):
                    os.makedirs(os.path.join(folder_path, ".project"))
                    st.success(
                        f"Selected directory is empty. Created '.project' directory at {folder_path}."
                    )
                    st.session_state.selected_directory = folder_path
                    st.rerun()
                elif ".project" in os.listdir(folder_path):
                    st.session_state.selected_directory = folder_path
                    st.success(f"Selected project directory: {folder_path}.")
                    st.rerun()
                else:
                    st.error(
                        "Please select an empty directory or a directory that already contains a '.project' directory."
                    )
            else:
                st.error(
                    "The selected directory must be inside the Streamlit app directory or its subdirectories."
                )
        else:
            st.error("Invalid directory path. Please enter a valid folder path.")
else:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner(text="Generating..."):
            generate_code(prompt, st.session_state.selected_directory)

        response = f"Done! You can find it in selected directory"
        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})
