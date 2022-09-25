import pygame
import random
from Button import Button
from Bar import Bar
from pprint import PrettyPrinter
import copy

pygame.init()

p = PrettyPrinter()

WIDTH = 800
HEIGHT = 800

win = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (50, 50, 50)
BLUE = (0, 0, 255)

buttons = []
text = ["Selection Sort", "Insertion Sort", "Merge Sort", "Bubble Sort", "Reset"]

speed = 10
number_of_bars = 50

side_buffer = 35
buffer = 15
button_buffer = 150
y_buffer = (2 * buffer) + button_buffer

space = (WIDTH - (2 * side_buffer)) / number_of_bars
width = space * 3 / 4


def setup_bars(number_of_bars, minim, maxim):
    bars = []

    y = HEIGHT - y_buffer

    max_val = 0
    for i in range(number_of_bars):
        value = random.randint(minim, maxim)
        max_val = max(value, max_val)

        bars.append(Bar((space - width) / 2 + side_buffer + i * space, y + (buffer / 2), width, value))
        bars[i].set_pos(i)

    Bar.set_factor((HEIGHT - y_buffer) / max_val)
    for bar in bars:
        bar.set_points()

    return bars


def setup_buttons(number_of_buttons, y, button_width, button_height, text=None):
    button_space = ((WIDTH - 2 * side_buffer) - (number_of_buttons * button_width)) / (number_of_buttons - 1)

    for i in range(number_of_buttons):
        buttons.append(Button((button_space + button_width) * i + side_buffer, y, button_width, button_height, GRAY))

        if text is not None:
            buttons[i].set_text(text[i])


def merge(arr1, arr2, bars):
    final_arr = []

    combined = []
    for i in arr1 + arr2:
        combined.append(i.get_pos())

    first = arr1[0]
    last = arr2[len(arr2) - 1]

    while len(arr1) > 0 and len(arr2) > 0:
        arr1[0].set_color(RED)
        arr2[0].set_color(RED)
        update(bars)
        pygame.time.delay(speed)

        if arr1[0].get_value() < arr2[0].get_value():
            arr1[0].set_color(GRAY)
            final_arr.append(arr1.pop(0))
        else:
            arr2[0].set_color(GRAY)
            final_arr.append(arr2.pop(0))

        if len(arr1) > 0:
            arr1[0].set_color(GRAY)
        if len(arr2) > 0:
            arr2[0].set_color(GRAY)

        first.set_color(GREEN)
        last.set_color(GREEN)

        update(bars)
        pygame.time.delay(speed)

    if len(arr1) > 0:
        final_arr += arr1
    else:
        final_arr += arr2

    for i in range(len(final_arr)):
        final_arr[i].update_x(combined[i], space, width, side_buffer)
        final_arr[i].set_pos(combined[i])
        update(bars)
        pygame.time.delay(speed)

    first.set_color(GRAY)
    last.set_color(GRAY)

    return final_arr


def merge_sort(arr, bars):
    length = len(arr)

    if len(arr) <= 1:
        return arr

    mid = length // 2

    first = arr[:mid]
    second = arr[mid:]

    return merge(merge_sort(first, bars), merge_sort(second, bars), bars)


def bubble_sort(bars):
    while True:
        swaps = 0
        for i in range(len(bars) - 1):
            bars[i].set_color(GREEN)
            bars[i + 1].set_color(RED)
            update(bars)
            pygame.time.delay(speed)

            if bars[i].get_value() > bars[i + 1].get_value():
                temp = bars[i]
                bars[i] = bars[i + 1]
                bars[i + 1] = temp

                bars[i].update_x(i, space, width, side_buffer)
                bars[i + 1].update_x(i + 1, space, width, side_buffer)

                update(bars)
                pygame.time.delay(speed)

                swaps += 1

            bars[i].set_color(GRAY)
            bars[i + 1].set_color(GRAY)

        if swaps == 0:
            break

    for i in range(len(bars)):
        y = HEIGHT - y_buffer + buffer
        Bar.set_factor((HEIGHT - y_buffer) / (len(bars) - 1))

        # bars[i].set_value(i)
        # bars[i].set_height()
        bars[i].set_color(BLUE)

        update(bars)
        pygame.time.delay(20)

    return bars


def insertion_sort(bars):
    for i in range(1, len(bars)):
        index = i

        bars[index].set_color(GREEN)
        update(bars)
        pygame.time.delay(speed)

        while index != 0 and bars[index].get_value() < bars[index - 1].get_value():
            temp = bars[index]
            bars[index] = bars[index - 1]
            bars[index - 1] = temp

            bars[index].update_x(index, space, width, side_buffer)
            bars[index - 1].update_x(index - 1, space, width, side_buffer)

            index -= 1

            update(bars)
            pygame.time.delay(speed)
        bars[index].set_color(GRAY)
        update(bars)
        pygame.time.delay(speed)

    for i in range(len(bars)):
        y = HEIGHT - y_buffer + buffer
        Bar.set_factor((HEIGHT - y_buffer) / (len(bars) - 1))

        # bars[i].set_value(i)
        # bars[i].set_height()
        bars[i].set_color(BLUE)

        update(bars)
        pygame.time.delay(20)

    return bars


def selection_sort(bars):
    for i in range(len(bars)):
        min_index = i
        bars[i].set_color(GREEN)
        update(bars)

        for j in range(i + 1, len(bars)):
            bars[j].set_color(GREEN)
            update(bars)

            if bars[j].get_value() < bars[min_index].get_value():
                if min_index != i:
                    bars[min_index].set_color(GRAY)
                min_index = j

            pygame.time.delay(speed)
            bars[j].set_color(GRAY)
            if min_index != i:
                bars[min_index].set_color(RED)

        bars[i].set_color(GRAY)

        temp = bars[i]
        bars[i] = bars[min_index]
        bars[min_index] = temp

        bars[i].update_x(i, space, width, side_buffer)
        bars[min_index].update_x(min_index, space, width, side_buffer)

        bars[i].set_color(BLUE)
        update(bars)
        pygame.time.delay(speed * 2)

    return bars


def update(bars):
    win.fill(WHITE)
    pygame.draw.line(win, BLACK, (side_buffer, HEIGHT - button_buffer), (WIDTH - side_buffer, HEIGHT - button_buffer))

    for button in buttons:
        button.draw(win)

    for bar in bars:
        bar.draw(win)

    pygame.display.update()


def main():
    running = True

    bars = setup_bars(number_of_bars, 5, 100)
    unsorted_bars = copy.copy(bars)

    setup_buttons(5, HEIGHT - 2/3 * button_buffer, 100, 50, text)

    is_sorted = False

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and is_sorted is False:
                for i in range(len(buttons)):
                    if buttons[i].check_hover(pygame.mouse.get_pos()):
                        if i == 0:
                            bars = selection_sort(bars)
                        elif i == 1:
                            bars = insertion_sort(bars)
                        elif i == 2:
                            bars = merge_sort(bars, bars)
                            for bar in bars:
                                bar.set_color(BLUE)
                                update(bars)
                                pygame.time.delay(speed)
                        elif i == 3:
                            bars = bubble_sort(bars)
                        else:
                            bars = setup_bars(number_of_bars, 5, 100)

            for button in buttons:
                button.set_highlight(pygame.mouse.get_pos())

        update(bars)
    quit()


main()
