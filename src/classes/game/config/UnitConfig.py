class UnitConfig:
    def __init__(self, name: str, display_name: str,  owner_name: str, description: str, cost: int):
        self.name = name
        self.display_name = display_name
        self.owner_name = owner_name
        self.description = description
        self.cost = cost

    def create_from_config():
        raise NotImplementedError("create_from_config() must be implemented")