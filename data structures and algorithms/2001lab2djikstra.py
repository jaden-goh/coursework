import math
import random
import time
import heapq
from statistics import mean

# =========================================================
# 1. Dijkstra implementations
# =========================================================

def dijkstra_matrix_array(graph, source=0):
    """
    graph: adjacency matrix
           graph[u][v] = weight, or math.inf if no edge
    """
    n = len(graph)
    dist = [math.inf] * n
    visited = [False] * n
    dist[source] = 0

    for _ in range(n):
        u = -1
        best = math.inf

        # extract-min by scanning array
        for i in range(n):
            if not visited[i] and dist[i] < best:
                best = dist[i]
                u = i

        if u == -1:
            break

        visited[u] = True

        # relax by scanning whole row
        for v in range(n):
            w = graph[u][v]
            if not visited[v] and w != math.inf:
                nd = dist[u] + w
                if nd < dist[v]:
                    dist[v] = nd

    return dist


def dijkstra_adjlist_heap(graph, source=0):
    """
    graph: adjacency list
           graph[u] = list of (v, weight)
    """
    n = len(graph)
    dist = [math.inf] * n
    dist[source] = 0
    pq = [(0, source)]

    while pq:
        d, u = heapq.heappop(pq)

        # skip stale entries
        if d != dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))

    return dist


# =========================================================
# 2. Graph generators
# =========================================================

def generate_random_edges(n, density, weight_range=(1, 20), directed=False, seed=None):
    """
    Returns a list of edges (u, v, w).
    density in [0,1]
    """
    if seed is not None:
        random.seed(seed)

    edges = []

    if directed:
        for u in range(n):
            for v in range(n):
                if u != v and random.random() < density:
                    w = random.randint(*weight_range)
                    edges.append((u, v, w))
    else:
        for u in range(n):
            for v in range(u + 1, n):
                if random.random() < density:
                    w = random.randint(*weight_range)
                    edges.append((u, v, w))

    return edges


def ensure_connected_undirected(n, extra_density, weight_range=(1, 20), seed=None):
    """
    Builds a connected undirected graph by:
    1. making a random spanning tree
    2. adding extra random edges with probability = extra_density
    Returns edge list.
    """
    if seed is not None:
        random.seed(seed)

    edges = []
    existing = set()

    # random spanning tree
    for v in range(1, n):
        u = random.randint(0, v - 1)
        w = random.randint(*weight_range)
        a, b = min(u, v), max(u, v)
        edges.append((a, b, w))
        existing.add((a, b))

    # extra edges
    for u in range(n):
        for v in range(u + 1, n):
            if (u, v) not in existing and random.random() < extra_density:
                w = random.randint(*weight_range)
                edges.append((u, v, w))
                existing.add((u, v))

    return edges


def edges_to_matrix(n, edges, directed=False):
    graph = [[math.inf] * n for _ in range(n)]
    for i in range(n):
        graph[i][i] = 0

    for u, v, w in edges:
        graph[u][v] = min(graph[u][v], w)
        if not directed:
            graph[v][u] = min(graph[v][u], w)

    return graph


def edges_to_adjlist(n, edges, directed=False):
    graph = [[] for _ in range(n)]

    for u, v, w in edges:
        graph[u].append((v, w))
        if not directed:
            graph[v].append((u, w))

    return graph


# =========================================================
# 3. Timing helper
# =========================================================

def time_function(func, arg, repeats=5):
    times = []
    for _ in range(repeats):
        start = time.perf_counter()
        func(arg, 0)
        end = time.perf_counter()
        times.append(end - start)
    return mean(times)


# =========================================================
# 4. Empirical experiment
# =========================================================

