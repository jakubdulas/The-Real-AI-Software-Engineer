from typing import Callable, List, Optional, Any
from .models import User


class EventConfig:
    """
    Configuration class for meeting event manager.

    Attributes:
        all_in_one_room (bool): If True, the event starts with all users in one room in the first round.
        user_sort_func (Optional[Callable[[User, List[User]], List[User]]]):
            Custom function that sorts, for a given user, the other users by preference.
            If None, defaults to no specific ordering.
        initial_users (List[User]): User objects participating in the event.
    """

    def __init__(
        self,
        all_in_one_room: bool = True,
        user_sort_func: Optional[Callable[[User, List[User]], List[User]]] = None,
        initial_users: Optional[List[User]] = None,
    ) -> None:
        """
        Initializes configuration for the event manager.

        Args:
            all_in_one_room: Whether to start with an all-participant meeting.
            user_sort_func: Custom user pairing sort function.
            initial_users: List of User objects participating.
        """
        self.all_in_one_room = all_in_one_room
        self.user_sort_func = user_sort_func
        self.initial_users: List[User] = (
            initial_users if initial_users is not None else []
        )

    def set_user_sort_func(
        self, func: Callable[[User, List[User]], List[User]]
    ) -> None:
        """
        Set the custom sorting function for user pairings.
        Args:
            func: A callable that for given (user, users) returns a sorted list of users by preference.
        """
        self.user_sort_func = func

    def add_user(self, user: User) -> None:
        """
        Add a user to the initial user list.
        Args:
            user: The User object to add.
        """
        self.initial_users.append(user)

    def __repr__(self) -> str:
        return (
            f"<EventConfig(all_in_one_room={self.all_in_one_room}, "
            f"user_sort_func={'set' if self.user_sort_func else 'default'}, "
            f"initial_users={len(self.initial_users)} users)>"
        )
