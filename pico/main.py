from src.controllers.main_controller import MainController
import time

main_controller = MainController()
last_time_meaure = time.ticks_ms()
update_interval = 50

while True:
    if time.ticks_diff(time.ticks_ms(), last_time_meaure) > update_interval:
        main_controller.loop()
        last_time_meaure = time.ticks_ms()