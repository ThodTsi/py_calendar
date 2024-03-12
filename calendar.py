import csv
event = []
with open('events.csv','r') as csv_r:     #prosthiki twn gegonotwn toy arxeiou sth lista kata thn ekkinhsh gia na mhn xathoun ta prohgoymena dedomena
    csv_reader = csv.reader(csv_r)
    for r in csv_reader:
            if r != [] and r != ['DATE','HOUR','DURATION','TITLE']:
                event.append(r)
f = open('events.csv','w')
def add_events(event,f):            #katagrafh twn gegonotwn mazi me ta kainouria sto arxeio
    with f as add_csv:
        csv_writer = csv.writer(add_csv)
        header = ['DATE','HOUR','DURATION','TITLE']
        csv_writer.writerow(header)
        for i in event:
            csv_writer.writerow(i)
        f.close()
add_events(event,f)


writer = csv.writer(f)
import calendar
calendar.setfirstweekday(0)
from datetime import datetime
current_date = datetime.now()
month  = current_date.month    
year = current_date.year
def make_month(year,month,event):  
    import calendar  
    ls = calendar.monthcalendar(year,month)
    days = [' Mon |',' Tue |',' Wed |',' Thu |',' Fri |',' Sat |',' Sun  ']
    for i in range(len(ls)):
        c = 0
        while c <= 6:
            found = False
            temp = ls[i][c]
            if ls[i][c] < 10:
                if event != []:                #dhmiourgia ths optikhs morfhs tou mhna kai euresi hmerwn me programmatismena gegonota
                    if month < 10:
                        for j in event:
                            if j[0][0:4] == str(year) and j[0][5:6] == str(month) and j[0][7:8] == str(temp):
                                ls[i][c] = '[* ' + str(ls[i][c]) + ']|'
                                found = True
                    else: 
                        for j in event:
                            if j[0][0:4] == str(year) and j[0][5:7] == str(month) and j[0][8:9] == str(temp):
                                ls[i][c] = '[* ' + str(ls[i][c]) + ']|'
                                found = True
                if found == False:
                    ls[i][c] = '[  ' + str(ls[i][c]) + ']|'

            else:
                if event != []:
                    if month < 10:
                        for j in event:
                            if j[0][0:4] == str(year) and j[0][5:6] == str(month) and j[0][7:9] == str(temp):
                                ls[i][c] = '[*' + str(ls[i][c]) + ']|'
                                found = True
                    else:
                        for j in event:
                            if j[0][0:4] == str(year) and j[0][5:7] == str(month) and j[0][8:10] == str(temp):
                                ls[i][c] = '[* ' + str(ls[i][c]) + ']|'
                                found = True
                if found == False:
                    ls[i][c] = '[ ' + str(ls[i][c]) + ']|'
            if c == 6:
                ls[i][c] = ls[i][c][0:-1]
            c += 1

    temp = calendar.monthrange(year,month)          #sumplhrwma hmerwn prohgoumenou mhna 
    i = temp[0] - 1
    if month != 1:
        prev_month = month - 1
    else:
        prev_month = 12
    t = calendar.monthrange(year,prev_month)
    t = t[1]
    while i >= 0:

        ls[0][i] = '  ' + str(t) + ' |'
        i -= 1
        t -= 1

    i = 0                   #sumplhrwma hmerwn epomenou mhna
    t = 1
    while i <= 6:
        if ls[len(ls)-1][i] == '[  0]|' or ls[len(ls)-1][i] == '[  0]':
            if i == 6:
                ls[len(ls)-1][i] = '   ' + str(t)
            else:
                ls[len(ls)-1][i] = '   ' + str(t) + ' |'
            t += 1 
        i += 1
    print('______________________________________________')      #ektipwsh telikhs morfhs mhna
    print(calendar.month_abbr[month], year)    
    print('______________________________________________')
    for i in days:
        if i != ' Sun  ':
            print(i,end='')
        else:
            print(i)
    for i in range(len(ls)):            
        j = 0 
        while j <= 6:
            if j == 6:
                print(ls[i][j])
            else:
                print(ls[i][j],end='')
            j += 1
    print('______________________________________________')

def print_menu(make_m):
    print(make_m)
    print('Πατήστε ENTER για προβολή του επόμενου μήνα, "q" για έξοδο ή κάποια από τις παρακάτω επιλογές:')
    print('    "-" για πλοήγηση στον προηγούμενο μήνα' )
    print('    "+" για διαχείριση των γεγονότων του ημερολογίου')
    print('    "*" για εμφάνιση των γεγονότων ενός επιλεγμένου μήνα')

