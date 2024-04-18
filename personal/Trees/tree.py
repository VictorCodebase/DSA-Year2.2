class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        #Creates the root node

    def addChild(self, child):
        child.parent = self
        self.children.append(child)
    
    def printTree(self):
        space = ' ' * self.getLevel()
        prefix = space + "|--"
        print(prefix + self.data)
        if (self.children):
              for child in self.children:
                    child.printTree()
    
    def getLevel(self):
        level = 0
        p = self.parent
        while p:
                level += 1
                p = p.parent
                
        return level
            

    
def buildTree():
    root = TreeNode("Devices")
    
    handheld = TreeNode("Hand Held")
    handheld.addChild(TreeNode("Techno"))
    handheld.addChild(TreeNode("Vivo"))
    handheld.addChild(TreeNode("Samsung"))
    
    laptops = TreeNode("Laptops")
    laptops.addChild(TreeNode("HP"))
    laptops.addChild(TreeNode("Samsung"))
    laptops.addChild(TreeNode("Dell"))
    laptops.addChild(TreeNode("Compaq"))
    
    root.addChild(handheld)
    root.addChild(laptops)
    return root
      
if __name__=='__main__':
     root = buildTree()
     root.printTree()
     