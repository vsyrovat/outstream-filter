from mylib.filter import filter

test_data = [
    {"in": [], "out": []},
    {"in": [{"id": 1, "timestamp": 2}], "out": [{"id": 1, "timestamp": 2}]},
    {
        "in": [{"id": 1, "timestamp": 2}, {"id": 1, "timestamp": 3}],
        "out": [{"id": 1, "timestamp": 3}],
    },
    {
        "in": [{"id": 1, "timestamp": 5}, {"id": 1, "timestamp": 4}],
        "out": [{"id": 1, "timestamp": 5}],
    },
]


def test_filter():
    for i, t in enumerate(test_data):
        assert filter(t["in"]) == t["out"]
