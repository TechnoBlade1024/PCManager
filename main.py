import json
import os


def fs_tree(root):
    results = {}
    for (dirpath, dirnames, filenames) in os.walk(root):
        parts = dirpath.split(os.sep)
        curr = results
        for p in parts:
            curr = curr.setdefault(p, {})
    return results
out=fs_tree('e:')
print(json.dumps(out))
