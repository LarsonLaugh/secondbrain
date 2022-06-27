# define classes
class Node:
    def __init__(self, name, parent, children):
        self.name = name
        self.prt = parent
        self.chd = children
        for p in parent:
            if self not in p.chd:
                p.add_children(self)

    def add_parent(self, ParentNode):
        self.prt.append(ParentNode)

    def add_children(self, ChildNode):
        self.chd.append(ChildNode)

    def rename(self, name):
        self.name = name

    def print(self):
        print('\n-----------')
        print(self.name)
        print('Parents('+str(len(self.prt))+'):')
        if len(self.prt) > 0:
            for p in self.prt:
                print(p.name)
        else:
            print(' NULL\n')
        print('Children('+str(len(self.chd))+'):')
        if len(self.chd) > 0:
            for c in self.chd:
                print(c.name)
        else:
            print(' NULL\n')
        print('-----------\n')


class Book:
    def __init__(self, title, author, year, link, parent):
        self.name = title
        self.author = author
        self.year = year
        self.link = link
        self.prt = parent
        for p in parent: # In case the parent is created beforehand (Usual situation)
            if self not in p.chd: # In case we have already initiated this Book, and attached it to its parents
                p.add_children(self)
    def print(self):
        print('\n-----------')
        print(self.name)
        print('Parents('+str(len(self.prt))+'):')
        if len(self.prt) > 0:
            for p in self.prt:
                print(p.name)
        else:
            print(' NULL')
        print('AUTHOR:')
        if len(self.author) > 0:
            for author in self.author:
                print(author)
        else:
            print(' NULL')
        print('YEAR:')
        print(self.year)
        print('-----------')

if __name__ == '__main__':
    print('Initialize this library')
    # Initialize an empty library root
    root = Node('yourlibrary', [], [])
    # add nodes under the root
    computerscience = Node('CS', [root], [])
    physics = Node('PHY', [root], [])
    # add more books
    c1 = Book('CSbook1', ['wang'], 2008, 'empty', [computerscience])
    c2 = Book('CSbook2', ['wang'], 2013, 'empty', [computerscience])
    p2 = Book('CSbook3', ['wang'], 2014, 'empty', [physics])
    root.print()
    computerscience.print()
    physics.print()
    c1.print()
    c2.print()
    p2.print()
