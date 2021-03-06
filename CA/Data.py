import numpy as  np

flag=True

ROOM_M=40 #房间长
ROOM_N=40 #房间宽

EXIT_X=ROOM_M/2
EXIT_Y=ROOM_N

LOGO_NULL=0
LOGO_PEOPLE=1
LOGO_WALL=10
# LOGE_BAR=20
LOGO_EXIT=100

# STATIC_FIELD=0

'''-------------------------------------------------------------------------------'''
'''---------------------------背景场----------------------------------------------'''
'''-------------------------------------------------------------------------------'''
def STATIC_FIELD1():
    STATIC_FIELD = np.zeros((40, 40))
    for b in range(35, 39):
        for jj in range(0, 19):  # 左部门口边界
            STATIC_FIELD[jj][39] = -1000
            STATIC_FIELD[jj][b] = 4.5
        for kk in range(22, 39):  # 右部门口边界
            STATIC_FIELD[kk][39] = -1000
            STATIC_FIELD[kk][b] = 4.5
        for e in range(19, 22):
            STATIC_FIELD[e][b] = 5  # 教室上部  含出口
            STATIC_FIELD[e][39] = 1000
    for ii in range(0, 39):
        STATIC_FIELD[0][ii] = -1000
        STATIC_FIELD[ii][0] = -1000
        STATIC_FIELD[39][ii] = -1000
        STATIC_FIELD[39][39] = -1000  # 教室边界
    for l in range(6, 38, 2):
        for m in range(6, 19):  # 教室课桌之间
           STATIC_FIELD[l][m] = 3
        for n in range(22, 35):
            STATIC_FIELD[l][n] = 2
    for o in range(5, 37, 2):
        for oo in range(6, 19):
            STATIC_FIELD[o, oo] = -1000
        for ooo in range(22, 35):
            STATIC_FIELD[o, ooo] = -1000
    for j in range(1, 6):
        for i in range(1, 39):  # 教室下部
            STATIC_FIELD[i][j] = 1
    for z in range(19, 22):
        for zz in range(6, 35):
            STATIC_FIELD[zz][z] = 3.5
    for cc in range(5, 37):
        for c in range(1, 6):
            STATIC_FIELD[c][cc] = 4
        for ccc in range(35, 39):
            STATIC_FIELD[ccc][cc] = 4
    print(STATIC_FIELD)
    return STATIC_FIELD
def STATIC_FIELD2():
    STATIC_FIELD = np.zeros((40, 40))
    '----------------------教室最上部----------------------------'
    for b in range(35, 39):
        for jj in range(0, 19):  # 左部门口边界
            STATIC_FIELD[jj][39] = -1000
            STATIC_FIELD[jj][b] = 4.8
        for kk in range(22, 39):  # 右部门口边界
            STATIC_FIELD[kk][39] = -1000
            STATIC_FIELD[kk][b] = 4.8
        for e in range(19, 22):
            STATIC_FIELD[e][b] = 5  # 教室上部  含出口
            STATIC_FIELD[e][39] = 1000
    '-------------------------教室边界---------------------------'
    for ii in range(0, 39):
        STATIC_FIELD[0][ii] = -1000
        STATIC_FIELD[ii][0] = -1000
        STATIC_FIELD[39][ii] = -1000
        STATIC_FIELD[39][39] = -1000  # 教室边界
    '-------------------------教室课桌---------------------------'
    for l in range(6, 38, 2):
        '''教室课桌之间'''
        for m in range(6, 19):
            '''上部'''
            STATIC_FIELD[l][m] = 4
        for n in range(22, 35):
            '''下部'''
            STATIC_FIELD[l][n] = 3.5
    for o in range(5, 37, 2):
        for oo in range(6, 19):
            STATIC_FIELD[o, oo] = -1000
        for ooo in range(22, 35):
            STATIC_FIELD[o, ooo] = -1000
    '-----------------------教室下部-------------------------------'
    for j in range(1, 6):
        for i in range(1, 39):  # 教室下部
            STATIC_FIELD[i][j] = 3
    '-----------------------桌椅中过道-----------------------------'
    for z in range(19, 22):
        for zz in range(6, 35):
            STATIC_FIELD[zz][z] = 4.5
    '-----------------------教室两翼-------------------------------'
    for cc in range(5, 37):
        for c in range(1, 6):
            STATIC_FIELD[c][cc] = 3
        for ccc in range(35, 39):
            STATIC_FIELD[ccc][cc] = 3
    print(STATIC_FIELD)
    return STATIC_FIELD
'''-----------------------------------------------------------------------------'''
PEOPLE_DENSITY=0.1
PEOPLE_NUMBER=int(ROOM_M*ROOM_N*PEOPLE_DENSITY)
