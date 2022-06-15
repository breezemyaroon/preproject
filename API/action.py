from conDB import Con

class Action:
    def getHW():
        data = Con.getHW()
        return data
    
    
    def update_set_ware(ID, status): 
        t = Con.update_set_ware(ID, status)
        if( t):
            data ={"error": False}
        else:
            data = {"error": True}
            
        return data
        
    def select_ware(ID):  
        data = Con.select_ware(ID)
        return data
    
    def ADD_Hard_Ware(name, HW_name):
        ID = Con.ADD_Hard_Ware(name, HW_name)
        if( ID):
            data =Con.select_ware(ID)
        else:
            data = {"error": True}
            
        return data
    
    # def delete_from_were(ID):
    #     data = Con.delete_from_were(ID)
    #     return data
    