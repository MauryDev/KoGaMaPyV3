class GameInfo:
    id: int
    name: str
    description: str
    @classmethod
    def FromJson(cls,jsonobj):
        ret = cls()
        data = jsonobj["data"]
        if data is not None:

            ret.id = data["id"]
            ret.name = data["name"]
            ret.description = data["description"]
        return ret