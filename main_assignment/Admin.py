from openpyxl import Workbook, load_workbook


class adminLogin:
    AdminUsername = "admin"
    AdminPassword = "admin"

    def LoginAdmin(self):
        adminusername = input("Enter Your Admin Username: ")
        adminpassword = input("Enter Your Admin Password: ")
        if adminpassword == self.AdminPassword and adminusername == self.AdminUsername:
            return True
        else:
            return False

