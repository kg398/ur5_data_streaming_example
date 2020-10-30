import time
import numpy as np
import scipy.optimize as optimize

import waypoints as wp
import kg_robot as kgr

def main():
    print("------------Configuring Burt-------------\r\n")
    #burt = kgr.kg_robot()
    burt = kgr.kg_robot(port=30010,db_host="192.168.1.10")
    print("----------------Hi Burt!-----------------\r\n\r\n")

    
    try:
        while 1:
            ipt = input("cmd: ")
            if ipt == 'close':
                break
            elif ipt == 'home':
                print(burt.home())

            elif ipt == 't':
                burt.teach_mode.record()
            elif ipt == 'p':
                burt.teach_mode.play()


            elif ipt == 'test':
                demand_pose = burt.getl()
                toc = time.time()

                #init data streaming
                burt.stream_data_start(0.01)

                #loop servoj and read pose
                for i in range(0,100):
                    demand_pose[0]+=0.001
                    burt.servoj(demand_pose,control_time=0.01)
                    current_pose = burt.read_msg()
                    print(time.time()-toc,': ',current_pose)
                    time.sleep(0.009)

                #stop data streaming
                burt.stream_data_stop()

                #flush recv buffer
                time.sleep(0.5)
                print(burt.ping())
                print(burt.ping())

    finally:
        print("Goodbye")
        burt.close()
if __name__ == '__main__': main()