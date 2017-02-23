#mixes TKinter GUI with Game
from Tkinter import *

#these routines tie game model and GUI together
def end_turn():
    objMarket.upkeep_calc(objPlayer)
    objMarket.end_turn(objPlayer)
    objGUI.end_turn(objMarket.turn)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice,objPlayer.prod_update(),objPlayer.upkeep_update())
    objGUI.update_army(objPlayer.army_count("S"), objPlayer.hunger_count())
def build(item):
    objMarket.build_generic(objPlayer,item)
    objGUI.update_bd(objPlayer.bd_count("L"),objPlayer.bd_count("S"),objPlayer.bd_count("R"),objPlayer.bd_count("B"))
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice,objPlayer.prod_update(),objPlayer.upkeep_update())
def sell(item):
    objMarket.sell_generic(objPlayer,item)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice,objPlayer.prod_update(),objPlayer.upkeep_update())
def recruit_army():
    objMarket.recruit_army(objPlayer)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice,objPlayer.prod_update(),objPlayer.upkeep_update())
    objGUI.update_army(objPlayer.army_count("S"), objPlayer.hunger_count())
def release_army():
    objMarket.release_army(objPlayer)
    objGUI.update_player(objPlayer.gold,objPlayer.wood,objPlayer.stone,objPlayer.rice,objPlayer.prod_update(),objPlayer.upkeep_update())
    objGUI.update_army(objPlayer.army_count("S"),objPlayer.hunger_count())
    
