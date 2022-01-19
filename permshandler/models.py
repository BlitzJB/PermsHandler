import json
import discord


class Group:
    def __init__(self, name, permissions):
        self.name = name
        self.level = permissions["level"]
        self.users, self.roles = set(permissions["users"]), set(permissions["roles"])

    def is_user_quelified(self, user: discord.Member) -> bool:
        _id = user.id
        _role_ids = {role.id for role in user.roles}
        return (
            True
            if (_id in self.users or set.intersection(self.roles, _role_ids) != set())
            else False
        )

    def __repr__(self):
        return f"Group[{self.level}] {self.name} users:{len(self.users)} roles:{len(self.roles)}"


class Permissions:
    def __init__(self, path_to_perm_store: str = "./permshandler/permstore.json"):
        with open(path_to_perm_store, "r") as f:
            self.raw = json.load(f)

        self.groups = [Group(name, self.raw[name]) for name in self.raw]

    def _get_group(self, group: str) -> Group:
        match = [g for g in self.groups if g.name == group]
        return match[0] if match else None

    def is_user_authorized(self, user: discord.Member, group: str) -> bool:
        group = self._get_group(group)
        applicable_groups = [
            g for g in self.groups if group.level < g.level
        ]
        applicable_groups.append(group) # Add the group itself to the list and no other group of *its own level*
        authorized = [g.is_user_quelified(user) for g in applicable_groups]
        return True if any(authorized) else False
    
    def __repr__(self):
        return f"Permissions[{len(self.groups)} groups]"
