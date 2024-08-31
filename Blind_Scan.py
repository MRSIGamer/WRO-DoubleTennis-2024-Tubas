from Scan import scan



def blind_scan():
    """Makes A Search Without Using the Pixy Camera(linear search)"""
    scan("start_left")
    scan("start_right")
    scan("left")
    scan("middle")
    scan("right")
    scan("go_home_left")
    scan("go_home_middle")
    scan("go_home_right")
    return True



