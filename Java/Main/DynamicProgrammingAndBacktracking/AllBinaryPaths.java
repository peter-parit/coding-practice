package DynamicProgrammingAndBacktracking;


import java.util.ArrayList;
import java.util.List;

class AllBinaryPaths {
    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        backtrack(root, "", result);
        return result;
    }

    private void backtrack(TreeNode node, String path, List<String> result) {
        if (node == null) return;

        if (path.isEmpty()) {
            path += node.val;
        } else {
            path += "->" + node.val;
        }

        // if is leaf
        if (node.left == null && node.right == null) {
            result.add(path);
            return;
        }

        // include left node and include right node
        backtrack(node.left, path, result);
        backtrack(node.right, path, result);
    }
}