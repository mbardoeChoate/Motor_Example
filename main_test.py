import pytest
from robot import Robot
from motor import Motor

@pytest.fixture
def robot():
    # Setup code to create a Robot instance before each test
    robot_instance = Robot(name="TestBot", color="red")
    return robot_instance

def test_robot_initialization(robot):
    # Test that the robot's properties are initialized correctly
    assert robot.name == "TestBot", "Robot name should be initialized correctly"
    assert robot.color == "red", "Robot color should be initialized correctly"
    assert isinstance(robot.left_motor, Motor), "Left motor should be an instance of Motor"
    assert isinstance(robot.right_motor, Motor), "Right motor should be an instance of Motor"

def test_drive_forward(robot):
    robot.drive_forward(1)
    assert robot.left_motor.get_speed() == 1, "Left motor speed should be set to 1"
    assert robot.right_motor.get_speed() == 1, "Right motor speed should be set to 1"

def test_reverse(robot):
    # Assuming there's a method to reverse direction in the Motor class
    robot.drive_forward(1)  # Set initial direction
    robot.reverse()
    # Assuming reversing changes the direction/speed to negative or some logic you've defined
    assert robot.left_motor.get_speed() < 0, "Left motor speed should be negative after reversing"
    assert robot.right_motor.get_speed() < 0, "Right motor speed should be negative after reversing"

def test_turn_left(robot):
    robot.turn_left()
    assert robot.left_motor.get_speed() == 0, "Left motor speed should be 0 when turning left"
    assert robot.right_motor.get_speed() == 1, "Right motor speed should be 1 when turning left"

def test_turn_right(robot):
    robot.turn_right()
    assert robot.right_motor.get_speed() == 0, "Right motor speed should be 0 when turning right"
    assert robot.left_motor.get_speed() == 1, "Left motor speed should be 1 when turning right"
