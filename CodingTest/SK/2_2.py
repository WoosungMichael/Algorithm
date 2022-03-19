def solution(arr, processes):
    answer = []
    read = []
    write = []
    for i in processes:
        i_s = i.split()
        if i_s[0] == "read":
            read.append(i_s)
        else:
            write.append(i_s)

    r_i = 0
    w_i = 0
    time = 0

    while True:
        while w_i < len(write) and int(write[w_i][1]) <= time:
            for i in range(int(write[w_i][3]), int(write[w_i][4]) + 1):
                arr[i] = write[w_i][5]
            time += int(write[w_i][2])
            w_i += 1
            print("-------")
            print(time)

        tmp = []
        last = time
        duration = int(read[r_i][2])
        # last = 0
        # duration = 0
        while r_i < len(read) and int(read[r_i][1]) <= time:
            
            answer.append("".join(arr[int(read[r_i][3]):int(read[r_i][4]) + 1]))
            
            if int(read[r_i][1]) <= last:
                if duration < int(read[r_i][2]):
                    time += int(read[r_i][2]) - duration
                    duration = int(read[r_i][2])
                    
            else:
                if(int(read[r_i][1]) < int(write[w_i][1])):
                    if int(read[r_i][1]) + int(read[r_i][2]) > time:
                        time = int(read[r_i][1]) + int(read[r_i][2])
                        duration = int(read[r_i][2])

            # if int(read[r_i][1]) + int(read[r_i][2]) <= last + duration:
            #     time = time
            # else:
            #     time = int(read[r_i][1]) + int(read[r_i][2])
            # last = time

            #duration = int(read[r_i][2])

            r_i += 1

            print("+++++++")
            print(time)
            if w_i < len(write) and int(write[w_i][1]) <= time:
                break
        
        print("<<<<<<<")
        print(time)
        time += 1
        if w_i >= len(write) and r_i >= len(read):
            break

    answer.append(time)

    return answer
