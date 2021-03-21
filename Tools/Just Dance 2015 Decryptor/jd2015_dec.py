import os 

import binascii

import json 

import struct 

Codename = input("Codename: ")

# Musictrack

Musictrack = open(Codename.lower() + "_musictrack.tpl.ckd","rb")

musictrackbyte = Musictrack.read(1)

MarkersClip = []

SignaturesBeats = []

SignaturesClip = []

SectionsClip = []


while musictrackbyte:
  
  if binascii.hexlify(musictrackbyte) == b'80':
    
    musictrackbyte = Musictrack.read(4)
    
    if binascii.hexlify(musictrackbyte) == b'00000070':
      
      musictrackbyte = Musictrack.read(4)
      
      if binascii.hexlify(musictrackbyte) == b'0000004c':
        
        # Markers
        
        lenMarkers = struct.unpack("!I",Musictrack.read(4))[0]
        
        for x in range(lenMarkers):
          
          Beats = struct.unpack("!I",Musictrack.read(4))[0]
        
          MarkersClip.append(Beats)
        
        # Signatures
        
        for x in range(4):
          
          
          Signatures = {}
          
          musictrackbyte = struct.unpack("!I",Musictrack.read(4))[0]
          
          SignaturesBeats.append(musictrackbyte)
          
        Signatures["__class"] = "MusicSignature"
          
        Signatures["marker"] = SignaturesBeats[0]
          
        Signatures["beats"] = SignaturesBeats[1]
          
        SignaturesClip.append(Signatures)
        
        # Sections 
        
        lenSections = struct.unpack("!I",Musictrack.read(4))[0]
        
        for x in range(lenSections):
          
          
          
          Class = binascii.hexlify(Musictrack.read(4))
          
          Marker = struct.unpack("!I",Musictrack.read(4))[0]
          
          SectionType = struct.unpack("!I",Musictrack.read(4))[0]
          CommomLenght = binascii.hexlify(Musictrack.read(4))
          
          Sections = {"__class":"MusicSection","marker":Marker,"sectionType":SectionType,"comment":""}
          
          SectionsClip.append(Sections)
          
        for x in range(2):
          
          musictrackbyte = Musictrack.read(4)
        
        # VideoStartTime
        
        VideoStartTime = struct.unpack(">f",Musictrack.read(4))[0]
        
        
        
        StrVideoStartTime = str(VideoStartTime)[0:9]
      # MusictrackDecrypted
      
      DecryptedMusictrack = {"__class":"Actor_Template","WIP":0,"LOWUPDATE":0,"UPDATE_LAYER":0,"PROCEDURAL":0,"STARTPAUSED":0,"FORCEISENVIRONMENT":0,"COMPONENTS":[{"__class":"MusicTrackComponent_Template","trackData":{"__class":"MusicTrackData","structure":{"__class":"MusicTrackStructure","markers": MarkersClip
        ,"signatures": SignaturesClip
        ,"sections": SectionsClip
        ,"startBeat":0,"endBeat":lenMarkers,"fadeStartBeat":0,"useFadeStartBeat":False,"fadeEndBeat":0,"useFadeEndBeat":False,"videoStartTime":float(StrVideoStartTime),"previewEntry":48,"previewLoopStart":48,"previewLoopEnd":144,"volume":0,"fadeInDuration":0,"fadeInType":0,"fadeOutDuration":0,"fadeOutType":0},"path":"world/maps/" + Codename.lower() + "/audio/" + Codename.lower() + ".wav","url":"jmcs://jd-contents/" + Codename + "/" + Codename + ".ogg"}}]}
      
        
      with open(Codename + "_decrypted_musictrack.tpl.ckd","w") as g:
          
        g.write(json.dumps(DecryptedMusictrack))
        g.close()
          
  musictrackbyte = Musictrack.read(1)

# Ktape 

Ktape = open(Codename.lower() + "_tml_karaoke.ktape.ckd","rb")

KtapeBytes = Ktape.read(1)

KtapeClips = []

while KtapeBytes:
  
  if binascii.hexlify(KtapeBytes) == b'68':
    
    KtapeBytes = Ktape.read(7)
    
    if binascii.hexlify(KtapeBytes) == b'552a4100000050':
      
      KtapeId = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeTrackId = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeIsActive = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeStartTime = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeDuration = struct.unpack("!I",Ktape.read(4))[0]
      
      Pitch = struct.unpack("!I",Ktape.read(4))[0]
      
      LenLyrics = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeLyrics = Ktape.read(LenLyrics)
      
      KtapeIsEndOfLine = struct.unpack("!I",Ktape.read(4))[0]
      
      KtapeClass = {}
      
      KtapeClass["__class"] = "Tape"
      
      KtapeDecrypted = {"__class":"KaraokeClip","Id":KtapeId,"TrackId":KtapeTrackId,"IsActive":KtapeIsActive,"StartTime":KtapeStartTime,"Duration":KtapeDuration,"Pitch":8.661958,"Lyrics":KtapeLyrics.decode("utf-8"),"IsEndOfLine":KtapeIsEndOfLine,"ContentType":1,"StartTimeTolerance":4,"EndTimeTolerance":4,"SemitoneTolerance":5}
      
      KtapeClips.append(KtapeDecrypted)
      
      KtapeClass["Clips"] = KtapeClips
      
      KtapeClass["TapeClock"] = 0 
      
      KtapeClass["TapeBarCount"] = 1 
      KtapeClass["FreeResourcesAfterPlay"] = 0 
      
      KtapeClass["MapName"] = Codename
      
      KtapeClass["SoundwichEvent"] = ""
    
  KtapeBytes = Ktape.read(1)
  

