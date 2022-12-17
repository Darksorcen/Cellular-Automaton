import itertools


class ConwaySolver:
    def __init__(self, screen_size, rsize):
        # {(posx, posy): bool}
        self.rects = dict()

        for x in range(screen_size[0]//rsize):
            for y in range(screen_size[1]//rsize):
                self.rects[(x, y)] = False

        self.permutations = list(itertools.permutations((0, 1, -1), 2))
        self.permutations += [(1, 1), (-1, -1)]

    def check_rules(self):
        """
        Check the rules of Conway's Game of Life
        """
        # FIXME: to comment
        # FIXME: maybe change the way of affecting self.permutations
        # TOADD: customizing rules
        # (0, 1), (0, -1), (1, 0), (1, -1), (-1, 0), (-1, 1), (1, 1), (-1, -1)]

        new_rects = dict()
        for pos, val in self.rects.items():
            count = 0
            alive = val

            # count all neighbors alive
            for i in range(len(self.permutations)):
                if count > 3:
                    break
                pos_to_get = (pos[0]+self.permutations[i][0],
                              pos[1]+self.permutations[i][1])

                count += self.rects.get(pos_to_get, 0)

            if (count == 2 or count == 3) and alive:
                new_rects[pos] = True
            elif count == 3 and not alive:
                new_rects[pos] = True
            else:
                new_rects[pos] = False

        self.rects = new_rects