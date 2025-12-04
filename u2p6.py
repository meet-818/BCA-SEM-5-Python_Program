def remove(duplicate):
    final_list = []
    for num in duplicate:
        if num not in final_list:
            final_list.append(num)
    return final_list
duplicate = [1,1,2,2,3,4,3,5]
print(remove(duplicate))
