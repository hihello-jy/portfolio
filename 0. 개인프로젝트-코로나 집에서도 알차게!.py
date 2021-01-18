## 이 프로젝트는 코로나로 인해 집에서 보내는 시간이 많아지면서,
## 생산적이고 알찬 하루를 만들기 위해
## 하고 싶은 활동을 선택하면 각 활동에 도움이 되는 관련 링크를 알려주고
## 각 활동들의 횟수를 카운팅해 하루에 어느 활동을 하며 보냈는지 기록해주는 프로그램입니다.

activity_name=["공부,책읽기","운동","요리","음악듣기"]
count=[0,0,0,0]

def result (choice):
    count [choice-1] += 1
    print()
    print ("누적 %s량: " %(activity_name[choice-1]), count[choice-1])
    print ("공부와 책읽기, 운동, 요리, 음악듣기", count)
    print ("---------------------------------------------------------")
    
while(1):
    print("종료:0, 공부,책읽기:1, 운동:2, 요리:3, 음악듣기:4")
    choice=int(input("원하는 활동을 선택하세요: "))

    if choice ==0:
        print()
        print("오늘 하루도 수고했어요!!!")
        print ("(최종) 공부와 책읽기, 운동, 요리, 음악듣기", count)
        break
    
    elif choice ==1:
        print("아는게 힘! 오늘은 공부를 해보자")
        print("관련 링크: https://www.youtube.com/watch?v=xtDZMnewkik")
        result(choice)
        print()
        
    elif choice ==2:
        print("몸을 건강하게! 오늘은 운동을 해보자")
        print("관련 링크: https://www.youtube.com/channel/UCxHcczukcG21up2MBe8yP_Q")
        result(choice)
        print()
        
    elif choice==3:
        print("오늘은 내가 요리왕! 요리를 해보자")
        print("관련 링크: https://www.youtube.com/channel/UCyn-K7rZLXjGl7VXGweIlcA")
        result(choice)
        print()
        
    elif choice==4:
        print("힐링타임! 오늘은 음악을 듣자")
        print("관련 링크: https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
        result(choice)
        print()

    else: #사용자가 0,1,2,3,4 가 아닌 다른 걸 입력했을 때 오류메세지와 함께 처음부터 다시 시작할 수 있도록 하였다.
        print("잘못 입력하셨습니다.(0~4 중에서 선택하세요.) 프로그램을 다시 시작합니다.")
        continue
        

