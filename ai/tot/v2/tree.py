class TreeNode:
    def __init__(self, thought, finish=False, score=None, score_reason=None):
        self.thought = thought
        self.finish = finish
        self.score = score
        self.score_reason = score_reason
        self.children = []

    def add_child(self, thought, finish=False, score=None, score_reason=None):
        """Add a child node with the given thought, finish status, and score"""
        child = TreeNode(thought, finish, score, score_reason)
        self.children.append(child)
        return child

    def remove_child(self, thought):
        """Remove a direct child node with the given thought"""
        for i, child in enumerate(self.children):
            if child.thought == thought:
                return self.children.pop(i)
        return None

    def __str__(self, level=0):
        """String representation of the node and its children with indentation"""
        score_str = f", score: {self.score}" if self.score is not None else ""
        result = (
            "  " * level
            + f"{{thought: '{self.thought}', finish: {self.finish}{score_str}}}\n"
        )
        for child in self.children:
            result += child.__str__(level + 1)
        return result

    def is_leaf(self):
        """Check if the node is a leaf node (has no children)"""
        return len(self.children) == 0


class ThoughtTree:
    def __init__(self, root_thought="Root", root_score=None):
        """Initialize the tree with a root node"""
        self.root = TreeNode(root_thought, score=root_score)

    def find_node(self, thought, node=None):
        """Find a node with the given thought"""
        if node is None:
            node = self.root

        if node.thought == thought:
            return node

        for child in node.children:
            result = self.find_node(thought, child)
            if result:
                return result

        return None

    def find_parent(self, thought, node=None, parent=None):
        """Find the parent of a node with the given thought"""
        if node is None:
            node = self.root

        # Check if any of this node's children match the target
        for child in node.children:
            if child.thought == thought:
                return node

        # Recursively check all children
        for child in node.children:
            result = self.find_parent(thought, child, node)
            if result:
                return result

        return None

    def add_thought(
        self, parent_thought, new_thought, finish=False, score=None, score_reason=None
    ):
        """Add a thought node as a child of the parent thought node with optional score"""
        parent = self.find_node(parent_thought)
        if parent:
            return parent.add_child(new_thought, finish, score, score_reason)
        else:
            raise ValueError(f"Parent thought '{parent_thought}' not found in the tree")

    def set_score(self, thought, score):
        """Set the score for a node"""
        node = self.find_node(thought)
        if node:
            node.score = score
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def change_thought(self, thought, new_thought):
        """Set the score for a node"""
        node = self.find_node(thought)
        if node:
            node.thought = new_thought
            node.score = None
            node.score_reason = None
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def get_score(self, thought):
        """Get the score for a node"""
        node = self.find_node(thought)
        if node:
            return node.score
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def set_score_reason(self, thought, score_reason):
        """Set the score reason for a node"""
        node = self.find_node(thought)
        if node:
            node.score_reason = score_reason
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def get_score_reason(self, thought):
        """Get the score reason for a node"""
        node = self.find_node(thought)
        if node:
            return node.score_reason
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def get_highest_scoring_nodes(self, count=1):
        """Return the highest scoring nodes"""
        nodes_with_scores = []

        def collect_scored_nodes(node):
            if node.score is not None:
                nodes_with_scores.append((node.thought, node.score))
            for child in node.children:
                collect_scored_nodes(child)

        collect_scored_nodes(self.root)
        # Sort by score in descending order
        sorted_nodes = sorted(nodes_with_scores, key=lambda x: x[1], reverse=True)
        return sorted_nodes[:count]

    def remove_node(self, thought, preserve_children=True):
        """
        Remove a node from the tree

        Args:
            thought: The thought content of the node to remove
            preserve_children: If True, the children of the removed node
                              will be attached to the parent of the removed node.
                              If False, the entire subtree will be removed.

        Returns:
            The removed node
        """
        # Cannot remove the root node
        if thought == self.root.thought:
            raise ValueError("Cannot remove the root node")

        # Find the parent of the node to remove
        parent = self.find_parent(thought)
        if not parent:
            raise ValueError(f"Thought '{thought}' not found in the tree")

        # Find the node to remove
        node_to_remove = None
        for i, child in enumerate(parent.children):
            if child.thought == thought:
                node_to_remove = parent.children.pop(i)
                break

        # If we want to preserve the children, attach them to the parent
        if preserve_children and node_to_remove:
            for child in node_to_remove.children:
                parent.children.append(child)

        return node_to_remove

    def mark_as_finished(self, thought):
        """Mark a thought node as finished"""
        node = self.find_node(thought)
        if node:
            node.finish = True
        else:
            raise ValueError(f"Thought '{thought}' not found in the tree")

    def get_leaf_nodes(self):
        """Return all leaf nodes (nodes with no children)"""
        leaves = []

        def collect_leaves(node):
            if node.is_leaf():
                leaf_data = {"thought": node.thought, "finish": node.finish}
                if node.score is not None:
                    leaf_data["score"] = node.score
                leaves.append(leaf_data)
            else:
                for child in node.children:
                    collect_leaves(child)

        collect_leaves(self.root)
        return leaves

    def get_all_paths(self):
        """Return all paths from root to each leaf node or finished node"""
        all_paths = []

        def dfs(node, current_path):
            # Add current node to the path
            node_data = {"thought": node.thought, "finish": node.finish}
            if node.score is not None:
                node_data["score"] = node.score
            if node.score_reason is not None:
                node_data["score_reason"] = node.score_reason
            current_path.append(node_data)

            # If it's a leaf node or a finished node, add the path to all_paths
            if node.is_leaf() or node.finish:
                all_paths.append(current_path.copy())

            # Continue DFS for each child
            for child in node.children:
                dfs(child, current_path.copy())

        # Start DFS from root
        dfs(self.root, [])
        return all_paths

    def get_finished_paths(self):
        """Return all paths that end with a finished node"""
        all_paths = self.get_all_paths()
        return [path for path in all_paths if path[-1]["finish"]]

    def get_not_finished_paths(self):
        """Return all paths that end with a finished node"""
        all_paths = self.get_all_paths()
        return [
            path
            for path in all_paths
            if not path[-1]["finish"] or "score" not in path[-1]
        ]

    def are_all_paths_finished(self):
        return len(self.get_all_paths()) == len(self.get_finished_paths())

    def get_highest_scoring_path(self):
        """Return the path with the highest cumulative score"""
        all_paths = self.get_all_paths()

        if not all_paths:
            return None

        # Calculate sum of scores for each path (ignoring nodes without scores)
        path_scores = []
        for path in all_paths:
            total_score = sum(node.get("score", 0) for node in path)
            path_scores.append((path, total_score))

        # Return the path with the highest total score
        return max(path_scores, key=lambda x: x[1])

    def __str__(self):
        """String representation of the entire tree"""
        return str(self.root)

    def to_dict(self):
        """Convert the tree to a dictionary for serialization"""

        def node_to_dict(node):
            node_dict = {
                "thought": node.thought,
                "finish": node.finish,
                "score": node.score,
                "score_reason": node.score_reason,
                "children": [node_to_dict(child) for child in node.children],
            }
            return node_dict

        return {"root": node_to_dict(self.root)}

    @classmethod
    def from_dict(cls, data):
        """Create a ThoughtTree from a dictionary"""
        tree = cls(
            root_thought=data["root"]["thought"], root_score=data["root"]["score"]
        )

        def add_children(parent_node, children_data):
            for child_data in children_data:
                child = parent_node.add_child(
                    child_data["thought"],
                    child_data["finish"],
                    child_data["score"],
                    child_data["score_reason"],
                )
                add_children(child, child_data["children"])

        add_children(tree.root, data["root"]["children"])
        return tree
