def merge_files(self):
    res = list()
    for f1 in self.listDomainToMerge:
        item = json.load(open(f1, encoding="utf-8"))
        res.append(item)

    with open('../Configuration%s/configuration.json' % self.owner, 'w') as output:
        output.write(json.dumps(res, ensure_ascii=False, indent=2))
