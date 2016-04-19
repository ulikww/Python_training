from sys import maxsize

class Group:
    def __init__(self,name=None,header=None,footer=None,Parent_group=None,id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.Parent_group = Parent_group
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id,self.name, self.header,self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name and self.Parent_group is None or other.Parent_group is None or self.Parent_group == other.Parent_group


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

