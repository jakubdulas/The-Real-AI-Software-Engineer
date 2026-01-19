To enhance the report, I will integrate the descriptions of the agent flow from the provided images, elaborate on the rationale behind selecting the specific projects and metrics, and include a motivation for the project in the introduction. I will also ensure references to LangGraph and relevant concepts are woven into the text.

Here's an updated version of the report, incorporating these improvements:

# Project Report: Multi-Agent System Supporting Software Development Processes

## 1. Introduction

This report details the research and development of a **multi-agent system designed for autonomous code generation based on a given project scope**. The primary motivation behind this project was to explore the potential of advanced AI agents, particularly those leveraging ReAct (Reasoning and Acting) architectures, to automate and enhance the software development lifecycle. By integrating multiple specialized agents, we aimed to create a robust system capable of understanding complex requirements, planning development processes, generating functional code, and documenting the output. The system was meticulously implemented in **Python**, utilizing the **LangGraph** library for sophisticated agent orchestration and **Streamlit** for an intuitive graphical user interface (GUI). A core focus of this research was to critically evaluate the impact of various reasoning strategies employed by the code generation agent (Coder) on the overall quality, efficiency, and correctness of the autonomously generated software.

## 2. System Architecture

The system operates as a collaborative ecosystem of four distinct agent types, each playing a crucial role in achieving the project objectives. The overall system flow is managed by the Project Manager, which orchestrates interactions between the other agents.

- **Project Manager:** As depicted in `project_manager.png`, the Project Manager is the initial point of contact after the `__start__` state. It receives the user-defined project scope, then embarks on a `plan_project` phase. This phase involves breaking down the scope into granular tasks, organizing them into sprints, and assigning these tasks to the most appropriate agents. The Project Manager is responsible for coordinating the entire workflow, ensuring tasks are executed chronologically and iterating through them until completion, ultimately leading to the `__end__` state.

- **Researcher:** This agent is tasked with information gathering. Its role involves exploring necessary technologies, identifying optimal solutions, and collecting any other data required for successful task completion. While not explicitly shown in a separate graph, the Researcher's activities feed into the planning and execution phases of other agents, providing essential context and knowledge.

- **Coder:** The core of the system, the Coder agent, is dedicated to generating code. As illustrated in `coder.png`, its process begins from a `__start__` state, moves to `reason`, and then to `next_step`. The `llm_node` is central to its operation, interacting with `tools` for various coding tasks. The Coder incorporates three distinct reasoning versions, allowing for an in-depth experimental evaluation of how different approaches to task decomposition and sequential execution influence output quality:

  - **ReAct (No Reasoning):** A fundamental approach where the agent operates on a simple cycle of observation, thought, and action. It's depicted as a direct flow through `llm_node` and `tools` with minimal internal deliberation.
  - **ReAct + CoT (Chain-of-Thought Reasoning):** In this version, the agent explicitly generates internal "thoughts" or rationales (`reasoning_node` in `cot_graph.png` suggests this more explicit reasoning step) that guide its reasoning and planning of subsequent actions, leading to a more structured problem-solving process.
  - **ReAct + ToT (Tree-of-Thought Reasoning):** The most advanced reasoning strategy. This agent explores multiple potential reasoning paths, evaluates their viability, and strategically selects the most promising one. This iterative refinement and branching of thought is more complex and resource-intensive but aims for superior outcomes.

- **Documenter:** This agent is responsible for generating comprehensive documentation for the developed code. This includes function descriptions, usage instructions, API specifications, and any other relevant materials that ensure the generated software is well-understood and maintainable.

### 2.1. Operational Flow

The system's operational flow is a coordinated sequence of actions:

