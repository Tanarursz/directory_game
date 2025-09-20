import curses
import time

def main(stdscr):
    curses.curs_set(1)
    stdscr.nodelay(True)  # ne blokkolja a getch()
    stdscr.timeout(100)   # 100 ms ciklusidő

    text = ""
    x = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "Írj valamit (ESC kilép):")
        stdscr.addstr(1, 0, text)
        stdscr.refresh()

        key = stdscr.getch()

        if key == -1:
            continue  # nincs billentyű, megy tovább

        if key == 27:  # ESC billentyű
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            text = text[:-1]
        elif 32 <= key <= 126:  # nyomtatható karakterek
            text += chr(key)

        time.sleep(0.01)

curses.wrapper(main)
