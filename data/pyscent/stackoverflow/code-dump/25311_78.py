import wikipedia

def categorySorter(targetCats, pagesToCheck, mainCategory):
    targetList = []
    nonTargetList = []
    targetCats = [i.lower() for i in targetCats]

    print('Sorting pages...')
    print('Sorted:', end=' ', flush=True)
    for page in pagesToCheck:

        e = openPage(page)

        def deepList(l):
            for item in l:
                if item[1] == 'SUBPAGE_ID':
                    deepList(item[2])
                else:
                    catComparator(item[0], item[1], targetCats, targetList, nonTargetList, pagesToCheck[-1])

        if e[1] == 'SUBPAGE_ID':
            deepList(e[2])
        else:
            catComparator(e[0], e[1], targetCats, targetList, nonTargetList, pagesToCheck[-1])

    print()
    print()
    print('Results:')
    print(mainCategory, ': ', targetList, sep='')
    print()
    print('Non-', mainCategory, ': ', nonTargetList, sep='')

def openPage(page):
    try:
        pageList = [page, wikipedia.WikipediaPage(page).categories]
    except wikipedia.exceptions.PageError as p:
        pageList = [page, 'NONEXIST_ID']
        return
    except wikipedia.exceptions.DisambiguationError as e:
        pageCategories = []
        for i in e.options:
            if '(disambiguation)' not in i:
                pageCategories.append(openPage(i))
        pageList = [page, 'SUBPAGE_ID', pageCategories]
        return pageList
    finally:
        return pageList

def catComparator(pageTitle, pageCategories, targetCats, targetList, nonTargetList, lastPage):

    # unhash to view the categories of each page
    #print(pageCategories)
    pageCategories = [i.lower() for i in pageCategories]

    any_in = False
    for i in targetCats:
        if i in pageTitle:
            any_in = True
    if any_in:
        print('', end = '', flush=True)
    elif compareLists(targetCats, pageCategories):
        any_in = True

    if any_in:
        targetList.append(pageTitle)
    else:
        nonTargetList.append(pageTitle)

    # Just prints a pretty list, you can comment out until next hash if desired
    if any_in:
        print(pageTitle, '(T)', end='', flush=True)
    else:
        print(pageTitle, '(F)',end='', flush=True)

    if pageTitle != lastPage:
        print(',', end=' ')
    # No more commenting

    return any_in

def compareLists (a, b):
    for i in a:
        for j in b:
            if i in j:
                return True
    return False
