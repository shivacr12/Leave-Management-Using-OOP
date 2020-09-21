import company_database
import company_structure_hierarchy

# *******************THE MAIN PROGRAM***********************
if __name__=="__main__":
    company_database.company_database()

    while True:
        userchoice = input(
            "\n\nENTER 1 : TO LOGIN AS ADMINISTRATOR\nENTER 2 : TO LOGIN AS RA\nENTER 3 : TO LOGIN AS EMPLOYEE\nENTER 4 : TO QUIT\n")
        try:
            userchoice = int(userchoice)
        except:
            print("SEEMS YOU DID NOT ENTER A VALID INTEGER")
        else:
            if userchoice == 1:
                if len(company_database.admin_list) == 0:
                    admin = company_structure_hierarchy.Admin()
                    company_database.admin_list.append(admin)
                elif len(company_database.admin_list) == 1 and admin.credentials_verifier():
                    while True:
                        userchoice1 = input(
                            "\nENTER 1 : TO ADD MEMBER\nENTER 2 : TO VIEW PEOPLE UNDER YOU\nENTER 3 : TO LOGOUT\n")
                        if userchoice1 == '1':
                            admin.add_employee()
                        elif userchoice1 == '2':
                            if len(admin.under) == 0:
                                print("THERE IS NO ONE WORKING UNDER U YET")
                            elif len(admin.under):
                                admin.view_people_under_you()
                        elif userchoice1 == '3':
                            admin.logout()
                            break
                        else:
                            print("\n  INVALID OPTION  \n")

            elif userchoice == 2:
                if len(company_database.admin_list) == 0:
                    print("\n     CANNOT ADD REPORTING AUTHORITY WITHOUT THE EXISTANCE OF ADMINISTRATOR     \n")
                    continue
                elif len(company_database.admin_list) == 1 and len(company_database.RA_list):
                    reporting_authority = admin.ra.credentials_verifier()
                    if reporting_authority:
                        while True:
                            userchoice2 = input(
                                "\nENTER 1 : TO VIEW PEOPLE UNDER YOU\nENTER 2 : TO APPROVE OR REJECT LEAVES\nENTER 3 : TO LOGOUT\n")
                            if userchoice2 == '1':
                                if len(reporting_authority.under)==0:
                                    print("   THERE IS NO ONE WORKING UNDER YOU YET")
                                elif len(company_database.RA_list):
                                    reporting_authority.view_people_under_you()
                            elif userchoice2 == '2':
                                reporting_authority.approve_or_reject_leaves()
                            elif userchoice2 == '3':
                                reporting_authority.logout()
                                break
                            else:
                                print("\n   INVALID OPTION   \n")
                elif len(company_database.RA_list) == 0:
                    print("\n      NO REPORTING AUTHORITIES EXIST YET...TO CREATE ONE LOGIN AS ADMINISTRATOR...")
                    continue

            elif userchoice == 3:
                if len(company_database.admin_list) == 0 and len(company_database.RA_list) == 0:
                    print(
                        "\n        CANNOT ADD AN EMPLOYEE WITHOUT THE EXISTANCE OF ADMINISTRATOR AS WELL AS REPORTING AUTHORITY    \n")
                    continue
                elif len(company_database.admin_list) == 1 and len(company_database.RA_list) and len(company_database.employee_list):
                    employe = admin.ra.employee.credentials_verifier()
                    if employe:
                        while True:
                            userchoice3 = input(
                                "\nENTER 1 : TO APPLY LEAVE\nENTER 2 : TO GET LEAVE STATUS\nENTER 3 : TO LOGOUT\n")
                            if userchoice3 == '1':
                                employe.apply_leave()
                            elif userchoice3 == '2':
                                employe.leave_status()
                            elif userchoice3 == '3':
                                employe.logout()
                                break
                            else:
                                print("\n              INVALID OPTION            \n")
                elif len(company_database.employee_list) == 0:
                    print("\n    NO EMPLOYEE CREATED YET...TO CREATE LOGIN AS ADMINISTRATOR")
                    continue


            elif userchoice == 4:
                quit()

            else:
                print("\n             INVALID OPTION             \n")



