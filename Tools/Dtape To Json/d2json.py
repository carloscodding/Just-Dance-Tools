import json 

import os 


import matplotlib


try:
  os.mkdir("Input")
  os.mkdir("Output")

except:
  
  print("D2JSON By Carlos_")
  
  # Timelines
  Codename = input("Codename: ")
  
  with open("Input//songdesc.tpl.ckd") as jsonfile:
    songdesc = json.load(jsonfile)
    
  with open("Input//" + Codename + "_musictrack.tpl.ckd") as jsonfile:
    musictrack = json.load(jsonfile)
    
  with open("Input//" + Codename + "_tml_karaoke.ktape.ckd") as jsonfile:
    ktape = json.load(jsonfile)
  
  with open("Input//" + Codename + "_tml_dance.dtape.ckd") as jsonfile:
    
    dtape = json.load(jsonfile)
    

  # Input Json 
  
  BeatsSeparator = []
  
  LyricsSeparator = []
  
  PictosSeparator = []
  
  
  for musictrack_components in musictrack["COMPONENTS"]:

    markers = musictrack_components["trackData"]["structure"]["markers"]
    
    previewentry = musictrack_components["trackData"]["structure"]["previewEntry"]
    
    previewloopstart = musictrack_components["trackData"]["structure"]["previewLoopStart"]
    
    
    for markers in markers:
      
      beats = markers /48 
    
      
      BeatsSeparator.append(int(beats))
    
    division = 2502.66305525460462 / (60000 / (BeatsSeparator[30] - BeatsSeparator[29]))
  
  for ktape_clips in ktape["Clips"]:
    Lyrics = {}
    
    time = ktape_clips["StartTime"]
    
    TimeCount = time * division
    
    duration = ktape_clips["Duration"]
    
    DurationCount = duration * division
    
    text = ktape_clips["Lyrics"]
    
    isendofline = ktape_clips["IsEndOfLine"]
    
    
    Lyrics["time"] = int(TimeCount)
    Lyrics["duration"] = int(DurationCount)
    Lyrics["text"] = text
    Lyrics["isLineEnding"] = isendofline

    LyricsSeparator.append(Lyrics)
  

    
  for clips in dtape["Clips"]:
    if clips["__class"] == "PictogramClip":
      
      Pictos = {}
      
      PictoTime = clips["StartTime"] * division
      
      PictoDuration = clips["Duration"] * division
      
      
      PictoName = clips["PictoPath"].replace("world/maps/" + Codename.lower() + "/timeline/pictos/","").replace(".png","")
      
      Pictos["time"] = int(PictoTime)
      
      Pictos["duration"] = int(PictoDuration)
      
      Pictos["name"] = PictoName
      
      PictosSeparator.append(Pictos)
      
    
    
  for Song_Components in songdesc["COMPONENTS"]:
    
    pass
    
    
    
    
  inputjson = {
  "MapName": Codename,
  "JDVersion": 2021,
  "OriginalJDVersion": 2021,
  "Artist": Song_Components["Artist"],
  "Title": Song_Components["Title"],
  "Credits": Song_Components["Credits"],
  "NumCoach": Song_Components["NumCoach"],
  "CountInProgression": 1,
  "DancerName": "Unknown Dancer",
  "LocaleID": Song_Components["LocaleID"],
  "MojoValue": 0,
  "Mode": 6,
  "Status": 3,
  "LyricsType": 0,
  "BackgroundType": 0,
  "Difficulty": Song_Components["Difficulty"],
  "DefaultColors": {
    "lyrics": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["lyrics"],keep_alpha = True).replace("#","0x")),
    "theme": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["theme"],keep_alpha = True).replace("#","0x")),
    "songColor_1A": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["songcolor_1a"],keep_alpha = True).replace("#","0x")),
    "songColor_1B": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["songcolor_1b"],keep_alpha = True).replace("#","0x")),
    "songColor_2A": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["songcolor_2a"],keep_alpha = True).replace("#","0x")),
    "songColor_2B": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["songcolor_2b"],keep_alpha = True).replace("#","0x"))
  },  
  "lyricsColor": str(matplotlib.colors.to_hex(Song_Components["DefaultColors"]["lyrics"],keep_alpha = True).replace("#ff","#")),
  "videoOffset": BeatsSeparator[0],
  "beats": BeatsSeparator,
  "lyrics": LyricsSeparator,
  "pictos": PictosSeparator,
  "AudioPreview": {
    "coverflow": {
      "startbeat": previewentry
    },
    "prelobby": {
      "startbeat": previewloopstart
    }
  },
  "AudioPreviewFadeTime": 0.5
}
  
  with open("Output//" + Codename + ".json","w") as g:
    g.write(json.dumps(inputjson,ensure_ascii=False))
    
    g.close()
    
  
  # Input Moves 
  
  if Song_Components["NumCoach"] == 1:
    
    MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 0:
          
          Moves0 = {}
          
          Moves0Time = moves["StartTime"] * division
          
          Moves0Duration = moves["Duration"] * division
          
          Moves0Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves0["name"] = Moves0Name
              
            Moves0["time"] = int(Moves0Time)
              
            Moves0["duration"] = int(Moves0Duration)
              
            MovesSeparator.append(Moves0)
              
              
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves0Time:
              
              Moves0["name"] = Moves0Name
              
              Moves0["time"] = int(Moves0Time)
              
              Moves0["duration"] = int(Moves0Duration)
              
              Moves0["goldMove"] = 1
              
              MovesSeparator.append(Moves0)
          
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
            
            
  if Song_Components["NumCoach"] == 2:
    
    MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 0:
          
          Moves0 = {}
          
          Moves0Time = moves["StartTime"] * division
          
          Moves0Duration = moves["Duration"] * division
          
          Moves0Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves0["name"] = Moves0Name
              
            Moves0["time"] = int(Moves0Time)
              
            Moves0["duration"] = int(Moves0Duration)
              
            MovesSeparator.append(Moves0)
              
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves0Time:
              
              Moves0["name"] = Moves0Name
              
              Moves0["time"] = int(Moves0Time)
              
              Moves0["duration"] = int(Moves0Duration)
              
              Moves0["goldMove"] = 1
              
              MovesSeparator.append(Moves0)
          
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
        
        elif moves["CoachId"] == 1:
          
          MovesSeparator = []
        
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 1:
          
          Moves1 = {}
          
          Moves1Time = moves["StartTime"] * division
          
          Moves1Duration = moves["Duration"] * division
          
          Moves1Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves1["name"] = Moves1Name
              
            Moves1["time"] = int(Moves1Time)
              
            Moves1["duration"] = int(Moves1Duration)
              
            MovesSeparator.append(Moves1)
              
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves1Time:
              
              Moves1["name"] = Moves1Name
              
              Moves1["time"] = int(Moves1Time)
              
              Moves1["duration"] = int(Moves1Duration)
              
              Moves1["goldMove"] = 1
              
              MovesSeparator.append(Moves1)
          
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
  
  if Song_Components["NumCoach"] == 3:
    
    MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 0:
          
          Moves0 = {}
          
          Moves0Time = moves["StartTime"] * division
          
          Moves0Duration = moves["Duration"] * division
          
          Moves0Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves0["name"] = Moves0Name
              
            Moves0["time"] = int(Moves0Time)
              
            Moves0["duration"] = int(Moves0Duration)
              
            MovesSeparator.append(Moves0)
              
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves0Time:
              
              Moves0["name"] = Moves0Name
              
              Moves0["time"] = int(Moves0Time)
              
              Moves0["duration"] = int(Moves0Duration)
              
              Moves0["goldMove"] = 1
              
              MovesSeparator.append(Moves0)
          
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
        
        elif moves["CoachId"] == 1:
          
          MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 1:
          
          Moves1 = {}
          
          Moves1Time = moves["StartTime"] * division
          
          Moves1Duration = moves["Duration"] * division
          
          Moves1Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves1["name"] = Moves1Name
              
            Moves1["time"] = int(Moves1Time)
              
            Moves1["duration"] = int(Moves1Duration)
              
            MovesSeparator.append(Moves1)
              
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves1Time:
              
              Moves1["name"] = Moves1Name
              
              Moves1["time"] = int(Moves1Time)
              
              Moves1["duration"] = int(Moves1Duration)
              
              Moves1["goldMove"] = 1
              
              MovesSeparator.append(Moves1)
          
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
            
        
        elif moves["CoachId"] == 2:

          Moves2Separator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 2:
          
          Moves2 = {}
          
          Moves2Time = moves["StartTime"] * division
          
          Moves2Duration = moves["Duration"] * division
          
          Moves2Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves2["name"] = Moves2Name
              
            Moves2["time"] = int(Moves2Time)
              
            Moves2["duration"] = int(Moves2Duration)
              
            Moves2Separator.append(Moves2)
              
          with open("Output//" + Codename + "_moves2.json","w") as g:
            g.write(json.dumps(Moves2Separator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves2Time:
              
              Moves2["name"] = Moves2Name
              
              Moves2["time"] = int(Moves2Time)
              
              Moves2["duration"] = int(Moves2Duration)
              
              Moves2["goldMove"] = 1
              
              Moves2Separator.append(Moves2)
          
          with open("Output//" + Codename + "_moves2.json","w") as g:
            g.write(json.dumps(Moves2Separator))
            g.close()
  
  if Song_Components["NumCoach"] == 4:
    
    MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 0:
          
          Moves0 = {}
          
          Moves0Time = moves["StartTime"] * division
          
          Moves0Duration = moves["Duration"] * division
          
          Moves0Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".png","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves0["name"] = Moves0Name
              
            Moves0["time"] = int(Moves0Time)
              
            Moves0["duration"] = int(Moves0Duration)
              
            MovesSeparator.append(Moves0)
              
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves0Time:
              
              Moves0["name"] = Moves0Name
              
              Moves0["time"] = int(Moves0Time)
              
              Moves0["duration"] = int(Moves0Duration)
              
              Moves0["goldMove"] = 1
              
              MovesSeparator.append(Moves0)
          
          with open("Output//" + Codename + "_moves0.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
        
        elif moves["CoachId"] == 1:
          
          MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 1:
          
          Moves1 = {}
          
          Moves1Time = moves["StartTime"] * division
          
          Moves1Duration = moves["Duration"] * division
          
          Moves1Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves1["name"] = Moves0Name
              
            Moves1["time"] = int(Moves1Time)
              
            Moves1["duration"] = int(Moves1Duration)
              
            MovesSeparator.append(Moves1)
              
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves1Time:
              
              Moves1["name"] = Moves1Name
              
              Moves1["time"] = int(Moves1Time)
              
              Moves1["duration"] = int(Moves1Duration)
              
              Moves1["goldMove"] = 1
              
              MovesSeparator.append(Moves1)
          
          with open("Output//" + Codename + "_moves1.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
            
        
        elif moves["CoachId"] == 2:

          Moves2Separator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 2:
          
          Moves2 = {}
          
          Moves2Time = moves["StartTime"] * division
          
          Moves2Duration = moves["Duration"] * division
          
          Moves2Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves2["name"] = Moves2Name
              
            Moves2["time"] = int(Moves2Time)
              
            Moves2["duration"] = int(Moves2Duration)
              
            MovesSeparator.append(Moves2)
              
          with open("Output//" + Codename + "_moves2.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves2Time:
              
              Moves2["name"] = Moves2Name
              
              Moves2["time"] = int(Moves2Time)
              
              Moves2["duration"] = int(Moves2Duration)
              
              Moves2["goldMove"] = 1
              
              MovesSeparator.append(Moves2)
          
          with open("Output//" + Codename + "_moves2.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
        elif moves["CoachId"] == 3:

          MovesSeparator = []
    
    for moves in dtape["Clips"]:

      if moves["__class"] == "MotionClip":
        
        if moves["CoachId"] == 3:
          
          Moves3 = {}
          
          Moves3Time = moves["StartTime"] * division
          
          Moves3Duration = moves["Duration"] * division
          
          Moves3Name = moves["ClassifierPath"].replace("world/maps/" + Codename.lower() + "/timeline/moves/","").replace(".msm","")
          
          GoldMove = moves["GoldMove"]
          
          if GoldMove == 0:
            Moves3["name"] = Moves3Name
              
            Moves3["time"] = int(Moves3Time)
              
            Moves3["duration"] = int(Moves3Duration)
              
            MovesSeparator.append(Moves3)
              
          with open("Output//" + Codename + "_moves3.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
        
          
          if GoldMove == 1:
            GoldMoveTime = moves["StartTime"]* division
            
            if GoldMoveTime == Moves3Time:
              
              Moves3["name"] = Moves3Name
              
              Moves3["time"] = int(Moves3Time)
              
              Moves3["duration"] = int(Moves3Duration)
              
              Moves3["goldMove"] = 1
              
              MovesSeparator.append(Moves3)
          
          with open("Output//" + Codename + "_moves3.json","w") as g:
            g.write(json.dumps(MovesSeparator))
            g.close()
