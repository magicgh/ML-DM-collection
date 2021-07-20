 <font face="Roboto"> <h1> <center> Paper Report<br> Optimizing Impression Counts for
Outdoor Advertising </center> </h1> </font>

<font face="Roboto">

## The Table of Notations

$$
\begin{array}{|l|l|}
\hline \text { Symbol } & \text { Description } \\
\hline p(S, t)\left(p^{\uparrow}(S, t)\right) & \text { The (upper bound) influence of } S \text { to } t \\
\hline I(S)\left(I^{\uparrow}(S)\right) & \text { The (upper bound) influence of } S \text { to } \mathcal{T} \\
\hline \Delta\left(S_{2} \mid S_{1}\right) & \text { The marginal influence of adding } S_{2} \text { into } S_{1} \\
\hline
\end{array}
$$

## Questions and Answers

<h3> 1. Studies related to this work, and how this work differs from them. </h3>

> Note: you might need to briefly read the literature mentioned in the *Related Work* section of this paper.

The main differences between existing works and ICOA are summarized as follows.
$$
\begin{array}{|c|c|c|c|}
\hline & \text { ICOA } & \text { TIP } & \text { Site Selection } \\
\hline \text { Audience } & \text { Moving trajectory } & \text { Moving trajectory } & \text { Fixed location } \\
\hline \text { Influence } & \text { Logistic } & \text { One-time impression } & \text { N.A. } \\
\hline|\mathrm{S}| & \text { Budget Constrained } & \text { Budget Constrained } & \text { Predefined } k \text { -size } \\
\hline
\end{array}
$$

#### Trajectory-driven Influential Billboard placement (TIP)

TIP studies billboard placement to achieve the best advertising outcome. The core difference lies in the influence model. In particular, TIP assumes that a user can be influenced so long as one billboard is close enough to the trajectory the user travels along. Under such an influence model, when multiple billboards are close to a trajectory, the marginal influence is reduced to capture the property of diminishing returns. Therefore, TIP focuses on identifying and reducing the overlap of the influence among different billboards to the same trajectories.

Impression Counts for Outdoor Advertising (ICOA) is built upon a logistic influence model which has been widely adopted in consumer behavior studies. To maximize the influence to users, authors need to control the overlap to some extent by impressing the same users several times.

#### Site Selection, and Location-aware IM (LIM)

The LIM problem is extended from Influence Maximization (IM) problem, which aims to select a size-$k$ subset from a given social network. The difference is that LIM only measures the spread of influence on users who are located in the given search region. Although IM/LIM and ICOA share the same ultimate goal, which is to maximize influence, they are different in two aspects. First, influence models of IM/LIM are submodular, whereas the logistic model is not. This implies that the simple greedy approach is not suitable for ICOA. Second, in the IM problem, the influence can be spread from a user to others.

<h3> 2. Problem Definition: especially illustrate any earlier evidence that are used to support the way authors define the influence here? Is there any other alternative way to define the problem? How do authors measure the influence? Any other scenarios that could not be covered by the current definition? </h3>

#### Preliminary

A trajectory database is denoted as $\mathcal{T} = {t_1, t_2, \ldots, t_{|\mathcal{T}|} }$, where each trajectory $t = {p_1, p_2, \ldots, p_{|t |} }$ is a set of points generated from the trajectory of a user. Point $p$ consists of the latitude $lat$ and longitude $lng$. Given a billboard database $\mathcal{U} = {o_1, o_2, \ldots, o_{|\mathcal{U}|} }$, each billboard o is a tuple $\{loc,w\}$, where $loc$ is also a coordinate and $w$ is the cost of billboard $o$.

Authors assume there are only two states of whether a user meets a billboard. When the user meets a billboard, authors say this billboard impresses the user; otherwise, no impression is delivered. Therefore, authors use the Bernoulli random variable $I (o, t )$ denoting the states whether $o$ impresses $t$ , where $I (o, t ) = 1$ denotes that $o$ delivers an impression to $t$, otherwise $I (o, t ) = 0$. Specifically, Authors define that $o$ impresses $t$ , denoted as $I (o, t ) = 1$, if $∃t .p_i$ , such that $dist (t .p_i , o.loc) ≤ λ$, where $dist (·)$ computes the Euclidean distance between $p_i$ and $o.loc$, $λ$ is a given distance threshold.

