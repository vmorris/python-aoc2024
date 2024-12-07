import copy
import operator
import logging
from aoc2024.util import get_input
from networkx import (
    Graph,
    spring_layout,
    draw,
    get_edge_attributes,
    draw_networkx_edge_labels,
)

# import networkx
import matplotlib.pyplot as plt

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def build_tree(tree: Graph, parent, operands, depth):
    logger.info(f"build_tree: parent:{parent.get("value")}, operands: {operands}")
    if not operands:
        return tree
    operand = operands.pop(0)
    children = list()
    parent_value = parent.get("value")
    for op in [(operator.add, "+"), (operator.mul, "*")]:
        i = 0
        child_value = op[0](parent_value, operand)
        tree.add_node(depth + i, value=child_value)
        # tree.add_edge(parent_value, child_value, operation=f"{op[1]} {operand}")
        children.append(child_value)
        i += 1
    for c in children:
        logger.info(
            f"- recursive call: old_parent:{parent.get("value")}, new_parent:{tree.nodes[c].get("value")} "
        )
        build_tree(tree, tree.nodes[c], copy.copy(operands), depth + 10)


def solve_part1(entries):
    result = 0
    for expected, operands in entries.items():
        logger.debug(f"{expected}: {operands}")
        tree = Graph()
        root_val = operands.pop(0)
        tree.add_node(0, value=root_val)
        build_tree(tree=tree, parent=tree.nodes[root_val], operands=operands, depth=1)
        pos = spring_layout(tree, seed=42)
        # node_lables = networkx.get_node_attributes(tree, "operand")
        edge_labels = get_edge_attributes(tree, "operation")
        draw(
            tree,
            pos,
            with_labels=True,
            node_size=700,
            node_color="skyblue",
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
