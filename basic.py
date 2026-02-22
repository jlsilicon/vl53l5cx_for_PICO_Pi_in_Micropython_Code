###  basic.py


# from sensor import make_sensor
if( 1 ) :
    from machine import I2C, Pin

    from vl53l5cx.mp import VL53L5CXMP

#    scl_pin, sda_pin, lpn_pin, _ = (22, 21, 12, 13)
    scl_pin, sda_pin, lpn_pin, _ = (5, 4, 6, 13)
    i2c = I2C(0, scl=Pin(scl_pin, Pin.OUT), sda=Pin(sda_pin), freq=1_000_000)
#    i2c = I2C(0, scl=Pin(scl_pin, Pin.OUT), sda=Pin(sda_pin), freq=2_000_000)

    tof = VL53L5CXMP(i2c, lpn=Pin(lpn_pin, Pin.OUT, value=1))


from vl53l5cx  import  DATA_TARGET_STATUS, DATA_DISTANCE_MM
from vl53l5cx  import  STATUS_VALID, RESOLUTION_4X4 , RESOLUTION_8X8


def main():

#    tof = make_sensor()  ## - see above 
    tof.reset()

    if not tof.is_alive():
        raise ValueError("VL53L5CX not detected")

    tof.init()


#    tof.resolution = RESOLUTION_4X4
#    grid = 3
    tof.resolution = RESOLUTION_8X8
    grid = 7


    tof.ranging_freq = 2
#    tof.ranging_freq = 4
    
    ## integration_time_ms = 2 - 1000 
#    tof.integration_time_ms = 66   ## - Noisy 
    tof.integration_time_ms = 120   ## - Little Noisy     ## - Default     ## - Good 
#    tof.integration_time_ms = 200   ## -  Noisy + Slow 

    tof.sharpener_percent = 10  ## - 10% => 0% XXXX     ## - Good 
#    tof.sharpener_percent = 20  ## - 20% => 0% XXXX     ## - Default 
#    tof.sharpener_percent = 30  ## - 30% => 0-5% XXXX 
#    tof.sharpener_percent = 40  ## - 40% => 2-10% XXXX 
#    tof.sharpener_percent = 50  ## - 50% => 10% XXXX 
    
    ## target_order : 1 (Closest) , 2 (Strongest)
    tof.target_order = 1    ## - Good 
#    tof.target_order = 2

    ## ranging_mode : ANGING_MODE_AUTONOMOUS = 3 , RANGING_MODE_CONTINUOUS = 1 
#    tof.ranging_mode = 1 
#    tof.ranging_mode = 3 


    tof.start_ranging({DATA_DISTANCE_MM, DATA_TARGET_STATUS})

    while True:
        if tof.check_data_ready():
            results = tof.get_ranging_data()
            distance = results.distance_mm
            status = results.target_status

            ## output :
            ## - pins are Top
            ## - Left <-> Right Backwards 

            for i, d in enumerate(distance) :
                
                if status[i] == STATUS_VALID:
#                    print("{:4}".format( int((d) / 1) ), end=" ")  ## - mm
#                    print("{:4}".format( int((d) / 10) ), end=" ")  ## - cm 
                    print("{:4}".format( int((d) / 100) ), end=" ")  ## - dm
#                    print("{:4}".format(    ((d) / 1000.0) ), end=" ")  ## - m
                else:
                    print("xxxx", end=" ")

                if (i & grid) == grid:
                    print("")

            print("")


main()
