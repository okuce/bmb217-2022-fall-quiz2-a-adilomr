# adil ömer polat
#20227170214
#bilgisayr mühendisliği 2.sınıf


class Otobus:
    """Otobus bilet satis takip sinifi"""
    plaka:str=""
    nerden:str=""
    nereye:str=""
    bos_koltuk:int=0
    dolu_koltuk:int=0

    def __init__(self,plaka,nerden,nereye,dolu_koltuk):
        self.plaka=plaka
        self.nerden=nerden
        self.nereye=nereye
        self.dolu_koltuk=dolu_koltuk 
        
    def bilet_sat(self):
        """Otobusteki dolu koltuk sayisini 1 artirir"""
        self.dolu_koltuk -=1
        
        
    
    def bilet_iade(self):
        """Otobusteki dolu koltuk sayisini 1 azaltir"""
        self.bos_koltuk -=1
        

    
    def durum_yaz(self):
        """Otobusun guzergahini, plakasini,bos ve dolu koltuk sayisini yazdirir"""
        print(self.nerden,self.nereye,self.plaka,self.bos_koltuk,self.dolu_koltuk)
        
