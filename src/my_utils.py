from global_controller.global_controller import Global_Controller

def set_global_controller(gc: Global_Controller):
    gc.update(Global_Controller.SHUTDOWN, False)