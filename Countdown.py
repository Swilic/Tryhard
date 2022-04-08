import time


def countdown(t):
    # Tant que t est superieur a 0
    while t:
        # divmod = division entiere et reste (à répéter!)
        mins, secs = divmod(t, 60)
        # end r pas tout compris        :02d = 2 chiffres avec 0 en début
        print(end=f"\r{mins}:{secs:02d}")
        t -= 1
        time.sleep(1)


if __name__ == "__main__":
    countdown(60)
    print(end="\rBoom!")
