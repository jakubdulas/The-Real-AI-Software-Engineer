from typing import List
from models.models import User, MeetingRoom, Meeting


def setup_first_meeting_all_together(
    users: List[User], room_name: str = "All Users Room", config: dict = None
) -> Meeting:
    """
    Set up the first meeting where all users are assigned to a single room.

    Args:
        users (List[User]): List of all active users.
        room_name (str): Name for the meeting room.
        config (dict, optional): Optional config dict that may specify whether to trigger this setup.

    Returns:
        Meeting: The created Meeting instance with all users in a single room.
    """
    if config and not config.get("first_meeting_all_in_one_room", True):
        # By default, run the all-in-one-room logic, unless explicitly disabled
        return None

    active_users = [user for user in users if not user.on_break]
    room = MeetingRoom(room_id=1, name=room_name)
    meeting = Meeting(meeting_id=1, room=room, participants=active_users)
    return meeting
