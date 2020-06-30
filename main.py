import tkinter
import tkinter.messagebox
import cv2
from PIL import ImageTk, Image
import os
import requests

from datetime import datetime

def show_Location(locationframe):
    # Scrap response from below url using IP address of the system
    response = requests.get('https://ipinfo.io/')
    loc_tracker = response.json()

    # Country from the response
    country = loc_tracker['country']
    if country == "IN":
        country = "India"

    # State from the response
    state = loc_tracker['region']

    # City from the response
    city = loc_tracker['city']

    # Latitude and Longitude from the response
    location = loc_tracker['loc'].split(',')
    latitude = location[0]
    longitude = location[1]

    # Print all the above location parameters
    lblshowLocation=tkinter.Label(locationframe)
    lblshowLocation.pack(fill='both',expand=True)
    lblCountry=tkinter.Label(lblshowLocation,text="Country: {0}".format(country),font=("Times New Roman", 16, "bold"))
    lblCountry.pack()
    lblState=tkinter.Label(lblshowLocation,text="State: {0}".format(state),font=("Times New Roman", 16, "bold"))
    lblState.pack()
    lblCity = tkinter.Label(lblshowLocation, text="City: {0}".format(city),font=("Times New Roman", 16, "bold"))
    lblCity.pack()
    lblLatitude = tkinter.Label(lblshowLocation, text="Latitude: {0}".format(latitude),font=("Times New Roman", 16, "bold"))
    lblLatitude.pack()
    lblLongitude = tkinter.Label(lblshowLocation, text="Longitude: {0}".format(longitude),font=("Times New Roman", 16, "bold"))
    lblLongitude.pack()


BASE_DIR = os.path.dirname(__file__)+"/Captured/image"
BASE_DIR2 = os.path.dirname(__file__)+"/recording/outputVideo"
frame1=frame2=frame3=None
var_start_recording=False
video1=video2=video3=None
def initialize_video():
    global video1,video2,video3
    if (cap.isOpened() == False):
        tkinter.messagebox("Failed", "Unable to read camera feed")
    else:
        frame_width = int(cap.get(3))
        frame_height = int(cap.get(4))
        video1 = cv2.VideoWriter(BASE_DIR2 + '1.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20,
                                 (frame_width, frame_height))
        video2 = cv2.VideoWriter(BASE_DIR2 + '2.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20,
                                 (frame_width, frame_height))
        video3 = cv2.VideoWriter(BASE_DIR2 + '3.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20,
                                 (frame_width, frame_height))
        
def start_recording():
    global var_start_recording
    var_start_recording=True
    initialize_video()
def stop_recording():
    global var_start_recording
    var_start_recording = False


def record_video():
    global var_start_recording ,video1,video2,video3,frame1,frame2,frame3
    if var_start_recording:
        video1.write(frame1)
        video2.write(frame2)
        video3.write(frame3)


fr=1
def capture_picture():
    global fr
    file1 = BASE_DIR + str(fr) + '_1.jpg'
    file2 = BASE_DIR + str(fr) + '_2.jpg'
    file3 = BASE_DIR + str(fr) + '_3.jpg'
    cv2.imwrite(file1, frame1)
    cv2.imwrite(file2, frame2)
    cv2.imwrite(file3, frame3)
    fr += 1
    tkinter.messagebox.showinfo("Sucess","Picture Captured Successfully")
def video_stream1():
        global frame1
    # while(True):
        _, frame = cap.read()
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,str(datetime.now()),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
        # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame1=frame
        img = Image.fromarray(frame)
        img=img.resize((350, 250), Image.ANTIALIAS)
        imgtk = ImageTk.PhotoImage(image=img)
        lbldisplay1.imgtk = imgtk
        lbldisplay1.configure(image=imgtk)

        # time.sleep(1000)
        


        lbldisplay1.after(30, video_stream2)
