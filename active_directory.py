class Group:
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)


def is_user_in_group(user: str, group: Group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    if len(group.get_groups()) == 0:
        return False
    
    for subgroup in group.get_groups():
        if is_user_in_group(user, subgroup):
            return True

for group in [parent, child, sub_child]:
    if not is_user_in_group("Mehmet", group):
        print(f"Fail in {group.get_name()}")
    else:
        print(f"Success. {sub_child_user} is in {group.get_name()}")