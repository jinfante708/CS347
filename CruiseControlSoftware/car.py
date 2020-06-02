from cruise_control import CruiseControl
from log import Log

class Car:
    def __init__(self):
        self._speed = 0
        self._cruise_control = CruiseControl()
        self._logs = []
    
    def get_current_speed(self):
        return self._speed
    
    def get_cc_status(self):
        return self._cruise_control.get_status()
    
    def get_cc_speed(self):
        return self._cruise_control.get_speed()
    
    def get_logs(self):
        copy = []
        for log in self._logs:
            copy.append(log)
        return copy

    '''
    Return true if the cc_speed is set appropriately, false otherwise.
    '''
    def set_cc_speed(self):
        if self._cruise_control.check_range(self._speed):
            self._cruise_control.set_speed(self._speed)
            return True
        else:
            return False

    def clear_cc_speed(self):
        self._logs.append(Log("Cruise control speed has been cleared and set to 0."))
        self._cruise_control.set_speed(0)

    def increment(self):
        self._logs.append(Log("Speed has been incremented by 1 from " + str(self._speed) + " to " + str(self._speed + 1)))
        self._speed += 1
    
    def decrement(self):
        self._logs.append(Log("Speed has been decremented by 1 from " + str(self._speed) + " to " + str(self._speed - 1)))
        self._speed -= 1
    
    def activate_cc(self):
        self._logs.append(Log("Cruise control has been activated."))
        self._cruise_control.activate()
    
    def deactivate_cc(self):
        self._logs.append(Log("Cruise control has been deactivated."))
        self._cruise_control.deactivate()

    def increment_cc(self):
        self._logs.append(Log("Cruise control speed has been incremented by 1 from " + str(self._speed) + " to " + str(self._speed + 1)))
        self._cruise_control.increment()
    
    def decrement_cc(self):
        self._logs.append(Log("Cruise control speed has been decremented by 1 from " + str(self._speed) + " to " + str(self._speed - 1)))
        self._cruise_control.decrement()