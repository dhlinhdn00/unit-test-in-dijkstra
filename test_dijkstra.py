import pytest
from dijkstra import base_dijikstra, wrong_dijkstra_empty, wrong_dijkstra_single
import argparse

def test_empty_graph():
    # result = base_dijikstra({}, 'A')
    result = wrong_dijkstra_empty({}, 'A')
    expected = {}
    assert result == expected, f"Failed with empty graph: Expected {expected} but got {result}"
    print("test_empty_graph passed.")

def test_single_node():
    # result = base_dijikstra({'A': {}}, 'A')
    result = wrong_dijkstra_single({'A': {}}, 'A')
    expected = {'A': 0}
    assert result == expected, f"Failed with single node graph:: Expected {expected} but got {result}"
    print("test_single_node passed.")

def test_complex_graph():
    graph = {
        'A': {'B': 2, 'C': 3},
        'B': {'A': 2, 'D': 4},
        'C': {'A': 3, 'D': 1},
        'D': {'B': 4, 'C': 1}
    }
    result = base_dijikstra(graph, 'A')
    # result = base_dijikstra(graph, 'A', 3)
    expected = {'A': 0, 'B': 2, 'C': 3, 'D': 4}
    assert result == expected, f"Failed with complex graph: Expected {expected} but got {result}"
    print("test_complex_graph passed.")

def test_multiple_equivalent_paths():
    graph = {
        'A': {'B': 1, 'C': 1},
        'B': {'D': 1},
        'C': {'D': 1},
        'D': {}
    }
    result = base_dijikstra(graph, 'A')
    # result = base_dijikstra(graph, 'A', 5)
    expected = {'A': 0, 'B': 1, 'C': 1, 'D': 2}
    assert result == expected, f"Failed with multiple equivalent paths: Expected {expected} but got {result}"
    print("test_multiple_equivalent_paths passed.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run specific tests for Dijkstra algorithm.")
    parser.add_argument("--test_case", type=str, choices=["empty", "single", "complex", "multiple"], help="Choose which test case to run")
    args = parser.parse_args()

    if args.test_case == "empty":
        test_empty_graph()
    elif args.test_case == "single":
        test_single_node()
    elif args.test_case == "complex":
        test_complex_graph()
    elif args.test_case == "multiple":
        test_multiple_equivalent_paths()
