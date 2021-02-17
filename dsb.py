'''
this is the file holding the description texts to be inserted
this file is imported to the src.py
'''

bf_desc = [
    "Brute-Force Algorithm:",
    " ",
    "Summary:",
    "The brute force algorithm is very aggressive.",
    "It checks every single line segment against every other line segment for an intersection.",
    "This is done through vector mathematics, direction vectors and scalars.",
    " ",
    "Order List:",
    "This algorithm produces an ordered list of intersection points, in order of intersections from left to right.",
    " ",
    "Efficiency:",
    "The efficiency of this algorithm is O(n*n). This is due to the fact that the presence of",
    "intersections has to be checked between all line segments. This is computationally expensive.",
    "There is no consideration of shortcuts, rather all possibilities are computed till it ﬁnds a solution."
]

bo_desc = [
    "Bentley-Ottmann Algorithm:",
    " ",
    "Summary:",
    "The Bentley-Ottmann algorithm incorporates the idea of an imaginary line.",
    "This line will sweep from left-to-right over the line segments to compute",
    "all the intersecting pairs of line segments. Once again, this is done through",
    "vector mathematics, direction vectors and scalars.",
    " ",
    "Event Queue:",
    "This algorithm keeps an event queue.",
    "Adding a line-segment to the list when its leftmost endpoint is discovered during",
    "the sweep and also deleting a line-segment from the list when its rightmost endpoint",
    "is discovered during the sweep. This way, when the sweep reaches the end of the plane,",
    "the event queue should be empty.",
    " ",
    "Order List:",
    "This algorithm produces an ordered list of intersection points, in order of",
    "when they are discovered by the sweep-line."
    " "
    "Efficiency:",
    "The efficiency of this algorithm is O((n + k)logn). This algorithm is output-sensitive",
    "as the running time is sensitive to the size of the output. This algorithm is also intersection-sensitive",
    "as the number of intersections contributes to the size of the output generated."
]
sh_desc = [
    "Shamos-Hoey Algorithm:",
    " ",
    "Summary:",
    "The Shamos-Hoey algorithm also incorporates the idea of an imaginary line.",
    "This line will sweep from left-to-right over the line segments. Once it discovers its first intersection,",
    "the algorithm will stop. Once again, this is done through vector mathematics, direction vectors and scalars.",
    " ",
    "Event Queue:",
    "This algorithm keeps an event queue. Adding a line-segment to the list when its leftmost endpoint is discovered",
    "during the sweep and also deleting a line-segment from the list when its rightmost endpoint is discovered during the sweep.",
    "As the algorithm stops at the first intersection that is discovered, the event queue will not be empty by the time the algorithm terminates.",
    " ",
    "Order List:",
    "This algorithm produces an ordered list of intersection points, in order of when they are discovered by the sweep-line.",
    " ",
    "Efficiency:",
    "The efficiency of this algorithm is O(nlogn) time to compute due to it terminating on the ﬁrst intersection point that it discovers.",
    "As the algorithm terminates at the first intersection point, its efficiency is not sensitive to the number of intersections that it discovers.",
]

effic_desc = [
    "Efficiency:",
    " ",
    "Brute-Force Algorithm:",
    "O(n*n) is very computationally expensive. Out of all the algorithms, where we see a high number of line segments,the brute-force algorithm",
    "will always be the most inefficient.",
    " ",
    "Bentley-Ottmann Algorithm:",
    "O((n + k)logn) is very efficient in terms of taking into consideration the number of intersections. Where we see a high number of line",
    "segments but low number of intersections, the brute-force algorithm will play its part as an efficient algorithm.",
    " ",
    "Shamos-Hoey Algorithm:",
    "O(nlogn) is also very efficient which is all due to how the algorithm terminates at the first intersection",
    "point that it discovers. Because of this, the efficiency is not hindered by a large number of intersection points within the plane.",
    " ",
    "Summary:",
    "If we look at the map-overlay problem, we wish to discover every intersection point that exists within the plane. The likeliness that when two thematic",
    "map layers overlap, all of their line segments intersect is slim. Knowing this, the better suited algorithm would be the Bentley-Ottmann algorithm rather",
    "than the Brute-Force algorithm. We have a plane with many line segments whereby, all intersections in existence need to be identiﬁed and we know that",
    "not every pair of line segments intersect. Here, the Shamos-Hoey algorithm would not be suitable as we are interested in ﬁnding more than one intersection.",
    "However, where we concern ourself with robotic movement, a given motion trajectory between two ligaments such as the humanoids arms, we only need to look at",
    "whether this motion trajectory has any intersection. We are not interested in searching for every single intersection within the plane. For this, the Shamos-Hoey algorithm",
    "would be better suited. Furthermore, the eﬃciency O(nlogn) of the Shamos-Hoey algorithm compared to O((n+k)logn) is also another key reason the Shamos-Hoey would be a better suit.",
    "We would expect the movement of a humanoid to be ﬂawless and not at any stage have to pause for a long-period of time to calculate its next movements. The Shamos-Hoey algorithm yielding",
    "a higher eﬃciency would mean that intersections can be calculated faster, which will in turn, contribute towards the ﬂawless movement of the humanoid robot."
]
