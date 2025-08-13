from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

angle = 0  # rotation angle

# Step 2: Define cube edges
def draw_cube():
    glBegin(GL_LINES)
    # Front face
    glVertex3f(-1, -1,  1); glVertex3f( 1, -1,  1)
    glVertex3f( 1, -1,  1); glVertex3f( 1,  1,  1)
    glVertex3f( 1,  1,  1); glVertex3f(-1,  1,  1)
    glVertex3f(-1,  1,  1); glVertex3f(-1, -1,  1)

    # Back face
    glVertex3f(-1, -1, -1); glVertex3f( 1, -1, -1)
    glVertex3f( 1, -1, -1); glVertex3f( 1,  1, -1)
    glVertex3f( 1,  1, -1); glVertex3f(-1,  1, -1)
    glVertex3f(-1,  1, -1); glVertex3f(-1, -1, -1)

    # Connecting edges
    glVertex3f(-1, -1,  1); glVertex3f(-1, -1, -1)
    glVertex3f( 1, -1,  1); glVertex3f( 1, -1, -1)
    glVertex3f( 1,  1,  1); glVertex3f( 1,  1, -1)
    glVertex3f(-1,  1,  1); glVertex3f(-1,  1, -1)
    glEnd()

# Step 4 & 5: Display function with camera + rotation
def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(3, 3, 3, 0, 0, 0, 0, 1, 0)  # camera
    glRotatef(angle, 1, 1, 1)             # rotation
    draw_cube()

    glutSwapBuffers()
    angle += 1  # update angle

# Projection setup so cube is visible
def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, aspect, 1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

# Step 1 & 3: Initialize OpenGL
def init():
    glClearColor(0, 0, 0, 1)  # background black
    glColor3f(1, 1, 1)        # white lines
    glEnable(GL_DEPTH_TEST)   # enable depth test

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"Rotating 3D Wireframe Cube")

    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutIdleFunc(display)  # Step 6: animation loop

    glutMainLoop()

if __name__ == "__main__":
    main()
