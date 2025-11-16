
class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.isEnd = False
        self.next = None
        self.child = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def findchild(self, node, char):
        curr = node.child
        while curr:
            if curr.val == char:
                return curr
            curr = curr.next
        return None            

    def search(self, word):
        curr = self.root
        for char in word:
            node = self.findchild(curr, char)
            if not node:
                return False
            curr = node
        return curr.isEnd
    
    def insert(self, word):
        if not word:
            return False
        curr = self.root
        for char in word:
            hit = self.findchild(curr, char)
            if hit:
                curr = hit
                continue
            elif not curr.child or curr.child.val > char :
                new = TrieNode(val=char)
                temp = curr.child
                curr.child = new
                new.next = temp
                curr = new
            else:
                temp = curr.child
                new = TrieNode(val=char)
                while temp.next and temp.next.val < char:
                    temp = temp.next
                t = temp.next
                temp.next = new
                new.next = t
                curr = new
        curr.isEnd = True
    

    """def bfs(self, node):
        Queue = queues
        curr = node
        while curr:
            Queue.enqueue(curr)
            curr = curr.next


    def dfs(self, node):
        # Pre Order
        print(node.val)
        child = node.child
        while child:
            self.dfs(child)
            child = child.next"""
        
    def printAllWords(self, root, prefix=""):
        if not root:
            return
        
        prefix += root.val
        
        if root.isEnd:
            print(prefix)
        
        temp = root.child
        
        while temp:
                self.printAllWords(temp, prefix)
                temp = temp.next
                
        return

    def printAllWordsReverse(self, root, prefix=""):
        if not root:
            return
        
        if root.next:
            self.printAllWordsReverse(root.next, prefix)
        
            temp = root.child
            prefix += root.val
            if root.isEnd:
                print(prefix)
            else:
                self.printAllWordsReverse(temp, prefix)
        
        else:
            temp = root.child
            prefix += root.val
            if root.isEnd:
                print(prefix)
            else:
                self.printAllWordsReverse(temp, prefix)

        return
                    

# --- TEST HARNESS FOR YOUR TRIE ---

def assert_eq(got, exp, msg=""):
    ok = (got == exp)
    print(f"[{'OK' if ok else 'X '}] {msg} -> got={got!r}, exp={exp!r}")
    return ok

def run_basic_tests():
    t = Trie()

    # Insert a mixed set (order intentionally scrambled)
    words = ["app", "apt", "bat", "bad", "apple", "ape", "ale", "bar", "bark"]
    for w in words:
        t.insert(w)

    # Re-insert duplicates (should NOT create logical duplicates)
    for w in ["app", "apple", "bat", "bar"]:
        t.insert(w)

    print("\n=== All words (should be lexicographic if siblings kept sorted) ===")
    t.printAllWords(t.root)  # starts from root

    print("\n=== Search: present words ===")
    for w in ["app", "apple", "apt", "ape", "ale", "bat", "bad", "bar", "bark"]:
        assert_eq(t.search(w), True, f"search({w})")

    print("\n=== Search: absent words / prefixes ===")
    for w in ["ap", "apply", "apps", "b", "ba", "barke", "cat", ""]:
        assert_eq(t.search(w), False, f"search({w})")

    print("\n=== Prefix relationships sanity checks ===")
    # 'app' is end-of-word and parent of 'apple'
    assert_eq(t.search("app"), True, "prefix 'app' should be a word")
    assert_eq(t.search("apple"), True, "'apple' should be a word")
    assert_eq(t.search("ap"), False, "'ap' should be a prefix only")

    print("\n=== Diverging branches sanity checks (ape vs ale) ===")
    assert_eq(t.search("ape"), True, "search(ape)")
    assert_eq(t.search("ale"), True, "search(ale)")

    print("\n=== Reinsert idempotence ===")
    before = t.search("bar")
    t.insert("bar")
    after = t.search("bar")
    assert_eq(before and after, True, "reinsert 'bar' remains searchable")

def run_edge_tests():
    t = Trie()

    print("\n=== Empty insertion behavior ===")
    # Your insert("") returns False and should not mark root as word
    res = t.insert("")
    assert_eq(res, False, "insert('') returns False")
    assert_eq(t.search(""), False, "search('') should be False with your policy")

    print("\n=== Single-word path ===")
    t.insert("zzz")
    assert_eq(t.search("zzz"), True, "search(zzz)")
    assert_eq(t.search("zz"), False, "search(zz) (prefix only)")
    print("Words now:")
    t.printAllWords(t.root)

    print("\n=== Many siblings under same parent ===")
    t = Trie()
    for w in ["ba", "bb", "bc", "bd", "be", "bf"]:
        t.insert(w)
    print("Words (check sibling order under 'b'):")
    t.printAllWords(t.root)
    for w in ["ba","bb","bc","bd","be","bf"]:
        assert_eq(t.search(w), True, f"search({w})")

if __name__ == "__main__":
    # If your file still has `import queues` at top and that module doesn't exist,
    # comment it out or guard it:
    # try: import queues
    # except ImportError: pass

    run_basic_tests()
    run_edge_tests()


def insert_words(t, words):
    for w in words:
        t.insert(w)

def test_reverse_prints():
    t = Trie()
    # Intentionally include: 
    # - a prefix word with children (app/apple)
    # - diverging branches (ape/ale)
    # - multiple top-level branches (a… vs b…)
    words = ["app", "apple", "apt", "ape", "ale", "bat", "bad", "bar", "bark"]
    insert_words(t, words)

    print("=== Forward (for reference) ===")
    t.printAllWords(t.root)

    print("\n=== Reverse (your current function) ===")
    t.printAllWordsReverse(t.root)

    print("\nExpected words present in Reverse (order will be reverse-lexicographic):")
    expected = ["bark","bar","bat","bad","apple","app","apt","ape","ale"]  # conceptual set
    print(" ".join(expected))

def test_prefix_with_children():
    t = Trie()
    insert_words(t, ["app", "apple", "apply"])
    print("=== Reverse (should include app, apple, apply) ===")
    t.printAllWordsReverse(t.root)

def test_many_siblings_under_one_parent():
    t = Trie()
    insert_words(t, ["ba", "bb", "bc", "bd", "be"])
    print("=== Reverse (should be be bd bc bb ba) ===")
    t.printAllWordsReverse(t.root)

if __name__ == "__main__":
    test_reverse_prints()
    print()
    test_prefix_with_children()
    print()
    test_many_siblings_under_one_parent()
