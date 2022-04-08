from openpyxl import Workbook, load_workbook


class register:
    def UserRegister(self):
        username = input('Please Enter Your Username: ')
        if username in open('userregister.txt', 'r').read():
            print('Username Already Exists. Try with a different one')
            return False
        password = input('Please Enter Your Password: ')
        c_password = input('Re-Enter Your Password: ')
        if password != c_password:
            print('Passwords did not match')
            return False
        file = open('userregister.txt', 'a')
        file.write(username)
        file.write(' ')
        file.write(password)
        file.write('\n')
        file.close()
        print(username + ' syour account has been created successfully. Welcome!!')
        return True




