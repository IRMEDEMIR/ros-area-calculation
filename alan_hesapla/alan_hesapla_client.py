#!/usr/bin/env python3

import sys
import rospy
from deneme_paket.srv import alan_hesapla
from deneme_paket.srv import alan_hesaplaRequest
from deneme_paket.srv import alan_hesaplaResponse

def alan_hesapla_client(kenar1, kenar2):
    rospy.wait_for_service('alan_hesapla')
    try:
        alan_hesaplaa = rospy.ServiceProxy('alan_hesapla', alan_hesapla)
        resp1 = alan_hesaplaa(kenar1, kenar2)
        return resp1.alan
    except rospy.ServiceException as e:
        print ("Service call failed: %s"%e)

def usage():
    return "%s [kenar1 kenar2]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        kenar1 = int(sys.argv[1])
        kenar2 = int(sys.argv[2])
    else:
        print (usage())
        sys.exit(1)
    print ("Requesting %s*%s"%(kenar1, kenar2))
    alan = alan_hesapla_client(kenar1, kenar2)
    print ("%s * %s = %s"%(kenar1, kenar2, alan))