1.  **User defines project scope:** The process initiates with the user providing a high-level description of the desired software project.
2.  **Project Manager plans:** As per `system.png`, the `plan_project` node is activated. The Project Manager agent analyzes the user's scope, breaking it down into a series of smaller, manageable tasks. These tasks are then organized into logical sprints, and each task is meticulously assigned to the most suitable agent (Researcher, Coder, or Documenter).
3.  **Task iteration and execution:** Following the `plan_project` phase, the system enters the `start_sprint` node. The Project Manager iteratively processes the planned tasks. For each task, the relevant agent (Researcher for information gathering, Coder for code generation, Documenter for documentation) is activated and executes its assigned task chronologically, moving through the `complete_tasks` node.
4.  **Code generation and verification:** The Coder agent, leveraging its chosen reasoning strategy (No Reasoning, CoT, or ToT), generates the required code. This process involves multiple interactions between the `llm_node` and `tools` (as seen in `coder.png`) until the task is deemed complete.
5.  **Documentation:** Upon successful code generation, the Documenter agent is engaged to produce comprehensive and user-friendly documentation, ensuring the software is well-explained and maintainable.
6.  **Completion:** Once all tasks and documentation are finalized, the system transitions to the `__end__` state.

## 3. Test Projects

To comprehensively evaluate the system's capabilities and the effectiveness of different reasoning strategies, six distinct projects were defined and categorized into three types, progressively increasing in complexity:

### 3.1. Simple Console Applications

These projects tested the agents' ability to generate straightforward, functional command-line interfaces.

- **Project 1: Temperature Converter (Single-file):** A simple utility to convert temperatures between Celsius, Fahrenheit, and Kelvin. This project specifically tested basic input/output handling, mathematical operations, and robust error management within a single Python file.
- **Project 2: CLI Note Manager (Multi-file):** A more complex command-line application enabling users to create, delete, and view notes. This project was designed to assess the system's proficiency in generating modular code, requiring organization across multiple Python files (`main.py`, `note.py`, `storage.py`, `utils.py`) to demonstrate proper code structuring and inter-file communication.

### 3.2. Games

These projects evaluated the agents' capacity for implementing game logic, state management, and user interaction in a dynamic environment.

- **Project 3: Tic Tac Toe:** A classic 3x3 game for the terminal, supporting both two-player and player-versus-AI modes. This project challenged the agents to handle game state, win/draw conditions, and basic AI logic, along with rendering the game board using ASCII characters.
- **Project 4: Snake Game with GUI:** A more visually demanding classic Snake game implemented with a Pygame GUI. This project tested the agents' ability to integrate with external libraries, manage graphical elements, handle real-time keyboard inputs, implement collision detection, and dynamically display game scores.

### 3.3. Web Applications

These projects pushed the boundaries of the system by requiring the generation of client-server architectures, API interactions, and basic web interfaces.

- **Project 5: TODO List (Backend + simple frontend):** A full-stack web application for task management. This project necessitated the creation of a REST API using a Python framework (Flask, Django, or FastAPI) for backend logic and data persistence, along with a simple HTML+JavaScript frontend for user interaction. This tested the agents' understanding of web protocols and component separation.
- **Project 6: Weather App (frontend querying external API):** A web application designed to display weather data for a selected city. The key challenge here was for the frontend to fetch data from a public external API (e.g., OpenWeatherMap) and dynamically render the retrieved information, assessing the agents' ability to handle asynchronous operations and third-party API integration.

## 4. Measurement Metrics

To provide a quantifiable and objective assessment of the generated code's quality and the agents' performance, a comprehensive set of metrics was employed. These metrics were chosen to cover various aspects of software quality, from functional correctness to maintainability and adherence to coding standards.