def video_stream2():
    global frame2
    _, frame = cap.read()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,str(datetime.now()),(10,30), font, 1,(255,255,255),2,cv2.LINE_AA)
    # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame2=cv2image
    img = Image.fromarray(cv2image)
    img=img.resize((350, 250), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(image=img)
    lbldisplay2.imgtk = imgtk
    lbldisplay2.configure(image=imgtk)
    lbldisplay2.after(30, video_stream3)
master=None
def video_stream3():
    global master,frame3
    
    _, frame = cap.read()
    
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    

    blur_frame = cv2.GaussianBlur(cv2image, (15, 15), 0)
    
    if master is None:
        master = blur_frame


    # delta frame
    delta_frame = cv2.absdiff(master, blur_frame)
    
    # threshold frame
    threshold_frame = cv2.threshold(delta_frame, 15, 255, cv2.THRESH_BINARY)[1]
    
    # cv2image = cv2.cvtColor(threshold_frame, cv2.COLOR_BGR2GRAY)
    # cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame3=threshold_frame
    img = Image.fromarray(threshold_frame)
    img=img.resize((350, 250), Image.ANTIALIAS)
    imgtk = ImageTk.PhotoImage(image=img)
    lbldisplay3.imgtk = imgtk
    lbldisplay3.configure(image=imgtk)
    record_video()
    lbldisplay3.after(30, video_stream1)
def recordonoff():
    if btnrecstop['text']=="RECORD":
        if (tkinter.messagebox.askyesno("Start Record", "Do you want to Start Recording of Video")):
            btnrecstop['text']="STOP"
            start_recording()
    else:
        if (tkinter.messagebox.askyesno("Stop Record", "Do you want to Stop Recording Video")):
            btnrecstop['text'] = "RECORD"
            stop_recording()

def exit_prog():
    if(tkinter.messagebox.askyesno("Exit","Do you want to exit from program")):
        root.destroy()
def getlocation():
    for e in frmrightdisplay.pack_slaves():
        e.destroy()
    show_Location(frmrightdisplay)
root=tkinter.Tk()
root.minsize(900,600)
root['bg']='black'
lblmsg=tkinter.Label(root,text='WEBCAM MOTION',font=("Times New Roman", 26, "bold"))
lblmsg.pack(fill='x',pady=20)
frmtopdisplay=tkinter.Frame(root)
frmtopdisplay.pack()
frmleft=tkinter.Frame(frmtopdisplay,width=350,height=250,bg='blue')
frmleft.pack(side='left',padx=10,pady=10)
lbldisplay1 = tkinter.Label(frmleft)
lbldisplay1.pack(fill='both', padx=10, pady=10)
frmright=tkinter.Frame(frmtopdisplay,width=350,height=250,bg='blue')
frmright.pack(side='right',padx=10,pady=10)
lbldisplay2 = tkinter.Label(frmright)
lbldisplay2.pack(fill='both', padx=10, pady=10)
frmbottomdisplay=tkinter.Frame(root)
frmbottomdisplay.pack()
frmleft1=tkinter.Frame(frmbottomdisplay,width=350,height=250,bg='blue')
frmleft1.pack(side='left',padx=10,pady=10)
lbldisplay3 = tkinter.Label(frmleft1)
lbldisplay3.pack(fill='both', padx=10, pady=10)

frmright1=tkinter.Frame(frmbottomdisplay,width=350,height=250,bg='blue')
frmright1.pack(side='right',padx=10,pady=10)
frmrightbuttom=tkinter.Frame(frmright1,bg='blue',width=165,height=230)
frmrightbuttom.pack(side='left',padx=5,pady=5)
btncapture=tkinter.Button(frmrightbuttom,text='CAPTURE',font=("Times New Roman", 16, "bold"),command=capture_picture)
btncapture.pack(fill='x',pady=5)
btnrecstop=tkinter.Button(frmrightbuttom,text='RECORD',font=("Times New Roman", 16, "bold"),command=recordonoff)
btnrecstop.pack(fill='x',pady=5)
btnbrowse=tkinter.Button(frmrightbuttom,text='Location',font=("Times New Roman", 16, "bold"),command=getlocation)
btnbrowse.pack(fill='x',pady=5)
btnexit=tkinter.Button(frmrightbuttom,text='EXIT',font=("Times New Roman", 16, "bold"),command=exit_prog)
btnexit.pack(fill='x',pady=5)
frmrightdisplay=tkinter.Frame(frmright1,bg='red',width=165,height=230)
frmrightdisplay.pack(side='right',padx=5,pady=5)

cap = cv2.VideoCapture(0)
# th1=threading.Thread(target=video_stream1)
# th1.start()
video_stream1()
# root.after(1,video_stream1)
root.after(1,video_stream1)
#
# video_stream3()

# showdisplay1(frmleft)


root.mainloop()
