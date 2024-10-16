
    
        

def solution(video_len, pos, op_start, op_end, commands):
    vm, vs = map(int,video_len.split(":"))
    v = vm*60+vs
    pm, ps = map(int,pos.split(":"))
    p = pm*60+ps
    osm, oss = map(int,op_start.split(":"))
    os = osm*60+oss
    oem, oes = map(int,op_end.split(":"))
    oe = oem*60+oes
    if os <= p <= oe:
            p = oe
    for c in commands:
        if c == "next":
            p += 10
            if p > v:
                p = v
        elif c == "prev":
            p -= 10
            if p < 0:
                p = 0
        if os <= p <= oe:
            p = oe
    
    pm = p // 60
    ps = p % 60
    answer = ("%02d:%02d"%(pm,ps))
            
    
    
    return answer