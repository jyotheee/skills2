from operator import itemgetter, attrgetter

def count_unique(string):
    dict = {}

    for word in string.split():
        if word in dict:
            dict[word] += 1
        else:    
            dict[word] = 1

    print dict   

def exists_in_list(list, number):
    
    exists = False

    for index in range(0, len(list)):
        if number == list[index]:
            exists = True
    
    return exists        

def common_items(list1, list2):
    list3 = []
    #for each element in the first list, match it with each element of second list
    for index1 in range(0, len(list1)):
        for index2 in range(0, len(list2)):
            if list1[index1] == list2[index2]:
                #to avoid repetion of same elements in the new list
                if not exists_in_list(list3, list1[index1]):
                        list3.append(list1[index1])

    print list3

#returns a list of common items between two lists using dictionaries
def common_items2(list1, list2):
    match_dict = {}
    mlist = []

    for index1 in range(0, len(list1)):
        for index2 in range(0, len(list2)):
            if(list1[index1] == list2[index2]):
                if list1[index1] in match_dict:
                    match_dict[list1[index1]] += 1
                else:
                    match_dict[list1[index1]] = 1 
                       
    for k, v in sorted(match_dict.iteritems()):
        mlist.append(k)

    return mlist

def sum_zero(list1):
    list_pairs = []
    for index in range(0, len(list1)):
        for nextindex in range(index+1, len(list1)):
            if list1[index] + list1[nextindex] == 0:
                list_pairs.append((list1[index], list1[nextindex]))

    print list_pairs

def find_duplicates(words):
    
    word_dict = {}
    new_word_list = []

    for index in range(0, len(words)):
        if words[index] in word_dict:
            word_dict[words[index]] += 1
        else:
            word_dict[words[index]] = 1    

    for k, v in word_dict.iteritems():
        new_word_list.append(k)

    print "List without duplicates is %r" %new_word_list   

def word_length(words):
    word_dict = {}
    new_list = []

    for index in range(0, len(words)):
        if words[index] in word_dict:
            pass
        else:
            word_dict[words[index]] = len(words[index])    

    print "dictionary list of word lengths is", word_dict

    #extract tuples from the word_dict
    tuplelist = sorted(word_dict.items(), key=itemgetter(1))
    print "Tuple list is %r " % tuplelist

    for tuple in tuplelist:
        new_list.append(tuple[0])

    print "Sorted word list is %r " % new_list    


def main():

    #prints the count of each word in an input string
    string = "I do not like green eggs and ham. I do not like green eggs and ham."
    count_unique(string)

    #returns a list of all common items beween both lists
    list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
    list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
    words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

    common_items(list1, list2)

    print "Using the dictionary approach"
    commonlist = common_items2(list1, list2)
    print commonlist

    sum_zero(list1)

    find_duplicates(words)

    word_length(words)



if __name__ == "__main__":
    main()