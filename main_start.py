from def_lotto import *
from slack_engin import *
from main_vr import vr_main
from def_kw import startGlobal, save_stockQty, saveMyDeposit, startGlobal, saveMyRevenue
from def_ss import *

# for key, value in rsiResult().items():
#     slackSendMsg_rsi_check(f"{key}  : {value}")

if __name__ == '__main__':
    # startGlobal()
    # kw_Login_2("kwak")
    # save_stockQty("kwak", "무매", "45")
    # saveMyDeposit("kwak", "무매", "45")
    saveMyRevenue("kwak", "무매", "45")
    pass