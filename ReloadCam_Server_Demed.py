#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines
#Creado por Dagger

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Demed(ReloadCam_Main.Server):

    def GetUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt('maanpH1wfNbK2dTFkp-hYJ2zb7zkzJvYz8iWqmGkq7E=')
        return realUrl

    def GetRedirectUrl(self):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)
        realUrl = ReloadCam_Helper.Decrypt("maanpH1wfNfRzdjU15KhqJ1xr7yfztydxNNfp55j")
        return realUrl

    def GetClines(self):
        print "Now getting Demed clines!"
        demedClines = []
        demedClines.append(self.__GetDemedCline())
        return filter(None, demedClines)

    def __GetDemedCline(self):

        values= {
            'user': ReloadCam_Helper.GetRandomString(5),
            'pass': 'demed',
            'submit':'Active User!'
        }

        htmlCode = ReloadCam_Helper.GetPostHtmlCode(values, None, self.GetUrl())
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None

