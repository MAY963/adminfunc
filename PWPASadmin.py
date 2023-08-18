def admin():
    print('Wlecome')
    print('What would you like to do ?\n1.View\n2.Edit\n3.Update self profile')
    funcadm = int(input('Please choose the function desired via the numbers given: '))
    if funcadm == 1:
        print('What item would you like to read ?\n1.Tutor\n2.Receptionist\n3.Tutor Monthly Income\n4.Back to Main Menu')
        funcadmv = int(input('Please enter the number of the item: '))
        if funcadmv == 1:
            while True:
                with open('TtrLvlSject.txt', 'r') as vwttrlvlsject:
                    vwtline = vwttrlvlsject.readlines()
                    vwtr = input('Please enter the name of the tutor to be viewed :')
                    for line in vwtline:
                            if vwtr in line:
                                print(line)
                                vwttrlvlsject.close()
                cvt = input('Would you like to continue viewing\nYes or No :')
                if cvt.lower() == 'no':
                    admin()
        elif funcadmv == 2:
            while True:
                with open('Receptionist.txt', 'r') as vwrcpt:
                    vwrline = vwrcpt.readlines()
                    vwrp = input('Please enter the name of the receptionist you want to view :')
                    for line in vwrline:
                        if vwrp in line:
                            print(line)
                            vwrcpt.close()
                cvr = input('Would you like to continue\nYes or No :')
                if cvr.lower() == 'no':
                    admin()
        elif funcadmv == 3:
            while True:
                with open('TtrLvlSject.txt', 'r') as ttrinc:
                    tinco = ttrinc.readlines()
                    vtinc = input('Please enter the name of the tutor\'s income you wish to see :')
                    for line in tinco:
                        tico = line.strip().split(',')
                        if vtinc in tico:
                            print(vtinc, '\'s monthly income : RM', int(tico[4])*5000)
                cvti = input('Would you like to continue :\nYes or No :')
                if cvti.lower() == 'no':
                    admin()
        elif funcadmv == 4:
            admin()
    elif funcadm == 2:
        print('Would you like to edit:\n1.Register\n2.Delete\n3.Back to Main Menu')
        funcadme = int(input('Please enter the funtion you would like to proceed with: '))
        if funcadme == 1:
            print('Would you like to register:\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
            funcadm3 = int(input('Please enter the number of your choice: '))
            if funcadm3 == 1:
                while True:
                    with open('TtrLvlSject.txt', 'a') as tifo:
                        tname = input('Please register your name: ')
                        tphnum = int(input('Please register your phone number: '))
                        tmail = input('Please register your email: ')
                        sject = input('Please register your subject: ')
                        sjlvl = int(input("Please enter the subject's level: "))
                        tfo = tname+','+str(tphnum) + ','+tmail + ',' + sject + ',' + str(sjlvl) + '\n'
                        tifo.write(tfo)
                        tifo.close()
                        print('New Tutor added')
                        cat = input('Would you like to continue ?\nYes or No :')
                        if cat.lower() == 'no':
                            admin()
            elif funcadm3 == 2:
                while True:
                    with open('Receptionist.txt', 'a') as rifo:
                        rname = input('Please register your name: ')
                        rphnum = int(input('Please register your phone number: '))
                        rmail = input('Please register your email: ')
                        rfo = rname+','+str(rphnum) + ','+rmail+'\n'
                        rifo.write(rfo)
                        rifo.close()
                        print('New Receptionist added')
                        car = input('Would you like to continue ?\nYes or No :')
                        if car.lower() == 'no':
                            admin()
            elif funcadm3 == 3:
                admin()
        elif funcadme == 2:
            print('Which category would you like to delete an item in :\n1.Tutor\n2.Receptionist\n3.Back to Main Menu')
            funcadmd = int(input('Please enter the number of the option :'))
            if funcadmd == 1:
                while True:
                    dttr = input('Please enter the name of the tutor to be deleted')
                    with open('TtrLvlSject.txt', 'r') as radttrlvlsject:
                        rtline = radttrlvlsject.readlines()
                        with open('TtrLvlSject.txt', 'w') as dltttr:
                            for line in rtline:
                                if dttr in line:
                                    pass
                                else:
                                    dltttr.write(line)
                            print(dttr, 'Deleted')
                    cdltttr = input('Would you like to continue deleting tutor :\nYes or No :')
                    if cdltttr.lower() == 'no':
                        admin()
            if funcadmd == 2:
                while True:
                    dtrecp = input('Please enter the name of the receptionist to be deleted')
                    with open('Receptionist.txt', 'r') as radrecp:
                        rrline = radrecp.readlines()
                        with open('Receptionist.txt', 'w') as dltrec:
                            for line in rrline:
                                if dtrecp in line:
                                    pass
                                else:
                                    dltrec.write(line)
                            print(dtrecp, 'Deleted')
                    cdltrec = input('Would you like to continue deleting receptionist ?\nYes or No :')
                    if cdltrec.lower() == 'no':
                        admin()
            elif funcadmd == 3:
                admin()
        elif funcadme ==3:
            admin()
    elif funcadm == 3:
        while True:
            with open ('adm.txt','r') as admchce:
                rdadmline = admchce.readlines()
            updtadm = input('Please enter the name of the admin\'s profile to be updated :')
            with open('adm.txt','w') as altadmpf:
                for line in rdadmline:
                    if updtadm in line:
                        nadmnm = input('Please enter your name :')
                        nadmgdr = input('Please enter your gender :')
                        nadmdob = input('Please enter your date of birth with the following format(01 January 2000) :')
                        nadmem = input('Please enter your email :')
                        nadmphnum = input('Please enter your phone number')
                        nadmadrs = input('Please enter your address :')
                        nwadm = f"{nadmnm},{nadmgdr},{nadmdob},{nadmem},{nadmphnum},{nadmadrs}"
                        altadmpf.write(nwadm+'\n')
                    else:
                        altadmpf.write(line)
            calterpf = input('Would you like to continue making changes in admin profile ?\nYes or no')
            if calterpf.lower() == 'no':
                admin()

admin()