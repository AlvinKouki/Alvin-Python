
            emy2_x = random.randint(int(emy2_wh), int(bg_x - emy2_wh))
            emy2_y = random.randint(int(emy2_wh), int(emy2_hh + 100))

    if emy2_f == True:
        emy2_y += emy2_shift
        for n in range(MISSILE_MAX):
            if msl_f[n] == True and is_hit(emy2_x, emy2_y, m