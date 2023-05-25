from sys import stdin
from typing import List, Dict
from collections import defaultdict

enum: Dict[str, int] = {
    ""ordinary"": 0,
    ""confidential"": 1,
    ""settings"": 2,
    ""system"": 3,
}

pv: Dict[str, Dict[str, List[int]]] = {
    ""admin"": {
        ""read"": [0, 1, 2, 3],
        ""edit"": [0, 1, 2, 3]
    },
    ""experienced"": {
        ""read"": [0, 2, 3],
        ""edit"": [0, 1]
    },
    ""user"": {
        ""read"": [0],
        ""edit"": [0]
    },
}

lines: List[str] = [i.strip() for i in stdin.readlines()[:-1]]
files: Dict[str, List[str]] = defaultdict(list)
[files[i.split()[-1]].append(i.split()[0]) for i in (j for j in lines[:lines.index(""."")])]

for i in lines[lines.index(""."") + 1:]:
    user_name, rw, file_name = i.split()[::-1]
    rw_file: str = [k for k, v in files.items() for s in v if file_name == s][0]
    print(f""Access {'granted' if enum.get(rw_file) in pv.get(user_name, {}).get(rw, []) else 'denied'}"") 