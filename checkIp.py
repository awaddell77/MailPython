import subprocess

def checkIp():
    res = subprocess.check_output('curl ipv4bot.whatismyipaddress.com', shell=True)
    return str(res)
