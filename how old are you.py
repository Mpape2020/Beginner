#was able to make an age calculator while also being able to involve choice
Name = input("Please enter your name:")
Age = input("Please enter your age:")
choose = input("choose between 'hours' 'minutes' or 'seconds:" )
h = int(Age)*365.25*24
m = int(Age)*365.25*24*60
s = int(Age)*365.25*24*60*60
hour = ('hours')
hour1 = ('Hours')
min = ('minutes')
min1 = ('Minutes')
sec = ('seconds')
sec1 = ('Seconds')
if choose == hour or choose == hour1:
    print('Great!', Name + ",", "you are", h, "hours old!")
if choose == min or choose == min1:
    print('OH awesome!', Name + ',', "you are", m, "minutes old!")
if choose == sec or choose == sec1:
    print('Goodness!', Name + ',', "you are", s, 'seconds old!')
