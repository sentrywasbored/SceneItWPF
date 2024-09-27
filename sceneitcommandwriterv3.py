def write_sceneit_allPlay(packName, VTS ,startPGC, endPGC):
  index = startPGC
  with open(packName+'_pullAllPlay_VTS0'+str(VTS)+'.bat','w') as f:
    while index < (endPGC+1):
      f.write("mkdir .\AllPlayClips\VTS_0"+str(VTS)+"\Clip"+str(index)+'\n')
      f.write('.\pgcdemux.exe -pgc '+str(index)+' -m2v -aud .\VIDEO_TS\VTS_0'+str(VTS)+'_0.IFO .\AllPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\n')
      index += 1

def write_sceneit_myPlay(packName, VTS ,startPGC, endPGC):
  index = startPGC
  with open(packName+'_pullMyPlay_VTS0'+str(VTS)+'.bat','w') as f:
    while index < (endPGC+1):
      f.write("mkdir .\MyPlayClips\VTS_0"+str(VTS)+"\Clip"+str(index)+'\n')
      f.write('.\pgcdemux.exe -vid '+str(index)+' -m2v -aud .\VIDEO_TS\VTS_0'+str(VTS)+'_0.IFO .\MyPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\n')
      index += 1
      
def write_allplay_ffmpeg(packName, VTS ,startClip, endClip):
  index = startClip
  with open(packName+'_ffmpeg_VTS0'+str(VTS)+'.bat','w') as f:
    while index < (endClip+1):
      f.write('mkvmerge -o .\AllPlayClips\VTS_0'+str(VTS)+'\AllPlay'+str(index)+'.mkv .\AllPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\VideoFile.m2v .\AllPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\AudioFile_80.ac3'+'\n')
      f.write('rmdir /s /q .\AllPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\n')
      index += 1
def write_myplay_ffmpeg(packName, VTS ,startClip, endClip):
  index = startClip
  with open(packName+'_ffmpeg_VTS0'+str(VTS)+'.bat','w') as f:
    while index < (endClip+1):
      f.write('mkvmerge -o .\MyPlayClips\VTS_0'+str(VTS)+'\MyPlay'+str(index)+'.mkv .\myPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\VideoFile.m2v .\MyPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\AudioFile_80.ac3 '+'\n')
      f.write('rmdir /s /q .\MyPlayClips\VTS_0'+str(VTS)+'\Clip'+str(index)+'\n')
      index += 1


def main():
  # creating an empty list
  AllPlayVTSList = []
  MyPlayVTSList = []
  name =  input("Welcome to Sentry's Scene It? extaction builder. Please enter the name of the disc you are ripping: ")

  # number of elements as input
  n = int(input("Enter number of All Play VTS you would like to rip: "))
  print("Please state the VTS number (single digit) of the desired IFOs to rip")

  # iterating till the range
  for i in range(0, n):
    ele = int(input())
    # adding the element
    AllPlayVTSList.append(ele) 

  print(AllPlayVTSList)
  n = int(input("Enter number of My Play VTS you would like to rip: "))
  print("Please state the VTS number (single digit) of the desired IFOs to rip")

  # iterating till the range
  for i in range(0, n):
    ele = int(input())
    # adding the element
    MyPlayVTSList.append(ele) 

  print(MyPlayVTSList)
  
  
  for i in range(len(AllPlayVTSList)):
    allPlayStart = int(input("Enter the PGC number of the first All Play clip you would like to rip: "))
    allPlayEnd = int(input("Enter the PGC number of the last All Play clip you would like to rip: "))
    write_sceneit_allPlay(name, AllPlayVTSList[i], allPlayStart, allPlayEnd)
    write_allplay_ffmpeg(name, AllPlayVTSList[i], allPlayStart, allPlayEnd)
  for i in range(len(MyPlayVTSList)):
    myPlayStart = int(input("Enter the VOB ID of the first My Play clip you would like to rip:"))
    myPlayEnd = int(input("Enter the VOB ID of the last My Play clip you would like to rip:" ))
    write_sceneit_myPlay(name, MyPlayVTSList[i], myPlayStart, myPlayEnd)
    write_myplay_ffmpeg(name, MyPlayVTSList[i], myPlayStart, myPlayEnd)
  print("Thank you for using Sentry's Scene It? Exraction Builder. Have a nice day.")
main()