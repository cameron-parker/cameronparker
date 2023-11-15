# -*- coding: utf-8 -*-
"""
@author: cameron parker
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


'''General function to create a strikzone and plot pitches from a Trackman csv.'''

def plot(table: pd.DataFrame):
    '''Plot pitches on a strikezone from df. Must have columns
    PlateLocHeight and PlateLocSide in table.'''
    
    # Define the strike zone dimensions
    left = -0.708  # Left edge in feet
    right = 0.708  # Right edge in feet
    bottom = 1.667  # Bottom edge in feet
    top = 3.417  # Top edge in feet

    xarr = table['PlateLocSide'].to_numpy()
    yarr = table['PlateLocHeight'].to_numpy()
    
    # Create a plot
    fig, ax = plt.subplots()

    # Plot the strike zone as a rectangle
    strike_zone = plt.Rectangle((left, bottom), right - left, top - bottom, fill=False, color='black', linewidth=3)
    ax.add_patch(strike_zone)

    # Set plot limits to match the strike zone dimensions
    ax.set_xlim(-3, 3)  # Adjust these values to fit your specific needs
    ax.set_ylim(0, 5)

    # Divide the strike zone into nine equally sized boxes
    box_width = (right - left) / 3
    box_height = (top - bottom) / 3

    half_w = (right + left) / 2
    half_h = (top + bottom) / 2

    for i in range(3):
        for j in range(3):
            # Calculate the coordinates of each box
            box_left = left + i * box_width
            box_right = box_left + box_width
            box_bottom = bottom + j * box_height
            box_top = box_bottom + box_height

            # Create a rectangle for the box
            box = plt.Rectangle((box_left, box_bottom), box_width, box_height, fill=False, color='black')
            ax.add_patch(box)

    # Add boxes for the regions above, below, to the sides, and in the corners of the strike zone
    above_box = patches.Rectangle((left, top), right - left, .33, fill=False, color='black')
    below_box = patches.Rectangle((left, bottom), right - left, -.33, fill=False, color='black')
    left_box = patches.Rectangle((left, bottom), -.33, top-half_h, fill=False, color='black')
    tleft_box = patches.Rectangle((left, half_h), -.33, top-half_h, fill=False, color='black')
    right_box = patches.Rectangle((right, bottom), .33, top-half_h, fill=False, color='black')
    tright_box = patches.Rectangle((right, half_h), .33, top-half_h, fill=False, color='black')
    top_left_box = patches.Rectangle((left, top), -.33, .33, fill=False, color='black')
    top_right_box = patches.Rectangle((right, top), .33, .33, fill=False, color='black')
    bottom_left_box = patches.Rectangle((left, bottom), -.33, -.33, fill=False, color='black')
    bottom_right_box = patches.Rectangle((right, bottom), .33, -.33, fill=False, color='black')

    # Add the boxes to the plot
    ax.add_patch(above_box)
    ax.add_patch(below_box)
    ax.add_patch(left_box)
    ax.add_patch(right_box)
    ax.add_patch(top_left_box)
    ax.add_patch(top_right_box)
    ax.add_patch(bottom_left_box)
    ax.add_patch(bottom_right_box)
    ax.add_patch(tleft_box)
    ax.add_patch(tright_box)

    
    for x, y in zip(xarr, yarr):
        plt.scatter(x, y, color='red', s=20, marker='o')
    
    plt.axis('off')  # Turn off the axis labels
    plt.show()


