#mixes TKinter GUI with Game
from Tkinter import *

#these routines tie game model and GUI together
def end_turn():
    objMarket.end_turn(objPlayer)
    objGUI.end_turn(objMarket.turn)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice)
def build(item):
    objMarket.build_generic(objPlayer,item)
    objGUI.update_bd(objPlayer.bd_count("L"),objPlayer.bd_count("S"),objPlayer.bd_count("R"))
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice)
def sell(item):
    objMarket.sell_generic(objPlayer,item)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice)
    
#Main GUI
class mainGUI(object):
    def __init__(self):
        self.interface = Tk()
        #Containers for various information
        self.frame_turn = Canvas(self.interface, bg="blue", height = 20, width = 400)
        self.frame_stats = Canvas(self.interface, bg="red", height=100, width=130)
        self.frame_buildings = Canvas(self.interface, bg="red", height=100, width=130)
        self.frame_commands = LabelFrame(self.interface)
        self.frame_canvas = Canvas(self.interface, bg="black", height = 200, width = 170)
        #placement on overall window/interface
        self.frame_turn.grid(column = 0, row = 0, columnspan = 3)
        self.frame_stats.grid(column = 1, row = 1)
        self.frame_commands.grid(column = 0, row = 1, rowspan = 2,sticky = E)
        self.frame_buildings.grid(column = 1, row = 2)
        self.frame_canvas.grid(column = 2, row = 1, rowspan = 2, sticky = N+S)
        #text based tag for turn number
        self.turn = self.frame_turn.create_text(200,10, text="TURN: " + str(objMarket.turn))
        #inset list of buildings
        self.lumbermills = self.frame_buildings.create_text(10,10, anchor = NW, text="LUMBERMILLS: " + str(objPlayer.bd_count("L")))
        self.stonemills = self.frame_buildings.create_text(10,30, anchor = NW, text="STONEMILLS: " + str(objPlayer.bd_count("S")))
        self.ricefields = self.frame_buildings.create_text(10,50, anchor = NW, text="RICEFIELDS: " + str(objPlayer.bd_count("R")))
        #text based tags for player's economy
        self.gold = self.frame_stats.create_text(10,10, anchor = NW, text="GOLD: " + str(objPlayer.gold))
        self.wood = self.frame_stats.create_text(10,30, anchor = NW, text="WOOD: " + str(objPlayer.wood))
        self.stone = self.frame_stats.create_text(10,50, anchor = NW, text="STONE: " + str(objPlayer.stone))
        self.rice = self.frame_stats.create_text(10,70, anchor = NW, text="RICE: " + str(objPlayer.rice))        
        #buttons and placement for player commands
        self.button1 = Button(self.frame_commands, text="BUILD", command = self.show_build_menu)
        self.button2 = Button(self.frame_commands, text="SELL", command = self.show_sell_menu)
        self.button3 = Button(self.frame_commands, text="END TURN", command = end_turn)
        self.button1.grid(column = 0, row = 0, sticky=W+E)
        self.button2.grid(column = 0, row = 1, sticky=W+E)
        self.button3.grid(column = 0, row = 2, sticky=W+E)
    def show_build_menu(self):
        self.top = Toplevel()
        self.frame_sub_commands = Frame(self.top)
        self.frame_sub_commands.grid(column=0, row=0)
        self.button1 = Button(self.frame_sub_commands, text="LUMBERMILL", command= lambda: build("L"))
        self.button2 = Button(self.frame_sub_commands, text="STONEMILL", command = lambda: build("S"))
        self.button3 = Button(self.frame_sub_commands, text="RICEFIELD", command = lambda: build("R"))
        self.button1.grid(column = 0, row = 0, sticky=W+E)
        self.button2.grid(column = 0, row = 1, sticky=W+E)
        self.button3.grid(column = 0, row = 2, sticky=W+E)
    def show_sell_menu(self):
        self.top = Toplevel()        
        self.frame_sub_commands = Frame(self.top)
        self.frame_sub_commands.grid(column=0, row=0)
        self.button1 = Button(self.frame_sub_commands, text="WOOD", command= lambda: sell("W"))
        self.button2 = Button(self.frame_sub_commands, text="STONE", command = lambda: sell("S"))
        self.button3 = Button(self.frame_sub_commands, text="RICE", command = lambda: sell("R"))
        self.button1.grid(column = 0, row = 0, sticky=W+E)
        self.button2.grid(column = 0, row = 1, sticky=W+E)
        self.button3.grid(column = 0, row = 2, sticky=W+E)
    def update_player(self,p_g,p_w,p_s,p_r):
        self.frame_stats.itemconfig(self.gold, text = "GOLD: " + str(p_g))
        self.frame_stats.itemconfig(self.wood, text = "WOOD: " + str(p_w))
        self.frame_stats.itemconfig(self.stone, text = "STONE: " + str(p_s))
        self.frame_stats.itemconfig(self.rice, text = "RICE: " + str(p_r))
    def update_bd(self,p_l,p_s,p_r):
        self.frame_buildings.itemconfig(self.lumbermills, text = "LUMBERMILLS: " + str(p_l))
        self.frame_buildings.itemconfig(self.stonemills, text = "STONEMILLS: " + str(p_s))
        self.frame_buildings.itemconfig(self.ricefields, text = "RICEFIELDS: " + str(p_r))
    def end_turn(self,i):
        self.frame_turn.itemconfig(self.turn, text = "TURN: " + str(i))
    def show_screen(self):
        #Models get stuck here until you close the Tkinter window
        self.interface.mainloop()

