import time, vlc  
 
my_media = vlc.MediaPlayer("video_name.mp4")  
my_media.play() #to start the player
my_media.stop() #to stop the player

def vlc_video(src):           
    vlc_obj = vlc.Instance() # creating an instance of vlc    
    vlcplayer = vlc_obj.media_player_new() # creating a media player
    vlcmedia = vlc_obj.media_new(src)  # creating a media    
    vlcplayer.set_media(vlcmedia)  # setting media to the player  
    vlcplayer.play()  # playing the video 
    time.sleep(0.5)  # waiting time   
    video_duration = vlcplayer.get_length() # getting the duration of the video  
    print("Duration : " + str(video_duration))     
vlc_video("video_name.mp4") 