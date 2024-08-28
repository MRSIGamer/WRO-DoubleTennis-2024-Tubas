"""Stops The Game And Everything In The Game """

from Movement_Methods import Movement



movement = Movement()


def Stop_Game():
    """A Method That Fully Stops The Game"""
    movement.DriveBase.stop(brake=True)
    movement.Turn_Hiter_Back()
    movement.Open_Catcher_Untill_Stalled()