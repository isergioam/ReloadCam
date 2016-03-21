#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#Refrescador automatico de clines
#Creado por Dagger

import ReloadCam_Main, ReloadCam_Helper

def GetVersion():
    return 1

#Filename must start with Server, classname and argument must be the same!
class Mario(ReloadCam_Main.Server):

    def GetUrl(self, serverNo):
        #Pon un breakpoint aqui si quieres ver la URL verdadera ;)

        if (serverNo < 4):
            realUrl = ReloadCam_Helper.Decrypt("maanpH1wfOnc453OxaObopempK7fk-DakLGSpJyjcq5-oZU=")
        elif (serverNo > 4 and serverNo < 9):
            realUrl = ReloadCam_Helper.Decrypt("maanpH1wfOnc453OxaObopempK7fk-DakLGSpJyjcq5_oZU=")
        elif (serverNo > 9):
            realUrl = ReloadCam_Helper.Decrypt("maanpH1wfOnc453OxaObopempK7fk-DakLGSpJyjcq6AoZU=")
        
        realUrl = realUrl + str(serverNo)
        return realUrl

    def GetClines(self):
        print "Now getting Mario clines!"
        marioClines = []
        marioClines.append(self.__GetMarioCline(1))
        marioClines.append(self.__GetMarioCline(2))
        marioClines.append(self.__GetMarioCline(3))
        marioClines.append(self.__GetMarioCline(4))
        marioClines.append(self.__GetMarioCline(5))
        marioClines.append(self.__GetMarioCline(6))
        marioClines.append(self.__GetMarioCline(7))
        marioClines.append(self.__GetMarioCline(8))
        marioClines.append(self.__GetMarioCline(9))
        marioClines.append(self.__GetMarioCline(10))
        marioClines.append(self.__GetMarioCline(11))
        marioClines.append(self.__GetMarioCline(12))
        return filter(None, marioClines)

    def __GetMarioCline(self, serverNo):
        htmlCode = ReloadCam_Helper.GetHtmlCode(None, self.GetUrl(serverNo))
        cline = ReloadCam_Helper.FindStandardClineInText(htmlCode)
        if cline != None and ReloadCam_Helper.TestCline(cline):
            return cline
        return None