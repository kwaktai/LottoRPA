from def_lotto import kw_Login, openLoto, kw_close
import time
from slack_engin import *
from def_kw import get_today_hoilday, startGlobal
import logging
import traceback


def user_name():
    pass


if __name__ == '__main__':
    try:
        if get_today_hoilday() is True:
            user = "han"
            startGlobal()
            kw_Login(user)
            time.sleep(30)
            slackSendMsg(f"{user}의 무한매수가 시작합니다.")
            openLoto(user=user)
            time.sleep(30)
            # closeLoto()
            time.sleep(10)
            # mess = check_message_lotto()
            # if mess == None:
            #     slackSendMsg(f"{user}의 무한매수를 완료하였습니다.")
            # else:
            #     slackSendMsg(mess)
            slackSendMsg(f"{user}의 무한매수를 완료합니다.")
            # save_screenshot(user)
            # kw_close()
            slackSendMsg(f"{user}의 영운문(Global)를 종료합니다.")
            startGlobal()
        else:
            slackSendMsg("주말 입니다.({user})")
    except:
        slackSendMsg(f"{user} : 에러발생 확인바람.")
        startGlobal()
        logging.error(traceback.format_exc())
