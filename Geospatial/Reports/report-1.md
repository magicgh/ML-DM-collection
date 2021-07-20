<font face="Roboto"> <h1> <center> Paper Report <br>Trajectory-driven Influential Billboard Placement </center> </h1> </font>

<font face="Roboto">

## The Table of Notations

$$\begin{array}{ll}
\hline \text { Symbol } & \text { Description } \\
\hline t(\mathcal{T}) & \text { A trajectory (database) } \\
U & \text { A set of billboards that a user wants to advertise } \\
L & \text { the total budget of a user } \\
I(S) & \text { The influence of a selected billboard set } S \\
P & \text { A billboard partition } \\
\vartheta_{i j} & \text { The overlap ratio between clusters } \\
\Delta(b \mid S) & \text { The marginal influence of } b \text { to } S \\
\theta & \text { The threshold for a } \theta \text { -partition } \\
\mathbb{I} & \text { The DP influence matrix: } I[i][l] \text { is the maximum influ- } \\
& \text { ence of the billboards selected from the first } i \text { clusters } \\
& \text { within budget } l(i \leq m \text { and } l \leq L) \\
\xi & \text { The local influence matrix: } \xi[i][l] \text { is the influence re- } \\
& \text { turned by EnumSel }\left(C_{i}, l\right) \text {, i.e., the maximum influence } \\
& \text { of billboards selected from cluster } C_{i} \text { within budget } l \\
\hline
\end{array}$$

<h2> Questions and Answers </h2>

<h3> 1. Motivation of the work.  </h3>
Outdoor advertising has a global marketing with a huge profit and a great potential. Compared with other kinds of advertising mediums such as TV and mobile, outdoor advertising delivers a high return on investment.  
As a highest used medium for outdoor advertising, billboards are slightly expensive for advertisers. As a result, the cost of renting a billboard is proportional to its influence and it is extremely important to avoid expensive computation while achieving the same competitive influence value for advertisers.  
Besides, in other scenarios like store site selection problem which needs to consider the influence gain with relation to the cost of the store under a budget constraint, a strategy that is similar to the billboard placement problem is required.

<h3> 2. Studies related to this work, and how this work differs from each of them. </h3>

> Note: you might need to briefly read the literature mentioned in the *Related Work* section of this paper.

The primary goal of this paper is to maximize the influence of billboards on users within a budget. In the second section, some related work proposed by authors are shown as follows:

<h4> Maximized Bichromatic Reverse k Nearest Neighbor (MaxBRkNN) </h4>

The MaxBRkNN queries aim to find the optimal location to establish a new store such that it is a kNN of the maximum number of users based on the spatial distance between the store and users' location. Recently, Wang et al. proposed a methods to find the optimal bus route in term of maximum bus capacity by considering the audiences' source-destination trajectory data. To solve this problem, they first developed an index to handle dynamic trajectory updates and then introduced a filter refinement framework for processing queries using the proposed indexes. Next, they showed how to use RkNNT (*Reverse $k$ Nearest Neighbor Search over Trajectory*) to solve the optimal route planning problem MaxRkNNT (MinRkNNT), which was to search for the optimal route from a start location to an end location that could attract the maximum (or minimum) number of passengers based on a pre-defined travel distance threshold.  

The TIP (Trajectory-driven Influential Billboard Placement) problem is different from MaxBRkNN in two aspects: First, MaxBRkNN assumes that each user in associated with a fixed location. On the contrary, the audience can meet more than one billboard while moving along a trajectory in the TIP model, which indicates that the TIP problem is more complicate in that location information is more dynamic. Second, billboards at different locations may have different costs, making the optimization problem more intricate, however, MaxBRkNN assumes that the costs of candidates store locations are the same.
  
#### Influence Maximization and its variations

The original Influence Maximization (IM) problem is to find a size-$k$ subset of all nodes in a social network that could maximize the spread of influence. There are several models to capture the influence spread, such as Independent Cascade and Linear Threshold and this problem has been proven to be NP-hard. Some new models are also introduced to solve IM under complex scenarios. For example, Li et al. find the seed users in a location-ware social network such that the seeds have the highest influence upon a regional group of audiences. Guo et al. select top-$k$ influential trajectories based on users' check-in locations.

In addition, there are some discrepancies between TIP problems and IM Problems. The first point is that the cardinality of the optimal set in IM problems is often pre-determined owing that the cost of each candidate is equal to each other. However, the costs of billboards at different locations differ from one to anther in the TIP problem, thus the theoretical guarantee of the naive greedy algorithm is poor. Next, since IM problems adopt a different influence model to the TIP problem, they mainly focus on how to efficiently and effectively estimate the influence propagation, while TIP aims to optimize the profit of $k$-combination by leveraging the geographical properties of billboards and trajectories.
  
