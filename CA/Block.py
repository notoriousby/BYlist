class Block():
    def __init__(self,logo=0):
        self.logo=logo
        self.x=0
        self.y=0
        self.type=True
        self.isCrowded=False
        self.isMove=True
        self.PeopleInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.distanceInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.tableInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.wallInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.exitInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.crowdedInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.jamInCome={1:0.0,2:0.0,3:0,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.allInComeBySort={}# 排序后的总收益
        self.allInCome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
        self.staticfieldInCome={1:0.0,2:0.0,3:0.3,4:0.0,5:0.0,6:0.0,7:0.0,8:0.0,9:0.0}