#Main GUI
class mainGUI(object):
    def __init__(self):
        self.interface = Tk()
        #Containers for various information
        self.frame_turn = Canvas(self.interface, bg="blue", height = 20, width = 400)
        self.frame_economy = Canvas(self.interface, bg="red", height = 80, width = 400)
        self.frame_stats = Canvas(self.interface, bg="red", height=100, width=130)
        self.frame_buildings = Canvas(self.interface, bg="red", height=100, width=130)
        self.frame_commands = LabelFrame(self.interface)
        self.frame_army = Canvas(self.interface, bg="red", height=50, width=170)
        self.frame_canvas = Canvas(self.interface, bg="black", height = 100, width = 170)
        #placement on overall window/interface
        self.frame_turn.grid(column = 0, row = 0, columnspan = 3)
        self.frame_economy.grid(column = 0, row = 1, columnspan = 3)
        self.frame_stats.grid(column = 1, row = 2)
        self.frame_commands.grid(column = 0, row = 2, rowspan = 2,sticky = E)
        self.frame_buildings.grid(column = 1, row = 3)
        self.frame_army.grid(column = 2,row=2)
        self.frame_army.grid(column = 2,row=2, sticky = N)
        self.frame_canvas.grid(column = 2, row = 3, rowspan=2, sticky = S)
        #text based tag for turn number
        self.turn = self.frame_turn.create_text(200,10, text="TURN: " + str(objMarket.turn))
        #text for economy
        self.production = self.frame_economy.create_text(100,10, text="PRODUCTION: 0")
        self.upkeep = self.frame_economy.create_text(300,10, text="UPKEEP: 0")
        #text list of buildings
        self.lumbermills = self.frame_buildings.create_text(10,10, anchor = NW, text="LUMBERMILLS: " + str(objPlayer.bd_count("L")))
        self.stonemills = self.frame_buildings.create_text(10,30, anchor = NW, text="STONEMILLS: " + str(objPlayer.bd_count("S")))
        self.ricefields = self.frame_buildings.create_text(10,50, anchor = NW, text="RICEFIELDS: " + str(objPlayer.bd_count("R")))
        self.barracks = self.frame_buildings.create_text(10,70, anchor = NW, text="UNITS: 0")
        self.army = self.frame_army.create_text(10,10, anchor=NW, text = "")
        self.hunger = self.frame_army.create_text(10,30, anchor=NW, text = "")
        #text based tags for player's economy
        self.gold = self.frame_stats.create_text(10,10, anchor = NW, text="GOLD: " + str(objPlayer.gold))
        self.wood = self.frame_stats.create_text(10,30, anchor = NW, text="WOOD: " + str(objPlayer.wood))
        self.stone = self.frame_stats.create_text(10,50, anchor = NW, text="STONE: " + str(objPlayer.stone))
        self.rice = self.frame_stats.create_text(10,70, anchor = NW, text="RICE: " + str(objPlayer.rice))        
        #buttons and placement for player commands
        self.button4 = Button(self.frame_commands, text="ARMY", state = DISABLED, command = self.show_army_menu)
        self.button1 = Button(self.frame_commands, text="BUILD", command = self.show_build_menu)
        self.button2 = Button(self.frame_commands, text="SELL", command = self.show_sell_menu)
        self.button3 = Button(self.frame_commands, text="END TURN", command = end_turn)
        self.button4.grid(column = 0, row = 0, sticky=W+E)
        self.button1.grid(column = 0, row = 1, sticky=W+E)
        self.button2.grid(column = 0, row = 2, sticky=W+E)
        self.button3.grid(column = 0, row = 3, sticky=W+E)
    def show_build_menu(self):
        self.top = Toplevel()
        self.frame_sub_commands = Frame(self.top)
        self.frame_sub_commands.grid(column=0, row=0)
        self.bbutton1 = Button(self.frame_sub_commands, text="LUMBERMILL", command= lambda: build("L"))
        self.bbutton2 = Button(self.frame_sub_commands, text="STONEMILL", command = lambda: build("S"))
        self.bbutton3 = Button(self.frame_sub_commands, text="RICEFIELD", command = lambda: build("R"))
        self.bbutton4 = Button(self.frame_sub_commands, text="BARRACKS", command = lambda: build("B"))
        self.bbutton1.grid(column = 0, row = 0, sticky=W+E)
        self.bbutton2.grid(column = 0, row = 1, sticky=W+E)
        self.bbutton3.grid(column = 0, row = 2, sticky=W+E)
        self.bbutton4.grid(column = 0, row = 3, sticky=W+E)
    def show_sell_menu(self):
        self.top = Toplevel()        
        self.frame_sub_commands = Frame(self.top)
        self.frame_sub_commands.grid(column=0, row=0)
        self.sbutton1 = Button(self.frame_sub_commands, text="WOOD", command= lambda: sell("W"))
        self.sbutton2 = Button(self.frame_sub_commands, text="STONE", command = lambda: sell("S"))
        self.sbutton3 = Button(self.frame_sub_commands, text="RICE", command = lambda: sell("R"))
        self.sbutton1.grid(column = 0, row = 0, sticky=W+E)
        self.sbutton2.grid(column = 0, row = 1, sticky=W+E)
        self.sbutton3.grid(column = 0, row = 2, sticky=W+E)
    def show_army_menu(self):
        self.top = Toplevel()
        self.frame_sub_commands = Frame(self.top)
        self.frame_sub_commands.grid(column=0,row=0)
        self.abutton1 = Button(self.frame_sub_commands, text="RECRUIT", command= recruit_army)
        self.abutton2 = Button(self.frame_sub_commands, text="RELEASE", command = release_army)
        self.abutton1.grid(column = 0, row = 0, sticky=W+E)
        self.abutton2.grid(column = 0, row = 1, sticky=W+E)
    def update_player(self,p_g,p_w,p_s,p_r,i_r,x_r):
        self.frame_stats.itemconfig(self.gold, text = "GOLD: " + str(p_g))
        self.frame_stats.itemconfig(self.wood, text = "WOOD: " + str(p_w))
        self.frame_stats.itemconfig(self.stone, text = "STONE: " + str(p_s))
        self.frame_stats.itemconfig(self.rice, text = "RICE: " + str(p_r))
        self.frame_economy.itemconfig(self.production, text = "PRODUCTION: " + str(i_r))
        self.frame_economy.itemconfig(self.upkeep , text = "UPKEEP: " + str(x_r))

    def update_bd(self,p_l,p_s,p_r,p_b):
        self.top.withdraw()
        self.frame_buildings.itemconfig(self.lumbermills, text = "LUMBERMILLS: " + str(p_l))
        self.frame_buildings.itemconfig(self.stonemills, text = "STONEMILLS: " + str(p_s))
        self.frame_buildings.itemconfig(self.ricefields, text = "RICEFIELDS: " + str(p_r))
        if p_b !=0:
            self.frame_buildings.itemconfig(self.barracks, text = "BARRACKS")
            self.button4.config(state = NORMAL)
    def update_army(self,p_a,p_h):
        self.frame_army.itemconfig(self.army, text = "UNITS: " + str(p_a))
        if int(p_h) > 0:
            self.frame_army.itemconfig(self.hunger, text = str(p_h) + "HUNGRY UNITS")
        else:
            self.frame_army.itemconfig(self.hunger, text = "")
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
            objLM = lumbermill("L",20,10,10,10,0,0,0)
            if objLM.check_cost(player) == True:
                player.gold -= objLM.cost_gold
                player.wood -= objLM.cost_wood
                player.stone -= objLM.cost_stone
                player.buildings.append(objLM)
                return "LUMBERMILL BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD LUMBERMILL"
        elif item == "S":
            objSM = stonemill("S",10,20,10,0,10,0,0)
            if objSM.check_cost(player) == True:
                player.gold -= objSM.cost_gold
                player.wood -= objSM.cost_wood
                player.stone -= objSM.cost_stone
                player.buildings.append(objSM)
                return "STONEMILL BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD STONEMILL"
        elif item == "R":
            objRF = rice_field("R",20,20,20,0,0,10,0)
            if objRF.check_cost(player) == True:
                player.gold -= objRF.cost_gold
                player.wood -= objRF.cost_wood
                player.stone -= objRF.cost_stone
                player.buildings.append(objRF)
                return "RICEFIELD BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD RICEFIELD"
        elif item == "B":
            objBk = barracks("B",30,30,30,0,0,0,10)
            if objBk.check_cost(player) == True:
                player.gold -= objBk.cost_gold
                player.wood -= objBk.cost_wood
                player.stone -= objBk.cost_stone
                player.buildings.append(objBk)
                return "RICEFIELD BUILT"
            else:
                return "NOT ENOUGH RESOURCES TO BUILD BARRACKS"
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
    def recruit_army(self,player):
        #check enough resources are available
        if player.gold >=10 and player.rice >=10:
            objUnit = army_unit()
            player.army.append(objUnit)
            player.gold -=10
            player.rice -=10
            return "Unit Purchased"
        else:
            return "Not enough resources"
    def release_army(self,player):
        if len(player.army) == 0:
            pass
        else:
            del player.army[len(player.army)-1]
    def end_turn(self,player):
        #Calc Production
        for x in player.buildings:
            x.production(player)
        self.turn+=1
    def upkeep_calc(self,player):
        for x in player.army:
            x.eat_rice(player)
        for x in player.buildings:
            x.eat_rice(player)
        player.defect_army()


