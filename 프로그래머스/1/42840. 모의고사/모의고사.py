def solution(answers):
    answer = []
    stu1=[1,2,3,4,5]
    n1=5
    stu2=[2,1,2,3,2,4,2,5]
    n2=8
    stu3=[3,3,1,1,2,2,4,4,5,5]
    n3=10
    cnt=[0,0,0]
    cnt1, cnt2,cnt3=0,0,0
    
    for i in range(len(answers)):
        if answers[i]==stu1[i%n1]:
            cnt[0]+=1
        if answers[i]==stu2[i%n2]:
            cnt[1]+=1
        if answers[i]==stu3[i%n3]:
            cnt[2]+=1
    
    print(cnt)
    max_val = max(cnt)
    
    answer=list(map(lambda i : i+1, filter(lambda i:max_val==cnt[i], range(len(cnt)))))
    
    return answer