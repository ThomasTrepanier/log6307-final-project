def merge_list(list1, list2):
    resultant_data = []
    list2.reverse()

    for i,j in zip(range(0, len(list1)), range(0, len(list2))):
        if list2[j] is not None:
            s = list1[i]+list2[j]
        else:
            s = list1[i]
        resultant_data.append(str(s))

    return ' '.join(resultant_data)

#Provide different values for the variables and test your program
list1=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
list2=['y','tor','e','eps','ay',None,'le','n']
merged_data=merge_list(list1,list2)
print(merged_data)