with open(Codename.lower() + "_Decrypted_karaoke.ktape.ckd","w") as g:
  
  g.write(json.dumps(KtapeClass))
  g.close()
  

# Dtape 

Dtape = open(Codename.lower() + "_tml_dance.dtape.ckd","rb")

DtapeBytes = Dtape.read(1)

DtapeClips = []

while DtapeBytes:
  
  if binascii.hexlify(DtapeBytes) == b'95':
    
    DtapeClass = {}
    DtapeBytes = Dtape.read(7)
      
    if binascii.hexlify(DtapeBytes) == b'5384a100000070':
        
        DtapeId = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeTrackId = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeIsActive = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeStartTime = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeDuration = struct.unpack("!I",Dtape.read(4))[0]
        
        lenNameMsm = struct.unpack("!I",Dtape.read(4))[0]
        
        NameMsm = Dtape.read(lenNameMsm)
        
        lenPath = struct.unpack("!I",Dtape.read(4))[0]
        
        Path = Dtape.read(lenPath)
        
        DtapeBytes = Dtape.read(4)
        
        DtapeBytes = Dtape.read(4)
        
        goldMove = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeCoachId = struct.unpack("!I",Dtape.read(4))[0]
        
        DtapeClass["__class"] = "Tape"

      
        MotionClip = {"__class":"MotionClip","Id":DtapeId,"TrackId":DtapeTrackId,"IsActive":DtapeIsActive,"StartTime":DtapeStartTime,"Duration":DtapeDuration,"ClassifierPath":Path.decode("utf-8") + NameMsm.decode("utf-8"),"GoldMove":goldMove,"CoachId":DtapeCoachId,"MoveType":0,"Color":[1,0.988235,0.592157,0.572549],"MotionPlatformSpecifics":{"X360":{"__class":"MotionPlatformSpecific","ScoreScale":1,"ScoreSmoothing":0,"LowThreshold":0.200000,"HighThreshold":1},"ORBIS":{"__class":"MotionPlatformSpecific","ScoreScale":1,"ScoreSmoothing":0,"LowThreshold":-0.200000,"HighThreshold":0.600000},"DURANGO":{"__class":"MotionPlatformSpecific","ScoreScale":1,"ScoreSmoothing":0,"LowThreshold":0.200000,"HighThreshold":1}}}
        
        DtapeClips.append(MotionClip)
        
        if goldMove == 1:
          
        
          GoldEffectClip = {"__class":"GoldEffectClip","Id":DtapeId,"TrackId":DtapeTrackId,"IsActive":1,"StartTime":DtapeStartTime,"Duration":DtapeDuration,"EffectType":1}
          
          
          DtapeClips.append(GoldEffectClip)
          
        else:
          pass
        
  if binascii.hexlify(DtapeBytes) == b'52':
    
    DtapeBytes = Dtape.read(7)
    
    if binascii.hexlify(DtapeBytes) == b'ec896200000038':
      
      PictoId = struct.unpack("!I",Dtape.read(4))[0]
      
      PictoTrackId = struct.unpack("!I",Dtape.read(4))[0]
      
      PictoIsActive = struct.unpack("!I",Dtape.read(4))[0]
      
      PictoStartTime = struct.unpack("!I",Dtape.read(4))[0]
      
      PictoDuration = struct.unpack("!I",Dtape.read(4))[0]
      
      lenNamePicto = struct.unpack("!I",Dtape.read(4))[0]
      
      NamePicto = Dtape.read(lenNamePicto)
      
      lenPictoPath = struct.unpack("!I",Dtape.read(4))[0]
      
      PictoPath = Dtape.read(lenPictoPath)
      
      PictogramClip = {"__class":"PictogramClip","Id":PictoId,"TrackId":PictoTrackId,"IsActive":PictoIsActive,"StartTime":PictoStartTime,"Duration":PictoDuration,"PictoPath":PictoPath.decode("utf-8") + NamePicto.decode("utf-8"),"CoachCount":4294967295}
      
      DtapeClips.append(PictogramClip)
    
      DtapeClass["__class"] = "Tape"
      
      DtapeClass["Clips"] = DtapeClips
      
      DtapeClass["TapeClock"] = 0 
      
      DtapeClass["TapeBarCount"] = 1 
      DtapeClass["FreeResourcesAfterPlay"] = 0 
      
      DtapeClass["MapName"] = Codename
      
      DtapeClass["SoundwichEvent"] = ""
      
      
      
      
      
  DtapeBytes = Dtape.read(1)
  

with open(Codename.lower() + "_Decrypted_dance.dtape.ckd","w") as g:
  
  g.write(json.dumps(DtapeClass))
  g.close()

print("Decrypted With Sucess")
