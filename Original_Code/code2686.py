def verify(s: str):
    if not s or s[0] in ""}])"" or s[-1] in ""([{"" or len(s) % 2 == 1:
        return False
    g = {
        ""("": {""end"": "")"", ""l"": []},
        ""["": {""end"": ""]"", ""l"": []},
        ""{"": {""end"": ""}"", ""l"": []},
        "")"": {""end"": ""("", ""l"": []},
        ""]"": {""end"": ""["", ""l"": []},
        ""}"": {""end"": ""{"", ""l"": []}
    }
    gr = []
    for i in range(len(s)):
        tm = 0
        d = {i: []}
        for j in range(i, len(s)):
            if s[j] == s[i]:
                tm += 1
            if s[j] == g[s[i]][""end""]:
                tm -= 1
                if tm == 0:
                    d[i].append(s[j])
                    break
            d[i].append(s[j])
        if tm == 0 and d[i][0] not in "")]}"":
            gr.append(d)

    if not gr or len(gr) != len(s) // 2:
        return False

    for i in gr:
        for j in i.values():
            if len(j) % 2 == 1:
                return False
            if not all([j.count(i) == j.count(g[i][""end""]) for i in ""([{""]):
                return False

    return True

print(""YES"" if verify(input()) else ""NO"") 