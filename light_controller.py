import subprocess

class LightController:
    def turn_off(self):
        subprocess.run("echo 0 | sudo tee  /sys/class/leds/led0/brightness", shell=True)
        subprocess.run("echo 0 | sudo tee /sys/class/leds/led1/brightness", shell=True)

    def turn_on(self):
        subprocess.run("echo 1 | sudo tee  /sys/class/leds/led0/brightness", shell=True)
        subprocess.run("echo 1 | sudo tee /sys/class/leds/led1/brightness", shell=True)


if __name__ == "__main__":
    light_contrl = LightController()
    light_contrl.turn_off()