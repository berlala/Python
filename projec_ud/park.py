
car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def park(pos_x, pos_y, time, velocity):
    global car_parameters
        
    
    if( pos_y >37.5 ):
        car_parameters["throttle"] = -0.1
        car_parameters["steer"] = 1
        car_parameters["brake"] = 0
    elif(pos_y >35 ):
        car_parameters["throttle"] = -0.01
        car_parameters["steer"] = 0
        car_parameters["brake"] = 0
    elif(pos_y >31.5 ):
        car_parameters["throttle"] = -0.01
        car_parameters["steer"] = -1
        car_parameters["brake"] = 0	
    else:
        car_parameters["throttle"] = 0
        car_parameters["steer"] = 0
        car_parameters["brake"] = 1
    
    return car_parameters
    
import src.simulate as sim
sim.run(park)
