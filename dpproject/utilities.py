
import configparser

def ioTest():
    fileName = "test.out"
    outFile = open(fileName,"a+")
    
    name = input("Enter Your Name:")
    print("Hello " + name)
    outFile.write("Name Entered:" + name + "\n")
    
    x = int(input("Enter Value 1:"))
    y = int(input("Enter Value 2:"))
    print("The sum is " + str(x + y))
    outFile.write("The sum is " + str(x + y) + "\n")
    
    outFile.close()
    
    inFile = open(fileName,"r")
    line1 = inFile.read()
    line2 = inFile.read()
    
    print(line1)
    print(line2)

def propertyExample():
    print("Read in Properties")
    config = configparser.ConfigParser()
    config.read("config.properties")
    
    print(config.get('Database','database'))
    
    print(config.get('Database','host'))
    
    print("Execute Properties")
    
    import config
    print(config.database)
    
    print(config.host)
    
    print(config.dbprops)
    print(config.dbprops['database'])
    
def systemCommands():
    print("System Commands")
    import subprocess
    
    result = subprocess.run("foobar",shell=True)
    if result.returncode == 0:
        print("Success!")
    else:
        print("Command Failed!!!")
        
systemCommands()

print("End Of Program")