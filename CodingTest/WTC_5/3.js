function solution(board) {
    var answer = 0;
    var dx = [-1, 0, 1, 0]
    var dy = [0, -1, 0, 1]
    var n = board.length

    var index = 0
    while(index < n){
        var cnt = 0
        var vi, vj, v = []
        for(vi = 0;vi < n;vi++){
            var tmp = []
            for(vj = 0;vj < n; vj++){
                tmp[vj] = 0
            }
            v[vi] = tmp
        }

        var j, alpha, dfs
        for(j = 0; j < n; j++){
            if(v[index][j] == 0){
                v[index][j] = 1
                dfs = [[index, j]]
                cnt ++
                alpha = board[index][j]
                var iii = 0
                while(iii < dfs.length){
                    var x, y
                    x = dfs[iii][0]
                    y = dfs[iii][1]
                    for(var ii = 0; ii < 4; ii++){
                        if(0 <= x + dx[ii] && x + dx[ii] < n){
                            if(0 <= y + dy[ii] && y + dy[ii] < n){
                                if(v[x + dx[ii]][y + dy[ii]] == 0){
                                    if(board[x + dx[ii]][y + dy[ii]] == alpha){
                                        dfs.push([x + dx[ii], y + dy[ii]])
                                        v[x + dx[ii]][y + dy[ii]] = 1
                                        cnt += 1
                                    }
                                }
                            }
                        }
                    }
                    iii++
                }   
            }
        }
        if(cnt > answer)
            answer = cnt



        cnt = 0
        var vi, vj, v = []
        for(vi = 0;vi < n;vi++){
            var tmp = []
            for(vj = 0;vj < n; vj++){
                tmp[vj] = 0
            }
            v[vi] = tmp
        }

        var j, alpha, dfs
        for(j = 0; j < n; j++){
            if(v[j][index] == 0){
                v[j][index] = 1
                dfs = [[j, index]]
                cnt ++
                alpha = board[j][index]
                var iii = 0
                while(iii < dfs.length){
                    var x, y
                    x = dfs[iii][0]
                    y = dfs[iii][1]
                    for(var ii = 0; ii < 4; ii++){
                        if(0 <= x + dx[ii] && x + dx[ii] < n){
                            if(0 <= y + dy[ii] && y + dy[ii] < n){
                                if(v[x + dx[ii]][y + dy[ii]] == 0){
                                    if(board[x + dx[ii]][y + dy[ii]] == alpha){
                                        dfs.push([x + dx[ii], y + dy[ii]])
                                        v[x + dx[ii]][y + dy[ii]] = 1
                                        cnt += 1
                                    }
                                }
                            }
                        }
                    }
                    iii++
                }   
            }
        }
        if(cnt > answer)
            answer = cnt


        index++
    }
    return answer;
}