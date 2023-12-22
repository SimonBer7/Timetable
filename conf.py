from generator.lesson import Lesson

"""
Define instances of the Leason class representing different subjects
Each Leason instance contains an ID, subject code, lecturer, duration, day count, and type
"""
WA = Lesson(1, "WA", "Pavlat", 24, 4, "cviceni")
C = Lesson(2, "C", "Studenkova", 24, 4, "klasika")
AJ = Lesson(3, "AJ", "Juchelka", 5, 1, "klasika")
M = Lesson(4, "M", "Neugebauerova", 24, 4, "klasika")
PV = Lesson(5, "PV", "Ing. Mandik", 18, 3, "cviceni")
TP = Lesson(6, "TP", "Nohejl", 24, 4, "klasika")
DS = Lesson(7, "DB", "Kantnerova", 19, 3, "cviceni")
AM = Lesson(8, "AM", "Kallmunzer", 24, 4, "klasika")
TV = Lesson(9, "TV", "Lopocha", 2, 1, "telocvicna")
PIS = Lesson(10, "PIS", "Brcakova", 18, 3, "klasika")
CIT = Lesson(11, "CIT", "Mazuch", 17, 3, "cviceni")
PSS = Lesson(12, "PSS", "Masopust", 8, 2, "cviceni")
VH = Lesson(0, "VH", "None", 0, 0, "None")


timetable = [WA.id, WA.id, C.id, AJ.id, M.id, VH.id, PV.id, PV.id, VH.id, VH.id, M.id, TP.id, DS.id, DS.id, AJ.id, AM.id, VH.id, TV.id, VH.id, VH.id, PIS.id, C.id, CIT.id, CIT.id, AM.id, M.id, DS.id, VH.id, VH.id, VH.id, WA.id, M.id, PIS.id, PV.id, AJ.id, C.id, PSS.id, VH.id, VH.id, VH.id, VH.id, PIS.id, PIS.id, AJ.id, TV.id, PSS.id, PSS.id, VH.id, VH.id, VH.id]



