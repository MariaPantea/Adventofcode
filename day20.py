import numpy as np

import utils
import numpy as np

import utils


def parse_modules():
    modules = []
    for d in data:
        from_, to_ = d.split('->')
        from_ = from_.strip()
        type_ = None
        if from_[0] in ['%', '&']:
            type_ = from_[0]
            from_ = from_[1:]
        elif from_ == 'broadcaster':
            type_ = 'broadcaster'
        to_ = list(map(lambda x: x.strip(), to_.split(',')))

        modules.append((type_, from_, to_))
    return modules


class Node:
    def __init__(self, name, type_, neighbors):
        self.name = name
        self.type_ = type_
        self.neighbors = neighbors
        self.is_on = False
        self.prev_pulse = {}  # False = low, True = high


class PulseGraph:
    def __init__(self, modules):
        self.modules = modules
        self.graph = {}
        self._build_graph()
        self.pulse_queue = []

    def _build_graph(self):
        for type_, name, neighbors in self.modules:
            if name not in self.graph:
                self.graph[name] = Node(name, type_, neighbors)

        # add prev_pulse for conjunction nodes
        for node in self.graph.values():
            neighbors = node.neighbors
            for n in neighbors:
                n = self.get_node(n)
                if n is not None and n.type_ == '&':
                    n.prev_pulse[node.name] = False

    def get_node(self, name):
        if name not in self.graph:
            return None
        return self.graph[name]

    def get_state(self):
        return tuple((n.name, n.is_on, tuple(n.prev_pulse)) for n in self.graph.values())

    def send_pulse(self, from_node, to_node, is_high):
        node = self.get_node(to_node)
        if node is None:
            return
        match node.type_:
            case 'broadcaster':
                # send same pulse to all neighbors
                for n in node.neighbors:
                    self.pulse_queue.append((node.name, n, is_high))

            case '%':
                # if a flip-flop module receives a low pulse, it flips between on and off.
                # If it was off, it turns on and sends a high pulse.
                # If it was on, it turns off and sends a low pulse.
                if is_high:
                    return
                node.is_on = not node.is_on
                for n in node.neighbors:
                    self.pulse_queue.append((node.name, n, node.is_on))

            case '&':
                # When a pulse is received, the conjunction module first updates its memory for that input.
                # Then, if it remembers high pulses for all inputs, it sends a low pulse; otherwise, it sends a high pulse.
                node.prev_pulse[from_node] = is_high
                if all(node.prev_pulse.values()):
                    is_high = False
                else:
                    is_high = True
                for n in node.neighbors:
                    self.pulse_queue.append((node.name, n, is_high))

            case _:
                print(f'Unknown type {node.type_}')
                return

    def press_button(self):
        n_pulses = {True: 0, False: 0}
        self.pulse_queue.append((None, 'broadcaster', False))
        rx_is_low = False
        while self.pulse_queue:
            from_node, to_node, is_high = self.pulse_queue.pop(0)
            if to_node == 'rx' and not is_high:
                rx_is_low = True
            n_pulses[is_high] += 1
            self.send_pulse(from_node, to_node, is_high)
        return n_pulses, rx_is_low


def run(n_presses):
    for i in range(n_presses):
        state = graph.get_state()
        if state in seen_states:
            print(i)
            presses_left = n_presses - i
            skipped_cycles = presses_left // i
            actual_presses_left = presses_left % i
            total_n_pulses[True] += skipped_cycles * total_n_pulses[True]
            total_n_pulses[False] += skipped_cycles * total_n_pulses[False]
            run(actual_presses_left)
            break

        seen_states.add(state)
        n_pulses, _ = graph.press_button()
        total_n_pulses[True] += n_pulses[True]
        total_n_pulses[False] += n_pulses[False]


if __name__ == '__main__':
    data = utils.read_input('inputs/day20.txt')
    modules = parse_modules()

    # Part 1
    graph = PulseGraph(modules)
    seen_states = set()
    total_n_pulses = {True: 0, False: 0}
    run(1000)
    print('Part 1: ', total_n_pulses[True] * total_n_pulses[False])

    # Part 2
    # Inspection of the graph shows that the rx node is only connected to one conjunction nodes,
    # which in turn are connected to 4 other conjunction nodes. These conjunction nodes are connected each conjunction node,
    # which in turn are connected to a set of flip-flop nodes. The flip-flop nodes are connected to each other
    # in groups of 12, and one of them to the broadcaster node. Acting as a 12-bit counter.
    #
    #
    #                 %rx
    #                  |
    #                 &ll <- sends low
    #              /  /  \  \
    #            &kl &vm &kv &vb <- all sends high
    #             |   |   |   |
    #           &ff  &th  &hb &tj  <- all sends low
    #           /     |    |    \
    #     %-..-%  %-..%  %-..%  %-..%  <- all flip-flop nodes need to send a high pulse to their conjunction nodes
    #         \      |     |      /
    #               broadcaster       <- sends low
    #
    # By decoding the binary number from the flip-flop nodes, we get the number of cycles needed to fire up the
    # connected conjunction node. The cycle will be a prime number so just multiply the cycles together to get the answer.
    # someone made a cool simulation: https://www.reddit.com/media?url=https%3A%2F%2Fi.redd.it%2Fgiirl4g74f7c1.gif

    cycles = []
    graph = PulseGraph(modules)
    broadcaster = graph.get_node('broadcaster')
    for flip_flop_node in broadcaster.neighbors:
        flip_flop_node = graph.get_node(flip_flop_node)
        b = ""
        while True:
            flip_flop_neighbours = [graph.get_node(n) for n in flip_flop_node.neighbors]

            # check if any of the neighbors are conjunction nodes
            is_conjunction = any(node.type_ == '&' for node in flip_flop_neighbours)
            b += '1' if is_conjunction else '0'

            # get all connected flip-flop nodes
            flip_flops = [cn for cn in flip_flop_neighbours if cn.type_ == '%']
            if not flip_flops:
                break
            flip_flop_node = flip_flops[0]

        cycles.append(int(''.join(reversed(b)), 2))

    print('Part 2: ', np.prod(cycles))
