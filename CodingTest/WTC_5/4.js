function solution(numstrs, words) {
    var answer = [];
    var arr = []
    arr[0] = ['0', 'O', '()']
    arr[1] = ['1', 'I']
    arr[2] = ['2', 'Z', 'S', '7_']
    arr[3] = ['3', 'E', 'B']
    arr[4] = ['4', 'A']
    arr[5] = ['5', 'Z', 'S']
    arr[6] = ['6', 'b', 'G']
    arr[7] = ['7', 'T', 'Y']
    arr[8] = ['8', 'B', 'E3']
    arr[9] = ['9', 'g', 'q']

    for(var i = 0; i < words.length; i++){
        var cnt = 0
        var w = words[i]
        flag = false
        for(var j = 0; j < numstrs.length; j++){
            var n_i = 0
            var w_i
            for(w_i = 0; w_i < numstrs[j].length - w.length; w_i++){
                var flag2 = true
                n_i = 0
                for(var ijij = w_i; ijij < w_i + w.length; ijij++){
                    flag2 = false
                    for(var tmp = 0; tmp < arr[w[n_i]].legnth; tmp++){
                        if(numstrs[j][ijij] == arr[w[n_i]][tmp]){
                            n_i++
                            flag2 = true
                            break
                        }
                    }
                    if(flag2 == false)
                        break
                }
                if(flag2){
                    cnt++;
                    break
                }

            }

        }
        answer[i] = cnt
    }
    return answer;
}