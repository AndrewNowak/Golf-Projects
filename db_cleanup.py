def db_clean(golf_data):
    data=[]
    for i in range(len(golf_data)):
        if (pull_1[i][0] != 999 and pull_1[i][1] != 999 and pull_1[i][2] != 999 and pull_1[i][3] != 999 and pull_1[i][4] != 999) and (pull_1[i][0] != 0 and pull_1[i][1] != 0 and pull_1[i][2] != 0 and pull_1[i][3] != 0 and pull_1[i][4] != 0) :
            data.append(pull_1[i][:])
    return data