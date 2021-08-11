import java.util.List;

/** Tree class that represents the binary tree to be searched.
 * @author Jennifer Gabriela Tirok
 * @version 11th August 2021
 */

public class Tree {
  // The integer value of the current node in the tree
  private int value;
  // The List of children nodes
  private List<Tree> children;

  public Tree(int value, List<Tree> children) {
    this.value = value;
    this.children = children;
  }
  
  /** Invokes the longestPath(int parentValue, int parentPathLength) function and 
   *  uses 0 as a placeholder for the parameters required.
   */
  public int longestPath() {
    return longestPath(0, 0);
  }

  /** Search through each children nodes by recursively calling the 
   *  longestPath(int parentValue, int parentPathLength).
   *  Calculate the longest path of consecutive integers in the tree.
   * @param parentValue: the integer value of the parent node.
   * @param parentPathLength: the longest path of consecutive integers seen so far.
   * @return Returns the longest path of consecutive integers in the tree
   */
  public int longestPath(int parentValue, int parentPathLength) {
    int currentPathLength;
    if (this.value == parentValue + 1) {
      currentPathLength = parentPathLength + 1;
    } else {
      currentPathLength = 1;
    }
    
    int maxLength = currentPathLength;

    // Iterate through the List of children nodes
    for (Tree child: this.children) {
      int maxChildLength = child.longestPath(this.value, currentPathLength);
      maxLength = Math.max(maxLength, maxChildLength);
    }

    return maxLength;
  }
}