#### Maximum $k$-coverage problem

This problem, which focuses to select at most $k$ sets from $S$ to maximize the number of elements covered given a universe of elements $U$ and a collection $S$ of subsets from $U$, has been shown to be NP-hard. Its derivation, the budgeted maximum coverage (BMC) problem further considers a cost for each subset and tries to maximize the coverage with a budget constraint. It has been shown that the naive greedy algorithm no longer produces solutions with an approximation guarantee for BMC. To solve this issue, Khuller et al. devise a variant of the greedy-based algorithm for BMC. However, the performance of this algorithm in solving TLP problem does not scale well in practice.

### 3. Problem Definition, and especially illustrate why we define it in this way? Is there any other alternative way to define the problem? Why we want to capture the influence overlap, and how we capture it? Any other scenarios that could not be covered by the current definition?

#### Problem Definition

In a trajectory database $\mathcal{T}$, each trajectory $t$ is in the form of a sequence of locations $t = \{p_1, p_2, \ldots, p_{|t|}\}$; a trajectory location $p_i$ is represented by $\{\mathrm{lat}, \mathrm{lng}\}$, where $\mathrm{lat}$ and $\mathrm{lng}$ are the latitude and longitude of the location, respectively. A billboard $b$ is in the form of a tuple $\{\mathrm{loc}, \mathrm{w}\}$, where $\mathrm{loc}$ and $\mathrm{w}$ denote $b$'s location and leasing cost respectively. Without loss of generality, it is assumed that a billboard carries either zero or one advertisement at any time.

The TIP Problem can be defined as follows:
> Given a trajectory database $\mathcal{T}$, a set of billboards $U$, and a cost budget $L$, find a subset of billboard $S$, which maximizes the expected number of influenced trajectories such that the total cost of billboards in $S$ is less than $L$.

Notice that the definition of problem above is similar to the knapsack problem, thus defining in this way is more perspicuous and acceptable for new learners to comprehend the TIP problem.

Specifically, there is alternative way to define the TIP problem. In the process of proving that the TIP problem is NP-hard, we reduce the Set Cover problem to it. It is known that the Set Cover problem is NP-complete, also NP-hard. In this case, we can define the TIP problem in respect of the Set Cover problem:
> Given a collection of subsets $S_1, S_2, \ldots, S_m$ of a universe of elements $U'$, we wish to know whether there exist $k$ of the subsets whose union is equal to $U'$.

#### Influence Overlap

Influence overlap of the selected billboards is one of the critical real-world features to be taken in consideration in the TIP problem. If the selected billboards have a large overlap in their influenced trajectories, advertisers may waste money for repeatedly influencing the audiences who have already seen their ads. Hence it is very important to capture the influence overlap and reduce it.

In this paper, authors introduce the concept of *Overlap Ratio* to quantify the influence overlap, and the definition of it is stated below:
> For two clusters $C_i$ and $C_j$, the ratio of the overlap between $C_i$ and $C_j$ relative to $C_i$, denoted by $\vartheta_{ij}$, is defined as
>$$\vartheta_{ij} = \argmax_{\forall S_i \subseteq C_i}\frac{\Omega(S_i|C_i)}{I(S_i)}$$
>where $S_i$ is a subset of $C_i$, i.e., $I(S_i) + I(C_j) - I(S_i \cup C_j)$.

In addition, there are two other ways to describe the influence overlap:

* Measuring the volume of the clusters' overlap directly, i.e., $\vartheta_{ij} = \Omega(C_i, C_j)/I(U)$.

* Measuring the overlap ratio between billboards in one cluster and those that are not in this cluster, which can be described by the following equation:
$$\vartheta_{i} = \argmax_{b_i \in C_i} \frac{I\left(\left\{b_{i}\right\}\right)+I\left(\overline{C_{i}}\right)-I\left(\overline{C_{i}} \cup\left\{b_{i}\right\}\right)}{I\left(\left\{b_{i}\right\}\right)}$$

However, this kind of measurement may cause that $U$ cannot be divided into a set of small yet balanced clusters due to its rigid constraint.

### 4. Solution part: please try to write down how the following solutions, i.e., NaiveGreedy, GreedySel, PartitionSel. Ideally, for each solution, please write down the pseudocode (using your own understanding, rather than copy and paste from the paper) and an example to explain how it works. Last, what kind of index/data structure do we use to accelerate the computation?

#### NaiveGreedy

NaiveGreedy is a straightforward method to select the billboard $b$ with the largest marginal influence, i.e., $\delta(b|S)/w(\{b\})$, to a candidate solution set $S$, until the budget is exhausted.
The pseudocode based on Rust is as follows:

```rust
fn naive_greedy(U: &mut Vec<Billboard>, L:i32) -> Vec<Billboard> {
    let mut S = vec![];
    let mut sum: i32 = 0;
    U.sort_by(|a, b| b.marginal_influence.cmp(&a.marginal_influence))
    for b in U.iter() {
        if sum + b.cost > L {
            break;
        }
        S.push(b);
        sum += b.cost;
    }
    S
}
```

For example, given two billboards $b_1$ with influence $1$ and $b_2$ with influence $x$. Let $w(b_1) = 1$, $w(b_2) = x + 1$ and
$L = x + 1$. The solution picked by the greedy heuristic contains the set $b_1$ and the influence is $1$.

#### GreedySel

Notice that the method proposed above is a greedy heuristic algorithm, which means it cannot find a optimal solution in many cases. To solve this issue, the best single billboard solution should be also considered. The pseudocode of GreedySel based on Rust is as follows:

```rust
fn greedy_sel(U: &mut Vec<Billboard>, L:i32) -> Vec<Billboard> {
    let mut S = vec![];
    let mut total_cost: i32 = 0;
    let mut total_influence: i32 = 0;
    U.sort_by(|a, b| b.marginal_influence.cmp(&a.marginal_influence))
    for b in U.iter() {
        if total_cost + b.cost > L {
            break;
        }
        S.push(b);
        total_cost += b.cost;
        total_influence += b.influence;
    }
    let mut single_solution: option<Billboard> = None;
    for b in U.iter() {
        if b.influence > single_solution.influence && b.cost <= L {
            single_solution = Some(b);
        }
    }
    if single_solution.unwrap().influence > total_influence {
        return vec![single_solution.unwrap()];
    }
    else {
        return S;
    }
}
```

For example, given two billboards $b_1$ with influence $1$ and $b_2$ with influence $x$. Let $w(b_1) = 1$, $w(b_2) = x + 1$ and
$L = x + 1$. The solution picked by the GreedySel contains the set $b_2$ and the influence is $x$. In this case, $b_2$ is the best single billboard solution which is neglected in the greedy heuristic.

Arrays are used in both greedy algorithms to store the billboard information.

#### PartitionSel

Literally, PartitionSel, or PartSel in short, is a method that partition $U$ into a set of small clusters, then compute the locally influential billboards for each cluster, and finally merge the local billboards to generate the globally influential billboards of $U$. In detail, there are two phases in the PartSel:

* First, partition $U$ into $m$ clusters, namely $C_1, C_2, ..., C_m$, where different clusters have little influence overlap to the same trajectories. To select the locally influential billboards set $S[i][l_i]$ from cluster $C_i$ within budget $l_i$, where $S[i][l_i]$ has the maximum influence $\xi[i][l_i]$$, \mathrm{EnumSel(C_i, l_i)}$ should be executed in this phase.

* Second, assign a budget to each cluster $C_i$ and take the union of $S[i][l_i]$ as the globally influential billboards set, where $\sum \limits_{i=1}^m l_i \leq L$. Formally, the goal of PartSel is to maximize the following objective function by dynamic programming:

$$\begin{array}{c}
\sum_{i=1}^{m} \xi[i]\left[l_{i}\right] \\
\text { s.t. } \sum \limits_{i=1}^m l_i \leq L
\end{array}$$

The pseudocode of PartSel based on Rust is as follows:

```rust
fn part_sel(P: &mut Vec<Billboard>, L:i32) -> Vec<Billboard> {
    let mut S = vec![];
    let mut I = [[0; L + 1]; P.len()];
    let mut V = [[0; L + 1]; P.len()];
    Init(&I, &V);
    for i in 0..P.len() {
        for j in 0..L + 1{
            V[i][j] = enum_sel(Cluster[i], j);
            let mut C: option<BillboardSet> = None;
            for k in 0..j + 1 {
                if I[i][j] < I[i - 1][j - k] + V[i][k] {
                    I[i][j] = I[i - 1][j - k] + V[i][k];
                    C = Some(candidate_billboard(Cluster[i], k));
                }
            }
            for x in C.unwrap().iter() {
                S.push(x);
            }
        }
    }
    S
}
```

For instance, given a partition of $U$ as $P=\{C_1, C_2, C_3\}$, where $b_i \in U, C_1 = \{b_1, b_2, b_3\}, C_2 = \{b_4, b_5, b_6\}, C_3 = \{b_7, b_8, b_9\}$. Suppose that $L = 4$, and we intend to maximize the global influence within the budget limit. According to the algorithm, $\xi[i][j]$ have already been computed by invoking $\mathrm{enum\_sel}(\textnormal{Cluster[i], j})$. As a result, we only show that how to compute $I[i][j]$ in this example. Intuitively, $I[0][j] = 0 \space (0 \leq j \leq L), I[1][j] = \xi[1][j] \space (0\leq j \leq L)$. In light of other cases, we can derive that
$$\begin{aligned}
    I[2][1] &= \max\{I[1][0] + \xi[2][1], I[1][1] + \xi[2][0] \} \\
    I[2][2] &= \max\{I[1][0] + \xi[2][2], I[1][1] + \xi[2][1], I[1][2] + \xi[2][0] \} \\
    I[2][3] &= \max\{I[1][0] + \xi[2][3], I[1][1] + \xi[2][2], I[1][2] + \xi[2][1], I[1][3] + \xi[2][0] \} \\
    I[2][4] &= \max\{I[1][0] + \xi[2][4], I[1][1] + \xi[2][3], I[1][2] + \xi[2][2], I[1][3] + \xi[2][1], I[1][4] + \xi[2][0] \} \\
    I[3][1] &= \max\{I[2][0] + \xi[3][1], I[2][1] + \xi[3][0] \} \\
    I[3][2] &= \max\{I[2][0] + \xi[3][2], I[2][1] + \xi[3][1], I[2][2] + \xi[3][0] \} \\
    I[3][3] &= \max\{I[2][0] + \xi[3][3], I[2][1] + \xi[3][2], I[2][2] + \xi[3][1], I[2][3] + \xi[3][0] \} \\
    I[3][4] &= \max\{I[2][0] + \xi[3][4], I[2][1] + \xi[3][3], I[2][2] + \xi[3][2], I[2][3] + \xi[3][1], I[2][4] + \xi[3][0] \} \\
\end{aligned}$$
In each equation above, we also need to find the sets of selected billboards corresponding to the influence value $\xi[i][j]$ and $I[i][j]$. For simplicity, let $Set(\cdot)$ be the selected billboards in respect to the influence value. In terms of maximal items in the equations, the billboards with a largest influence value can be calculated by the union operation of two sets. For example, if $\displaystyle \bar{k} = \argmax_{ 0 \leq k \leq j} \{I[i-1][j - k] + \xi[i][k]\}$, then $Set(I[i][j]) = Set(I[i-1][j - \bar{k}]) + Set(\xi[i][\bar{k}])$.

In PartitionSel, the idea of dynamic programming is used to accelerate the computation, and computing local influence and global influence is another small trick to speed up the computation efficiency compared with $\mathrm{EnumSel}$.

<h3> 5. Experiment: you should include the experiment setup, dataset, setup of parameters, and illustrate each experiment done in the paper and the purpose of doing so. </h3>

#### Experiment Setup

* Datasets
  * Billboard data of LA and NYC is crawled from LAMAR.
  * Trajectory data is obtained from two types of real datasets: the TLC trip record dataset for NYC and the Foursquare check-in dataset for LA. Most trajectories are generated using Google Maps API.

* Performance Measurement  
  Performance of all methods is evaluated by the runtime and the influence value of the selected billboards. Each experiment is repeated 10 times, and the average performance is reported.

* Billboard Costs  
  Authors generate the cost of a billboard $b$ by designing a function proportional to the number of trajectories influenced by $b$:
  $$w(b) = [\beta \cdot I(b)/100] \times 1000$$
  where $\beta$ is a factor chosen from $0.8$ to $1.2$ randomly to simulate various cost-benefit ratio.
* Parameter
$$
\begin{array}{|c|c|}
\hline \text { Parameter } & \text { Values } \\
\hline L & 100 \mathrm{k}, \mathbf{1 5 0 k}, \ldots 300 \mathrm{k} \\
\hline|\mathcal{T}| \text { (NYC) } & 40 \mathrm{k}, \ldots, \mathbf{1 2 0 k} \ldots, 4 \mathrm{~m} \\
\hline|\mathcal{T}| \text { (LA) } & 40 \mathrm{k}, 80 \mathrm{k}, \mathbf{1 2 0 k}, 160 \mathrm{k}, 200 \mathrm{k} \\
\hline|U| \text { (NYC) } & 0.5 \mathrm{k}, 1 \mathrm{k}, 1.46 \mathrm{k},(2 \mathbf{k} \ldots 10 \mathrm{k} \text { by replication) } \\
\hline|U| \text { (LA) } & 1 \mathrm{k}, 2 \mathbf{k}, 3 \mathrm{k},(4 \mathrm{k} \ldots 10 \mathrm{k} \text { by replication) } \\
\hline \theta & 0,0.1,0.2,0.3,0.4 \\
\hline \lambda & 25 \mathrm{~m}, \mathbf{5 0 m}, 75 \mathrm{~m}, 100 \mathrm{~m} \\
\hline
\end{array}
$$
The default one is highlighted in bold.
* Development Environment  
  All codes are implemented in Java, and experiments are conducted on a server with 2.3 GHz Intel Xeon 24 Core CPU and 256GB memory running Debian/4.0 OS.

#### Experiments

* Choice of θ-partition
  * Purpose: A good choice of $\theta$ strikes a balance between the efficiency and effectiveness of PartSel and LazyProbe.

  * Method: Varying $\theta$ from $0$ to $0.4$, and record the number of clusters as input of PartSel and LazyProbe methods, the percentage of the largest cluster size over $U$ (i.e., $\frac{C_m}{U}$), the runtime and the influence value of PartSel and LazyProbe.

  * Observations:  
    1. With the increase of $\theta$, the influence quality decreases and the efficiency is improved, because for a larger $\theta$, the tolerated influence overlap is larger and there are many more clusters with larger overlaps.
    2. When $\theta$ is $0.1$ and $0.2$, PartSel and LazyProbe achieve the best influence, while the efficiency of $0.2$ is not much worse than that of $θ=0.3$.
    3. In one extreme case that $θ=0.4$, although the generated clusters are dispersed and small, it results in high overlaps among clusters, so the influence value drops and becomes worse than GreedySel, and meanwhile the efficiency of PartSel (LazyProbe) only improves by around 12 (6) times as compared to that of $θ=0.2$ on the NYC (LA) dataset.

    4. All other methods beat the TrafficVol baseline by 45% in term of the influence value of selected billboards.

<h3> 6. Bonus part: try to understand the LazyProbe method and write down your understanding of why LazyProbe can further improve the efficiency of PartSel. </h3>

LazyProbe is proposed to reduce the number of calls to $\mathrm{EnumSel(C_i, l)}$ and its theoretical equivalence on approximation ratio is identical with the EnumSel.

In the PartSel, the most time consuming part is to calculate the local influence of clusters using $\mathrm{EnumSel(C_i, l)}$. To reduce the executive time and enhance the the efficiency of algorithm, we can estimate an upper bound of $\xi[i][q]$, denoted as $\xi^{\uparrow}[i][q]$.

Heuristically, $\xi^{\uparrow}[i][q]$ can be computed by GreedySel. In other words,
$$\xi^{\uparrow}[i][q] = I(S') + \frac{I(S' \cup \{b_{k+1}\})-I(S')}{L-w(S')}$$
where $S' = \{b_1, b_2, \ldots, b_k\}$ represents the selected billboards whose cost is less than $L$ and $b_{k+1}$ is a candidate billboard which would cause the total cost greater than $L$ if it is selected. In this way, the upper bound of $\xi[i][q]$ can be estimated by computing the slope of I-w curve.

Aside from that, $I[i][l]$ can also be computed by estimating its lower bound, represented as $I^{\downarrow}[i][l]$. Initially, $I[i][l]$ is set to $I[i-1][l]$ and the value of it can be updated through the dynamic programming algorithm in PartSel.

The strategy in dynamic programming is changed in LazyProbe, on account that we have a good estimation of $\xi^{\uparrow}[i][q]$, so that we only update $I^{\downarrow}[i][l]$ when $I^{\downarrow}[i][l] \leq I[i-1][l-q] + \xi^{\uparrow}[i][q]$. What's more, we do not invoke $\mathrm{EnumSel(C_i, l)}$ every time so long as $\xi[i][q]$ has been computed.

In conclusion, LazyProbe can further improve the efficiency of PartSel saying that it reduce the number of calls to EnumSel by estimating $I^{\downarrow}[i][l]$ and $\xi^{\uparrow}[i][q]$.
</font>
