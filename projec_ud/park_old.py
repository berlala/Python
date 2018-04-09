
car_parameters = {"throttle": 0, "steer": 0, "brake": 0}

def park(pos_x, pos_y, time, velocity):
    global car_parameters
        
    
    if(time < 3):
        car_parameters["throttle"] = 0.2
        car_parameters["steer"] = 0
        car_parameters["brake"] = 0
    elif(pos_y > 41):
        car_parameters["throttle"] = -0.5
        car_parameters["steer"] = 0
        car_parameters["brake"] = 0
    elif(pos_y < 41 and  pos_x < 126):
        car_parameters["throttle"] = - 0.8
        car_parameters["steer"] = 24
        car_parameters["brake"] = 0
    elif(pos_y < 35 and pos_y>32.5 and  pos_x > 126):
        car_parameters["throttle"] = - 0.8
        car_parameters["steer"] = -24
        car_parameters["brake"] = 0
    else:
        car_parameters["throttle"] = 0
        car_parameters["steer"] = 0
        car_parameters["brake"] = 1
    
    return car_parameters
    
import src.simulate as sim
sim.run(park)
