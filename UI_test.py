# -*- coding: utf-8 -*-
import subprocess
# from typing_extensions import Unpack
import uiautomation as auto
import time
import pyautogui as pag
from passdoc import pw
pw = pw.passWord()


def test():
    print(auto.GetRootControl())
    subprocess.Popen('notepad.exe')
    # you should find the top level window first, then find children from the top level window
    notepadWindow = auto.WindowControl(searchDepth=1, ClassName='Notepad')
    if not notepadWindow.Exists(3, 1):
        print('Can not find Notepad window')
        exit(0)
    print(notepadWindow)
    notepadWindow.SetTopmost(True)
    # find the first EditControl in notepadWindow
    edit = notepadWindow.EditControl()
    # usually you don't need to catch exceptions
    # but if you meet a COMError exception, put it in a try block
    try:
        # use value pattern to get or set value
        # or edit.GetPattern(auto.PatternId.ValuePattern)
        edit.GetValuePattern().SetValue('Hello')
    except auto.comtypes.COMError as ex:
        # maybe you don't run python as administrator
        # or the control doesn't have a implementation for the pattern method(I have no solution for this)
        pass
    edit.SendKeys('{Ctrl}{End}{Enter}World')
    print('current text:', edit.GetValuePattern().Value)
    # find the first TitleBarControl in notepadWindow,
    # then find the second ButtonControl in TitleBarControl, which is the Maximize button
    notepadWindow.TitleBarControl().ButtonControl(foundIndex=2).Click()
    # find the first button in notepadWindow whose Name is '关闭', the close button
    # the relative depth from Close button to Notepad window is 2
    notepadWindow.ButtonControl(searchDepth=2, Name='닫기').Click()
    # then notepad will popup a window askes you to save or not, press hotkey alt+n not to save
    auto.SendKeys('{Alt}n')


def zoom_test():
    zoom = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    # searchDepth=3, ClassName='Afx:00FF0000:b:00010003:00000006:002009C3')
    # searchDepth=3, ClassName='Afx:00FF0000:b:00010003:00000006:002009C3')

    if not zoom.Exists(3, 1):
        print('Can not find Zoom window')
        exit(0)
    print("0")
    print(zoom)
    selectByChildTree(zoom)


def selectByChildTree(zoom):

    pane = controlTracing(zoom)


def controlTracing(zoom):

    items = zoom.GetChildren()[0].GetChildren()[
        0].GetChildren()[0].GetChildren()[0].GetChildren()[2].GetChildren()[9].GetChildren()
    # print('current text:', items.GetValuePattern().Value)
    printControls(items)
# ------------------------------------------------------------------------------------------------------------------


def setEsc():
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    edit = winControl.EditControl(foundIndex=1)
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')
    edit.SendKeys('{esc}')


def def_accNumEdit_2150():
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    accNumEdit = winControl.EditControl(foundIndex=2)

    return accNumEdit


def printControlValues():
    winControl = auto.WindowControl(
        searchDepth=1, ClassName='_NFHeroMainClass')
    for i in range(1, 11):
        try:
            accNumEdit = winControl.EditControl(foundIndex=i)
            getAccValue = accNumEdit.GetValuePattern().Value
            print(f"{i} :{getAccValue}")
        except:
            print(f"{i} : 는 없음")


def printControls(items):
    for i in items:
        print(i)


def setMainSearch(menuNum):
    print(f"------------------------------------------")
    print(f"시작 : {menuNum}")
    setEsc()
    winControl = auto.WindowControl(
        searchDepth=1, Name='영웅문Global')
    edit = winControl.EditControl(foundIndex=1)
    # print(edit.GetValuePattern().Value)  # 계좌번호 가져왔다!
    editTarget = edit.GetValuePattern()
    editTarget.SetValue(menuNum)
    edit.SendKeys('{Enter}')


def kw_Login_2(user="kwak", xy=2):
    anWindow = auto.WindowControl(
        searchDepth=2, Name='영웅문Global')
    # if not anWindow.Exists(10, 1):
    #     print('Can not find Notepad window')
    #     # exit(0)
    #     return 0
    # anWindow.SetActive()
    return anWindow


if __name__ == '__main__':
    # manuList = ["2153", "2150", "2111"]
    a = kw_Login_2()
    print(str(a)[:2])
    # manuList = ["2153"]
    # for i in manuList:
    #     setMainSearch(i)
    printControlValues()
    pass
