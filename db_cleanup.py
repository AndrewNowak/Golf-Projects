def db_clean():
    mycursor.execute("SELECT * FROM standings_new")
    pull_1 = mycursor.fetchall()

    data=[]
    for i in range(len(pull_1)):
        if (pull_1[i][2] != 999 and pull_1[i][9] != 999 and pull_1[i][10] != 999 and pull_1[i][11] != 999 and pull_1[i][12] != 999) and (pull_1[i][2] != 0 and pull_1[i][9] != 0 and pull_1[i][10] != 0 and pull_1[i][11] != 0 and pull_1[i][12] != 0) :
            data.append(pull_1[i][:])
    return data