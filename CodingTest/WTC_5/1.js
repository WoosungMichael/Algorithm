function solution(salaries, days) {
    var answer = 0;
    var i = 0
    while(i < salaries.length){
        if(days % salaries[i][0] == 0)
            answer += salaries[i][1] * parseInt(days / salaries[i][0])
        else
            answer += salaries[i][1] * (parseInt(days / salaries[i][0]) + 1)
        i++
    }
    return answer;
}