s=input()
am_pm=s[-2:].lower()
time=s[:2]

t=int(time)
#print(type(am_pm),type(t))
if t<12 and am_pm=='pm':
    newt=t+12
elif t < 12 and am_pm == 'am':
    newt = s[:2]
elif t==12 and am_pm=='am':
    newt=str("00")
elif t==12 and am_pm=='pm':
    newt=t

#print(newt)
st=str(newt)
#print(s.replace(time,st))
mt=s.replace(time,st)
print(mt[:-2])
