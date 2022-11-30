import pygame
import random
from itertools import cycle

pygame.init()

WIDTH = 300
HEIGHT = 500
NUM_BARS = 300

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font Credit: https://www.fontspace.com/pixeboy-font-f43730
FONT = pygame.font.Font('static/retro_font.ttf', 30)


def iterative_reverse_quick_sort(arr, l, h):

	def partition(arr, l, h):
		i = ( l - 1 )
		x = arr[h]

		for j in range(l, h):
			if arr[j] <= x:

				i = i + 1
				arr[i], arr[j] = arr[j], arr[i]

		arr[i + 1], arr[h] = arr[h], arr[i + 1]
		return (i + 1)

	size = h - l + 1
	stack = [0] * (size)

	top = -1

	top = top + 1
	stack[top] = l
	top = top + 1
	stack[top] = h

	while top >= 0:

		h = stack[top]
		top = top - 1
		l = stack[top]
		top = top - 1

		p = partition( arr, l, h )

		if p-1 > l:
			top = top + 1
			stack[top] = l
			top = top + 1
			stack[top] = p - 1

		if p + 1 < h:
			top = top + 1
			stack[top] = p + 1
			top = top + 1
			stack[top] = h

		yield arr.copy()[::-1]


def iterative_reverse_bubble_sort(l):
	changed = True
	while changed:
		changed = False
		for i in range(len(l) - 1):
			if l[i] < l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				changed = True
				yield l.copy()


def iterative_reverse_insertion_sort(l):
	for i, value in enumerate(l):
		for j in range(i - 1, -1, -1):
			if l[j] > value:
				l[j + 1] = l[j]
				l[j] = value
				yield l.copy()[::-1]


def render(screen, bars: list[int]):
	width_of_each_bar = WIDTH // len(bars)
	for x, bar in enumerate(bars):

		surf = pygame.Surface((width_of_each_bar, bar))
		surf.fill((bar, 60, 60))

		screen.blit(surf,(WIDTH - width_of_each_bar - (x * width_of_each_bar), HEIGHT-bar))


def main():
	unsorted = [random.randint(1, 255) for _ in range(NUM_BARS)]
	all_iterations = [*iterative_reverse_insertion_sort(unsorted)]
	bars = cycle(all_iterations)


	l = next(bars)
	last_iteration = all_iterations[-1]
	keep_sorting = False

	screen = pygame.display.set_mode([WIDTH, HEIGHT])
	pygame.display.set_caption("Algorithm Visualiser")
	clock = pygame.time.Clock()
	framerate = NUM_BARS

	text_surface = FONT.render('Insertion Sort', False, WHITE)


	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
			elif event.type == pygame.KEYDOWN:
				match event.key:
					case pygame.K_1:
						unsorted = [random.randint(1, 255) for _ in range(NUM_BARS)]
						all_iterations = [*iterative_reverse_insertion_sort(unsorted)]
						bars = cycle(all_iterations)
						l = next(bars)

						last_iteration = all_iterations[-1]
						keep_sorting = False
						framerate = NUM_BARS

						text_surface = FONT.render('Insertion Sort', False, WHITE)

					case pygame.K_2:
						unsorted = [random.randint(1, 255) for _ in range(NUM_BARS)]
						all_iterations = [*iterative_reverse_bubble_sort(unsorted)]
						bars = cycle(all_iterations)
						l = next(bars)
						
						last_iteration = all_iterations[-1]
						keep_sorting = False
						framerate = NUM_BARS

						text_surface = FONT.render('Bubble Sort', False, WHITE)

					case pygame.K_3:
						unsorted = [random.randint(1, 255) for _ in range(NUM_BARS)]
						first = unsorted.copy()
						all_iterations = [*iterative_reverse_quick_sort(unsorted, 0, len(unsorted) - 1)]
						bars = cycle(all_iterations)
						l = first
						
						last_iteration = all_iterations[-1]
						keep_sorting = False
						framerate = 8

						text_surface = FONT.render('Quick Sort', False, WHITE)

					case pygame.K_ESCAPE:
						return
					case pygame.K_SPACE:
						keep_sorting = not keep_sorting			

		screen.fill(BLACK)
		if keep_sorting:
			l = next(bars)
			if l == last_iteration:
				keep_sorting = False
		render(screen, l)
		
		clock.tick(framerate)
		screen.blit(text_surface, (0, 0))


		pygame.display.flip()

main()
pygame.quit()



