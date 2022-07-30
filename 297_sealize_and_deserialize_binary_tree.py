class Codec:

    def serialize(self, root):
        res = [""]

        def preorder(node):
            if not node:
                res[0] += "null$"
                return
            res[0] += str(node.val) + "$"
            preorder(node.left)
            preorder(node.right)
        
        preorder(root)
        return res[0][:-1]

    def deserialize(self, data):
        data = data.split("$")
        print(data)
        
        def build_tree(d):
            if not d or (d and d[0] == "null"):
                return None

            root = TreeNode(d[0])
            root.left = build_tree(d[1:])
            root.right = build_tree(d[2:])

            return root

        return build_tree(data)
