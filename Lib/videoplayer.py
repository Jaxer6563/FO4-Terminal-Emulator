import pygame
import moviepy.editor

pygame.init()
video = moviepy.editor.VideoFileClip("video.mp4")
video.preview()
pygame.quit()