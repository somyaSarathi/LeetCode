from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    mx, top = None, None

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if self.mx is None:
            self.mx = root.val
            self.top = root

        self.mx = max( self.mx, root.val )

        if not root.left and not root.right:
            self.mx = max(self.mx, root.val)
            return root.val

        if root.left and root.right:
            l = self.maxPathSum( root.left )
            r = self.maxPathSum( root.right )

            self.mx = max( self.mx, root.val + l + r, root.val + l, root.val + r )

            if self.top != root:
                return max( root.val + l, root.val + r, root.val )

        elif root.left:
            l = self.maxPathSum( root.left )
            self.mx = max( self.mx, root.val + l )

            if self.top != root:
                return max(root.val + l, root.val)

        elif root.right:
            r = self.maxPathSum( root.right )
            self.mx = max( self.mx, root.val + r )

            if self.top != root:
                return max(root.val + r, root.val)

        return self.mx