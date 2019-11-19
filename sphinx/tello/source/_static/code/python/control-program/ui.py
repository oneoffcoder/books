import tkinter as tki
from tkinter import Toplevel, Scale
import threading
import datetime
import os
import time
import platform

class TelloUI(object):
    """
    Wrapper class to enable the GUI.
    """
    def __init__(self, tello):
        """
        Initializes all the element of the GUI, supported by Tkinter

        :param tello: class interacts with the Tello drone.
        """
        self.tello = tello # videostream device
        self.thread = None # thread of the Tkinter mainloop
        self.stopEvent = None  
        
        # control variables
        self.distance = 0.1  # default distance for 'move' cmd
        self.degree = 30  # default degree for 'cw' or 'ccw' cmd

        # if the flag is TRUE,the auto-takeoff thread will stop waiting for the response from tello
        self.quit_waiting_flag = False
        
        # initialize the root window and image panel
        self.root = tki.Tk()
        self.panel = None

        # create buttons
        self.btn_landing = tki.Button(
            self.root, text='Open Command Panel', relief='raised', command=self.openCmdWindow)
        self.btn_landing.pack(side='bottom', fill='both',
                              expand='yes', padx=10, pady=5)
        
        # start a thread that constantly pools the video sensor for
        # the most recently read frame
        self.stopEvent = threading.Event()
        
        # set a callback to handle when the window is closed
        self.root.wm_title('TELLO Controller')
        self.root.wm_protocol('WM_DELETE_WINDOW', self.on_close)

        # the sending_command will send command to tello every 5 seconds
        self.sending_command_thread = threading.Thread(target = self._sendingCommand)
            
    def _sendingCommand(self):
        """
        Starts a while loop that sends 'command' to tello every 5 second.

        :return: None
        """    

        while True:
            self.tello.send_command('command')        
            time.sleep(5)

    def _setQuitWaitingFlag(self):  
        """
        Set the variable as TRUE; it will stop computer waiting for response from tello.

        :return: None
        """       
        self.quit_waiting_flag = True        
   
    def openCmdWindow(self):
        """
        Open the cmd window and initial all the button and text.

        :return: None
        """        
        panel = Toplevel(self.root)
        panel.wm_title('Command Panel')

        # create text input entry
        text0 = tki.Label(panel,
                          text='This Controller map keyboard inputs to Tello control commands\n'
                               'Adjust the trackbar to reset distance and degree parameter',
                          font='Helvetica 10 bold'
                          )
        text0.pack(side='top')

        text1 = tki.Label(panel, text=
                          'W - Move Tello Up\t\t\tArrow Up - Move Tello Forward\n'
                          'S - Move Tello Down\t\t\tArrow Down - Move Tello Backward\n'
                          'A - Rotate Tello Counter-Clockwise\tArrow Left - Move Tello Left\n'
                          'D - Rotate Tello Clockwise\t\tArrow Right - Move Tello Right',
                          justify='left')
        text1.pack(side='top')

        self.btn_landing = tki.Button(
            panel, text='Land', relief='raised', command=self.telloLanding)
        self.btn_landing.pack(side='bottom', fill='both',
                              expand='yes', padx=10, pady=5)

        self.btn_takeoff = tki.Button(
            panel, text='Takeoff', relief='raised', command=self.telloTakeOff)
        self.btn_takeoff.pack(side='bottom', fill='both',
                              expand='yes', padx=10, pady=5)

        # binding arrow keys to drone control
        self.tmp_f = tki.Frame(panel, width=100, height=2)
        self.tmp_f.bind('<KeyPress-w>', self.on_keypress_w)
        self.tmp_f.bind('<KeyPress-s>', self.on_keypress_s)
        self.tmp_f.bind('<KeyPress-a>', self.on_keypress_a)
        self.tmp_f.bind('<KeyPress-d>', self.on_keypress_d)
        self.tmp_f.bind('<KeyPress-Up>', self.on_keypress_up)
        self.tmp_f.bind('<KeyPress-Down>', self.on_keypress_down)
        self.tmp_f.bind('<KeyPress-Left>', self.on_keypress_left)
        self.tmp_f.bind('<KeyPress-Right>', self.on_keypress_right)
        self.tmp_f.pack(side='bottom')
        self.tmp_f.focus_set()

        self.btn_landing = tki.Button(
            panel, text='Flip', relief='raised', command=self.openFlipWindow)
        self.btn_landing.pack(side='bottom', fill='both',
                              expand='yes', padx=10, pady=5)

        self.distance_bar = Scale(panel, from_=0.02, to=5, tickinterval=0.01, digits=3, label='Distance(m)',
                                  resolution=0.01)
        self.distance_bar.set(0.2)
        self.distance_bar.pack(side='left')

        self.btn_distance = tki.Button(panel, text='Reset Distance', relief='raised',
                                       command=self.updateDistancebar,
                                       )
        self.btn_distance.pack(side='left', fill='both',
                               expand='yes', padx=10, pady=5)

        self.degree_bar = Scale(panel, from_=1, to=360, tickinterval=10, label='Degree')
        self.degree_bar.set(30)
        self.degree_bar.pack(side='right')

        self.btn_distance = tki.Button(panel, text='Reset Degree', relief='raised', command=self.updateDegreebar)
        self.btn_distance.pack(side='right', fill='both',
                               expand='yes', padx=10, pady=5)

    def openFlipWindow(self):
        """
        Open the flip window and initial all the button and text.

        :return: None
        """
        panel = Toplevel(self.root)
        panel.wm_title('Gesture Recognition')

        self.btn_flipl = tki.Button(
            panel, text='Flip Left', relief='raised', command=self.telloFlip_l)
        self.btn_flipl.pack(side='bottom', fill='both',
                            expand='yes', padx=10, pady=5)

        self.btn_flipr = tki.Button(
            panel, text='Flip Right', relief='raised', command=self.telloFlip_r)
        self.btn_flipr.pack(side='bottom', fill='both',
                            expand='yes', padx=10, pady=5)

        self.btn_flipf = tki.Button(
            panel, text='Flip Forward', relief='raised', command=self.telloFlip_f)
        self.btn_flipf.pack(side='bottom', fill='both',
                            expand='yes', padx=10, pady=5)

        self.btn_flipb = tki.Button(
            panel, text='Flip Backward', relief='raised', command=self.telloFlip_b)
        self.btn_flipb.pack(side='bottom', fill='both',
                            expand='yes', padx=10, pady=5)

    def telloTakeOff(self):
        return self.tello.takeoff()                

    def telloLanding(self):
        return self.tello.land()

    def telloFlip_l(self):
        return self.tello.flip('l')

    def telloFlip_r(self):
        return self.tello.flip('r')

    def telloFlip_f(self):
        return self.tello.flip('f')

    def telloFlip_b(self):
        return self.tello.flip('b')

    def telloCW(self, degree):
        return self.tello.rotate_cw(degree)

    def telloCCW(self, degree):
        return self.tello.rotate_ccw(degree)

    def telloMoveForward(self, distance):
        return self.tello.move_forward(distance)

    def telloMoveBackward(self, distance):
        return self.tello.move_backward(distance)

    def telloMoveLeft(self, distance):
        return self.tello.move_left(distance)

    def telloMoveRight(self, distance):
        return self.tello.move_right(distance)

    def telloUp(self, dist):
        return self.tello.move_up(dist)

    def telloDown(self, dist):
        return self.tello.move_down(dist)

    def updateDistancebar(self):
        self.distance = self.distance_bar.get()
        print(f'reset distance to {self.distance:.1f}')

    def updateDegreebar(self):
        self.degree = self.degree_bar.get()
        print(f'reset distance to {self.degree}')

    def on_keypress_w(self, event):
        print(f'up {self.distance} m')
        self.telloUp(self.distance)

    def on_keypress_s(self, event):
        print(f'down {self.distance} m')
        self.telloDown(self.distance)

    def on_keypress_a(self, event):
        print(f'ccw {self.degree} degree')
        self.tello.rotate_ccw(self.degree)

    def on_keypress_d(self, event):
        print(f'cw {self.degree} m')
        self.tello.rotate_cw(self.degree)

    def on_keypress_up(self, event):
        print(f'forward {self.distance} m')
        self.telloMoveForward(self.distance)

    def on_keypress_down(self, event):
        print(f'backward {self.distance} m')
        self.telloMoveBackward(self.distance)

    def on_keypress_left(self, event):
        print(f'left {self.distance} m')
        self.telloMoveLeft(self.distance)

    def on_keypress_right(self, event):
        print(f'right {self.distance} m')
        self.telloMoveRight(self.distance)

    def on_close(self):
        """
        Sets the stop event, cleanup the camera, and allow the rest of
        the quit process to continue.
        :return: None
        """
        print('[INFO] closing...')
        self.stopEvent.set()
        del self.tello
        self.root.quit()

