import tkinter as tk

import Header
import DiagramComponents

class UCI_Liquid_Engine_Plumbing:

    def __init__(self, gridLen):
        width = gridLen * 13
        height = gridLen * 17

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')
        #self.win.wm_attributes('-transparentcolor', 'black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'P&ID', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # ALL TANKS
        self.he1 = DiagramComponents.Tank(self.win, 'black', 'He F', '#b30056', gridLen, gridLen)
        self.he2 = DiagramComponents.Tank(self.win, 'black', 'He F', '#b30056', gridLen, gridLen)
        self.he3 = DiagramComponents.Tank(self.win, 'black', 'He F', '#b30056', gridLen, gridLen)
        self.n2 = DiagramComponents.Tank(self.win, 'black', 'N2', '#b30056', gridLen, gridLen)
        self.heCopv = DiagramComponents.Tank(self.win, 'black', 'He', '#b30056', gridLen, gridLen)
        self.lowDewar = DiagramComponents.Tank(self.win, 'black', 'LOX D', '#1d2396', gridLen, gridLen)
        self.loxProp = DiagramComponents.Tank(self.win, 'black', 'LOX', '#1d2396', gridLen, gridLen)
        self.lngDewar = DiagramComponents.Tank(self.win, 'black', 'LNG D', '#8a1900', gridLen, gridLen)
        self.lngProp = DiagramComponents.Tank(self.win, 'black', 'LNG', '#8a1900', gridLen, gridLen)
        self.he1.getWidget().place(x=gridLen * 0, y=gridLen * 5)
        self.he2.getWidget().place(x=gridLen * 1, y=gridLen * 5)
        self.he3.getWidget().place(x=gridLen * 2, y=gridLen * 5)
        self.n2.getWidget().place(x=gridLen * 3, y=gridLen * 5)
        self.heCopv.getWidget().place(x=gridLen * 8, y=gridLen * 1)
        self.lowDewar.getWidget().place(x=gridLen * 3, y=gridLen * 10)
        self.loxProp.getWidget().place(x=gridLen * 8, y=gridLen * 10)
        self.lngDewar.getWidget().place(x=gridLen * 3, y=gridLen * 13)
        self.lngProp.getWidget().place(x=gridLen * 11, y=gridLen * 11)

        # ALL CHECK VALVE


        # All VALVES
        self.one = DiagramComponents.Solenoid(self.win, 'black', 1, gridLen, gridLen, False, True, False, False)
        self.two = DiagramComponents.Solenoid(self.win, 'black', 2, gridLen, gridLen, False, True, False, True)
        self.three = DiagramComponents.Solenoid(self.win, 'black', 3, gridLen, gridLen, False, False, False, True)
        self.four = DiagramComponents.Solenoid(self.win, 'black', 4, gridLen, gridLen, True, True, False, False)
        self.five = DiagramComponents.Solenoid(self.win, 'black', 5, gridLen, gridLen, False, True, False, True)
        self.six = DiagramComponents.Solenoid(self.win, 'black', 6, gridLen, gridLen, True, False, True, False)
        self.seven = DiagramComponents.Solenoid(self.win, 'black', 7, gridLen, gridLen, False, True, False, True)
        self.eight = DiagramComponents.Solenoid(self.win, 'black', 8, gridLen, gridLen, False, True, False, True)
        self.nine = DiagramComponents.Solenoid(self.win, 'black', 9, gridLen, gridLen, False, True, False, True)
        self.ten = DiagramComponents.Solenoid(self.win, 'black', 10, gridLen, gridLen, False, True, False, True)
        self.eleven = DiagramComponents.Solenoid(self.win, 'black', 11, gridLen, gridLen, False, True, False, True)
        self.twelve = DiagramComponents.Solenoid(self.win, 'black', 12, gridLen, gridLen, True, False, True, False)
        self.thirteen = DiagramComponents.Solenoid(self.win, 'black', 13, gridLen, gridLen, True, False, True, False)
        self.fourteen = DiagramComponents.Solenoid(self.win, 'black', 14, gridLen, gridLen, True, False, True, False)
        self.one.getWidget().place(x=gridLen * 6, y=gridLen * 2)
        self.two.getWidget().place(x=gridLen * 6, y=gridLen * 3)
        self.three.getWidget().place(x=gridLen * 10, y=gridLen * 4)
        self.four.getWidget().place(x=gridLen * 8, y=gridLen * 5)
        self.five.getWidget().place(x=gridLen * 7, y=gridLen * 9)
        self.six.getWidget().place(x=gridLen * 6, y=gridLen * 10)
        self.seven.getWidget().place(x=gridLen * 12, y=gridLen * 10)
        self.eight.getWidget().place(x=gridLen * 5, y=gridLen * 11)
        self.nine.getWidget().place(x=gridLen * 7, y=gridLen * 11)
        self.ten.getWidget().place(x=gridLen * 5, y=gridLen * 12)
        self.eleven.getWidget().place(x=gridLen * 10, y=gridLen * 12)
        self.twelve.getWidget().place(x=gridLen * 6, y=gridLen * 13)
        self.thirteen.getWidget().place(x=gridLen * 8, y=gridLen * 13)
        self.fourteen.getWidget().place(x=gridLen * 11, y=gridLen * 13)

        # All Pressure Sensors
        self.ps1 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, True, False)
        self.ps2 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, True, False)
        self.ps3 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True)
        self.ps4 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, False, False)
        self.ps5 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, False, False)
        self.ps6 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True)
        self.ps1.getWidget().place(x=gridLen * 7, y=gridLen * 1)
        self.ps2.getWidget().place(x=gridLen * 5, y=gridLen * 2)
        self.ps3.getWidget().place(x=gridLen * 9, y=gridLen * 8)
        self.ps4.getWidget().place(x=gridLen * 10, y=gridLen * 9)
        self.ps5.getWidget().place(x=gridLen * 7, y=gridLen * 14)
        self.ps6.getWidget().place(x=gridLen * 12, y=gridLen * 14)


        # All PIPES
        self.p1 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d',
                                         False)
        self.p2 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p3 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, False, '#41d94d',
                                         False)
        self.p4 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d',
                                         False)
        self.p5 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p6 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d',
                                         False)
        self.p7 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d', False)
        self.p8 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p9 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                         False)
        self.p10 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p11 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d',
                                          False)
        self.p12 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d',
                                          False)
        self.p13 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d',
                                          False)
        self.p14 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d',
                                          False)
        self.p15 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, False, '#41d94d',
                                          False)
        self.p16 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                          False)
        self.p17 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                          False)
        self.p18 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d',
                                          False)
        self.p19 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d',
                                          False)
        self.p20 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d',
                                          False)
        self.p21 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d',
                                          False)
        self.p22 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d',
                                          False)

        self.p23 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d',
                                          False)
        self.p24 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d',
                                          False)
        self.p25 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d',
                                          False)
        self.p26 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d',
                                          False)
        self.p27 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, False, '#41d94d',
                                          False)
        self.p28 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d',
                                          False)
        self.p29 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                          False)
        #self.p30 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d',
        #                                  False)
        self.p31 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                          False)
        self.p32 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d',
                                          False)
        self.p33 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d',
                                          False)
        self.p34 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d',
                                          False)
        self.p35 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d',
                                          False)
        self.p36 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, True, '#41d94d',
                                          False)

        self.p37 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d',
                                          False)
        # self.p38 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d',
        #                                   False)
        self.p39 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d',
                                          False)
        self.p40 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d',
                                          False)
        self.p41 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, False, '#41d94d',
                                          False)
        self.p42 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, False, False, True, '#41d94d',
                                          False)
        self.p43 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, False, '#41d94d',
                                          False)

        self.ip1 = DiagramComponents.PipeIntersect(self.win, 'black', gridLen, gridLen, '#41d94d', False, False)

        self.p1.getWidget().place(x=gridLen * 7, y=gridLen * 2)
        self.p2.getWidget().place(x=gridLen * 8, y=gridLen * 2)
        self.p3.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.p4.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p5.getWidget().place(x=gridLen * 2, y=gridLen * 3)
        self.p6.getWidget().place(x=gridLen * 3, y=gridLen * 3)
        self.p7.getWidget().place(x=gridLen * 5, y=gridLen * 3)
        self.p8.getWidget().place(x=gridLen * 8, y=gridLen * 3)
        self.p9.getWidget().place(x=gridLen * 10, y=gridLen * 3)
        self.p10.getWidget().place(x=gridLen * 11, y=gridLen * 3)
        self.p11.getWidget().place(x=gridLen * 9, y=gridLen * 4)
        self.p12.getWidget().place(x=gridLen * 9, y=gridLen * 5)
        self.p13.getWidget().place(x=gridLen * 11, y=gridLen * 5)
        self.p14.getWidget().place(x=gridLen * 12, y=gridLen * 5)
        self.p15.getWidget().place(x=gridLen * 8, y=gridLen * 6)
        self.p16.getWidget().place(x=gridLen * 9, y=gridLen * 6)
        self.p17.getWidget().place(x=gridLen * 10, y=gridLen * 6)
        self.p18.getWidget().place(x=gridLen * 11, y=gridLen * 6)
        self.p19.getWidget().place(x=gridLen * 12, y=gridLen * 7)
        self.p20.getWidget().place(x=gridLen * 8, y=gridLen * 8)
        self.p21.getWidget().place(x=gridLen * 8, y=gridLen * 9)
        self.p22.getWidget().place(x=gridLen * 11, y=gridLen * 9)

        self.p23.getWidget().place(x=gridLen * 11, y=gridLen * 10)
        self.p24.getWidget().place(x=gridLen * 3, y=gridLen * 11)
        self.p25.getWidget().place(x=gridLen * 6, y=gridLen * 11)
        self.p26.getWidget().place(x=gridLen * 8, y=gridLen * 11)
        self.p27.getWidget().place(x=gridLen * 3, y=gridLen * 12)
        self.p28.getWidget().place(x=gridLen * 6, y=gridLen * 12)
        self.p29.getWidget().place(x=gridLen * 7, y=gridLen * 12)
        #self.p30.getWidget().place(x=gridLen * 8, y=gridLen * 8)
        self.p31.getWidget().place(x=gridLen * 9, y=gridLen * 12)
        self.p32.getWidget().place(x=gridLen * 11, y=gridLen * 12)
        self.p33.getWidget().place(x=gridLen * 8, y=gridLen * 14)
        self.p34.getWidget().place(x=gridLen * 9, y=gridLen * 14)
        self.p35.getWidget().place(x=gridLen * 10, y=gridLen * 14)
        self.p36.getWidget().place(x=gridLen * 11, y=gridLen * 14)

        #added to simulate bleeds for solenoids
        self.p37.getWidget().place(x=gridLen * 6, y=gridLen * 1)
        #self.p38.getWidget().place(x=gridLen * 7, y=gridLen * 5)
        self.p39.getWidget().place(x=gridLen * 10, y=gridLen * 5)
        self.p40.getWidget().place(x=gridLen * 6, y=gridLen * 9)
        self.p41.getWidget().place(x=gridLen * 5, y=gridLen * 10)
        self.p42.getWidget().place(x=gridLen * 12, y=gridLen * 11)
        self.p43.getWidget().place(x=gridLen * 6, y=gridLen * 14)


        # ALL CVs
        self.cv1 = DiagramComponents.CheckValve(self.win, 'black', 2, gridLen, gridLen)
        self.cv2 = DiagramComponents.CheckValve(self.win, 'black', 1, gridLen, gridLen)
        self.cv3 = DiagramComponents.CheckValve(self.win, 'black', 1, gridLen, gridLen)
        self.cv4 = DiagramComponents.CheckValve(self.win, 'black', 1, gridLen, gridLen)
        self.cv5 = DiagramComponents.CheckValve(self.win, 'black', 1, gridLen, gridLen)
        self.cv6 = DiagramComponents.CheckValve(self.win, 'black', 3, gridLen, gridLen)
        self.cv7 = DiagramComponents.CheckValve(self.win, 'black', 3, gridLen, gridLen)
        self.cv1.getWidget().place(x=gridLen * 7, y=gridLen * 3)
        self.cv2.getWidget().place(x=gridLen * 0, y =gridLen * 4)
        self.cv3.getWidget().place(x=gridLen * 1, y=gridLen * 4)
        self.cv4.getWidget().place(x=gridLen * 2, y=gridLen * 4)
        self.cv5.getWidget().place(x=gridLen * 3, y=gridLen * 4)
        self.cv6.getWidget().place(x=gridLen * 8, y=gridLen * 7)
        self.cv7.getWidget().place(x=gridLen * 11, y=gridLen * 8)


        # ALL Regs
        self.reg1 = DiagramComponents.PressureReg(self.win, 'black', 1, gridLen, gridLen)
        self.reg2 = DiagramComponents.PressureReg(self.win, 'black', 3, gridLen, gridLen)
        self.reg3 = DiagramComponents.PressureReg(self.win, 'black', 2, gridLen, gridLen)
        self.reg4 = DiagramComponents.PressureReg(self.win, 'black', 2, gridLen, gridLen)
        self.reg5 = DiagramComponents.PressureReg(self.win, 'black', 4, gridLen, gridLen)
        self.reg6 = DiagramComponents.PressureReg(self.win, 'black', 1, gridLen, gridLen)
        self.reg7 = DiagramComponents.PressureReg(self.win, 'black', 1, gridLen, gridLen)
        self.reg1.getWidget().place(x=gridLen * 4, y=gridLen * 3)
        self.reg2.getWidget().place(x=gridLen * 9, y=gridLen * 3)
        self.reg3.getWidget().place(x=gridLen * 8, y=gridLen * 4)
        self.reg4.getWidget().place(x=gridLen * 12, y=gridLen * 6)
        self.reg5.getWidget().place(x=gridLen * 11, y=gridLen * 7)
        self.reg6.getWidget().place(x=gridLen * 4, y=gridLen * 11)
        self.reg7.getWidget().place(x=gridLen * 4, y=gridLen * 12)

        # intersecting pipes
        self.ip1.getWidget().place(x=gridLen * 8, y=gridLen * 12)


        # ALL TEXT
        self.heFilter = Header.Text(self.win, 'black', "He Filter", gridLen, gridLen, 10)
        self.heFilter.getWidget().place(x=gridLen * 11, y =gridLen * 4)


        # NOZZLE
        self.n = DiagramComponents.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 9, y=gridLen * 15)



        # SET ALL VIRTUAL COMPONENTS (linked list)
        self.head = [self.he1, self.he2, self.he3, self.n2]
        #row1
        self.ps1.setNeighbors(None, None, self.p1, None)
        self.heCopv.setNeighbors(None, None, self.p2, None)
        self.p37.setNeighbors(None, None, self.one, None)
        #row2
        self.ps2.setNeighbors(None, None, self.p7, None)
        self.one.setNeighbors(self.p37, self.p1, None, None)
        self.p1.setNeighbors(self.ps1, self.p2, None, self.one)
        self.p2.setNeighbors(self.heCopv, None, self.p8, self.p1)
        #row3
        self.p3.setNeighbors(None, self.p4, self.cv2, None)
        self.p4.setNeighbors(None, self.p5, self.cv3, self.p3)
        self.p5.setNeighbors(None, self.p6, self.cv4, self.p4)
        self.p6.setNeighbors(None, self.reg1, self.cv5, self.p5)
        self.reg1.setNeighbors(None, self.p7, None, self.p6)
        self.p7.setNeighbors(self.ps2, self.two, None, self.reg1) #self.ps2, self.two, (THERMO)), self.reg1
        self.two.setNeighbors(None, self.cv1, None, self.p7)
        self.cv1.setNeighbors(None, self.p8, None, self.two)
        self.p8.setNeighbors(self.p2, self.reg2, self.reg3, self.cv1)
        self.reg2.setNeighbors(None, self.p9, self.p11, self.p8)
        self.p9.setNeighbors(None, self.p10, None, self.reg2)
        self.p10.setNeighbors(None, None, self.heFilter, self.p9)
        #row4
        self.cv2.setNeighbors(self.p3, None, self.he1, None)
        self.cv3.setNeighbors(self.p4, None, self.he2, None)
        self.cv4.setNeighbors(self.p5, None, self.he3, None)
        self.cv5.setNeighbors(self.p6, None, self.n2, None)
        # thermocouple
        self.reg3.setNeighbors(self.p8, None, self.four, None)
        self.p11.setNeighbors(self.reg2, self.three, self.p12, None)
        self.three.setNeighbors(None, None, self.p39, self.p11)
        self.heFilter.setNeighbors(self.p10, None, self.p13, None)
        #row 5
        self.he1.setNeighbors(self.cv2, None, None, None)
        self.he2.setNeighbors(self.cv3, None, None, None)
        self.he3.setNeighbors(self.cv4, None, None, None)
        self.n2.setNeighbors(self.cv5, None, None, None)
        self.four.setNeighbors(self.reg3, self.p12, None, None)
        self.p12.setNeighbors(self.p11, None, None, self.four)
        self.p13.setNeighbors(self.heFilter, self.p14, self.p18, None)
        self.p14.setNeighbors(None, None, self.reg4, self.p13)
        self.p39.setNeighbors(self.three, None, None, None)
        #row 6
        self.p15.setNeighbors(None, self.p16, self.cv6, None)
        self.p16.setNeighbors(None, self.p17, None, self.p15)
        self.p17.setNeighbors(None, self.p18, None, self.p16)
        self.p18.setNeighbors(self.p13, None, self.reg5, self.p17)
        self.reg4.setNeighbors(self.p14, None, self.p19, None)
        #row 7
        self.cv6.setNeighbors(self.p15, None, self.p20, None)
        self.reg5.setNeighbors(self.p18, self.p19, self.cv7, None) #TODO: Confirm connecting reg5 to cv 7
        #row 8
        #rel valve not implemented yet
        self.p20.setNeighbors(self.cv6, self.ps3, self.p21, None)
        self.ps3.setNeighbors(None, None, None, self.p20)
        self.cv7.setNeighbors(self.reg5, None, self.p22, None) #TODO: Confirm connecting cv7 to reg 5
        #row 9
        self.five.setNeighbors(None, self.p21, None, self.p40)
        self.p21.setNeighbors(self.p20, None, self.loxProp, self.five)
        self.ps4.setNeighbors(None, self.p22, None, None)
        self.p22.setNeighbors(self.cv7, None, self.p23, self.ps4)
        self.p40.setNeighbors(None, self.five, None, None)
        #rel valve not implemented yet
        #row 10
        self.lowDewar.setNeighbors(None, None, self.p24, None)
        self.six.setNeighbors(None, None, self.p25, self.p41)
        self.loxProp.setNeighbors(self.p21, None, self.p26, None)
        self.p23.setNeighbors(self.p22, self.seven, self.lngProp, None)
        self.seven.setNeighbors(None, None, self.p42, self.p23)
        self.p41.setNeighbors(None, self.six, None, None)
        self.p42.setNeighbors(self.seven, None, None, None)
        #row 11
        self.p24.setNeighbors(self.lowDewar, self.reg6, None, None)
        self.reg6.setNeighbors(None, self.eight, None, self.p24)
        self.eight.setNeighbors(None, self.p25, None, self.reg6)
        self.p25.setNeighbors(self.six, self.nine, None, self.eight)
        self.nine.setNeighbors(None, self.p26, None, self.p25)
        self.p26.setNeighbors(self.loxProp, None, self.ip1, self.nine)
        self.lngProp.setNeighbors(self.p23, None, self.p32, None)
        #row 12
        self.p27.setNeighbors(None, self.reg7, self.lngDewar, None)
        self.reg7.setNeighbors(None, self.ten, None, self.p27)
        self.ten.setNeighbors(None, self.p28, None, self.reg7)
        self.p28.setNeighbors(None, self.p29, self.twelve, self.ten)
        self.p29.setNeighbors(None, self.ip1, None, self.p28)

        #pipe intersect
        self.ip1.setNeighborsVertical(self.p26, None, self.thirteen, None)
        self.ip1.setNeighborsHorizontal(None, self.p31, None, self.p29)

        self.p31.setNeighbors(None, self.eleven, None, self.ip1)
        self.eleven.setNeighbors(None, self.p32, None, self.p31)
        self.p32.setNeighbors(self.lngProp, None, self.fourteen, self.eleven)
        #row 13
        self.lngDewar.setNeighbors(self.p27, None, None, None)
        self.twelve.setNeighbors(self.p28, None, self.p43, None)
        self.thirteen.setNeighbors(self.ip1, None, self.p33, None)
        self.fourteen.setNeighbors(self.p32, None, self.p36, None)
        #row 14
        self.ps5.setNeighbors(None, self.p33, None, None)
        self.p33.setNeighbors(self.thirteen, self.p34, None, self.ps5)
        self.p34.setNeighbors(None, self.p35, self.n, self.p33) 
        self.p35.setNeighbors(None, self.p36, None, self.p34)
        self.p36.setNeighbors(self.fourteen, self.ps6, None, self.p35)
        self.ps6.setNeighbors(None, None, None, self.p36)
        self.p43.setNeighbors(self.twelve, None, None, None)
        #row 15 and 16
        self.n.setNeighbors(self.p34, None, None, None)

        #set Solenoid inlets and outlets , 1 - top, 2 - right, 3 - down, 4 - left
        self.one.setIn(2)
        self.one.setOut(1)
        self.two.setIn(4)
        self.two.setOut(2)
        self.three.setIn(4)
        self.three.setOut(3)
        self.four.setIn(1)
        self.four.setOut(2)
        self.five.setIn(2)
        self.five.setOut(4)
        self.six.setIn(3)
        self.six.setOut(4)
        self.seven.setIn(4)
        self.seven.setOut(3)
        self.eight.setIn(4)
        self.eight.setOut(2)
        self.nine.setIn(4) 
        self.nine.setOut(2)
        self.ten.setIn(4)
        self.ten.setOut(2)
        self.eleven.setIn(4) 
        self.eleven.setOut(2)
        self.twelve.setIn(1)
        self.twelve.setOut(3)
        self.thirteen.setIn(1) 
        self.thirteen.setOut(3)
        self.fourteen.setIn(1) 
        self.fourteen.setOut(3)

        #set CheckValve inlets and outlets
        self.cv1.setIn(4) 
        self.cv1.setOut(2)
        self.cv2.setIn(3) 
        self.cv2.setOut(1)
        self.cv3.setIn(3) 
        self.cv3.setOut(1)
        self.cv4.setIn(3) 
        self.cv4.setOut(1)
        self.cv5.setIn(3) 
        self.cv5.setOut(1)
        self.cv6.setIn(1) 
        self.cv6.setOut(3)
        self.cv7.setIn(1) 
        self.cv7.setOut(3)



    def defaultState(self):
        self.p1.setState(False)
        self.p2.setState(False)
        self.p3.setState(False)
        self.p4.setState(False)
        self.p5.setState(False)
        self.p6.setState(False)
        self.p7.setState(False)
        self.p8.setState(False)
        self.p9.setState(False)
        self.p10.setState(False)
        self.p11.setState(False)
        self.p12.setState(False)
        self.p13.setState(False)
        self.p14.setState(False)
        self.p15.setState(False)
        self.p16.setState(False)
        self.p17.setState(False)
        self.p18.setState(False)
        self.p19.setState(False)
        self.p20.setState(False)
        self.p21.setState(False)
        self.p22.setState(False)
        self.p23.setState(False)
        self.p24.setState(False)
        self.p25.setState(False)
        self.p26.setState(False)
        self.p27.setState(False)
        self.p28.setState(False)
        self.p29.setState(False)
        self.p31.setState(False)
        self.p32.setState(False)
        self.p33.setState(False)
        self.p34.setState(False)
        self.p35.setState(False)
        self.p36.setState(False)

        self.one.setPipes(False, False, False, False)
        self.two.setPipes(False, False, False, False)
        self.three.setPipes(False, False, False, False)
        self.four.setPipes(False, False, False, False)
        self.five.setPipes(False, False, False, False)
        self.six.setPipes(False, False, False, False)

        self.ps1.setPipes(False)
        self.ps2.setPipes(False)
        self.ps3.setPipes(False)

        self.o1.setPipes(False)
        self.o2.setPipes(False)

        self.s1.setPipes(False, False, False, False)
        self.s2.setPipes(False, False, False, False)

        self.tp1.setPipes(False)
        

    def updatePipeStatus(self):
        print("AHHHHHHHH")



    def getWindow(self):
        return self.win







