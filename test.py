class sieunhan:
      def __init__(self,para_ten,para_vu_khi,para_mau_sac):
          self.ten = "sieu nhan " + para_ten
          self.vu_khi = para_vu_khi
          self.mau_sac = para_mau_sac
      def xin_chao(self):
          return "xin chao , ta chinh la "  + self.ten



sieu_nhan_A = sieunhan("Kteam", "Knowledge" , "tim rim")  
print(sieu_nhan_A.xin_chao())