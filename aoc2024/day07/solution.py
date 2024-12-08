import copy
import operator
import logging
import random
from networkx import (
    Graph,
    spring_layout,
    draw,
    get_edge_attributes,
    get_node_attributes,
    draw_networkx_edge_labels,
)
import matplotlib.pyplot as plt

from aoc2024.util import get_input

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def build_tree(tree: Graph, parent, operands):
    logger.info(f"build_tree: parent:{parent.get("value")}, operands: {operands}")
    if not operands:
        return
    operand = operands.pop(0)
    parent_value = parent.get("value")
    for op in [(operator.add, "+"), (operator.mul, "*")]:
        child_node_id = random.randint(1, 10000)
        child_value = op[0](parent_value, operand)
        logger.info(f"new child node: id:{child_node_id}, value:{child_value}")
        tree.add_node(child_node_id, id=child_node_id, value=child_value)
        tree.add_edge(parent.get("id"), child_node_id, operation=f"{op[1]} {operand}")
        build_tree(tree, tree.nodes[child_node_id], copy.copy(operands))


def solve_part1(entries):
    result = 0
    for expected, operands in entries.items():
        logger.debug(f"{expected}: {operands}")
        tree = Graph()
        root_val = operands.pop(0)
        node_id = 0
        tree.add_node(node_id, id=node_id, value=root_val)
        build_tree(tree=tree, parent=tree.nodes[node_id], operands=operands)
        pos = spring_layout(tree, seed=42)
        node_lables = get_node_attributes(tree, "value")
        node_color_map = list()
        for node in tree:
            if node == 0:
                node_color_map.append("red")
            else:
                node_color_map.append("skyblue")
        edge_labels = get_edge_attributes(tree, "operation")
        draw(
            tree,
            pos,
            with_labels=True,
            labels=node_lables,
            node_size=700,
            node_color=node_color_map,
            font_size=12,
        )
        draw_networkx_edge_labels(tree, pos, edge_labels=edge_labels)
        plt.show()
    return result


def solve_part2(entries):
    return


if __name__ == "__main__":  # pragma: no cover
    entries = get_input("aoc2024/day07/input", type="dict-ints")
    print(solve_part1(entries))
    print(solve_part2(entries))
