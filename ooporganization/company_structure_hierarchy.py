from abc import ABCMeta, abstractmethod
import company_database

employee_id = 0
#company_database.company_database()

class Credentials(metaclass=ABCMeta):
    @abstractmethod
    def credentials_verifier():
        return 0

    @abstractmethod
    def view_people_under_you():
        return 0

    @abstractmethod
    def logout():
        return 0


class Admin(Credentials):
    def __init__(self):
        global employee_id
        self.name = input("Enter your NAME :")
        self.id = employee_id = employee_id + 1
        print(f"YOUR DEFAULT ID IS SET AS : {self.id}")
        self.password = input("SET your PASSWORD :")
        self.under = []
        company_database.company_database_list.append(self)
        print("\n\n                CREDENTIALS SET SUCCESSFULLY                \n")

    def credentials_verifier(self):
        id_d = input("Enter your ID :")
        try:
            id_d = int(id_d)
        except:
            print("\n      PLEASE ENTER VALID NUMBER  ")
            return self.credentials_verifier()
        else:
            name_d = input("Enter your NAME :")
            password_d = input("Enter your PASSWORD :")
            if (name_d == self.name) and (password_d == self.password) and (id_d == self.id):
                print(f"\n***********  WELCOME {self.name}  ***********")
                return True
            else:
                print("\n*****************INVALID CREDENTIALS*****************\n")
                return False

    def add_employee(self):
        choice = input("Enter 1 : To add RA\nEnter 2 : To add EMPLOYEE\n")
        if choice == '1':
            self.ra = self.RA()
            return
        elif choice == '2':
            if len(company_database.RA_list) == 0:
                print(
                    "\n   Cannot add EMPLOYEE without ANY EXISTING REPORTING AUTHORITY  \n\n       ADD REPORTING AUTHORITY FIRST!!\n")
                return self.add_employee()
                # self.add_employee()
            elif len(company_database.RA_list) > 0:
                self.ra.employee = self.ra.Employee()  # self.employee=self.RA.Employee()
                return
        else:
            print("\n        INVALID OPTION... TRY AGAIN...")
            return self.add_employee()

    def view_people_under_you(self):
        for __ in self.under:
            print(f'ID     :{__.id}        NAME      :{__.name}')

    def logout(self):
        print(f"\n            {self.name} LOGGED OUT SUCCESSFULLY            \n")
        return

    class RA(Credentials):
        def __init__(self):
            global employee_id
            self.name = input("Enter the name of the REPORTING AUTHORITY TO BE ADDED :")
            self.id = employee_id = employee_id + 1
            print(f"{self.name}'s default ID is set as : {self.id}")
            self.password = input("SET the password :")
            self.under = []
            self.report_to = input(
                f"    SET the REPORTING AUTHORITY for {self.name}\n    ENTER ADMINISTRATOR'S NAME :")
            try:
                __ = int(input(f"    Enter the ID of the ADMINISTRATOR :"))
            except:
                print(
                    "\n          CREATE CREDENTIALS AGAIN..PLEASE ENTER A VALID NUMBER FOR REPORTING AUTHORITY'S ID   ")
                employee_id = employee_id - 1
                return self.__init__()
            else:
                for a in company_database.admin_list:
                    if a.name == self.report_to and a.id == __:
                        company_database.company_database_list.append(self)
                        a.under.append(self)
                        company_database.RA_list.append(self)
                        # append the created object to reporing object
                        print("\n            RA CREATED SUCESSFULLY..           \n")
                        return
                else:
                    print("\n      REPORT TO AUTHORITY WITH THE ENTERED CREDENTIALS IS UNAVAILABLE IN ADMINISTRATOR DATABASE...      \n")
                    employee_id = employee_id - 1
                    del (self)

        def credentials_verifier(self):
            i_d = input("Enter your ID :")
            try:
                i_d = int(i_d)
            except:
                print("\n    ENTER A VALID NUMBER     ")
                return self.credentials_verifier()
            else:
                na = input("Enter your NAME :")
                pass_word = input("Enter your PASSWORD :")
                for ra in company_database.RA_list:
                    if ra.name == na and ra.id == i_d and ra.password == pass_word:
                        print(f"\n        WELCOME {ra.name}         \n")
                        return ra  # check
                else:
                    print("\n      Sorry Invalid credentials....  \n")
                    return

        def view_people_under_you(self):
            for __ in self.under:
                print(
                    f"ID :{__.id}     NAME :{__.name}      LEAVES APPLIED :{__.leaves_applied}     LEAVES REMAINING :{__.leaves_remaining}\n")

        def approve_or_reject_leaves(self):
            leave_i_d = input("Enter the ID of the employee under you, to whom you'd like to grant leave :")
            try:
                leave_i_d = int(leave_i_d)
            except:
                print("\n      ENTER A VALID NUMBER     ")
                return self.approve_or_reject_leaves()
            else:
                for i in self.under:
                    if i.id == leave_i_d:
                        if i.leave_stat == 'N\A':
                            print(f"\n         {i.name} HAS NOT APPLIED FOR ANY LEAVE         \n")
                            return
                        elif i.leave_stat == 'REQUESTED':
                            print(f"\n      {i.name} HAS REQUESTED LEAVE FOR {i.leaves_applied} DAYS   ")
                            ra_choice = input("\n    ENTER 1 : TO APPROVE\n    ENTER 2 : TO REJECT\n")
                            if ra_choice == '1':
                                i.leaves_remaining = i.leaves_remaining - i.leaves_applied
                                i.leave_stat = 'APPROVED'
                                i.leaves_applied = 0
                                print("\n      LEAVE GRANTED    ")
                                return
                            elif ra_choice == '2':
                                i.leave_stat = 'REJECTED'
                                i.leaves_applied = 0
                                print("\n     REQUEST REJECTED      ")
                                return
                            else:
                                print("\n      INVALID OPTION     ")
                                return
                        elif i.leave_stat == 'APPROVED' or i.leave_stat == 'REJECTED':
                            print(f"\n     YOU HAVE ALREADY {i.leave_stat} REQUEST OF {i.name}     \n")
                            return
                else:
                    print("\n         THE REQUESTED ID DOES'NT EXIST IN PEOPLE WORKING UNDER YOU")

        def logout(self):
            print(f"\n      {self.name} LOGGED OUT SUCCESSFULLY      ")
            return

        class Employee(Credentials):
            def __init__(self):
                global employee_id
                self.name = input("Enter the name of the EMPLOYEE TO BE ADDED :")
                self.id = employee_id = employee_id + 1
                print(f"{self.name}'s default ID is set as : {self.id}")  # reporting heirarchy musr=t be defined
                self.password = input(f"SET password for {self.name} :")
                self.leaves_remaining = 10
                self.leaves_applied = 0
                self.leave_stat = 'N\A'
                print("\n@@@@@@@@@@   AVAILABLE REPORTING AUTHORITIES ARE     @@@@@@@@\n")
                for r_a in company_database.RA_list:
                    print(f"      NAME   :{r_a.name}    ID    :{r_a.id}      ")
                self.report_to = input(
                    f"\n      SET the REPORTING AUTHORITY for {self.name}\n          ENTER REPORTING AUTHORITY'S NAME :")
                __ = input(f"\n      Enter the ID of the Reporting Authority for {self.name} :")
                try:
                    __ = int(__)
                except:
                    print(
                        "\n     PLEASE ENTER A VALID NUMBER WHILE ENTERING THE REPORTING AUTHORITY'S ID..CREATE AGAIN     ")
                    employee_id = employee_id - 1
                    return self.__init__()
                else:
                    for r in company_database.RA_list:
                        if r.name == self.report_to and __ == r.id:
                            r.under.append(self)
                            company_database.company_database_list.append(self)
                            company_database.employee_list.append(self)
                            print("\n            EMPLOYEE CREATED SUCCESSFULLY               \n")
                            return
                    else:
                        print(
                            "\n         REPORT TO AUTHORITY WITH THE ENTERED CREDENTIALS IS UNAVAILABLE IN REPORTING AUTHORITY DATABASE..           \n")
                        employee_id = employee_id - 1
                        del self
                        return

            def credentials_verifier(self):
                try:
                    i_d = int(input("Enter your ID :"))
                except:
                    print("\n       ENTER A VALID NUMBER AS ID     ")
                    return self.credentials_verifier()
                else:
                    na = input("Enter your NAME :")
                    pass_word = input("Enter your PASSWORD :")
                    for emp in company_database.employee_list:
                        if emp.name == na and emp.id == i_d and emp.password == pass_word:
                            print(f"\n     WELCOME {emp.name}      \n")
                            return emp  # check
                    else:
                        print("\n    Sorry.. Invalid credentials....   \n")
                        return

            def view_people_under_you(self):
                pass

            def apply_leave(self):
                print(f"   YOU HAVE {self.leaves_remaining} LEAVES REMAINING \n")
                try:
                    self.leaves_applied = int(input("Enter the number of days you wanna take leave :"))
                except:
                    print("\n            PLEASE ENTER A VALID NUMBER      ")
                    return self.apply_leave()
                else:
                    if self.leaves_applied <= self.leaves_remaining and self.leaves_applied > 0:
                        self.leave_stat = 'REQUESTED'  # requested leave
                        print("\n           REQUEST SUBMITTED \n")
                    else:
                        self.leave_stat = 'N\A'
                        self.leaves_applied = 0
                        print("\n          REQUEST FAILED..\n")
                        emp_choice=input("    ENTER 1 : IF YOU WANT TO TRY AGAIN\n    ENTER 2 : TO QUIT")
                        if emp_choice=='1':
                            return self.apply_leave()
                        else:
                            return

            def leave_status(self):
                if self.leave_stat == 'N\A':
                    print("\n        N\A             \n")
                elif self.leave_stat == 'APPROVED':
                    print("       LEAVE APPROVED           \n")
                elif self.leave_stat == 'REQUESTED':
                    print(f"        LEAVE REQUESTED FOR {self.leaves_applied} DAYS : NO RESPONSE YET                    \n")
                elif self.leave_stat == 'REJECTED':
                    print("       LEAVE REJECTED                   \n")
                print(f"\n    YOU STILL HAVE {self.leaves_remaining} LEAVES LEFT          \n")

            def logout(self):
                print(f"\n     {self.name} LOGGED OUT SUCCESSFULLY             \n")
                return

