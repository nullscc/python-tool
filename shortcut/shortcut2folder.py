from win32com.client import Dispatch
import winshell
import os


def create_shortcuts(src_name, srcpath, despath):
    shell = Dispatch('WScript.Shell')
    shortcut_file = os.path.join(despath, src_name + '.lnk')
    shortcut = shell.CreateShortCut(shortcut_file)
    shortcut.Targetpath = os.path.join(srcpath, src_name)
    shortcut.WorkingDirectory = srcpath
    shortcut.save()

def recursive_create_shortcut(srcpath, despath):
    parents = os.listdir(srcpath)

    for parent in parents:
        child = os.path.join(srcpath,parent)
        if os.path.isdir(child):
            recursive_create_shortcut_of_jp(child)
        else:
            create_exe_shortcuts(parent, os.path.dirname(child), despath)

if __name__ == "__main__"
    recursive_create_shortcut(r"G:\pic", r"C:\Users\null\Desktop\sstt")