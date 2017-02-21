
class market(object):
    def __init__ (self):
        self.turn = 1
    def build_generic(self,player):
        item = raw_input("Build What?")
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
    def sell_generic(self,player):
        item = raw_input("Sell What?")
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
        strBuildings = ""
        for x in self.buildings:
            strBuildings = strBuildings + str(x.type) + ","
        return strBuildings
    def upkeep(self):
        #Upkeep of rice
        #if not enough rice, no production
        #if rice, but not enough for total, then reduced production
        pass
        
running = True

objPlayer = player()
objMarket = market()

while running ==True:

#THIS IS THE VIEW CONTROLLER!
    
    #display info
    print "TURN " + str(objMarket.turn)
    print "GOLD: " + str(objPlayer.gold)
    print "WOOD: " + str(objPlayer.wood)
    print "STONE: " + str(objPlayer.stone)
    print "RICE: " + str(objPlayer.rice)
    print objPlayer.show_buildings()
    
    #wait for button press
    action = raw_input("Player Input >>>")

    #process depending on button press
    #this can probably be broken to different functions
    if action == "BUILD":
        print str(objMarket.build_generic(objPlayer))
    elif action == "SELL":
        print str(objMarket.sell_generic(objPlayer))
    elif action == "END":
        print "END TURN"
        if objPlayer.gold >= 60:
            print "You Win"
            running = False
        else:
            objMarket.end_turn(objPlayer)
    else:
        print "Command Not Recognised"
    
print "GAME OVER"
