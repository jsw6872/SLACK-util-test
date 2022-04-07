import slack_noti
import inspect

def sum(a,b):
    return a+b

if __name__ == '__main__':
    sum(1,4)
    slack_noti.main(f'{inspect.getfile(inspect.currentframe())} 실행이 완료 됐습니다.')