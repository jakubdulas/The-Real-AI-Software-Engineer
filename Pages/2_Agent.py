import streamlit as st
import os
from ai.agents.coder.agent import Coder
from ai.tot.v1.graph import graph as tot_v1
from ai.tot.v2.graph import graph as tot_v2
from ai.cot.graph import cot_graph
from ai.agents.system.graph import create_system


def get_agent():
    # reasoning = tot_v1
    # match (st.session_state.reasoning):
    #     case "tot v1":
    #         reasoning = tot_v1
    #     case "tot v2":
    #         reasoning = tot_v2
    #     case "cot":
    #         reasoning = cot_graph

    st.session_state.coder = create_system(
        st.session_state.selected_directory, st.session_state.llm
    )


if (
    not "selected_directory" in st.session_state
    or not st.session_state["selected_directory"]
):
    st.title("🤖 Multi-Agent AI System for Software Development")

    st.header("🤖 Configure agent")
    st.session_state.llm = st.selectbox(
        "Select LLM",
        ("gpt-4o-mini", "gpt-4o", "gpt-4.1-nano", "gpt-4.1-mini", "gpt-4.1"),
    )
    # st.session_state.reasoning = st.selectbox(
    #     "Select Reasoning", ("tot v1", "tot v2", "cot")
    # )
    # st.session_state.algorithm = st.selectbox("Select Algorithm", ("sync", "linear"))

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

    if "coder" not in st.session_state:
        get_agent()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.spinner(text="Generating..."):
            output = st.session_state.coder.invoke(
                {"project_scope": prompt},
                config={"configurable": {"thread_id": 3}, "recursion_limit": 100},
            )

        if output["researcher_messages"]:
            with st.chat_message("assistant"):
                st.markdown(output["researcher_messages"][-1].content)
        if output["coder_messages"]:
            with st.chat_message("assistant"):
                st.markdown(output["coder_messages"][-1].content)
        if output["documenter_messages"]:
            with st.chat_message("assistant"):
                st.markdown(output["documenter_messages"][-1].content)

        if output["researcher_messages"]:
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": output["researcher_messages"][-1].content,
                }
            )
        if output["coder_messages"]:
            st.session_state.messages.append(
                {"role": "assistant", "content": output["coder_messages"][-1].content}
            )

        if output["researcher_messages"]:
            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": output["documenter_messages"][-1].content,
                }
            )