class army_unit(object):
    def __init__(self):
        self.type = "S"
        self.HP = 10
        self.ATK = 10
        self.DEF = 10
        self.upkeep_rice= 5
        self.cost_gold = 10
        self.cost_rice = 10
        self.hungry = False
        self.runaway = False
    def eat_rice(self,player):
        if self.hungry == True:
            self.runaway = True
        if player.rice < self.upkeep_rice:
            self.hungry = True
        else:
            self.hungry = False
        player.rice -=self.upkeep_rice


class building(object):
    def __init__(self,strName,cost_wood,cost_stone,cost_gold,prod_wood,prod_stone,prod_rice,upkeep_rice):
        self.type = strName
        self.cost_wood = cost_wood
        self.cost_stone = cost_stone
        self.cost_gold = cost_gold
        self.prod_wood = prod_wood
        self.prod_stone = prod_stone
        self.prod_rice = prod_rice
        self.upkeep_rice = upkeep_rice
    def production(self,player):
        if player.rice < 0:
            multiplier = 0.8
        else:
            multiplier = 1
        player.wood += self.prod_wood*multiplier
        player.stone += self.prod_stone*multiplier
        player.rice += self.prod_rice*multiplier
    def eat_rice(self,player):
        player.rice-= self.upkeep_rice
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
        building.__init__()

class stonemill(building):
    def __init(self):
        building.__init__()

class rice_field(building):
    def __init(self):
        building.__init__()
        
class barracks(building):
    def __init(self):
        building.__init__()
    def hire_units(self,player):
        pass
    def upkeep(self):
        print "CALCULATING UPKEEP"
        pass
    
class player(object):
    def __init__(self):
        self.gold = 500
        self.wood = 500
        self.stone = 500
        self.rice = 10
        self.buildings = []
        self.army = []
    def bd_count(self,i):
        x = 0
        for z in self.buildings:
            if str(z.type) == str(i):
                x+=1
        return x
    def army_count(self,i):
        x = 0
        for z in self.army:
            if str(z.type) == str(i):
                x+=1
        return x
    def hunger_count(self):
        x = 0
        for z in self.army:
            if z.hungry == True:
                x +=1
        return x              
    def defect_army(self):
        for x in self.army:
            if x.runaway == True:
                self.army.remove(x)
    def upkeep_update(self):
        #calc how much rice will be taken on end turn
        #number of soldiers + number of buildings with upkeep
        intRice = 0
        for x in self.army:
            intRice += x.upkeep_rice
        for x in self.buildings:
            intRice += x.upkeep_rice
        return intRice
    def prod_update(self):
        intProd = 0
        for x in self.buildings:
            if self.rice <= self.upkeep_update():
                intProd += 0.8*int(x.prod_rice)
            else:
                intProd += x.prod_rice
        return intProd

objPlayer = player()
objMarket = market()

objGUI = mainGUI()
objGUI.show_screen()

