def solution(s):
    answer = 0
    word_num=[('0',"zero"),('1',"one"), ('2',"two"), ('3',"three") 
              ,('4',"four"),('5',"five"),('6',"six")
              ,('7',"seven"),('8',"eight"),('9',"nine")]
    word=""
    for i in s:
        if '0'<=i<='9':
            answer=answer*10+int(i)
            print(answer)
            continue
        word+=i
        for a,b in word_num:
            if word==b:
                answer=answer*10+int(a)
                print(word)
                print(answer)
                word=""
                break
                  
    print(answer)    
    
    return answer

