# Graph Generators
### Classic
* `balanced_tree(r, h[, create_using])` Returns the perfectly balanced r-ary tree of height h.
* `barbell_graph(m1, m2[, create_using])` Returns the Barbell Graph: two complete graphs
connected by a path.
* `complete_graph(n[, create_using])` Return the complete graph K_n with n nodes.
* `complete_multipartite_graph(*subset_sizes)` Returns the complete multipartite graph
with the specified subset sizes.
* `circular_ladder_graph(n[, create_using])` Returns the circular ladder graph 𝐶𝐿𝑛 of
length n.
* `circulant_graph(n, offsets[, create_using])` Generates the circulant graph
𝐶𝑖𝑛(𝑥1,𝑥2,...,𝑥𝑚) with 𝑛 vertices.
* `cycle_graph(n[, create_using])` Returns the cycle graph 𝐶𝑛 of cyclically connected nodes.
* `dorogovtsev_goltsev_mendes_graph(n[, …])` Returns the hierarchically constructed
Dorogovtsev-Goltsev-Mendes graph.
* `empty_graph([n, create_using, default])` Returns the empty graph with n nodes and zero
edges.
* `full_rary_tree(r, n[, create_using])` Creates a full r-ary tree of n vertices.
* `ladder_graph(n[, create_using])` Returns the Ladder graph of length n.
* `lollipop_graph(m, n[, create_using])` Returns the Lollipop Graph; K_m connected to P_n.
* `null_graph([create_using])` Returns the Null graph with no nodes or edges.
* `path_graph(n[, create_using])` Returns the Path graph P_n of linearly connected nodes.
* `star_graph(n[, create_using])` Return the star graph
* `trivial_graph([create_using])` Return the Trivial graph with one node (with label 0) and no
edges.
* `turan_graph(n, r) Return the Turan Graph
* `wheel_graph(n[, create_using])` Return the wheel graph

---
### Lattice
* `grid_2d_graph(m, n[, periodic, create_using])` Returns the two-dimensional grid
graph.
* `grid_graph(dim[, periodic])` Returns the n-dimensional grid graph.
* `hexagonal_lattice_graph(m, n[, periodic, …])` Returns an m by n hexagonal lattice
graph.
* `hypercube_graph(n)` Returns the n-dimensional hypercube graph.
* `triangular_lattice_graph(m, n[, periodic, …])` Returns the 𝑚 by 𝑛 triangular lattice
graph.