Authors use the following equation to compute the effective influence of an ad placed at a billboard set $S$ which can impress a trajectory $t$:
$$
p(S, t)=\left\{\begin{array}{ll}
\frac{1}{1+\exp \left\{\alpha-\beta \cdot \Sigma_{o_{l} \in S} I\left(o_{i}, t\right)\right\}} & \text { if } \exists o_{i} \in S I\left(o_{i}, t\right)=1 \\
0 & \text { otherwise }
\end{array}\right.
$$
where $α$ and $β$ are the parameters that control $t$ ’s turning point for being influenced.

Next, authors define the influence of $S$ to a trajectory database $T$ as follows:
$$
I(S)=\sum_{t \in \mathcal{T}} p(S, t)
$$

#### Problem Definition

The ICOA problem can be defined as:

> Given a billboard database $\mathcal{U}$, a trajectory database $\mathcal{T}$, a budget constraint $B$ and the influence model $I (S)$, the ICOA problem is to find a subset $S ⊆ \mathcal{U}$ that maximizes the overall influence of $S$ such that the total cost of S does not exceed $B$. Formally,
> $$
\hat{S}=\underset{\cos t(S) \leq B}{\operatorname{argmax}} I(S)$$

The ICOA problem can also be defined as the Set Cover problem because it is NP-hard to approximate within any constant factor.

Due to the non-submodularity of ICOA, a greedy-based heuristic method cannot guarantee any constant approximation ratio.

<h3> 3. Solution part: please try to write down the initial solution proposed to solve this problem. What is the drawback of this solution? Given the drawbacks, what other techniques are proposed to optimize the performance of this initial solution, and intuitively describe how each optimization technique is going to address the drawbacks you found earlier? (using your own understanding, rather than copy and paste from the paper). Ideally, you can give some examples to explain the intuitive idea behind the techniques but it is not mandatory. </h3>

#### Branch-and-Bound

First, this algorithm initialize the global upper bound $U_G$ and global lower bound $L_G$, and a max heap $H$ with each entry denoted as $(S, \bar{S}, U )$, where $S$ is the set of billboards that have been selected as a feasible set, $\bar{S}$ is the set of billboards that have not been considered yet, and $U$ is the upper bound influence of the corresponding search space. $H$ is ordered by the upper bound value of each $S$. For each entry, as long as it matches the budget constraint, it will generate two new branches ($S^a$ and $S^b$) based on $S$ respectively. $S^a$ represents a feasible set where a billboard $o \in \bar{S}$ can be further added into $S$, and $S^b$ represents a feasible set excluding $o$.

Based on $S^a$ or $S^b$ and the corresponding $\bar{S}$, $\textnormal{ComputeBound}(·)$ will return a triple, i.e., ($S^c , L^a, U^a$) or ($S^c, L^b, U^b$), where $S^c$ is a candidate solution set returned by $\textnormal{ComputeBound}(·)$. $L^a$ and $U^a$ are the lower-bound influence and upper bound influence of $S^c$ respectively. If $L^a > L_G$, which means $S^c$ is better than the current best feasible solution $\hat{S}$, then $\hat{S}$ will be replaced by $S^c$ , and the global $L_G$ is updated. If $U^a > L_G$, it is possible that $S^a$ is a subset of the optimal solution. Therefore, $(S^a, \bar{S}, U^a)$ will be pushed into $H$. Authors repeat the search loop for all branches until $L_G ≥ U_G$.

#### ComputeBound

To estimate the upper bound of a branch w.r.t. a feasible set $S^{a}$, authors devise a submodular function (i.e., $p^{\uparrow}(S, t)$ and $\left.S=S^{a} \cup S^{*}\right)$ which tightly upper bounds the non-submoular influence function $p(S, t)$. Let $x(S)$ denote the number of effective impressions to $t$ obtained by placing ads in billboard set $S$ (i.e., $\left.x(S)=\Sigma_{o_{i} \in S} I\left(o_{i}, t\right)\right)$ and $f(x(S))=1 /(1+\exp \{\alpha-\beta \cdot x(S)\})=p(S, t)$. Authors draw a tangent
line $l(x)$ to upper bound $f(x) . l(x)$ intersects $f(x)$ at two points:
$\left(x\left(S^{a}\right), f\left(x\left(S^{a}\right)\right)\right)$ and $\left(x_{t}^{S^{a}}, f\left(x_{t}^{S^{a}}\right)\right)$ where the latter denotes the tangential point. Formally, authors define the upper bound function $p^{\uparrow}(S, t)$ for $S=S^{a} \cup S^{*}$ as follows  
If $l(x)$ exists:
$$
p^{\uparrow}(S, t)=\left\{\begin{array}{ll}
l(x) & \text { if } x\left(S^{a}\right) \leq x \leq x_{t}^{S^{a}} \\
f(x) & \text { if } x_{t}^{S^{a}}<x
\end{array}\right.
$$
Otherwise:
$$
p^{\uparrow}(S, t)=f(x)
$$
It is easy to see that $I^{\uparrow}(S) \geq I(S)$ as $p^{\uparrow}(S, t) \geq p(S, t)$ for all $S=$ $S^{a} \cup S^{*}$. Furthermore, $I^{\uparrow}(S)$ is submodular because it is a sum of submodular functions. To ease our presentation, authors define the marginal influence $I^{\uparrow}(\cdot)$ of adding $S_{2}$ into $S_{1}$ as below:
$$\Delta^{\uparrow}\left(S_{2} \mid S_{1}\right)=I^{\uparrow}\left(S_{1} \cup S_{2}\right)-I^{\uparrow}\left(S_{1}\right)$$

For example, in a search tree, each node is an entry $(S, \bar{S},U )$. The table shows the values of $S^c, U_G$ and $L_U$ for each search step. Let $B = 50, o_1.w = 10, o_2.w = 30, o_3.w = 30, o_4.w = 20$. The authors first initialize $H$ with an entry $(\{\}, {o_1, o_2, o_3, o_4}, ∞)$ as the root node of the searching tree. Next, at step 1, authors pop this entry, and invoke the algorithm to generate two branches based on this entry, and push them into $H$. Since $U^b > U^a > L_G$ and $L^b > L^a > L_G$, and they update $\hat{S}$ with $S^c = {o_3, o_4}$ and set $L_G = L^b = 0.6571$. Similarly, at step 4, the branch $S^a$ is pushed into $H$ since $U^a > L_G$. Note that, the branch $S^b$ will be pruned since $U^b < L_G$. For now, all branches based on the root node have been generated, and those with $U > L_G$ have been pushed into $H$. Subsequently, the branch with $S^b = \{\}$ and $\bar{S} = {o_2, o_3, o_4}$ is popped because it has the highest upper bound in $H$. $U_G$ will be replaced by $U$ of this branch, which means $U_G = U = 0.7657$. Six branches are generated with or without $o_2, o_3$ and $o_4$ respectively.

The branches which $U > L_G$ will be added into $H$, such as the branch $S^b$ of step 5 and the branch $S^a$ of step 7. When $L_G$ is larger than $U_G$, it means that, in the rest of branches in $H$, the one with the highest $U$ is worse than the optimal solution. The algorithm thus terminates. The upper bounding techniques lead to a constant approximation ratio for the solution returned by the branch-and-bound framework.

#### Branch-and-bound with $θ$-termination

In this algorithm, authors utilize a parameter $θ$ to control the termination condition – instead of using $L_G < U_G$, authors use $L_G < θU_G$ as the termination condition, where $θ ∈ (0, 1]$. When $L$ and $U$ are close enough, the search process terminates. It can be easily shown that the early termination technique achieves $\frac{\theta}{2} (1 − 1/e)$ approximation ratio.

<h3>4. Experiment: you should include the experiment setup, dataset, setup of key parameters, and illustrate some major experiments conducted. Last, summarize the key observation from the experiment results. </h3>

#### Experimental Setup

* Datasets  
  The real-world billboard datasets for the two largest cities in the US (NYC and LA) are crawled from LAMAR. The real-world trajectory datasets are obtained as follows. For NYC, five hundred thousand taxi trips are collected from TLC trip record. For LA, as there is no public taxi record, the Foursquare check-in data is collected to generate the trajectories using Google Maps API by randomly selecting the pick-up and drop-out locations from the check-ins.
* Performance Measurement  
  For each method authors evaluate the runtime and the influence value of the selected billboards. Each experiment is repeated ten times, and the average result is reported.
* Experiment Environment  
  All codes are implemented in Java. Experiments are conducted on a laptop with Intel Core i7-8550U CPU and 16GB memory running Windows 10.
* Parameter Settings  
Notice that the default one is highlighted in bold. $α$ and $β$ are the parameters in the logistic function that control $t$ ’s turning point for influence.
$$
\begin{array}{|c|c|}
\hline \text { Parameter } & \text { Values } \\
\hline B & 100 \mathrm{k}, 200 \mathrm{k}, 300 \mathrm{k}, 400 \mathrm{k}, 500 \mathrm{k} \\
\hline|\mathcal{T}| \text { (NYC) } & \text { 100k, 200k, } \mathbf{3 0 0 k}, 400 \mathrm{k}, 500 \mathrm{k},(1 \mathrm{~m}, \ldots, 5 \mathrm{~m}) \\
\hline|\mathcal{T}| \text { (LA) } & 50 \mathrm{k}, 100 \mathrm{k}, \mathbf{1 5 0 k}, 200 \mathrm{k}, 250 \mathrm{k} \\
\hline \beta / \alpha & 3 / 7,3 / 8,3 / 9,3 / 10,3 / 11 \\
\hline \epsilon & 10^{-4}, 10^{-3}, 10^{-2}, 10^{-1}, 1 \\
\hline \theta & 0.86,0.88, \mathbf{0 . 9 0}, 0.92,0.94 \\
\hline \lambda & 25 \mathrm{~m}, \mathbf{5 0 m}, 75 \mathrm{~m}, 100 \mathrm{~m} \\
\hline
\end{array}
$$

* Metrics & Methods for Comparison
  In this part, the efficiency, effectiveness and scalability of the methods should be evaluated. Despite the way of optimizing outdoor ad influence by considering the impression counts over moving trajectories, the following baselines also need to be compared:
  * Greedy: A basic greedy algorithm. In each iteration, it adds $o$ with the maximum ratio of marginal influence to cost (i.e., $\frac{\Delta^{\uparrow}(\{o\}|S^*)}{o.w}$) into $S^∗$ until reaching the budget constraint.

  * Top-$k$: In each iteration, it chooses o which can influence the maximum number of trajectories until reaching the budget constraint.
  * BBS: The branch-and-bound framework with $θ$-termination and Algorithm 2 for bound estimations.

  * PBBS: The branch-and-bound framework with $θ$-termination and Algorithm 3 for bound estimations.
  * LazyProbe: The best-performing method in the most recent trajectory-driven billboard placement study. LazyProbe can only work with a submodular influence function. Although it is not fair for our methods to be compared with a submodular influence model.

#### Varying the Budget $B$

* Effectiveness  
Authors make the following observations to test the effectiveness of the model.First, when the budget raises from 100k to 500k, both BBS and PBBS outperform Greedy, from 10% to 95%. Second, PBBS is slightly worse than BBS by up to 8%. Third, Top-k has the worst performance, as it gives preference to the billboard with the highest influence in each iteration, which is usually the most expensive billboard in the real world. Hence, it can only choose a few of billboards when the budget is fewer. When the budget is big enough, the growing effectiveness is mainly contributed from a growing number of billboards, which makes the advantage of our solutions dwindle to about 3 times in NYC, and 1 time in LA, respectively. Last, the advantage of BBS and PBBS in LA is less than that in NYC. One possible reason is that the distribution of trajectories in LA is comparatively even, making it more possible to have influence overlaps among billboards.

* Efficiency  
There are three observations: First, the running time of BBS increases significantly w.r.t. the budget $B$. This is because in every branch, BBS has to invoke Algorithm 2, which needs to calculate the unit marginal influence for all $o ∈ \bar{S}$ in each iteration. When $B$ increases, more billboards can be selected into $S^∗$, and thus more iterations are needed. Second, the running time of PBBS increases by 100\% when $B$ increases. Last, Top-$k$ is the fastest one since it only scans all billboards once.

#### Varying the Number of Trajectories $|\mathcal{T}|$

* Effectiveness  
First, the influence of all methods increase because more trajectories can be influenced. Second, the effectiveness of BBS and PBBS consistently outperform that of Greedy and Top-$k$ by up to 60% and 300%, respectively. Last, the advantage of efficiency of BBS and PBBS in LA is less than that in NYC.
* Efficiency  
First, PBBS is about one order of magnitude faster than BBS. Second, the running time of all methods increase almost linearly w.r.t. $|\mathcal{T}|$, except for Top-$k$, because it chooses the billboards that can influence the most number of trajectories, which can be
calculated off-line.

#### Scalability Test

To evaluate the scalability of our methods BBS and PBBS, authors vary $|\mathcal{T}|$ from 500k to 5M, and $|\mathcal{U}|$ from 1500 to 15000. the efficiency of BBS is more sensitive than that of PBBS when varying $|\mathcal{U}|$. With the increase of $|\mathcal{U}|$, the growth rate of running time of BBS is larger than that of PBBS. In particular, PBBS is 15 times faster than BBS at $|\mathcal{U}| = 1500$, while such performance gap increases to almost two orders of magnitude at $|\mathcal{U}| = 6000$.
</font>
