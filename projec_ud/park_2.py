
car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def park(pos_x, pos_y, time, velocity):
    global car_parameters
        
    
    if(time < 5):
        car_parameters["throttle"] = -0.1
        car_parameters["steer"] = 22
        car_parameters["brake"] = 0
    elif(time >5 and time < 8.1):
        car_parameters["throttle"] = -0.1
        car_parameters["steer"] = -22
        car_parameters["brake"] = 0
    else:
        car_parameters["throttle"] = 0
        car_parameters["steer"] = 0
        car_parameters["brake"] = 1
    
    return car_parameters
    
import src.simulate as sim
sim.run(park)