class Liquid_Engine_Plumbing:

    def __init__(self, gridLen):

        width = gridLen * 8
        height = gridLen * 12

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'P&ID', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # All TANKS
        self.gn2 = DiagramComponents.Tank(self.win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
        self.lox = DiagramComponents.Tank(self.win, 'black', 'LOx', '#1d2396', gridLen, gridLen)
        self.k = DiagramComponents.Tank(self.win, 'black', 'K', '#1d2396', gridLen, gridLen)
        self.gn2.getWidget().place(x=gridLen * 3, y=gridLen * 1)
        self.lox.getWidget().place(x=gridLen * 1, y=gridLen * 5)
        self.k.getWidget().place(x=gridLen * 6, y=gridLen * 5)

        # All SOLENOID VALVES
        self.one = DiagramComponents.Solenoid(self.win, 'black', 1, gridLen, gridLen, False, True, True, False)
        self.two = DiagramComponents.Solenoid(self.win, 'black', 2, gridLen, gridLen, False, True, False, False)
        self.three = DiagramComponents.Solenoid(self.win, 'black', 3, gridLen, gridLen, False, False, True, True)
        self.four = DiagramComponents.Solenoid(self.win, 'black', 4, gridLen, gridLen, False, True, False, False)
        self.five = DiagramComponents.Solenoid(self.win, 'black', 5, gridLen, gridLen, True, False, False, True)
        self.six = DiagramComponents.Solenoid(self.win, 'black', 6, gridLen, gridLen, False, True, False, True)
        self.one.getWidget().place(x=gridLen * 1, y=gridLen * 2)
        self.one.setIn(2)
        self.one.setOut(3)
        self.two.getWidget().place(x=gridLen * 0, y=gridLen * 4)
        self.two.setIn(2)
        self.three.getWidget().place(x=gridLen * 6, y=gridLen * 2)
        self.three.setIn(4)
        self.three.setOut(3)
        self.four.getWidget().place(x=gridLen * 5, y=gridLen * 4)
        self.four.setIn(2)
        self.five.getWidget().place(x=gridLen * 3, y=gridLen * 8)
        self.five.setIn(1)
        self.five.setOut(4)
        self.six.getWidget().place(x=gridLen * 4, y=gridLen * 7)
        self.six.setIn(4)
        self.six.setOut(2)

        # All STEPPER
        self.s1 = DiagramComponents.Stepper(self.win, 'black', gridLen, gridLen, True, False, False, True)
        self.s2 = DiagramComponents.Stepper(self.win, 'black', gridLen, gridLen, False, True, True, True)
        self.s1.getWidget().place(x=gridLen * 6, y=gridLen * 7)
        self.s2.getWidget().place(x=gridLen * 2, y=gridLen * 8)

        # All ORIFICES
        self.o1 = DiagramComponents.Orifice(self.win, 'black', gridLen, gridLen, True, False, True, False)
        self.o2 = DiagramComponents.Orifice(self.win, 'black', gridLen, gridLen, False, True, True, True)
        self.o1.getWidget().place(x=gridLen * 1, y=gridLen * 6)
        self.o2.getWidget().place(x=gridLen * 5, y=gridLen * 7)

        # All Pressure Sensors
        self.ps1 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, False, False)
        self.ps2 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True)
        self.ps3 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, True, True, True)
        self.ps1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.ps2.getWidget().place(x=gridLen * 7, y=gridLen * 3)
        self.ps3.getWidget().place(x=gridLen * 5, y=gridLen * 9)

        self.tp1 = DiagramComponents.TempSensor(self.win, 'black', gridLen, gridLen, True, False, False, False)
        self.tp1.getWidget().place(x=gridLen * 5, y=gridLen * 10)

        # All Text boxes
        self.t1 = Header.Text(self.win, 'black', 'K Fill', gridLen, gridLen, 12)
        self.t2 = Header.Text(self.win, 'black', 'K Drain', gridLen, gridLen, 12)
        self.t3 = Header.Text(self.win, 'black', 'LOx\nFill/Drain', gridLen, gridLen, 12)
        self.t4 = Header.Text(self.win, 'black', 'Regen\nCircuit', gridLen, gridLen, 12)
        self.t1.getWidget().place(x=gridLen * 7, y=gridLen * 4)
        self.t2.getWidget().place(x=gridLen * 7, y=gridLen * 6)
        self.t3.getWidget().place(x=gridLen * 1, y=gridLen * 9)
        self.t4.getWidget().place(x=gridLen * 7, y=gridLen * 9)

        # All PIPES
        self.p1 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p2 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p3 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p4 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p5 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p6 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p7 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p8 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, True, '#41d94d', False)
        self.p9 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p10 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p11 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p12 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p13 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p14 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, True, False, '#41d94d', False)
        self.p15 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p16 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, False, '#41d94d', False)
        self.p17 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p18 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, False, True, True, '#41d94d', False)
        self.p19 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p20 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p21 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, False, True, '#41d94d', False)
        self.p22 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
        self.p1.getWidget().place(x=gridLen * 2, y=gridLen * 2)
        self.p2.getWidget().place(x=gridLen * 3, y=gridLen * 2)
        self.p3.getWidget().place(x=gridLen * 4, y=gridLen * 2)
        self.p4.getWidget().place(x=gridLen * 5, y=gridLen * 2)
        self.p5.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p6.getWidget().place(x=gridLen * 3, y=gridLen * 3)
        self.p7.getWidget().place(x=gridLen * 6, y=gridLen * 3)
        self.p8.getWidget().place(x=gridLen * 1, y=gridLen * 4)
        self.p9.getWidget().place(x=gridLen * 3, y=gridLen * 4)
        self.p10.getWidget().place(x=gridLen * 6, y=gridLen * 4)
        self.p11.getWidget().place(x=gridLen * 3, y=gridLen * 5)
        self.p12.getWidget().place(x=gridLen * 3, y=gridLen * 6)
        self.p13.getWidget().place(x=gridLen * 6, y=gridLen * 6)
        self.p14.getWidget().place(x=gridLen * 1, y=gridLen * 7)
        self.p15.getWidget().place(x=gridLen * 3, y=gridLen * 7)
        self.p16.getWidget().place(x=gridLen * 1, y=gridLen * 8)
        self.p17.getWidget().place(x=gridLen * 5, y=gridLen * 8)
        self.p18.getWidget().place(x=gridLen * 6, y=gridLen * 8)
        self.p19.getWidget().place(x=gridLen * 2, y=gridLen * 9)
        self.p20.getWidget().place(x=gridLen * 3, y=gridLen * 9)
        self.p21.getWidget().place(x=gridLen * 4, y=gridLen * 9)
        self.p22.getWidget().place(x=gridLen * 6, y=gridLen * 9)

        # NOZZLE
        self.n = DiagramComponents.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 3, y=gridLen * 10)

        #self.s2.setNeighbors(None, self.five, self.p19, self.p16)
        #self.s1.setNeighbors(self.p13, None, None, self.o2)


        #SET ALL VIRTUAL COMPONENTS (linked list)
        self.head = self.gn2
        #row 1
        self.gn2.setNeighbors(None, None, self.p2, None)
        #row 2
        self.one.setNeighbors(None, None, self.p5, None)
        self.p1.setNeighbors(None, None, None, self.one)
        self.p2.setNeighbors(None, self.p3, self.p6, self.p1)
        self.p3.setNeighbors(None, self.p4, None, None)
        self.p4.setNeighbors(None, self.three, None, None)
        self.three.setNeighbors(None, None, self.p7, None)
        #row 3
        self.ps1.setNeighbors(None, None, None, None)
        self.p5.setNeighbors(None, None, self.p8, self.ps1)
        self.p6.setNeighbors(None, None, self.p9, None)
        self.p7.setNeighbors(None, self.ps2, self.p10, None)
        self.ps2.setNeighbors(None, None, None, None)
        #row 4
        self.two.setNeighbors(None, None, None, None)
        self.p8.setNeighbors(None, None, self.lox, self.two)
        self.p9.setNeighbors(None, None, self.p11, None)
        self.four.setNeighbors(None, None, None, None)
        self.p10.setNeighbors(None, None, self.k, self.four)
        #row5
        self.lox.setNeighbors(None, None, self.o1, None)
        self.p11.setNeighbors(None, None, self.p12, None)
        self.k.setNeighbors(None, None, self.p13, None)
        #row 6
        self.o1.setNeighbors(None, None, self.p14, None)
        self.p12.setNeighbors(None, None, self.p15, None)
        self.p13.setNeighbors(None, None, self.s1, None)
        #row 7
        self.p14.setNeighbors(None, None, self.p16, None)
        self.p15.setNeighbors(None, self.six, self.five, None)
        self.six.setNeighbors(None, self.o2, None, None)
        self.o2.setNeighbors(None, None, self.p17, None)
        self.s1.setNeighbors(None, None, None, self.o2)
        #row 8
        self.p16.setNeighbors(None, self.s2, None, None)
        self.s2.setNeighbors(None, None, self.p19, None)
        self.five.setNeighbors(None, None, None, self.s2)
        self.p17.setNeighbors(None, self.p18, None, None)
        self.p18.setNeighbors(None, None, self.p22, None)
        #row 9
        self.p19.setNeighbors(None, self.p20, None, None)
        self.p20.setNeighbors(None, None, self.n, None)
        self.p21.setNeighbors(None, None, None, self.p20)
        self.ps3.setNeighbors(None, None, self.tp1, self.p21)
        self.p22.setNeighbors(None, None, None, self.ps3)
        #row 10
        self.n.setNeighbors(None, None, None, None)
        self.tp1.setNeighbors(None, None, None, None)

        """# SET ALL VIRTUAL COMPONENTS (doubly linked list)
        self.head = self.gn2
        # row 1
        self.gn2.setNeighbors(None, None, self.p2, None)
        # row 2
        self.one.setNeighbors(None, self.p1, self.p5, None)
        self.p1.setNeighbors(None, self.p2, None, self.one)
        self.p2.setNeighbors(self.gn2, self.p3, self.p6, self.p1)
        self.p3.setNeighbors(None, self.p4, None, self.p2)
        self.p4.setNeighbors(None, self.three, None, self.p3)
        self.three.setNeighbors(None, None, self.p7, self.p4)
        # row 3
        self.ps1.setNeighbors(None, self.p5, None, None)
        self.p5.setNeighbors(self.one, None, self.p8, self.ps1)
        self.p6.setNeighbors(self.p2, None, self.p9, None)
        self.p7.setNeighbors(self.three, self.ps2, self.p10, None)
        self.ps2.setNeighbors(None, None, None, self.p7)
        # row 4
        self.two.setNeighbors(None, self.p8, None, None)
        self.p8.setNeighbors(self.p5, None, self.lox, self.two)
        self.p9.setNeighbors(self.p6, None, self.p11, None)
        self.four.setNeighbors(None, self.p10, None, None)
        self.p10.setNeighbors(self.p7, None, self.k, self.four)
        # row5
        self.lox.setNeighbors(self.p8, None, self.o1, None)
        self.p11.setNeighbors(self.p9, None, self.p12, None)
        self.k.setNeighbors(self.p10, None, self.p13, None)
        # row 6
        self.o1.setNeighbors(self.lox, None, self.p14, None)
        self.p12.setNeighbors(self.p11, None, self.p15, None)
        self.p13.setNeighbors(self.k, None, self.s1, None)
        # row 7
        self.p14.setNeighbors(self.o1, None, self.p16, None)
        self.p15.setNeighbors(self.p12, self.six, self.five, None)
        self.six.setNeighbors(None, self.o2, None, self.p15)
        self.o2.setNeighbors(None, self.s1, self.p17, self.six)
        self.s1.setNeighbors(self.p13, None, None, self.o2)
        # row 8
        self.p16.setNeighbors(self.p14, self.s2, None, None)
        self.s2.setNeighbors(None, self.five, self.p19, self.p16)
        self.five.setNeighbors(self.p15, None, None, self.s2)
        self.p17.setNeighbors(self.o2, self.p18, None, None)
        self.p18.setNeighbors(None, None, self.p22, self.p17)
        # row 9
        self.p19.setNeighbors(self.s2, self.p20, None, None)
        self.p20.setNeighbors(None, self.p21, self.n, self.p19)
        self.p21.setNeighbors(None, self.ps3, None, self.p20)
        self.ps3.setNeighbors(None, self.p22, self.tp1, self.p21)
        self.p22.setNeighbors(self.p18, None, None, self.ps3)
        # row 10
        self.n.setNeighbors(self.p20, None, None, None)
        self.tp1.setNeighbors(self.ps3, None, None, None)"""

    def defaultState(self):
        self.p1.setState(False)
        self.p2.setState(False)
        self.p3.setState(False)
        self.p4.setState(False)
        self.p5.setState(False)
        self.p6.setState(False)
        self.p7.setState(False)
        self.p8.setState(False)
        self.p9.setState(False)
        self.p10.setState(False)
        self.p11.setState(False)
        self.p12.setState(False)
        self.p13.setState(False)
        self.p14.setState(False)
        self.p15.setState(False)
        self.p16.setState(False)
        self.p17.setState(False)
        self.p18.setState(False)
        self.p19.setState(False)
        self.p20.setState(False)
        self.p21.setState(False)
        self.p22.setState(False)

        self.one.setPipes(False, False, False, False)
        self.two.setPipes(False, False, False, False)
        self.three.setPipes(False, False, False, False)
        self.four.setPipes(False, False, False, False)
        self.five.setPipes(False, False, False, False)
        self.six.setPipes(False, False, False, False)

        self.ps1.setPipes(False)
        self.ps2.setPipes(False)
        self.ps3.setPipes(False)

        self.o1.setPipes(False)
        self.o2.setPipes(False)

        self.s1.setPipes(False, False, False, False)
        self.s2.setPipes(False, False, False, False)

        self.tp1.setPipes(False)



    def getHead(self):
        return self.gn2

    def updatePipeStatus(self):
        self.defaultState()

        head = self.getHead()

        listMultiplePaths = []
        visited = []
        listMultiplePaths.append(head)

        # Basic traversal method
        while(len(listMultiplePaths) > 0):
            if(type(head) is DiagramComponents.Pipe):
                head.setState(True)

            if (head.top is not None and head.top not in visited):
                if(type(head.top) is DiagramComponents.Solenoid and head.top.getState()):
                    listMultiplePaths.append(head.top)
                    visited.append(head.top)
                elif(type(head.top) is not DiagramComponents.Solenoid and type(head.top) is not DiagramComponents.Stepper):
                    listMultiplePaths.append(head.top)
                    visited.append(head.top)
                elif (type(head.top) is DiagramComponents.Stepper and head.top.getPercentage() > 0):
                    listMultiplePaths.append(head.top)
                    visited.append(head.top)
            if (head.right is not None and head.right not in visited):
                if (type(head.right) is DiagramComponents.Solenoid and head.right.getState()):
                    listMultiplePaths.append(head.right)
                    visited.append(head.right)
                elif (type(head.right) is not DiagramComponents.Solenoid and type(head.right) is not DiagramComponents.Stepper):
                    listMultiplePaths.append(head.right)
                    visited.append(head.right)
                elif (type(head.right) is DiagramComponents.Stepper and head.right.getPercentage() > 0):
                    listMultiplePaths.append(head.right)
                    visited.append(head.right)
            if (head.bottom is not None and head.bottom not in visited):
                if (type(head.bottom) is DiagramComponents.Solenoid and head.bottom.getState()):
                    listMultiplePaths.append(head.bottom)
                    visited.append(head.bottom)
                elif (type(head.bottom) is not DiagramComponents.Solenoid and type(head.bottom) is not DiagramComponents.Stepper):
                    listMultiplePaths.append(head.bottom)
                    visited.append(head.bottom)
                elif (type(head.bottom) is DiagramComponents.Stepper and head.bottom.getPercentage() > 0):
                    listMultiplePaths.append(head.bottom)
                    visited.append(head.bottom)
            if (head.left is not None and head.left not in visited):
                if (type(head.left) is DiagramComponents.Solenoid and head.left.getState()):
                    listMultiplePaths.append(head.left)
                    visited.append(head.left)
                elif (type(head.left) is not DiagramComponents.Solenoid and type(head.left) is not DiagramComponents.Stepper):
                    listMultiplePaths.append(head.left)
                    visited.append(head.left)
                elif (type(head.left) is DiagramComponents.Stepper and head.left.getPercentage() > 0):
                    listMultiplePaths.append(head.left)
                    visited.append(head.left)

            listMultiplePaths.pop(0)
            if(len(listMultiplePaths) > 0):
                head = listMultiplePaths[0]
            else:
                break

        #edge checks for components with pipes (excluding pipes)
        if(self.p1.getState()):
            self.one.setFill(False, True, False, False)
        if(self.p4.getState()):
            self.three.setFill(False, False, False, True)
        if(self.p5.getState()):
            self.one.setFill(False, False, True, False)
            self.ps1.setFill(False, True, False, False)
        if(self.p7.getState()):
            self.three.setFill(False, False, True, False)
            self.ps2.setFill(False, False, False, True)
        if(self.p8.getState()):
            self.two.setFill(False, True, False, False)
            self.o1.setFill(True, False, False, False)
        if(self.p10.getState()):
            self.four.setFill(False, True, False, False)
        if(self.p14.getState()):
            self.o1.setFill(False, False, True, False)
        if(self.p15.getState()):
            self.five.setFill(True, False, False, False)
            self.six.setFill(False, False, False, True)
            if(self.six.getState()):
                self.six.setFill(False, True, False, False)
                self.o2.setFill(False, False, True, True)
            if(self.five.getState()):
                self.five.setFill(False, False, False, True)
                self.s2.setFill(False, True, False, False)
                if(self.s2.getPercentage() > 0):
                    self.s2.setFill(False, False, True, False)
        if(self.p13.getState()):
            self.s1.setFill(True, False, False, False)
            if(self.s1.getPercentage() > 0):
                self.s1.setFill(False, False, False, True)
                self.o2.setFill(False, True, True, False)
        if(self.p16.getState()):
            self.s2.setFill(False, False, False, True)
            if(self.s2.getPercentage() > 0):
                self.s2.setFill(False, False, True, False)
        if(self.p22.getState()):
            self.ps3.setFill(False, True, True, True)
            self.tp1.setFill(True, False, False, False)

    def getWindow(self):
        return self.win


