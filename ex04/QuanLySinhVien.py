from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def generateID(self):
        maxId = 1
        if self.soLuongSinhVien() > 0:    
            maxId = self.listSinhVien[0].get_id()  # Sử dụng getter để lấy ID
            for sv in self.listSinhVien:
                if maxId < sv.get_id():
                    maxId = sv.get_id()
            maxId = maxId + 1
        return maxId


    def soLuongSinhVien(self):
        return len(self.listSinhVien)  # Dùng len() thay vì __len__()

    def nhapSinhVien(self):
        svId = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap chuyen nganh của sinh vien: ")  # major nên là chuỗi
        diemTB = float(input("Nhap diem cua sinh vien: "))
        sv = SinhVien(svId, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)  # Cập nhật xếp loại học lực
        self.listSinhVien.append(sv)

    def updateSinhVien(self, ID):
        # Kiểm tra xem ID có phải là một số nguyên hợp lệ không
        try:
            ID = int(ID)
        except ValueError:
            print("ID phải là một số nguyên.")
            return

        sv = self.findByID(ID)
        if sv is not None:
            # Nhập lại thông tin sinh viên nếu tìm thấy
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap chuyen nganh của sinh vien: ")
            diemTB = float(input("Nhap diem cua sinh vien: "))
            
            # Cập nhật thông tin sinh viên
            sv.set_name(name)
            sv.set_sex(sex)
            sv.set_major(major)
            sv.set_diemTB(diemTB)
            self.xepLoaiHocLuc(sv)  # Cập nhật lại xếp loại học lực
            print("Cập nhật thông tin sinh viên thành công.")
        else:
            print(f"Sinh vien co ID {ID} khong ton tai.")  # Thông báo nếu không tìm thấy sinh viên


    def sortByID(self):
        self.listSinhVien.sort(key=lambda x: x._id, reverse=False)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda x: x._name, reverse=False)

    def sortByDiemTB(self):
        self.listSinhVien.sort(key=lambda x: x._diemTB, reverse=False)

    def findByID(self, ID):
        for sv in self.listSinhVien:
            if sv.get_id() == ID:  # Sử dụng getter để lấy giá trị ID
                return sv
        return None


    def findByName(self, keyword):
        listSV = []
        if self.soLuongSinhVien() > 0:  # Sửa thành soLuongSinhVien() đúng tên
            for sv in self.listSinhVien:
                if keyword.upper() in sv._name.upper():
                    listSV.append(sv)
        return listSV

    def deleteById(self, ID):
        # Kiểm tra xem ID có phải là một số nguyên hợp lệ không
        try:
            ID = int(ID)
        except ValueError:
            print("ID phải là một số nguyên.")
            return False

        sv = self.findByID(ID)
        if sv is not None:
            self.listSinhVien.remove(sv)  # Xóa sinh viên khỏi danh sách
            print(f"Sinh vien co ID {ID} da duoc xoa.")
            return True  # Trả về True nếu xóa thành công
        else:
            print(f"Sinh vien co ID {ID} khong ton tai.")
            return False  # Trả về False nếu không tìm thấy sinh viên

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"  # Sửa tên thuộc tính học lực đúng
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5:
            sv._hocLuc = "Trung bình"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        if len(listSV) > 0:  # Dùng len() thay vì __len__()
            for sv in listSV:
                print("{:<8} {:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien
