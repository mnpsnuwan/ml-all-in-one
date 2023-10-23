# Graph Generators
### Classic Graph
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
### Lattice Graph
* `grid_2d_graph(m, n[, periodic, create_using])` Returns the two-dimensional grid
graph.
* `grid_graph(dim[, periodic])` Returns the n-dimensional grid graph.
* `hexagonal_lattice_graph(m, n[, periodic, …])` Returns an m by n hexagonal lattice
graph.
* `hypercube_graph(n)` Returns the n-dimensional hypercube graph.
* `triangular_lattice_graph(m, n[, periodic, …])` Returns the 𝑚 by 𝑛 triangular lattice
graph.

---
### Small Graph
* `LCF_graph(n, shift_list, repeats[, create_using])` Return the cubic graph specified
in LCF notation.
* `bull_graph([create_using])` Returns the Bull graph.
* `chvatal_graph([create_using])` Returns the Chvátal graph.
* `cubical_graph([create_using])` Returns the 3-regular Platonic Cubical graph.
* `desargues_graph([create_using])` Return the Desargues graph.
* `diamond_graph([create_using])` Returns the Diamond graph.
* `dodecahedral_graph([create_using])` Return the Platonic Dodecahedral graph.
* `frucht_graph([create_using])` Returns the Frucht Graph.
* `heawood_graph([create_using])` Return the Heawood graph, a (3,6) cage.
* `hoffman_singleton_graph()` Return the Hoffman-Singleton Graph.
* `house_graph([create_using])` Returns the House graph (square with triangle on top).
* `house_x_graph([create_using])` Returns the House graph with a cross inside the house
square.
* `icosahedral_graph([create_using])` Returns the Platonic Icosahedral graph.
* `krackhardt_kite_graph([create_using])` Return the Krackhardt Kite Social Network.
* `moebius_kantor_graph([create_using])` Returns the Moebius-Kantor graph.
* `octahedral_graph([create_using])` Returns the Platonic Octahedral graph.
* `pappus_graph() Return the Pappus graph.
* `petersen_graph([create_using])` Returns the Petersen graph.
* `sedgewick_maze_graph([create_using])` Return a small maze with a cycle.
* `tetrahedral_graph([create_using])` Return the 3-regular Platonic Tetrahedral graph.
* `truncated_cube_graph([create_using])` Returns the skeleton of the truncated cube.
* `truncated_tetrahedron_graph([create_using])` Returns the skeleton of the truncated
Platonic tetrahedron.
* `tutte_graph([create_using])` Returns the Tutte graph.

---
### Random Graph
* `fast_gnp_random_graph(n, p[, seed, directed])` Returns a 𝐺𝑛,𝑝 random graph, also
known as an Erdős-Rényi graph or a binomial graph.
* `gnp_random_graph(n, p[, seed, directed])` Returns a 𝐺𝑛,𝑝 random graph, also known as
an Erdős-Rényi graph or a binomial graph.
* `dense_gnm_random_graph(n, m[, seed])` Returns a 𝐺𝑛,𝑚 random graph.
* `gnm_random_graph(n, m[, seed, directed])` Returns a 𝐺𝑛,𝑚 random graph.
* `erdos_renyi_graph(n, p[, seed, directed])` Returns a 𝐺𝑛,𝑝 random graph, also known
as an Erdős-Rényi graph or a binomial graph.
* `binomial_graph(n, p[, seed, directed])` Returns a 𝐺𝑛,𝑝 random graph, also known as an
Erdős-Rényi graph or a binomial graph.
* `newman_watts_strogatz_graph(n, k, p[, seed])` Returns a Newman–Watts–Strogatz
small-world graph. `watts_strogatz_graph(n, k, p[, seed])` Returns a Watts–Strogatz small-world graph.
* `connected_watts_strogatz_graph(n, k, p[, …])` Returns a connected Watts–Strogatz
small-world graph.
* `random_regular_graph(d, n[, seed])` Returns a random 𝑑 -regular graph on 𝑛 nodes.
* `barabasi_albert_graph(n, m[, seed])` Returns a random graph according to the Barabási–
Albert preferential attachment model.
* `dual_barabasi_albert_graph(n, m1, m2, p[, seed])` Returns a random graph according
to the dual Barabási–Albert preferential attachment model.
* `extended_barabasi_albert_graph(n, m, p, q[, …])` Returns an extended Barabási–
Albert model graph.
* `powerlaw_cluster_graph(n, m, p[, seed])` Holme and Kim algorithm for growing graphs
with powerlaw degree distribution and approximate average clustering.
* `random_kernel_graph(n, kernel_integral[, …])` Returns a random graph based on the
specified kernel.
* `random_lobster(n, p1, p2[, seed])` Returns a random lobster graph.
* `random_shell_graph(constructor[, seed])` Returns a random shell graph for the
constructor given.
* `random_powerlaw_tree(n[, gamma, seed, tries])` Returns a tree with a power law degree
distribution.
* `random_powerlaw_tree_sequence(n[, gamma, …])` Returns a degree sequence for a tree
with a power law distribution.
* `random_kernel_graph(n, kernel_integral[, …])` Returns a random graph based on the
specified kernel.

---
### Social Network Graph
* `karate_club_graph()` Returns Zachary’s Karate Club graph.
* `davis_southern_women_graph()` Returns Davis Southern women social network.
* `florentine_families_graph()` Returns Florentine families graph.
* `les_miserables_graph()` Returns co-appearance network of characters in the novel Less
Miserables.

---
### Community Graph
* `caveman_graph(l, k)` Returns a caveman graph of l cliques of size k.
* `connected_caveman_graph(l, k)` Returns a connected caveman graph of l cliques of size k.
* `relaxed_caveman_graph(l, k, p[, seed])` Returns a relaxed caveman graph.
* `random_partition_graph(sizes, p_in, p_out[, …])` Returns the random partition graph
with a partition of sizes.
* `planted_partition_graph(l, k, p_in, p_out[, …])` Returns the planted l-partition graph.
* `gaussian_random_partition_graph(n, s, v, …)` Generate a Gaussian random partition
graph.
* `ring_of_cliques(num_cliques, clique_size)` Defines a “ring of cliques” graph. 
* `stochastic_block_model(sizes, p[, nodelist, …])` Returns a stochastic block model
graph.
* `windmill_graph(n, k)` Generate a windmill graph.
