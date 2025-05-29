"""
Árvore AVL genérica com suporte a múltiplas referências por chave
(partindo da sua implementação original).

Autor: Taimisson de Carvalho Schardosim   Data: 27/05/2025
"""

from __future__ import annotations
from typing import Generic, List, Optional, TypeVar

K = TypeVar("K") # tipo da chave
R = TypeVar("R") # tipo da referencia

class Node(Generic[K, R]):
    __slots__ = ("key", "refs", "left", "right", "height")

    def __init__(self, key: K, ref: R):
        self.key = key
        self.refs: List[R] = [ref]
        self.left: Optional[Node[K, R]] = None
        self.right: Optional[Node[K, R]] = None
        self.height: int = 1;

    def __str__(self) -> str:
        return f"{self.key}"
    
    
class AVLTree(Generic[K, R]):
    __slots__ = ("root",)

    def __init__(self):
        self.root: Optional[Node[K, R]] = None

    def __str__(self) -> str:
        return str(self.root)

    # ---- utilidades ----

    def _h(self, n): return n.height if n else 0
    def _upd(self, n): n.height = 1 + max(self._h(n.left), self._h(n.right))
    def _bf(self, n): return self._h(n.left) - self._h(n.right)

    def _rot_right(self, y: Node[K, R]) -> Node[K, R]:
        x, y.left = y.left, y.left.right 
        x.right = y
        self._upd(y); self._upd(x)
        return x

    def _rot_left(self, x: Node[K, R]) -> Node[K, R]:
        y, x.right = x.right, x.right.left 
        y.left = x
        self._upd(x); self._upd(y)
        return y
    
    # ---- insercao 
                
    def insert(self, key: K, ref: R):
        def _ins(node: Optional[Node[K, R]], k: K, r: R) -> Node[K, R]:
            if not node:
                return Node(k, r)
            if k == node.key:
                node.refs.append(r)
                return node
            if k < node.key:
                node.left = _ins(node.left, k, r)
            else:
                node.right = _ins(node.right, k, r)
            
            self._upd(node)
            bf = self._bf(node)

            if bf > 1 and k < node.left.key: # LL 
                return self._rot_right(node)
            if bf < -1 and k > node.right.key: # RR
                return self._rot_left(node)
            if bf > 1 and k > node.left.key: # LR
                node.left = self._rot_left(node.left)
                return self._rot_right(node)
            if bf < -1 and k < node.right.key: # RL
                node.right = self._rot_right(node.right)
                return self._rot_left(node)
            return node
        
        self.root = _ins(self.root, key, ref)

    ## ---- busca exata
    def search(self, key: K) -> Optional[List[R]]:
        n = self.root
        while n: 
            if key == n.key: return n.refs
            n = n.left if key < n.key else n.right
        return None

    ## ---- intervalo ordenavel 

    def range_query(self, lo: K, hi: K) -> List[R]:
        res: List[R] = []
        def _dfs(node: Optional[Node[K, R]]):
            if not node: return
            if lo <= node.key: _dfs(node.left)
            if lo <= node.key <= hi: res.extend(node.refs)
            if node.key <= hi: _dfs(node.right)
        _dfs(self.root)
        return res

    # ---- prefixo de string    
    def prefix_query(self, prefix: str) -> List[R]:
        res: List[R] = []
        def _dfs(node: Optional[Node[K, R]]):
            if not node: return 
            if node.key.startswith(prefix):
                res.extend(node.refs)
                _dfs(node.left); _dfs(node.right)
            elif node.key < prefix:
                _dfs(node.right)
            else:
                _dfs(node.left)
        _dfs(self.root)
        return res
    
    # ---- remocao

    def remove(self, key: K, ref: R):
        def _rem(node: Optional[Node[K, R]], k: K, r: R) -> Optional[Node[K, R]]:
            if not node:
                return None

            # 1) Caminho de descida
            if k < node.key:
                node.left = _rem(node.left, k, r)
            elif k > node.key:
                node.right = _rem(node.right, k, r)
            else:                          # achou a chave
                try:                       # remove só aquela referência
                    node.refs.remove(r)
                except ValueError:
                    return node            # ref não estava aqui; nada a fazer

                if not node.refs:          # se zerou, remove o nó físico
                    if not node.left and not node.right:
                        return None
                    if not node.left:
                        return node.right
                    if not node.right:
                        return node.left
                    # dois filhos → substitui pelo sucessor
                    succ = node.right
                    while succ.left:
                        succ = succ.left
                    node.key, node.refs = succ.key, succ.refs
                    node.right = _rem(node.right, succ.key, succ.refs[0])

            # 2) Se o nó sumiu, sobe
            if node is None:
                return None

            # 3) Atualiza altura e reequilibra
            self._upd(node)
            bf = self._bf(node)

            if bf > 1 and self._bf(node.left) >= 0:           # LL
                return self._rot_right(node)
            if bf > 1 and self._bf(node.left) < 0:            # LR
                node.left = self._rot_left(node.left)
                return self._rot_right(node)
            if bf < -1 and self._bf(node.right) <= 0:         # RR
                return self._rot_left(node)
            if bf < -1 and self._bf(node.right) > 0:          # RL
                node.right = self._rot_right(node.right)
                return self._rot_left(node)

            return node  # já balanceado

        self.root = _rem(self.root, key, ref)
