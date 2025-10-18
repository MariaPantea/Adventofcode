import utils


def transfer_seeds(seeds, maps):
    for _, *map_ in maps:
        ranges = []
        for range_ in map_:
            dest, src, n = map(int, range_.split(' '))
            ranges.append((src, n, dest))

        transferred_seeds = []
        for seed in seeds:
            for src, n, dest in ranges:
                if src <= seed < src + n:
                    transferred_seeds.append(seed - src + dest)
                    break
            else:
                transferred_seeds.append(seed)
        seeds = transferred_seeds

    return seeds


def transfer_seed_ranges(seed_ranges, maps):
    for _, *map_ in maps:
        ranges = []
        for range_ in map_:
            dest, src, n = map(int, range_.split(' '))
            ranges.append((src, n, dest))

        transferred_seeds = []

        for seed_start, seed_n in seed_ranges:
            while seed_n != 0:
                in_any_range = False
                min_l = seed_n

                for src, n, dest in ranges:
                    if src <= seed_start < src + n:
                        # if in range, transfer as much as possible
                        offset = seed_start - src
                        l = min(n - offset, seed_n)
                        transferred_seeds.append((dest + offset, l))
                        seed_start += l
                        seed_n -= l
                        in_any_range = True
                        break
                    else:
                        if seed_start < src:
                            # if not in range, find closest upper range within seed_n
                            min_l = min(src - seed_start, min_l)

                if not in_any_range:
                    # if not in any range, transfer as much as possible
                    l = min(min_l, seed_n)
                    transferred_seeds.append((seed_start, l))
                    seed_start += l
                    seed_n -= l

        seed_ranges = transferred_seeds

    return (start for start, _ in seed_ranges)


if __name__ == '__main__':
    seeds, *maps = utils.read_input_as_doc('inputs/day5.txt').split('\n\n')
    seeds = list(map(int, seeds.split(' ')[1:]))
    maps = [m.split('\n') for m in maps]

    locations = transfer_seeds(seeds, maps)
    print('Part 1: ', min(locations))

    seeds_ranges = list(zip(seeds[::2], seeds[1::2]))
    locations = transfer_seed_ranges(seeds_ranges, maps)
    print('Part 2: ', min(locations))
