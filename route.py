# -*- coding: utf-8 -

# This file - route.py, is part of directord.

import re

def dispatchvod (medianame):
        return "192.168.1.13"

def route (medianame):
        if re.match ("^VOD\S+", medianame): # VOD find
                return dispatchvod (medianame)

        if re.match ("^41243\S+", medianame): # CCTV-1 find
                return "192.168.1.15"

        if re.match ("^41242\S+", medianame): # CCTV-2 find
                return "192.168.1.15"

        if re.match ("^41241\S+", medianame): # CCTV-3 find
                return "192.168.1.15"

        if re.match ("^41240\S+", medianame): # CCTV-4 find
                return "192.168.1.15"

        if re.match ("^41239\S+", medianame): # CCTV-5 find
                return "192.168.1.15"

        if re.match ("^41238\S+", medianame): # CCTV-6 find
                return "192.168.1.15"

        if re.match ("^41237\S+", medianame): # CCTV-8 find
                return "192.168.1.15"

        if re.match ("^41236\S+", medianame): # CCTV-10 find
                return "192.168.1.15"

        if re.match ("^41235\S+", medianame): # CCTV-xinwen find
                return "192.168.1.15"

        if re.match ("^41234\S+", medianame): # An Hui find
                return "192.168.1.15"

        if re.match ("^41233\S+", medianame): # Hu Nani find
                return "192.168.1.15"

        if re.match ("^41232\S+", medianame): # Dong Fang Wei Shi find
                return "192.168.1.15"

        if re.match ("^41231\S+", medianame): # Zhe Jiang Wei Shi  find
                return "192.168.1.15"

        if re.match ("^41230\S+", medianame): # Jiang Su Wei Shi find
                return "192.168.1.15"

        if re.match ("^41229\S+", medianame): # Chang Zhou Xin Wen find
                return "192.168.1.15"

        if re.match ("^41228\S+", medianame): # Hu Bei Wei Shi find
                return "192.168.1.15"

        if re.match ("^41227\S+", medianame): # Shan Dong Wei Shi find
                return "192.168.1.15"

        if re.match ("^41226\S+", medianame): # Guang Dong Wei Shi find
                return "192.168.1.15"

        if re.match ("^41225\S+", medianame): # Wu Jin Xin Wen  find
                return "192.168.1.15"

        if re.match ("^41224\S+", medianame): # He Nan Wei Shi find
                return "192.168.1.15"

        if re.match ("^41223\S+", medianame): # Dong Zuo Dian Ying find
                return "192.168.1.15"

        if re.match ("^41222\S+", medianame): # Jia Ting Ying Yuan find
                return "192.168.1.15"

        if re.match ("^41221\S+", medianame): # Di Yi Ju Chang find
                return "192.168.1.15"

        if re.match ("^41220\S+", medianame): # 7 Cai xi ju find
                return "192.168.1.15"

        if re.match ("^41219\S+", medianame): # Feng Yun Yin Yue find
                return "192.168.1.15"

        if re.match ("^41218\S+", medianame): # You Xi Feng Yun find
                return "192.168.1.15"

        if re.match ("^41217\S+", medianame): # Dong Man Xiu Chang find
                return "192.168.1.15"

        if re.match ("^41216\S+", medianame): # Jin Bao Ti Yu find
                return "192.168.1.15"

        if re.match ("^412156\S+", medianame): # Feng Yun Zu Qiu find
                return "192.168.1.15"

        if re.match ("^41214\S+", medianame): # 4 Hai Diao Yu find
                return "192.168.1.15"

        return None

if __name__ == "__main__":
        medianame = "VODC2011011613583204.ts"
        print "%s ---> %s" % (medianame, route (medianame))
        medianame = "1234VODC2011011613583204.ts"
        print "%s ---> %s" % (medianame, route (medianame))