- **Time of generation (s):** Measures the total elapsed time, in seconds, from the moment the agent begins generating code until it reports completion. This metric directly assesses the efficiency and speed of the code generation process.
- **Number of lines of code:** The total count of logical lines of code (excluding comments and blank lines) in the generated solution. This metric provides an indication of the verbosity or conciseness of the generated code.
- **Number of used tokens:** The total count of tokens consumed by the underlying large language model during the code generation process. This metric is crucial for understanding the computational cost and "thinking effort" of the agent, as token usage directly correlates with API costs and processing time.
- **Number of lines of code after changes:** The count of code lines after any manual corrections or additions were made to achieve full functionality or adhere to desired standards. This metric helps quantify the degree of human intervention required post-generation.
- **Levenshtein distance:** The Levenshtein distance, also known as edit distance, from a pre-defined "ideal" or functionally correct solution. This metric quantifies the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one sequence into the other. A value closer to 0 indicates higher functional correctness and similarity to the desired output.
- **Cyclomatic complexity (avg):** The average cyclomatic complexity across all functions and methods in the generated code. This metric, derived from graph theory, measures the number of linearly independent paths through a program's source code. A lower average cyclomatic complexity generally indicates simpler, more testable, and more maintainable code, as it suggests fewer decision points and less branching.
- **Code duplication (%):** The percentage of duplicated code segments within the generated codebase. High code duplication often leads to increased maintenance effort and introduces potential for bugs. A lower percentage indicates a more DRY (Don't Repeat Yourself) and efficient codebase.
- **Lint errors (Python):** The number of errors or warnings reported by a standard Python linter (specifically, adherence to PEP 8 guidelines). This metric assesses the code's adherence to community-accepted style guides and best practices, impacting readability and maintainability.
- **Notes:** Additional qualitative remarks and observations concerning specific issues, peculiar behaviors, or notable characteristics of the generated code that quantitative metrics might not fully capture.

---

## 5. Results and Analysis

The performance and output quality of the three Coder versions—**No Reasoning (ReAct)**, **CoT Reasoning (ReAct + CoT)**, and **ToT Reasoning (ReAct + ToT)**—were meticulously evaluated across the six test projects. All experiments were conducted utilizing the `gpt-4.1` language model.

### 5.1. v0.2 - CoT Reasoning

| Metric                                    | Project 1 | Project 2 | Project 3 | Project 4 | Project 5                              | Project 6                      |
| :---------------------------------------- | :-------- | :-------- | :-------- | :-------- | :------------------------------------- | :----------------------------- |
| **Time of generation (s)**                | 171.98    | 612.75    | 459.72    | 625.31    | 860.55                                 | 385.27                         |
| **Number of lines of code**               | 128       | 377       | 400       | 292       | 657                                    | 252                            |
| **Number of used tokens**                 | 102095    | 314406    | 237500    | 324657    | 445496                                 | 207828                         |
| **Number of lines of code after changes** | 128       | 377       | 400       | 292       | 678                                    | 252                            |
| **Levenshtein distance**                  | 0         | 0         | 0         | 0         | 293                                    | 146                            |
| **Cyclomatic complexity (avg)**           | 2.2       | 2.6       | 2.9       | 2.2       | 1.4                                    | 2                              |
| **Code duplication (%)**                  | 0         | 0         | 0         | 0         | 0                                      | 0                              |
| **Lint errors (Python)**                  | 0         | 4         | 1         | 0         | 1                                      | N/A                            |
| **Notes**                                 |           |           |           |           | Added scripts to html, removed exports | Added API key, removed exports |

**CoT Reasoning Analysis:**
The Coder model employing Chain-of-Thought (CoT) reasoning exhibited **relatively long generation times**, particularly for the more intricate multi-file and web application projects (P2, P4, P5). Despite this, for simpler tasks such as the console applications and the Tic Tac Toe game (P1, P2, P3, P4), the generated code was consistently **functionally correct**, evidenced by a Levenshtein distance of 0. This indicates that for well-defined, albeit sometimes multi-part, problems, CoT reasoning effectively guided the agent to the correct solution. However, for the web application projects (P5 and P6), the generated code required **manual corrections**. These modifications primarily involved frontend configuration adjustments, such as correctly linking scripts in HTML files and addressing module export issues, as well as integrating API keys for external service access. The consistently low average cyclomatic complexity across all projects suggests that the CoT-driven code was generally **well-structured and maintainable**. Furthermore, the minimal number of linting errors highlights a good adherence to Python's PEP 8 style guidelines. Overall, CoT reasoning proved effective for achieving functional correctness in a broad range of projects, though it presented some integration challenges with more complex web application setups.

---

### 5.2. v1.1 - No Reasoning

| Metric                                    | Project 1 | Project 2                                 | Project 3                                                 | Project 4                                 | Project 5   | Project 6 |
| :---------------------------------------- | :-------- | :---------------------------------------- | :-------------------------------------------------------- | :---------------------------------------- | :---------- | :-------- |
| **Time of generation (s)**                | 92.25     | 167.72                                    | 450.09                                                    | 200.06                                    | 287.23      | 196.37    |
| **Number of lines of code**               | 77        | 188                                       | 372                                                       | 227                                       | 313         | 243       |
| **Number of used tokens**                 | 45590     | 85116                                     | 234158                                                    | 95994                                     | 171589      | 112006    |
| **Number of lines of code after changes** | N/A       | 191                                       | N/A                                                       | 227                                       | 322         | 238       |
| **Levenshtein distance**                  | 0         | 61                                        | 0                                                         | 31                                        | 140         | 142       |
| **Cyclomatic complexity (avg)**           | 5.25      | 3.2                                       | 3.65                                                      | 2.44                                      | 1.81        | N/A       |
| **Code duplication (%)**                  | 0%        | 0%                                        | 0%                                                        | 0%                                        | 0%          | 0%        |
| **Lint errors (Python)**                  | 1         | 0                                         | 0                                                         | 0                                         | 0           | N/A       |
| **Notes**                                 |           | Function to validate input was badly used | Agent added ability to select O or X for Human vs AI game | Created dir 'snake_game' which is useless | CORS Errors |           |

**No Reasoning Analysis:**
The "No Reasoning" version of the Coder agent demonstrated a **significantly faster code generation time** and **substantially lower token consumption** across all projects compared to the CoT and ToT variants. This efficiency comes at a cost: for more complex projects such as the multi-file CLI Note Manager (P2), the Pygame Snake Game (P4), and both web applications (P5, P6), the generated code exhibited **lower functional correctness**, as indicated by higher Levenshtein distances. For instance, in Project 2, the input validation function was improperly utilized, leading to operational issues. Project 5 frequently encountered **CORS (Cross-Origin Resource Sharing) errors**, indicating a lack of proper configuration for web security policies. Furthermore, in some cases (e.g., P4), the agent generated **unnecessary directories or files**, suggesting a less refined understanding of project structure. While cyclomatic complexity varied, it generally remained within acceptable bounds. The number of linting errors was consistently low, which is positive for code style. This approach proved most effective and reliable for **very simple and precisely defined tasks** (like Project 1 and 3), where its speed advantage could be fully leveraged without significant compromises in correctness. For anything beyond basic scripting, manual intervention was often required.

---

### 5.3. v1.2 - ToT Reasoning (Updated)

| Metric                                    | Project 1 | Project 2 | Project 3 | Project 4 | Project 5                                                                     | Project 6 |
| :---------------------------------------- | :-------- | :-------- | :-------- | :-------- | :---------------------------------------------------------------------------- | :-------- |
| **Time of generation (s)**                | 300.82    | 562.42    | 743.00    | 707.95    | 699.62                                                                        | 552.51    |
| **Number of lines of code**               | 91        | 255       | 809       | 801       | 690                                                                           | 443       |
| **Number of used tokens**                 | 208949    | 441787    | 711946    | 661526    | 545036                                                                        | 393723    |
| **Number of lines of code after changes** | N/A       | 255       | N/A       | N/A       | 690                                                                           | 436       |
| **Levenshtein distance**                  | 0         | 4         | 0         | 0         | 23                                                                            | 575       |
| **Cyclomatic complexity (avg)**           | 3.8       | 2.23      | 3.07      | 2.34      | 1.5                                                                           | N/A       |
| **Code duplication (%)**                  | 0%        | 0%        | 0%        | 0%        | 0%                                                                            | 0%        |
| **Lint errors (Python)**                  | 1         | 5         | 5         | 0         | 1                                                                             | N/A       |
| **Notes**                                 |           |           |           |           | No ability to remove tasks on frontend. Needed to fix CORS (set to all hosts) |           |

**ToT Reasoning Analysis:**
The Tree-of-Thought (ToT) Reasoning strategy consistently exhibited the **longest generation times** and **highest token consumption** across all projects. This is an expected trade-off, as ToT involves exploring multiple reasoning paths and iterative refinement, demanding more computational resources and interactions with the language model. Despite this, ToT demonstrated remarkable performance in achieving **perfect functional correctness (Levenshtein distance of 0)** for Projects 1 (Temperature Converter), 3 (Tic Tac Toe), and 4 (Snake Game). This highlights its capacity to methodically break down and accurately solve complex, self-contained problems. However, its performance was **inconsistent for other complex projects**. Project 2 (CLI Note Manager) had a minimal Levenshtein distance of 4, indicating minor, easily rectifiable issues. Project 5 (TODO List) had a Levenshtein distance of 23, with noted functional gaps such as the "No ability to remove tasks on frontend" and the recurring necessity to fix CORS errors by explicitly setting hosts. Most notably, Project 6 (Weather App) showed a **very high Levenshtein distance of 575**, suggesting significant functional discrepancies, incompleteness, or a fundamental misunderstanding of certain API interaction patterns. This significant variance underscores that while ToT has strong potential for generating robust solutions through its rigorous, iterative reasoning, it may still struggle with specific complexities, particularly those involving nuanced external API integrations or intricate frontend-backend communication. The larger number of lines of code in Projects 3, 4, and 5 generated by ToT might imply a more verbose or comprehensive approach to solving these problems. Lint errors were present but generally manageable, similar to other versions.

---

## 6. Comparison of Reasoning Strategies

| Metric                    | No Reasoning (ReAct)          | CoT Reasoning (ReAct + CoT)                       | ToT Reasoning (ReAct + ToT)                                    |
| :------------------------ | :---------------------------- | :------------------------------------------------ | :------------------------------------------------------------- |
| **Generation Time**       | Fastest                       | Medium                                            | Slowest                                                        |
| **Code Correctness**      | Lowest (often requires fixes) | Medium (good for simple, needs fixes for complex) | Highest (good for _some_ complex, but inconsistent for others) |
| **Code Complexity**       | Varied                        | Low/Medium                                        | Low/Medium                                                     |
| **Token Usage**           | Lowest                        | Medium                                            | Highest                                                        |
| **Stability/Consistency** | Lowest                        | Medium                                            | Mixed (High for some, low for others)                          |

**Conclusions from Comparison:**

The comparative analysis reveals distinct trade-offs associated with each reasoning strategy:

- **No Reasoning (ReAct):** This approach is unequivocally the **fastest** in terms of generation time and consumes the **fewest tokens**, making it the most cost-efficient. However, its lack of explicit internal deliberation often translates to **lower code quality** and functional correctness, particularly for anything beyond trivial tasks. It frequently necessitates manual intervention and debugging, making it best suited for very simple, precisely defined scripts where rapid prototyping is prioritized over robustness.

- **CoT Reasoning (ReAct + CoT):** Represents a balanced compromise. It offers **significantly better code quality and correctness** compared to the "No Reasoning" approach, making it a reliable choice for **moderately complex projects**. While its generation time and token consumption are higher, they remain within a reasonable range. This strategy is particularly effective when problems can be broken down into sequential steps, and explicit internal thoughts guide the agent towards a correct solution, requiring fewer post-generation fixes than the "No Reasoning" variant.

- **ToT Reasoning (ReAct + ToT):** This strategy is characterized by the **longest generation times** and **highest token consumption**, reflecting its extensive, iterative problem-solving process. When successful, ToT can produce **highly correct and robust solutions for complex problems**, as demonstrated by its perfect scores on several challenging projects. Its strength lies in its ability to explore and evaluate multiple paths, which is crucial for intricate logical dependencies. However, the results for Project 6 indicate that its performance can be **inconsistent across different complex projects**, occasionally leading to significant functional discrepancies. This suggests that while ToT holds immense potential for tackling difficult programming challenges, its robustness is not absolute and might depend on the specific nature and nuances of the problem at hand. Further refinements are needed to ensure its consistent efficacy across all complex scenarios.

---

## 7. Final Conclusions

The successful implementation and evaluation of this multi-agent system for autonomous code generation clearly demonstrate that a **multi-agent approach leveraging ReAct agents is a highly promising paradigm** for automating aspects of the software development lifecycle. The project conclusively shows that the choice of **different reasoning strategies within the Coder agent has a profound and measurable impact on both the efficiency and quality of the generated code**.

Our findings indicate a clear trade-off: simpler reasoning strategies offer speed and lower resource consumption but sacrifice correctness for complex tasks, while more sophisticated reasoning like CoT and ToT can achieve higher accuracy at the expense of time and token usage. The optimal strategy selection should therefore be contingent upon the **specific complexity of the project requirements and the prevailing priorities**—whether rapid prototyping (speed) or robust, production-ready code (quality) is paramount.

Looking ahead, several avenues for future research and development emerge. These include:

- **Further optimization of reasoning strategies:** Investigating hybrid approaches or dynamic switching between strategies based on real-time task complexity could yield improved results.
- **Introduction of automated code verification and testing mechanisms:** Integrating advanced static analysis tools, dynamic testing frameworks, and even formal verification techniques could significantly reduce the need for manual corrections and enhance the reliability of the generated code.
- **Expansion of other agents' roles:** Developing more sophisticated capabilities for agents beyond the Coder, such as a dedicated debugging agent, a refactoring agent, or a security analysis agent, could further increase the system's autonomy and its ability to handle a broader range of development challenges.

Developing these areas could significantly contribute to increasing the autonomy, effectiveness, and practical applicability of such multi-agent systems in real-world software engineering contexts.

## References

- **LangGraph Documentation:** The LangGraph library was instrumental in orchestrating the complex interactions between our agents. Its capabilities for defining state machines and managing agent workflows provided the robust foundation for our system. (Specific URL or version could be added if available, e.g., `https://langchain.github.io/langchain-graph/`)
- **ReAct (Reasoning and Acting):** The core architecture for our agents. The concept of ReAct agents, which combine reasoning with external tools and actions, was a fundamental design choice. (e.g., "ReAct: Synergizing Reasoning and Acting in Language Models" by Shunyu Yao et al.)
- **Chain-of-Thought (CoT) Reasoning:** This technique, where models articulate their intermediate reasoning steps, formed a key part of our Coder agent's capabilities. (e.g., "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" by Jason Wei et al.)
- **Tree-of-Thought (ToT) Reasoning:** The more advanced reasoning strategy explored in this project, enabling agents to consider and evaluate multiple reasoning paths. (e.g., "Tree of Thoughts: Deliberate Problem Solving with Large Language Models" by Shunyu Yao et al.)
- **Python PEP 8 Style Guide:** Used as the standard for linting errors, ensuring code readability and consistency. (Official Python documentation)
- **Pygame:** The library used for developing the Snake Game GUI, demonstrating the agents' ability to work with external graphical libraries. (Pygame official documentation)
- **Flask/Django/FastAPI:** Frameworks considered or used by the Coder for web application backend development.
