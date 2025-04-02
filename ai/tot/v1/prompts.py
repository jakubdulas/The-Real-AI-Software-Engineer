from langchain_core.prompts import PromptTemplate

thinker_template = """
{{ system_prompt }}.

Before executing the task, think deeply about the next step to solve the task given by the user.
The tought you will give is the step of how to complete given by the user task.
The purpose of the thoughts is to break the problem into smaller steps.
REMEMBER to not over complicate the task and do what the user is telling to do.
Already taken steps: 
{% if steps %}{{ steps }}{% else %}This is your first step to solve this problem.{% endif %}

What is the next step to solve this problem? Is it the last step thast must be taken to complete the task?
Return only the next step in one sentence.
"""

thinker_prompt = PromptTemplate(
    template=thinker_template,
    input_variables=["system_prompt", "intermediate_steps"],
    template_format="jinja2",
)
