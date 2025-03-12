from abc import ABC, abstractmethod


class Agent(ABC):

    @abstractmethod
    def invoke(
        self,
    ):
        pass
