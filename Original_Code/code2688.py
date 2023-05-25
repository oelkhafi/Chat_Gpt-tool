#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re, sys, itertools, collections
from typing import List, Dict, Tuple, Set


class User:
    def __init__(self):
        self.reads: Set[str] = set()
        self.genre: Set[str] = set()
        self.count: Dict[str, int] = collections.defaultdict(int)

    def __str__(self):
        return str(dict(self.count))

GET_BOOK: str = ""Посоветуй мне книгу""
re_catalog: str = r""\s?(.+?)\s*\""(.+?)\""\s*\((.+?)\),?""
re_user_book: str = r'(.+)\s*\""(.+)\""'
re_get_user: str = f""{GET_BOOK}\s\((.+)\)""

values: List[str] = [i.strip() for i in sys.stdin.readlines()[:-1]]
catalogs: List[Tuple[str, str, str]] = re.findall(re_catalog, values[0])
users: Dict[str, User] = dict()
key2 = lambda x: x[2]


for line in values[1:]:
    if GET_BOOK in line:
        sovet: List[str] = list()
        user_name: str = re.match(re_get_user, line).group(1).strip()
        if user_name not in users:
            print(""Список пуст"")
            continue
        user: User = users[user_name]
        iter = itertools.groupby(sorted(catalogs, key=key2), key=key2)
        max_genre: int = max(user.count.items(), key=lambda x: x[1])[1]
        list_genre: list = [k for k, v in user.count.items() if v == max_genre]
        iter = [(n, list(i)) for n, i in iter if n in user.genre]
        for genre, group_catalog in iter:
            for cat in group_catalog:
                if cat[1] in user.reads:
                    pass
                else:
                    if cat[2] in list_genre:
                        sovet.append(cat[1])
        if sovet:
            print(*[f'""{i}""' for i in sovet], sep="", "")
        else:
            print(""Список пуст"")
    else:
        match = re.match(re_user_book, line)
        user_name: str = match.group(1).strip()
        book_name: str = match.group(2).strip()

        if user_name not in users:
            users[user_name] = User()

        users[user_name].reads.add(book_name)
        genre: str = [i for i in catalogs if i[1] == book_name][0][2]
        users[user_name].genre.add(genre)
        users[user_name].count[genre] += 1 