def ls_sort(ls):
    n = len(ls)
    for i in range(n-1):
        for j in range(0,n-i-1):
            y1,m1,d1 = '','',''
            c = 0 
            for k in ls[j][0]:     #diaxwrismos etous-mhna-hmeras se diaforetika strings
                if k != '-':
                    if c == 0:
                        y1 += k
                    elif c == 1:
                        m1 += k
                    else:
                        d1 += k
                else:
                    c += 1
            y2,m2,d2 = '','',''
            c = 0 
            for k in ls[j+1][0]:
                if k != '-':
                    if c == 0:
                        y2 += k
                    elif c == 1:
                        m2 += k
                    else:
                        d2 += k
                else:
                    c += 1
            y1,m1,d1,y2,m2,d2 = int(y1),int(m1),int(d1),int(y2),int(m2),int(d2)   #metatroph twn string se akeraioys kai sigkrisi tous gia thn taksinomhsh
            if y1 > y2:
                ls[j],ls[j+1] = ls[j+1],ls[j]
            elif y1 == y2:
                if m1 > m2:
                    ls[j],ls[j+1] = ls[j+1],ls[j]
                elif m1 == m2:
                    if d1 > d2:
                        ls[j],ls[j+1] = ls[j+1],ls[j]

def search_date(ls,y,m,temp):    
    for i in ls:
        if i[0][0:4] == str(y):         #dhmiourgia listas me ta gegonota toy mhna pou anazithsame
            if int(m) < 10 and i[0][5:6] == str(m):
                temp.append(i)
            elif int(m) >= 10 and i[0][5:7] == str(m):
                temp.append(i)
    c = 0 
    for i in temp:
        print(str(c)+'.' + '[' + i[3] + '] -> Date:', i[0], 'Time:', i[1], 'Duration:', i[2] )       #ektiposh gegonoton toy mhna poy anazhthsame
        c += 1
    return temp
 
def check_date(y,m,d):   #elegxos egkirothtas gia hmeromhnia
    flag = False
    while flag == False:
        if y >= 2023 and m >=1 and m <=12:
            num_d = calendar.monthrange(y,m)[1]
            if d >= 1 and d <= num_d: 
                flag = True
                date = str(y)+'-'+str(m)+'-'+str(d)
            else:
                print('Δώστε έγκυρη ημερομηνία:')
                y = int(input('Xρονιά:'))
                m = int(input('Mήνας:'))
                d = int(input('Ημέρα:'))
        else:
                print('Δώστε έγκυρη ημερομηνία:')
                y = int(input('Χρονιά:'))
                m = int(input('Μήνας:'))
                d = int(input('Ημέρα:'))
    return date






def check_time(h,m):   #elegxos egkirothtas gia wra
    flag = False
    while flag == False:
        if (h < 0 or h > 23) or (m < 0 or m > 59):
            print('Δώστε έγκυρη ώρα:')
            h = int(input('Ωρα:'))
            m = int(input('Λεπτά:'))
        else:
            flag = True 
            if m < 10:
                m = '0' + str(m)
            time = str(h)+':'+str(m)
    return time
    

def check_duration(dur):  #elegxos egkirothtas gia diarkeia
    flag = False
    while flag == False:
        if dur < 1 or dur > 23:
            print('Δώστε έγκυρη διάρκεια:')
            dur = int(input('Διάρκεια:'))
        else:
            flag = True
    return dur

def check_title(title):  #elegxos egkirothtas gia titlo
    while ',' in title:
        print('Δώστε έγκυρο τίτλο:')
        title = input('Τίτλος:')
    return title


sched = []                        #BONUS LEITOURGIA: emfanish simerinwn gegonotwn kata thn ekkinhsh ths
if event != []:
    import datetime
    x = datetime.datetime.now()
    m = x.month
    d = x.day
    y = x.year
    date = str(y) + '-' + str(m) + '-' + str(d)
    for i in event:
        if i[0] == date:
            sched.append(i)
    if len(sched) > 1:
        n = len(sched)
        for i in range(n-1):
            for j in range(0,n-i-1):
                if sched[j][1] > sched[j+1][1]:
                    sched[j][1],sched[j+1][1] = sched[j+1][1],sched[j][1]
                  
if sched != []:
    print('Ειδοποιήσεις σημερινών γεγονότων:')
    c = 0 
    for i in sched:
        print(str(c) + '.' , i)
        c += 1
else:
    print('Δεν υπάρχουν προγραμματισμένα γεγονότα για σήμερα')


