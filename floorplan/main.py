from dataclasses import dataclass, field
from re import finditer, search
from typing import Dict, List

@dataclass
class RowSegment():
    row_no : int
    col_start : int
    col_end : int

    def __repr__(self):
        return f'{self.row_no}:{self.col_start}-{self.col_end}'

@dataclass
class Space():
    name : str = 'noname'
    furn_count : Dict[str, int] = field(default_factory = dict)
    segs : List[RowSegment] = field(default_factory = list)
    complete : bool = False

    def __repr__(self):
        return f'{self.name}: {[i for i in self.furn_count.items()]}\n{[s for s in self.segs]}'

def readFromFile(filename):
    """
    :param filename: (str) The name of the file to read from.
    :return: (list) The list of lines from the file.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

plan = """
+---------------+-------------------+           +----------+
|               |                   |           |          |
|  (office)     |            C      |           |   C      |
|               |                   |           |          |
|           W   |                   +-----------+          |
|               |                   |           |          |
|   S           |   (bathroom)     S|      S    |          |
|           +---+--------+----------+           |          |
|          /P           S|                      |          |
|         /              |                      |          |
|        /   (kitchen)   |      (bedroom)       |  P       |
+-------+                |                      |          |
|        \               |                      |          |
|         \   SSWP       |   W              W   |          |
|          +-------------+----------------------+          |
|                                                          |
|             (hallway)                                    |
|    W                                                     |
+--------------+-------------+-------------+               |
               |             |              \              |
               |             |               \        C    |
               | P           |                \            |
               |             |                 \           |
        +------+           P |                  +----------+
        |S                   |                              
        |    (balcony)   C   |                              
        +--------------------+                              """

#plan = readFromFile('./plan.txt')
furn_types = 'CPSW'
workspaces = []
rooms = []
rows = plan.split('\n')
rows.pop(0)

for no, row in enumerate(rows):
    found = list(finditer(r'[^/\\|+-]+', row))
    if found:
        rsegs = [RowSegment(no, rs.start(), rs.end()) for rs in found]
        for ws in workspaces:
            for rs in rsegs:
                if max(ws.segs[-1].col_start, rs.col_start) < min(ws.segs[-1].col_end, rs.col_end): #add rs to ws
                    ws.segs.append(rs)
                    rsegs.remove(rs)
                    break
            else: #no rs added => complete
                text = ''.join([rows[s.row_no][s.col_start:s.col_end] for s in ws.segs])
                name = search(r'\(\w+\)', text)
                if name:
                    ws.name = name[0][1:-1]
                    ws.furn_count = {f: text.count(f) for f in furn_types}
                    rooms.append(ws)
                ws.complete = True
        #reset ws list to only not complete
        workspaces = [ws for ws in workspaces if ws.complete == False]
        #create new wss with remaining rss
        for rs in rsegs:
            newws = Space()
            newws.segs.append(rs)
            workspaces.append(newws)
#rooms = rooms.sort(key=lambda room: room.name)

for r in rooms:
    print(r)