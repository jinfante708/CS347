class CruiseControl:
    def __init__(self):
        self._cc_speed = 0
        self._status = False
    
    def get_speed(self):
        return self._cc_speed
    
    def get_status(self):
        return self._status
    
    def increment(self):
        self._cc_speed += 1
    
    def decrement(self):
        self._cc_speed -= 1

    def set_speed(self, new_speed):
        self._cc_speed = new_speed
    
    def activate(self):
        self._status = True
    
    def deactivate(self):
        self._status = False

    def check_range(self, new_speed):
        if new_speed >= 10 and new_speed <= 90:
            return True
        else:
            return False