class market(object):
    def __init__ (self):
        self.turn = 1
    def build_generic(self,player,item):
        if item == "L":
            objLM = lumbermill("L",20,10,10,10,0,0)
            if objLM.check_cost(player) == True:
                player.gold -= objLM.cost_gold
                player.wood -= objLM.cost_wood
                player.stone -= objLM.cost_stone
                player.buildings.append(objLM)
                return "LUMBERMILL BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD LUMBERMILL"
        elif item == "S":
            objSM = stonemill("S",10,20,10,0,10,0)
            if objSM.check_cost(player) == True:
                player.gold -= objSM.cost_gold
                player.wood -= objSM.cost_wood
                player.stone -= objSM.cost_stone
                player.buildings.append(objSM)
                return "STONEMILL BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD STONEMILL"
        elif item == "R":
            objRF = rice_field("R",20,20,20,0,0,10)
            if objRF.check_cost(player) == True:
                player.gold -= objRF.cost_gold
                player.wood -= objRF.cost_wood
                player.stone -= objRF.cost_stone
                player.buildings.append(objRF)
                return "RICEFIELD BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD RICEFIELD"
        else:
            return "Not Recognised"
    def sell_generic(self,player,item):
        if item == "W":
            if player.wood >=10:
                player.wood -=10
                player.gold +=5
                return "10 Units Wood Sold"
            else:
                return "Need 10 Units to Sell"
        if item == "R":
            if player.rice >=50:
                player.rice -=50
                player.gold +=10
                return "50 Units Rice Sold"
            else:
                return "Need 50 Units to Sell"
        elif item == "S":
            if player.stone >=5:
                player.stone -=5
                player.gold +=5
                return "5 Units Stone Sold"
            else:
                return "Need 5 Units to Sell"
        else:
            return "Not Recognised"
    def end_turn(self,player):
        for x in player.buildings:
            x.production(player)
        self.turn+=1

class army_unit(object):
    def __init__(self):
        pass

class building(object):
    def __init__(self,strName,cost_wood,cost_stone,cost_gold,prod_wood,prod_stone,prod_rice):
        self.type = strName
        self.cost_wood = cost_wood
        self.cost_stone = cost_stone
        self.cost_gold = cost_gold
        self.prod_wood = prod_wood
        self.prod_stone = prod_stone
        self.prod_rice = prod_rice
    def production(self,player):
        player.wood += self.prod_wood
        player.stone += self.prod_stone
        player.rice += self.prod_rice
    def upkeep(self,player):
        pass
    def check_cost(self,player):
        if self.cost_gold <= player.gold:
            if self.cost_wood <= player.wood:            
                if self.cost_stone <= player.stone:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

class lumbermill(building):
    def __init(self):
        building.__init__(20,10,10,10,0)

class stonemill(building):
    def __init(self):
        building.__init__(10,20,10,0,10)

class rice_field(building):
    def __init(self):
        building.__init__(20,20,20,0,0,10)
        
class barracks(building):
    def __init(self):
        building.__init__(30,30,20,0,0)
    def hire_units(self,player):
        pass
    
class player(object):
    def __init__(self):
        self.gold = 50
        self.wood = 50
        self.stone = 50
        self.rice = 0
        self.buildings = []
        self.army = []
    def show_buildings(self):
        #count L,S,R
        strBuildings = ""
        for x in self.buildings:
            strBuildings = strBuildings + str(x.type) + ","
        return strBuildings
    def bd_count(self,i):
        x = 0
        for z in self.buildings:
            if str(z.type) == str(i):
                x+=1
        return x
                                    
    def upkeep(self):
        #Upkeep of rice
        #if not enough rice, no production
        #if rice, but not enough for total, then reduced production
        pass

objPlayer = player()
objMarket = market()

objGUI = mainGUI()

objGUI.show_screen()

