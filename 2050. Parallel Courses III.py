class Solution(object):
    def minimumTime(self, n, relations, time):
        """
        n: number of courses
        relations: [prevCourse, nextCourse] dependencies
        time: time[i] = time required to complete course i+1
        """

        # Step 1: Build adjacency list
        # graph[i] = list of courses that depend on course i
        graph = [[] for _ in range(n)]

        for prev, next in relations:
            # Convert to 0-index
            graph[prev - 1].append(next - 1)

        # memo[i] will store:
        # the minimum time required to COMPLETE course i
        # including all its prerequisite chains
        memo = [-1] * n

        def calculateTime(course):
            """
            Returns the minimum time required to complete this course,
            considering all prerequisite chains.
            """

            # If already computed, return cached result
            if memo[course] != -1:
                return memo[course]

            # If no outgoing edges, it means:
            # no courses depend on it.
            # BUT this does NOT mean no prerequisites.
            # In this structure, edges go from prerequisite → next.
            # So if graph[course] is empty,
            # it means nothing depends on it.
            # However, this implementation computes forward.
            # So this acts as base case.
            if not graph[course]:
                memo[course] = time[course]
                return memo[course]

            # We need the maximum time among all dependent chains
            max_prerequisite_time = 0

            # For each course that depends on this course
            for prereq in graph[course]:
                max_prerequisite_time = max(
                    max_prerequisite_time,
                    calculateTime(prereq)
                )

            # Total time to complete this course =
            # its own time + longest dependent chain
            memo[course] = max_prerequisite_time + time[course]

            return memo[course]

        # The answer is the maximum time among all courses
        # because courses can be taken in parallel
        overall_min_time = 0

        for course in range(n):
            overall_min_time = max(
                overall_min_time,
                calculateTime(course)
            )

        return overall_min_time
