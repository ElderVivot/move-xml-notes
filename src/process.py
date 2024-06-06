import logging
import os
import shutil

logger = logging.getLogger(__name__)


class ProcessXmls(object):
    def __init__(self, pathWithXmls, fileNameFilter, pathReplaceName) -> None:
        self.__pathWithXmls = pathWithXmls
        self.__fileNameFilter = fileNameFilter
        self.__pathToReplace = pathReplaceName.split('|')[0]
        self.__pathDest = pathReplaceName.split('|')[1]

    def __moveFiles(self, pathFile, pathDest):
        try:
            shutil.move(pathFile, pathDest)
        except Exception as e:
            print(e)

    def process(self):
        for folder, _, files in os.walk(self.__pathWithXmls):
            for f in files:
                if (f.find(self.__fileNameFilter) < 0 and self.__fileNameFilter != "") or f.find('.xml') < 0:
                    continue
                pathFile = f'{folder}/{f}'
                pathDest = folder.replace(self.__pathToReplace, self.__pathDest)
                if os.path.exists(pathDest) is False:
                    os.makedirs(pathDest)
                pathDest = f'{pathDest}/{f}'
                print('Movendo arquivo', pathFile, pathDest, sep=' | ')
                self.__moveFiles(pathFile, pathDest)
