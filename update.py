#-*- coding: utf-8-*-
import requests
import codecs
from codecs import open
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

addresses=[
"https://addons.nvda-project.org/addons/trainingKeyboardCommands.es.html",
"https://addons.nvda-project.org/addons/outlookExtended.es.html",
"https://addons.nvda-project.org/addons/columnsReview.es.html",
"https://addons.nvda-project.org/addons/AudioChart.es.html",
"https://addons.nvda-project.org/addons/BluetoothAudio.es.html",
"https://addons.nvda-project.org/addons/textnav.es.html",
"https://addons.nvda-project.org/addons/calibre.es.html",
"https://addons.nvda-project.org/addons/systrayList.es.html",
"https://addons.nvda-project.org/addons/dropbox.es.html",
"https://addons.nvda-project.org/addons/extendedWinamp.es.html",
"https://addons.nvda-project.org/addons/ocr.es.html",
"https://addons.nvda-project.org/addons/unicodeBrailleInput.es.html",
"https://addons.nvda-project.org/addons/resourceMonitor.es.html",
"https://addons.nvda-project.org/addons/controlUsageAssistant.es.html",
"https://addons.nvda-project.org/addons/placeMarkers.es.html",
"https://addons.nvda-project.org/addons/virtualRevision.es.html",
"https://addons.nvda-project.org/addons/noBeepsSpeechMode.es.html",
"https://addons.nvda-project.org/addons/focusHighlight.es.html",
"https://addons.nvda-project.org/addons/eMule.es.html",
"https://addons.nvda-project.org/addons/emoticons.es.html",
"https://addons.nvda-project.org/addons/goldwave.es.html",
"https://addons.nvda-project.org/addons/readFeeds.es.html",
"https://addons.nvda-project.org/addons/bitChe.es.html",
"https://addons.nvda-project.org/addons/enhancedTouchGestures.es.html",
"https://addons.nvda-project.org/addons/clipContentsDesigner.es.html",
"https://addons.nvda-project.org/addons/dualvoice.es.html",
"https://addons.nvda-project.org/addons/newfon.es.html",
"https://addons.nvda-project.org/addons/easyTableNavigator.es.html",
"https://addons.nvda-project.org/addons/teamtalk.es.html",
"https://addons.nvda-project.org/addons/nvdaremote.es.html",
"https://addons.nvda-project.org/addons/wintenApps.es.html",
"https://addons.nvda-project.org/addons/vlc.es.html",
"https://addons.nvda-project.org/addons/dayOfTheWeek.es.html",
"https://addons.nvda-project.org/addons/goldenCursor.es.html",
"https://addons.nvda-project.org/addons/tipOfTheDay.es.html",
"https://addons.nvda-project.org/addons/crashHero.es.html",
"https://addons.nvda-project.org/addons/mp3DirectCut.es.html",
"https://addons.nvda-project.org/addons/toneMaster.es.html",
"https://addons.nvda-project.org/addons/stationPlaylist.es.html",
"https://addons.nvda-project.org/addons/reportSymbols.es.html",
"https://addons.nvda-project.org/addons/switchSynth.es.html",
"https://addons.nvda-project.org/addons/objPad.es.html",
"https://addons.nvda-project.org/addons/weatherPlus.es.html",
"https://addons.nvda-project.org/addons/classicSelection.es.html",
"https://addons.nvda-project.org/addons/AudioThemes3D.es.html",
"https://addons.nvda-project.org/addons/reviewCursorCopier.es.html",
"https://addons.nvda-project.org/addons/clipspeak.es.html",
"https://addons.nvda-project.org/addons/speakPasswords.es.html",
"https://addons.nvda-project.org/addons/speech_history.es.html",
"https://addons.nvda-project.org/addons/lambda.es.html",
"https://addons.nvda-project.org/addons/enhancedAria.es.html",
"https://addons.nvda-project.org/addons/objLocationTones.es.html",
"https://addons.nvda-project.org/addons/sayCurrentKeyboardLanguage.es.html",
"https://addons.nvda-project.org/addons/mozillaScripts.es.html",
"https://addons.nvda-project.org/addons/indentNav.es.html",
"https://addons.nvda-project.org/addons/brailleExtender.es.html",
"https://addons.nvda-project.org/addons/sentenceNav.es.html",
"https://addons.nvda-project.org/addons/textInformation.es.html",
"https://addons.nvda-project.org/addons/access8math.es.html",
"https://addons.nvda-project.org/addons/inputLock.es.html",
"https://addons.nvda-project.org/addons/toolbarsExplorer.es.html",
"https://addons.nvda-project.org/addons/screenCurtain.es.html",
"https://addons.nvda-project.org/addons/addonUpdater.es.html",
"https://addons.nvda-project.org/addons/bgtLullaby.es.html",
"https://addons.nvda-project.org/addons/mirc.es.html",
"https://addons.nvda-project.org/addons/mushClient.es.html",
"https://addons.nvda-project.org/addons/consoleTimer.es.html",
"https://addons.nvda-project.org/addons/visualStudio.es.html",
"https://addons.nvda-project.org/addons/speechPlayerInEspeak.es.html",
"https://addons.nvda-project.org/addons/ventrilo.es.html",
"https://addons.nvda-project.org/addons/clock.es.html",
"https://addons.nvda-project.org/addons/nvSpeechPlayer.es.html",
"https://addons.nvda-project.org/addons/pcKeyboardBrailleInput.es.html",
"https://addons.nvda-project.org/addons/quickBooks2014.es.html",
"https://addons.nvda-project.org/addons/teamViewer.es.html",
"https://addons.nvda-project.org/addons/word.es.html",
"https://addons.nvda-project.org/addons/instantTranslate.es.html"
]
warnings={
"sentenceNav":"Alteración de fuente: URL externa de complemento sustituida por propia",
}

for a in addresses:
	r=requests.get(a)
	f=open(a.split("/")[-1], "w", encoding="utf-8")
	f.write(r.content.split('<div id="content">')[-1].split("</div>")[0])
	f.close()
for b in warnings:
	print(u"Advertencia en %s: %s. Téngase en cuenta en la edición."%(b, warnings[b]))
