import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Point:
    """This is a class for a point in a 2D space.
    """
    def __init__(self, x, y):
        self.x, self.y = x, y


class Node:
    """This is a class to represent a node in the quadtree.
    """
    def __init__(self, x, y, w, h, pts):
        self.x, self.y = x, y
        self.w, self.h = w, h
        self.points = pts
        self.children = []

    def __lt__(self, other):
        return self.x < other.x


class QuadTree:
    """This is a class to generate a quadtree.
    """
    def __init__(self, n, k, w, h):
        """This is the constructor for the quadtree.

        Args:
            n (int): The number of points to be stored in the quadtree.
            k (int): The number of points per leaf node.
            w (int): The width of the quadtree.
            h (int): The height of the quadtree.
        """
        self.threshold = k
        self.points = [
            Point(np.random.uniform(0, w), np.random.uniform(0, h))
            for i in range(n)
        ]
        self.root = Node(0, 0, w, h, self.points)

    def addPoints(self, point):
        """This is a function to add points to the quadtree.

        Args:
            point (Node): A point to be added to the quadtree.
        """
        self.points.append(point)

    def getPoints(self):
        """This is a function to get all the points in the quadtree.

        Returns:
            list: A list of all the points in the quadtree.
        """
        return self.points

    def build(self):
        """This is a function to build the quadtree.
        """
        def DFS(u, k):
            if len(u.points) <= k:
                return
            x, y, _w, _h = u.x, u.y, u.w / 2, u.h / 2
            for _x, _y in zip([x, x + _w, x, x + _w], [y, y, y + _h, y + _h]):
                ch = Node(_x, _y, _w, _h, self.divide(_x, _y, _w, _h,
                                                      u.points))
                DFS(ch, k)
                u.children.append(ch)

        DFS(self.root, self.threshold)

    def divide(self, x, y, w, h, points):
        """This is a function to divide points.

        Args:
            x (float): The minimum x coordinate of the rectangle.
            y (float): The minimum y coordinate of the rectangle.
            w (float): The width of the rectangle.
            h (float): The height of the rectangle.
            points (list): A list of points.

        Returns:
            list: A list of points in the rectangle.
        """
        pts = []
        for point in points:
            if point.x >= x and point.x <= x + w and point.y >= y and point.y <= y + h:
                pts.append(point)
        return pts

    def getChildren(self, u):
        """This is a function to get children of a node.

        Args:
            u (Node): A node in the quadtree.

        Returns:
            list: A list of children belong to the node.
        """
        if len(u.children) == 0:
            return [u]
        else:
            children = []
            for child in u.children:
                children += (self.getChildren(child))
        return children

    def drawGraph(self, title, ax):
        """This is a function to draw a graph of the quadtree.

        Args:
            title (string): The title of the graph.
            ax (Axes): The axes of the graph.
        """
        plt.title(title)
        ch = self.getChildren(self.root)
        for node in ch:
            ax.add_patch(
                mpatches.Rectangle((node.x, node.y),
                                   node.w,
                                   node.h,
                                   fill=False))
        x = [p.x for p in self.points]
        y = [p.y for p in self.points]
        plt.plot(x, y, 'r.')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    def visualize(self):
        """This is a function to visualize the quadtree.
        """
        __, ax = plt.subplots(figsize=(12, 8))
        self.drawGraph("QuadTree", ax)

    def windowQuery(self, x0, y0, w, h):
        """This is a function to implement a window query in the quadtree.

        Args:
            x0 (float): The minimum x coordinate of the rectangle.
            y0 (float): The minimum y coordinate of the rectangle.
            w (float): The width of the rectangle.
            h (float): The height of the rectangle.

        """
        x1, y1 = x0 + w, y0 + h
        __, ax = plt.subplots(figsize=(12, 8))

        ax.add_patch(mpatches.Rectangle((x0, y0), w, h, fill=False, color='m'))

        def overlap(p0, p1, p2, p3):
            """This is a function to check if two rectangles overlap.

            Args:
                p0 (Point): The first point of the first rectangle.
                p1 (Point): The second point of the first rectangle.
                p2 (Point): The first point of the second rectangle.
                p3 (Point): The second point of the second rectangle.

            Returns:
                boolean: True if the two rectangles overlap, otherwise False.
            """
            return p2.x < p1.x and p2.y < p1.y and p0.x < p3.x and p0.y < p3.y

        def DFS(u):
            """This is a function to implement a depth-first search in the quadtree.

            Args:
                u (Node): A node in the quadtree.
            """
            if overlap(Point(u.x, u.y), Point(u.x + u.w, u.y + u.h),
                       Point(x0, y0), Point(x1, y1)):
                if len(u.children) == 0:
                    for p in u.points:
                        if x0 < p.x and p.x < x1 and y0 < p.y and p.y < y1:
                            plt.plot(p.x, p.y, 'kD')
                else:
                    for child in u.children:
                        DFS(child)

        DFS(self.root)
        self.drawGraph("Window Query", ax)

    def rangeQuery(self, x0, y0, r):
        """This is a function to implement a range query in the quadtree.

        Args:
            x0 (Point): The x coordinate of the center of a circle.
            y0 (Point): The y coordinate of the center of a circle.
            r (float): The radius of the circle.

        """
        __, ax = plt.subplots(figsize=(12, 8))

        ax.add_patch(mpatches.Circle((x0, y0), r, fill=False, color='m'))

        def overlap(p0, r, p1, p2):
            """This is a function to check if a rectangle and a circle overlap.

            Args:
                p0 (Point): The center point of the circle.
                r (float): The radius of the circle.
                p1 (Point): The first point of the rectangle.
                p2 (Point): The second point of the rectangle.

            Returns:
                boolean: True if the rectangle and circle overlap, otherwise False.
            """
            x = max(p1.x, min(p0.x, p2.x)) - p0.x
            y = max(p1.y, min(p0.y, p2.y)) - p0.y
            return (x**2 + y**2) <= r**2

        def DFS(u):
            """This is a function to implement a depth-first search in the quadtree.

            Args:
                u (Node): A node in the quadtree.
            """
            if overlap(Point(x0, y0), r, Point(u.x, u.y),
                       Point(u.x + u.w, u.y + u.h)):
                if len(u.children) == 0:
                    for p in u.points:
                        if (p.x - x0)**2 + (p.y - y0)**2 < r**2:
                            plt.plot(p.x, p.y, 'kD')
                else:
                    for child in u.children:
                        DFS(child)

        DFS(self.root)
        self.drawGraph("Range Query", ax)

    def knnQuery(self, qx, qy, k):
        """This is a function to implement a k-nearest-neighbors query in the quadtree.

        Args:
            qx (float): The x coordinate of the query point.
            qy (float): The y coordinate of the query point.
            k (int): The number of nearest neighbors.

        """
        from queue import PriorityQueue

        query = Point(qx, qy)
        __, ax = plt.subplots(figsize=(12, 8))
        plt.plot(qx, qy, 'mX')

        def min_dist(r, p):
            """This is a function to find the minimum distance between a query point and a node in the quadtree.

            Args:
                r (float): The radius of the circle.
                p (Node): A node in the quadtree.

            Returns:
                float: The minimum distance between the query point and the node.
            """
            dx = max(r.x - p.x, 0, p.x - r.x - r.w)
            dy = max(r.y - p.y, 0, p.y - r.y - r.h)
            return np.sqrt(dx**2 + dy**2)

        def points_dist(a, b):
            """This is a function to calculate the distance between two points.

            Args:
                a (Point): The first point.
                b (Point): The second point.

            Returns:
                float: The distance between the two points.
            """
            return np.sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

        q = PriorityQueue()
        knn = PriorityQueue()
        q.put((min_dist(self.root, query), self.root))
        while not q.empty():
            current = q.get()[1]
            if k == 0 and min_dist(current, query) > -knn.queue[0][0]:
                break
            elif len(current.children) == 0:
                for p in current.points:
                    if k > 0:
                        knn.put((-points_dist(p, query), p))
                        k -= 1
                    elif points_dist(p, query) < -knn.queue[0][0]:
                        knn.get()
                        knn.put((-points_dist(p, query), p))

            else:
                for child in current.children:
                    q.put((min_dist(child, query), child))

        while not knn.empty():
            p = knn.get()[1]
            plt.plot(p.x, p.y, 'kD')

        self.drawGraph("KNN Query", ax)