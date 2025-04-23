# graph.py

This module implements a multi-agent system supervised by an agent designed to manage multiple workers, including researchers and coders. The supervisor routes tasks to the appropriate agents until the work is completed.

## Constants

### `members`

A list containing the names of the agents that are part of the multi-agent system (in this case, "researcher" and "coder").

### `options`

A list that includes all agents and a "FINISH" option to indicate the completion of tasks.

## Classes

### `MultiAgentSystem`

This class is responsible for supervising a conversation between multiple worker agents. It manages task allocation and status tracking.

#### Constants:
- `SUPERVISOR_SYSTEM_PROMPT`: A string that guides the supervisor in managing the conversation among workers and deciding which worker will act next based on user requests.

#### Initialization:

The constructor initializes the `MultiAgentSystem`, setting up the necessary attributes for tracking agents and their states.

#### Methods:

- `add_agent(name, graph, state_schema)`:
  Adds an agent to the system, along with its graph and state schema. Defines how to invoke the agent within the multi-agent system.

- `build()`:
  Constructs the state graph for the multi-agent system, defining workflows between the supervisor and the various agents.

## Example:

The `MultiAgentSystem` can be executed directly, as shown in the main block, where it adds the "coder" and "researcher" agents, builds the system, and invokes a request to the system.