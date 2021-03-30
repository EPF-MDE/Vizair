from collections import namedtuple

class heroDto:
    _id        :str
    id         :int
    name       :str
    Gender     :str
    EyeColor   :str
    Race       :str
    HairColor  :str
    Height     :int
    Publisher  :str
    SkinColor  :str
    Alignment  :str
    Weight     :int

    def __init(self,_id, id, name, Gender, EyeColor, Race, HairColor, Height, Publisher, SkinColor, Alignment, Weight):
        self._id       = _id        
        self.id        = id        
        self.name      = name      
        self.Gender    = Gender    
        self.EyeColor  = EyeColor  
        self.Race      = Race      
        self.HairColor = HairColor 
        self.Height    = Height    
        self.Publisher = Publisher 
        self.SkinColor = SkinColor 
        self.Alignment = Alignment 
        self.Weight    = Weight  