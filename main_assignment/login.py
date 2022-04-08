class login:
    def UserLogin(self):
        print("---- Login to BookMyShow ----")
        username = input('Please Enter Your Registered Username: ')
        password = input('Please Enter Your Valid Password: ')
        get_data = open('userregister.txt', 'r').readlines()
        users_data = []
        for user in get_data:
            users_data.append(user.split())

        total_user = len(users_data)
        increment = 0
        login_success = 0
        while increment < total_user:
            usernames = users_data[increment][0]
            passwords = users_data[increment][1]
            if username == usernames and password == passwords:
                login_success = 1
            increment += 1

        if login_success == 1:
            print("Welcome: ", username)
            return True
        else:
            print('Invalid UserName or Password')
            return False
