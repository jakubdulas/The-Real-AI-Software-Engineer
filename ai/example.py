from langchain_openai import ChatOpenAI
import os
import subprocess
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0,
)


def generate_code(prompt, dir: str):
    code = llm.invoke(
        [
            (
                "system",
                "Your task is to generate python code. Ther response should be only code that I can copy and paste and run, NOT MARKDOWN. Start response with code not python'''. Genreate code based on the users request. ",
            ),
            ("human", prompt),
        ]
    ).content

    file_path = os.path.join(dir, "generated_script.py")

    # Save the generated code to a Python file
    with open(file_path, "w") as file:
        file.write(code)

    # Execute the generated Python code
    try:
        result = subprocess.run(
            ["python3", file_path], capture_output=True, text=True, check=True
        )
        return result.stdout  # Return the output of the execution
    except subprocess.CalledProcessError as e:
        return f"Error during execution: {e.stderr}"


if __name__ == "__main__":
    prompt = "Create a Python function that prints 'Hello, world!'"
    project_dir = "./"

    output = generate_code(prompt, project_dir)
    print("Generated Code Output:")
    print(output)