def run_experiment(
    sizes,
    densities,
    repeats=5,
    connected=True,
    directed=False,
    seed=42
):
    """
    Returns a list of result dictionaries.
    """
    random.seed(seed)
    results = []

    for n in sizes:
        for density in densities:
            if connected and not directed:
                edges = ensure_connected_undirected(n, density, seed=random.randint(1, 10**9))
            else:
                edges = generate_random_edges(n, density, directed=directed, seed=random.randint(1, 10**9))

            m = len(edges) if directed else 2 * len(edges)  # count both directions for undirected if you want adjacency-list edge scans

            matrix_graph = edges_to_matrix(n, edges, directed=directed)
            adjlist_graph = edges_to_adjlist(n, edges, directed=directed)

            t_matrix = time_function(dijkstra_matrix_array, matrix_graph, repeats=repeats)
            t_heap = time_function(dijkstra_adjlist_heap, adjlist_graph, repeats=repeats)

            results.append({
                "V": n,
                "E": m,
                "density": density,
                "matrix_array_time": t_matrix,
                "adjlist_heap_time": t_heap
            })

            print(
                f"V={n:4d}, density={density:.3f}, E={m:7d}, "
                f"matrix+array={t_matrix:.6f}s, adjlist+heap={t_heap:.6f}s"
            )

    return results


# =========================================================
# 5. Simple empirical growth analysis
# =========================================================

def estimate_growth_ratio(results, key):
    """
    For fixed density, compare time ratios as V doubles.
    If ratio is ~4, suggests O(V^2).
    """
    by_density = {}
    for row in results:
        by_density.setdefault(row["density"], []).append(row)

    print("\nEmpirical growth ratios")
    print("-" * 60)

    for density, rows in by_density.items():
        rows.sort(key=lambda x: x["V"])
        print(f"\nDensity = {density}")
        for i in range(1, len(rows)):
            prev = rows[i - 1]
            curr = rows[i]
            ratio_v = curr["V"] / prev["V"]
            ratio_t = curr[key] / prev[key] if prev[key] > 0 else float("inf")
            print(
                f"V: {prev['V']} -> {curr['V']} | "
                f"time ratio = {ratio_t:.3f} when V ratio = {ratio_v:.1f}"
            )


# =========================================================
# 6. Optional: fit log-log slope
# =========================================================

def loglog_slope(xs, ys):
    """
    Rough estimate of exponent p in y ~ c * x^p
    using simple least-squares on logs.
    """
    logx = [math.log(x) for x in xs]
    logy = [math.log(y) for y in ys]

    mx = sum(logx) / len(logx)
    my = sum(logy) / len(logy)

    num = sum((x - mx) * (y - my) for x, y in zip(logx, logy))
    den = sum((x - mx) ** 2 for x in logx)

    return num / den if den != 0 else float("nan")


def estimate_exponents(results):
    """
    For each density, estimate:
    - matrix+array time vs V
    - adjlist+heap time vs E
    """
    by_density = {}
    for row in results:
        by_density.setdefault(row["density"], []).append(row)

    print("\nEstimated log-log exponents")
    print("-" * 60)

    for density, rows in by_density.items():
        rows.sort(key=lambda x: x["V"])

        Vs = [r["V"] for r in rows]
        Es = [max(r["E"], 1) for r in rows]

        matrix_times = [r["matrix_array_time"] for r in rows]
        heap_times = [r["adjlist_heap_time"] for r in rows]

        p_matrix = loglog_slope(Vs, matrix_times)
        p_heap_E = loglog_slope(Es, heap_times)
        p_heap_V = loglog_slope(Vs, heap_times)

        print(
            f"Density={density}: "
            f"matrix vs V exponent ≈ {p_matrix:.3f}, "
            f"heap vs E exponent ≈ {p_heap_E:.3f}, "
            f"heap vs V exponent ≈ {p_heap_V:.3f}"
        )


# =========================================================
# 7. Main
# =========================================================

if __name__ == "__main__":
    # Use larger values if your machine is fast enough
    sizes = [50, 100, 200, 400]
    densities = [0.05, 0.2, 0.5]

    results = run_experiment(
        sizes=sizes,
        densities=densities,
        repeats=5,
        connected=True,
        directed=False,
        seed=42
    )

    # For matrix+array, expect roughly quadratic growth in V
    estimate_growth_ratio(results, "matrix_array_time")

    # For adjlist+heap, growth depends on both V and E
    estimate_growth_ratio(results, "adjlist_heap_time")

    estimate_exponents(results)