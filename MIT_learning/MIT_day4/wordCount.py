def wordCount(L):
    ret = {}
    for item in L:
        if item not in ret:
            ret[item] = 0
        ret[item] += 1
    return ret

print(wordCount(["sugar","egg","flour","egg","chocolate","flour"]))