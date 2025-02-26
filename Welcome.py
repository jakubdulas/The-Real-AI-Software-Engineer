import streamlit as st
import os


st.set_page_config(page_title="Multi-Agent AI System", page_icon="🤖", layout="wide")
st.session_state.app_dir = os.path.dirname(os.path.abspath(__file__))

st.session_state.selected_directory = None

st.title("🤖 Multi-Agent AI System for Software Development")
st.subheader("Automating Coding, Debugging, and Documentation with AI")

st.markdown(
    """
    The **Multi-Agent AI System** is designed to enhance software development efficiency by leveraging AI agents for
    **code generation, debugging, testing, and documentation automation**. This project provides students with hands-on
    experience in AI-driven software development, fostering skills in programming, machine learning, and IT project management.
    """
)

st.header("🎯 Project Objectives")
st.markdown(
    """
    - **Automate programming tasks** to minimize manual effort in coding.
    - **Enhance debugging and documentation** through AI-powered tools.
    - **Improve project management** by organizing system structures effectively.
    """
)

st.header("🛠 System Functionalities")
st.markdown(
    """
    - **Code Generation**: AI-driven code writing based on user input.
    - **Debugging & Testing**: Automated issue detection and resolution.
    - **Documentation Automation**: AI-generated project documentation.
    - **Information Retrieval**: Intelligent search for relevant documentation.
    - **Project Management**: Organizing project files and metadata efficiently.
    """
)

st.header("🎓 Learning Outcomes")
st.markdown(
    """
    By participating in this project, students will develop:
    - **AI Integration Skills**: Using Large Language Models (LLMs) & RAG techniques.
    - **Software Development Expertise**: Hands-on coding, debugging, and testing.
    - **Project Management Capabilities**: Organizing complex IT projects efficiently.
    - **Technical Documentation Skills**: Writing structured and comprehensive documentation.
    """
)
