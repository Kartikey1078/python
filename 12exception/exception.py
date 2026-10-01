# when error occur .python will noramlly stop or generate error
# so to prevent from this behaviour we use exception handling 

try:
  print(x)
except:
  print("An exception occurred")

#   Print one message if the try block raises a NameError and another for other errors:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


#   The finally block, if specified, will be executed regardless if the try block raises an error or not.
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


# This can be useful to close objects and clean up resources:
  try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")



# To throw (or raise) an exception, use the raise keyword.
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")