import pygame
import sys
import random
from scipy.spatial import ConvexHull

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Random Dots and Non-Intersecting Path')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
dot_color = (0, 255, 0)
path_color = (255, 0, 0)

# Number of dots
num_dots = 10

# Radius of dots
dot_radius = 5

# List to store dot coordinates
dots = [(random.randint(dot_radius, width - dot_radius), random.randint(dot_radius, height - dot_radius)) for _ in range(num_dots)]

# Function to find the convex hull and a non-intersecting path within the convex hull
def generate_non_intersecting_path(dots):
    hull = ConvexHull(dots)
    convex_hull_dots = [dots[i] for i in hull.vertices]
    order = list(range(len(convex_hull_dots)))
    random.shuffle(order)
    return order

# Function to reset the dots
def reset_dots():
    return [(random.randint(dot_radius, width - dot_radius), random.randint(dot_radius, height - dot_radius)) for _ in range(num_dots)]

# Main game loop
running = True
animation_step = 0
selected_dot = None
add_point_button = pygame.Rect(10, 10, 120, 30)
start_animation_button = pygame.Rect(140, 10, 140, 30)
reset_button = pygame.Rect(290, 10, 80, 30)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if add_point_button.collidepoint(event.pos):
                dots.append((random.randint(dot_radius, width - dot_radius), random.randint(dot_radius, height - dot_radius)))
            elif start_animation_button.collidepoint(event.pos):
                animation_step = 0
            elif reset_button.collidepoint(event.pos):
                dots = reset_dots()
                animation_step = 0

    # Draw background
    screen.fill(black)

    # Draw random dots
    for dot in dots:
        pygame.draw.circle(screen, dot_color, dot, dot_radius)

    # Draw convex hull
    convex_hull_dots = [dots[i] for i in ConvexHull(dots).vertices]
    pygame.draw.polygon(screen, white, convex_hull_dots, 2)

    # Animation to simulate the process of selecting the next point
    if animation_step < len(convex_hull_dots):
        selected_dot = convex_hull_dots[animation_step]
        pygame.draw.circle(screen, path_color, selected_dot, dot_radius + 2)

        # Draw the path up to the current selected point
        if animation_step > 0:
            ordered_dots = convex_hull_dots[:animation_step + 1]
            pygame.draw.lines(screen, path_color, False, ordered_dots, 2)

        animation_step += 1

    # Draw buttons
    pygame.draw.rect(screen, (100, 100, 100), add_point_button)
    pygame.draw.rect(screen, (100, 100, 100), start_animation_button)
    pygame.draw.rect(screen, (100, 100, 100), reset_button)

    font = pygame.font.Font(None, 36)
    add_point_text = font.render("Add Point", True, white)
    start_animation_text = font.render("Start Animation", True, white)
    reset_text = font.render("Reset", True, white)

    screen.blit(add_point_text, (20, 15))
    screen.blit(start_animation_text, (150, 15))
    screen.blit(reset_text, (300, 15))

    # Update the display
    pygame.display.flip()

    # Add a delay for visualization
    pygame.time.delay(500)

# Quit Pygame
pygame.quit()
sys.exit()
