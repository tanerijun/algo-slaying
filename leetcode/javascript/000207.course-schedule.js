/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 * Time complexity: O(E + V)
 * Space complexity: O(E + V)
 */
var canFinish = function (numCourses, prerequisites) {
  const prerequisiteMap = new Map();
  const visiting = new Set(); // store all courses along the current path

  for (let i = 0; i < numCourses; i++) {
    prerequisiteMap.set(i, []);
  }

  for (const [course, prerequisite] of prerequisites) {
    prerequisiteMap.get(course).push(prerequisite);
  }

  function dfs(course) {
    if (visiting.has(course)) {
      return false; // cycle detected
    }

    const prerequisites = prerequisiteMap.get(course);

    if (prerequisites.length === 0) {
      return true;
    }

    visiting.add(course);

    for (const prerequisite of prerequisites) {
      if (!dfs(prerequisite)) {
        return false;
      }
    }

    visiting.delete(course);
    prerequisiteMap.set(course, []); // mark course as completeable
    return true;
  }

  for (let c = 0; c < numCourses; c++) {
    if (!dfs(c)) {
      return false;
    }
  }

  return true;
};
