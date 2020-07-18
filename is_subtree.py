class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        if t is None:
            return True
        if s is None and t is not None:
            return False
        return self.isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right, t)
    
    def isSameTree(self,p,q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
