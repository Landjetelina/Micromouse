class PID:
    def __init__(self, Kp, Ki, Kd, dt):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.dt = dt
        
        self.prev_error = 0
        self.integral = 0

    def compute(self, error):
        # Proporcionalni
        P = self.Kp * error
        
        # Integralni (s anti-windup clampom)
        self.integral += error * self.dt
        self.integral = max(-500, min(500, self.integral))  # clamp
        I = self.Ki * self.integral
        
        # Derivativni
        D = self.Kd * (error - self.prev_error) / self.dt
        self.prev_error = error
        
        return P + I + D

    def reset(self):
        self.prev_error = 0
        self.integral = 0