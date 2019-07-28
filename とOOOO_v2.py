#ProjectしOOO - とOOOO module
import statistics
def avr(list):
    sum = 0
    ttl = 0
    for num in list:
       sum += num
       ttl += 1
    return(str(sum/ttl)+","+str(statistics.stdev(list)))
f = open("一.data","r")
a = []
i = 0
rcount = 0
while True:
    v = f.readline()
    if v == "":
        break
    v = v.upper()
    if v.endswith("\n"):
        v = v[:-1]
    p = len(v)-1
    rcount = len(v)
    for char in v:
        if i == 0:
            a.append([])
        a[ord(char)-65].append(p/(len(v)-1))
        p -= 1
    i += 1
f.close()
f = open("二.data","w")
for r in range(rcount):
    f.write(str(avr(a[r]))+"\n")