import sys

reglist = [["r0","00000000"],
           ["r1","00000000"],
           ["r2","00000000"],
           ["r3","00000000"],
           ["r4","00000000"],
           ["r5","00000000"],
           ["r6","00000000"],
           ["r7","00000000"],
           ["r8","00000000"],
           ["r9","00000000"],
           ["r10","00000000"],
           ["r11","00000000"],
           ["r12","00000000"],
           ["r13","00000000"],
           ["r14","00000000"],
           ["r15","00000000"]]

f = open(sys.argv[2], "w")
f.close()
f = open(sys.argv[2], "a")

def initfile():
    f = open(sys.argv[2], "w")
    f.close()

def writefile(fcontent):
    #f = open(sys.argv[2], "a")
    f.write(fcontent+"\n")
    #f.close()

def printreg():
    for x in reglist:
        writefile(x[0]+" "+x[1])

def updatereg(reg_name, reg_val):
    for x in reglist:
        if reg_name == x[0]:
            #writefile("updated reg: "+reg_name+" value: "+reg_val)
            x[1] = reg_val
            

def readfileelf(fpath):
    f = open(fpath, "r")
    linec = 1
    regname = ""
    regval = ""
    for line in f:
        print ("line: "+str(linec))
        #print line
        if "[33m" in line:
            iline = line.split(" ")
            writefile(iline[2].lower()+" "+iline[3].lower())
        if "[36mREGS:" in line:
            sline = line.rstrip().split(" ")
            #print sline
            for strval in sline:
                #print strval
                if "r" in strval or "isp" in strval:
                    regname = strval.replace("isp","r0")
                if ":" in strval and regname != "":                    
                    tmp = strval.split(":")
                    regval = tmp[1].replace("[0m","").lower()
                    #print "regname: "+regname+" val: "+regval
                    updatereg(regname,regval)
                    regname = ""
        #if "cycles" in line:
        if len(line) <=1:
            printreg()
        linec =linec +1
    f.close()

def readfilevisual(fpath):
    printreg()
    f = open(fpath, "r")
    linec = 1
    insstart = 0
    regstart = 0
    regname = ""
    regval = ""
    for line in f:
        print ("line: "+str(linec))
        if "regend" in line:
            regstart = 0
            printreg()

        if insstart == 1:
            sline = line.rstrip().split()
            writefile(sline[0].lower()+": "+sline[1].lower())
            insstart = 0
        if regstart == 1:
            if line[0] == 'r':
                sline = line.rstrip().split()
                for lines in sline:
                    if 'r' in lines:
                        regname = lines
                    if '=' in lines:
                        regval = lines.replace("=","")
                        updatereg(regname,regval)
          

        if "Insstart" in line:
            insstart = 1
        if "regstart" in line:
            regstart = 1
        linec =linec +1
    f.close()

#initfile()
if sys.argv[3]=='1':
    readfileelf(sys.argv[1])
else:
    readfilevisual(sys.argv[1])
f.close()