class Solids_Engine_Plumbing:

    def __init__(self, gridLen):

        width = gridLen * 3
        height = gridLen * 7

        self.win = tk.Tk()
        self.win.title("P&ID Diagram")
        self.win.geometry(str(width) + "x" + str(height))
        self.win.configure(bg='black')

        # CONSTANT
        fluidColor = '#41d94d'

        # HEADER
        self.header = Header.Header(self.win, 'black', 'P&ID', width, gridLen, 24)
        self.header.getWidget().place(x=gridLen * 0, y=gridLen * 0)

        # All TANKS
        self.gn2 = DiagramComponents.Tank(self.win, 'black', 'GN2', '#1d2396', gridLen, gridLen)
        self.ovp = DiagramComponents.Tank(self.win, 'black', 'Over\nPres', '#f542b9', gridLen, gridLen)
        self.gn2.getWidget().place(x=gridLen * 0, y=gridLen * 1)
        self.ovp.getWidget().place(x=gridLen * 2, y=gridLen * 1)

        # All SOLENOID VALVES
        self.one = DiagramComponents.Solenoid(self.win, 'black', 1, gridLen, gridLen, True, False, True, False)
        self.two = DiagramComponents.Solenoid(self.win, 'black', 1, gridLen, gridLen, True, False, True, False)
        self.one.getWidget().place(x=gridLen * 0, y=gridLen * 2)
        self.two.getWidget().place(x=gridLen * 2, y=gridLen * 2)

        # All Pressure Sensors
        self.ps1 = DiagramComponents.PressureSensor(self.win, 'black', gridLen, gridLen, False, False, False, True)
        self.ps1.getWidget().place(x=gridLen * 2, y=gridLen * 4)

        # All Text boxes
        self.t1 = Header.Text(self.win, 'black', 'Relief Valve', gridLen, gridLen, 12)
        self.t2 = Header.Text(self.win, 'black', 'WIRE 1', gridLen, gridLen, 12)
        self.t3 = Header.Text(self.win, 'black', 'WIRE 2', gridLen, gridLen, 12)
        self.t1.getWidget().place(x=gridLen * 0, y=gridLen * 4)
        self.t2.getWidget().place(x=gridLen * 2, y=gridLen * 5)
        self.t3.getWidget().place(x=gridLen * 2, y=gridLen * 6)

        # All PIPES
        self.p1 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, False, False, '#41d94d', False)
        self.p2 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, False, True, True, True, '#41d94d', False)
        self.p3 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, False, False, True, '#41d94d', False)
        self.p4 = DiagramComponents.Pipe(self.win, 'black', gridLen, gridLen, True, True, True, True, '#41d94d', False)
        self.p1.getWidget().place(x=gridLen * 0, y=gridLen * 3)
        self.p2.getWidget().place(x=gridLen * 1, y=gridLen * 3)
        self.p3.getWidget().place(x=gridLen * 2, y=gridLen * 3)
        self.p4.getWidget().place(x=gridLen * 1, y=gridLen * 4)


        # NOZZLE
        self.n = DiagramComponents.Nozzle(self.win, 'black', gridLen, gridLen * 1.5)
        self.n.getWidget().place(x=gridLen * 1, y=gridLen * 5)



    def getWindow(self):
        return self.win


"""gridLen = 60
plumbing = UCI_Liquid_Engine_Plumbing(gridLen)
plumbing.getWindow().mainloop()"""