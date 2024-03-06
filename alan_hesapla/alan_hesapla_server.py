#!/usr/bin/env python3

from deneme_paket.srv import alan_hesapla
from deneme_paket.srv import alan_hesaplaRequest
from deneme_paket.srv import alan_hesaplaResponse

import rospy

def handle_alan(req):
    print ("Returning [%s * %s = %s]"%(req.kenar1, req.kenar2, (req.kenar1 * req.kenar2)))
    return alan_hesaplaResponse(req.kenar1 * req.kenar2)

def alan_hesapla_server():
    rospy.init_node('alan_hesapla_server')
    s = rospy.Service('alan_hesapla', alan_hesapla, handle_alan)
    print ("Alan hesaplanıyor..")
    rospy.spin()
    
if __name__ == "__main__":
    alan_hesapla_server()
