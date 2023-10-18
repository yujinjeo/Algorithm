def solution(phone_book):
    phone_book.sort()
    k=0
    
    for i in range(1,len(phone_book)):
        if len(phone_book[i])>len(phone_book[i-1]):
            k+=1
            if phone_book[i].find(phone_book[i-k])==0 or phone_book[i].find(phone_book[i-1])==0:
                return False
            else: 
                continue
        else:
            k=0
            
    return True