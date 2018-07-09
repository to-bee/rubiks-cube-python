# --- Right ---
def right():
    return 2, slice(None), slice(None)


def right_rotation_top():
    return 2, 2, slice(None)


def right_rotation_down():
    return 2, 0, slice(None)


def right_rotation_back():
    return 2, slice(None), 0


def right_rotation_front():
    return 2, slice(None), 2


# --- Left ---
def left():
    return 0, slice(None), slice(None)


def left_rotation_top():
    return 0, 2, slice(None)


def left_rotation_down():
    return 0, 0, slice(None)


def left_rotation_back():
    return 0, slice(None), 0


def left_rotation_front():
    return 0, slice(None), 2


# --- Front ---
def front():
    return slice(None), slice(None), 2


def front_rotation_top():
    return slice(None), 2, 2


def front_rotation_right():
    return 2, slice(None), 2


def front_rotation_down():
    return slice(None), 0, 2


def front_rotation_left():
    return 0, slice(None), 2


# --- Back ---
def back():
    return slice(None), slice(None), 0


def back_rotation_top():
    return slice(None), 2, 0


def back_rotation_right():
    return 2, slice(None), 0


def back_rotation_down():
    return slice(None), 0, 0


def back_rotation_left():
    return 0, slice(None), 0


# --- Up ---
def up():
    return slice(None), 2, slice(None)


def up_rotation_front():
    return slice(None), 2, 2


def up_rotation_right():
    return 2, 2, slice(None)


def up_rotation_back():
    return slice(None), 2, 0


def up_rotation_left():
    return 0, 2, slice(None)


# --- Down ---
def down():
    return slice(None), 0, slice(None)


def down_rotation_front():
    return slice(None), 0, 2


def down_rotation_right():
    return 2, 0, slice(None)


def down_rotation_back():
    return slice(None), 0, 0


def down_rotation_left():
    return 0, 0, slice(None)
