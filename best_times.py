person1 = ['09:00', '10:30', '11:30', '12:00', '13:00', '14:30']
person2 = ['09:30', '10:00', '10:30', '12:00', '14:30', '16:00']
person3 = ['09:00', '09:30', '11:00', '11:30', '12:00', '13:30', '14:30', '15:00']
person4 = ['11:00', '11:30', '12:00', '14:00', '14:30', '16:30', '17:00']
# Available Times: '12:00' and '14:30'
#*args tuple
#s5 = s1.intersection(s2)
#s6 = s2 & s1


#s7 = set(person1) & set(person2) & set(person3) &set(person4)
#print(s7)

def meeting_time(meeting_peeps,*args):
    s1 = set(meeting_peeps)
    for cat in args:
        argset = set(cat) 
        s1 = s1.intersection(cat)
    print(s1)
    print(meeting_peeps)

        
        
 

meeting_time(person1, person2, person3, person4)