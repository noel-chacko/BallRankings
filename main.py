from espn import *
from run247 import *
from rivals import *
from on3 import *
from ranker import *
from nickname import *
from combine import *
from finalToHTML import *
import time

start_time = time.time()
espn()
print("Done ESPN")
run247()
print("Done 247")
rivals()
print("Done Rivals")
on3()
print("Done On3")

combine()
print("Done Combine")
nickname()
print("Done Nickname")
ranker()
print("Done Ranker")
toHTML()
print("Done HTML")

print("Process finished --- %s seconds ---" % (time.time() - start_time))