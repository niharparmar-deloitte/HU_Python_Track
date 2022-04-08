from main_assignment.Admin import adminLogin
from main_assignment.MoviesCRUD import moviescrud
from main_assignment.MoviesOperation import moviesoperation
from main_assignment.login import login
from main_assignment.registration import register


print("-----Welcome To BookMyShow-----")
obj_register = register()
obj_Admin = adminLogin()
obj_MoviesCRUD = moviescrud()
obj_MoviesOperation = moviesoperation()
obj_login = login()

while True:
    print("Press 1 for admin: ")
    print("Press 2 to register: ")
    print("Press 3 to login as user")
    print("Press 4 to exit")
    user_input = input()
    if user_input == "4":
        break
    elif user_input == "1":
        if obj_Admin.LoginAdmin():
            print("Login Successful! ")
            print()
            print("-----Welcome Admin-----")
            while True:
                print("Press 1 to add movie info. ")
                print("Press 2 to Edit movie info. ")
                print("Press 3 to Delete movie ")
                print("Press 4 to Logout")
                admin_input = input()
                if admin_input == "4":
                    break
                elif admin_input == "1":
                    if obj_MoviesCRUD.AddMovie():
                        pass
                    else:
                        continue
                elif admin_input == "2":
                    obj_MoviesCRUD.EditMovie()
                else:
                    obj_MoviesCRUD.DeleteMovie()
        else:
            print("Invalid Credentials. Please Try Again.")
    elif user_input == "2":
        if obj_register.UserRegister():
            print()
        else:
            continue
    elif user_input == "3":
        if obj_login.UserLogin():
            print()
            while True:
                obj_MoviesOperation.Movies()
                print("Enter Movie ID")
                print("Enter 0 to logout")
                choice = input()
                if choice == "0":
                    break
                else:
                    obj_MoviesOperation.MovieInfo(int(choice))
                    print()
                    print("Press 1 to Book Tickets")
                    print("Press 2 to Cancel Tickets")
                    print("Press 3 for user ratings")
                    userChoice = input()
                    if userChoice == "2":
                        obj_MoviesOperation.CancelTickets(int(choice))
                    elif userChoice == "3":
                        obj_MoviesOperation.UserRatings(int(choice))
                    elif userChoice == "1":
                        obj_MoviesOperation.BookTickets(int(choice))
                        print()
                    else:
                        print("Enter valid input!")
        else:
            continue
    else:
        print("Invalid Input ")
        continue