print_menu(make_m = make_month(year,month,event) )
option = input('Επιλέξτε ενέργεια:')
while option != 'q':
    if option == '':
        if month == 12:
            year += 1
            month = 1
            print(make_month(year,month,event))
        else:   
            month += 1   
            print(make_month(year,month,event))
    elif option == '-':
        if month == 1:
            month = 12
            year -= 1
            print(make_month(year,month,event))
        else:
            month -= 1
            print(make_month(year,month,event))
    elif option == '+':
        print('Διαχείριση γεγονότων ημερολογίου, επιλέξτε ενέργεια:')
        print(     '1 Καταγραφή νέου γεγονότος')
        print(     '2 Διαγραφή γεγονότος')
        print(     '3 Ενημέρωση γεγονότος')
        print(     '0 Επιστροφή στο κυρίως μενού')
        manage = int(input())
        if manage == 1:
            y = int(input('Ετος:'))
            m = int(input('Μήνας:'))
            d = int(input('Ημέρα:'))
            date = check_date(y,m,d)
            h = int(input('Ωρα:'))
            m = int(input('Λεπτά:'))
            time = check_time(h,m)
            dur = int(input('Διάρκεια:'))
            dur = check_duration(dur)
            title = input('Τίτλος:')
            title = check_title(title)
            event.append([date,time,dur,title])
            if len(event) > 1:    
                ls_sort(event)
            add_events(event,f = open('events.csv','w'))

        elif manage == 2:
            y = int(input('Δώστε έτος:'))
            while y < 2023:
                y = int(input('Δώστε έγκυρο έτος:'))
            m = int(input('Δώστε μήνα:'))
            while m < 1 or m > 12: 
                m = int(input('Δώστε έγκυρο μήνα:'))
            temp = []
            search_date(event,y,m,temp)
            if temp != []:
                delete = int(input('Δώστε αριθμό γεγονότος προς διαγραφή:'))
                event.remove(temp[delete])
                add_events(event,f = open('events.csv','w'))
            else:
                print('Δεν υπάρχουν προγραμματισμένα γεγονότα τον συγκεκριμένο μήνα')
        elif manage == 3:
            y = int(input('Ετος:'))
            while y < 2023:
                y = int(input('Δώστε έγκυρο έτος:'))
            m = int(input('Μήνας:'))
            while m < 1 or m > 12: 
                m = int(input('Δώστε έγκυρο μήνα:'))
            temp = []
            search_date(event,y,m,temp)
            if temp != []:
                update = int(input('Επιλέξτε γεγονός προς ενημέρωση:'))
                flag = False
                print('Ημερομηνία γεγονότος (',temp[update][0],'):')
                y = int(input('Ετος:'))
                m = int(input('Μήνας:'))
                d = int(input('Ημέρα:'))
                date = check_date(y,m,d)
                print('Ωρα γεγονότος (', temp[update][1],'):')
                h = int(input('Ωρα:'))
                m = int(input('Λεπτά:'))
                time = check_time(h,m)
                print('Διάρκεια γεγονότος (', temp[update][2],'):')
                dur = int(input('Δώστε διάρκεια γεγονότος:'))
                dur = check_duration(dur)
                print('Τίτλος γεγονότος (', temp[update][3],'):')
                title = input('Τίτλος:')
                title = check_title(title)
                rep = [date,time,dur,title]
                stop = False
                i = -1 
                while stop == False:
                    i += 1                   
                    if event[i] == temp[update]:
                        index = i
                        stop = True
                        event[i] = rep
                        add_events(event,f = open('events.csv','w'))
                        print('Το γεγονός ενημερώθηκε: <[',temp[update][3],'] -> Date:',temp[update][0],'Time:', temp[update][1],'Duration:',temp[update][2],'>')
            else: 
                print('Δεν υπάρχουν προγραμματισμένα γεγονότα για τον συγκεκριμένο μήνα')
        elif manage == 0:
            print_menu(make_m = make_month(year,month,event))

    elif option == '*':
        y = int(input('Ετος:'))
        while y < 2023:
            y = int(input('Δώστε έγκυρο έτος:'))
        m = int(input('Μήνας:'))
        while m < 1 or m > 12: 
            m = int(input('Δώστε έγκυρο μήνα:'))
        temp = []
        search_date(event,y,m,temp)
        if temp == []:
            print('Δεν υπάρχουν προγραμματισμένα γεγονότα για τον συγκεκριμένο μήνα')
            
        ex = input('Πατήστε οποιονδήποτε χαρακτήρα για επιστροφή στο κυρίως μενού:')
        if ex != None:
            print_menu(make_m = make_month(year,month,event))
    print_menu(make_m = make_month(year,month,event))
    option = input('Επιλέξτε ενέργεια:')


