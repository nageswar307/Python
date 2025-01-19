import logging

def divide(n,m):
  return n/m

logging.basicConfig(level=logging.DEBUG,filename = "C:\\Users\\DELL\\OneDrive\\Desktop\\log\\test.log")

# DEBUG INFO WARNING ERROR

num = int(input("please enter num"))
logging.debug(f"user entered numerator value as {num}")
den = int(input("please enter den"))
logging.debug(f"user entered denomerator value as {den}")
try:
    logging.info("calling divide function")
    division = divide(num,den)
    logging.info(f"divide fuinction returned value {division}")
    print(f"division of {num},{den} is {division}")
except ZeroDivisionError as e:
    logging.error(f"the user entered den value is {den}")
    den = int(input("please enter non zero value for den"))

    

