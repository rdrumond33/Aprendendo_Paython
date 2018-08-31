minutes = 210;

if minutes < 200:
	acount = minutes * 0.20
elif minutes >200 and minutes<400:
	acount = minutes * 0.18
elif minutes >400 and minutes < 800:
	acount = minutes * 0.08
	acount = minutes*0.15
else:

print "a conta e de :%.2f"%acount