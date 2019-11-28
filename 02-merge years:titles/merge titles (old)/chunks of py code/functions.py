##  Import packages
from difflib import SequenceMatcher


### calculate similarity with "SequenceMatcher" isJunk space
def similar(a, b):
    return SequenceMatcher(lambda x: x == " ", a, b).ratio()

### create the titles combinations
def lists_combinations(list1,list2):
    combination_list = []
    for i in list1:
        for j in list2: 
            similarity = similar(str(i[2]),str(j[2]))
            if (similarity > 0.8) :
                trial_id = str(i[0])+' _ '+str(j[0])
                trial_indicatror = str(i[1])+' _ '+str(j[1])
                title = str(i[2])+' _ '+str(j[2])

                new_tuple = (trial_id,trial_indicatror, title, similarity)
                combination_list.append(new_tuple)

    return(combination_list)

