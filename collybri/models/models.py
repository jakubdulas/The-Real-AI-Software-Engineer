from dataclasses import dataclass, field
from typing import Dict, Any, List, Callable, Protocol


class CandidateSorter(Protocol):
    def __call__(self, user: "User", candidates: List["User"]) -> List["User"]:
        """
        Protocol to define custom sorting logic for user matching preferences.
        Given a user and their candidate list, returns a prioritized (sorted) list of candidates.
        """
        ...


@dataclass
class User:
    """
    Represents a user in the online meeting platform.

    Attributes:
        user_id (int): Unique identifier for the user.
        name (str): Name of the user.
        preferences (Dict[str, Any]): User-specific preferences for meeting matching.
        on_break (bool): If True, user is on break for the next round.
    """

    user_id: int
    name: str
    preferences: Dict[str, Any] = field(default_factory=dict)
    on_break: bool = False


@dataclass
class MeetingRoom:
    """
    Represents a (virtual) meeting room.

    Attributes:
        room_id (int): Unique identifier for the room.
        name (str): Room name or label.
        capacity (int): Maximum number of users allowed in the room.
    """

    room_id: int
    name: str
    capacity: int


@dataclass
class Meeting:
    """
    Represents a scheduled meeting session.

    Attributes:
        meeting_id (int): Unique meeting session identifier.
        participants (List[User]): Users participating in the meeting.
        meeting_room (MeetingRoom): Room where meeting is held.
        time_slot (Any): Time info for the meeting (can be refined to datetime).
    """

    meeting_id: int
    participants: List[User]
    meeting_room: MeetingRoom
    time_slot: Any
