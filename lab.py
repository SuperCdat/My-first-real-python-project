import time
name=input('Hãy nhập tên của bạn - ')
print('Bạn có chắc tên bạn là',name,'?')
answer=input('có hay không? nhập y(có) hoặc n(không) - ')
while True:
    if answer=='y':
        print('Đã xong')
        time.sleep(1)
        break
    elif answer=='n':
        name=input('Hãy nhập tên của bạn - ')
        print('Bạn có chắc tên bạn là',name,'?')
        answer=input('có hay không? nhập y(có) hoặc n(không) - ')
        continue
    elif answer != 'y' or 'n':
        print('hãy nhập sự lựa chọn chính xác!')
        answer=input('có hay không? nhập y(có) hoặc n(không) - ')
        continue
old=int(input('Bạn bao nhiêu tuổi? - '))
while True:
    if old > 17:
        print('Bạn có chắc bạn',old,'tuổi?')
        yorn=input('có hay không? nhập y(có) hoặc n(không) - ')
        if yorn=='y':
            print(name, 'Cút')
            break
        elif yorn=='n':
            print('Nhập lại')
            old=int(input('Bạn bao nhiêu tuổi? - '))
            continue
        elif answer != 'y' or 'n':
            print('hãy nhập sự lựa chọn chính xác!')
            answer=input('có hay không? nhập y(có) hoặc n(không) - ')
            continue
    elif old < 18:
        print('Bạn có chắc bạn',old,'tuổi?')
        yorn=input('có hay không? nhập y(có) hoặc n(không) - ')
        if yorn=='y':
            print(name,'Bạn phải rời khỏi đây')
            break
        elif yorn=='n':
            print('Nhập lại')
            old=int(input('Bạn bao nhiêu tuổi? - '))
            continue
        elif answer != 'y' or 'n':
            print('hãy nhập sự lựa chọn chính xác!')
            answer=input('có hay không? nhập y(có) hoặc n(không) - ')
            continue

        
                
