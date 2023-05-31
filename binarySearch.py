def bsearch(l: list, item: int, start: int, end: int):
    if start == end: 
        res = start if l[start] == item else -1
        return res
    mid = (start + end) // 2
    if item > l[mid]: return bsearch(l, item, mid + 1, end)
    elif item < l[mid]: return bsearch(l, item, start, mid)
    else: return mid