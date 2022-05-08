function solution(scores) {
    var answer = [];
    var sum1 = 0
    var sum2 = 0
    var i = 0
    var score_arr = []
    while(i < scores.length){
        sum1 += scores[i][0]
        sum2 += scores[i][1]
        score_arr[i] = [scores[i][0], scores[i][1], i + 1]
        i++
    }
    score_arr.sort(function(a, b){
        if(a[0] + a[1] < b[0] + b[1]){
            return 1;
        }
        else if(a[0] + a[1] > b[0] + b[1]){
            return -1;
        }
        else{
            if(sum1 < sum2){
                if(a[0] < b[0]){
                    return 1
                }
                else if (a[0] > b[0]){
                    return -1
                }
                else{
                    if(a[2] > b[2]){
                        return 1
                    }
                    else if(a[2] < b[2]) {
                        return -1
                    }
                    else return 0
                }
            }
            else if(sum1 > sum2){
                if(a[1] < b[1]) {
                    return 1
                }
                else if (a[1] > b[1]){
                    return -1
                } 
                else{
                    if(a[2] > b[2]) {
                        return 1
                    }
                    else if(a[2] < b[2]){
                        return -1
                    }
                    else return 0
                }
            }
            else{
                if(a[2] > b[2]) {
                    return 1
                }
                else if(a[2] < b[2]) {
                    return -1
                }
                else return 0
            }
        }
    })

    i = 0
    while(i < score_arr.length){
        var j = 0
        while(j < score_arr.length){
            if(i + 1 === score_arr[j][2]){
                answer[i] = j + 1
                break
            }
            j++
        }
        i++
    }

    return answer;
}